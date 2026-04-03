import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

from core.predict import predict_default, apply_threshold
from core.shap_utils import shap_batch_fig
from utils.file_handler import load_uploaded_table
from utils.risk_labels import risk_label


REQUIRED_COLS = [
    'Age',
    'Income',
    'Education',
    'EmploymentType',
    'MaritalStatus',
    'LoanAmount',
    'InterestRate',
    'LoanTerm',
    'LoanPurpose',
    'CreditScore',
    'DTIRatio',
    'MonthsEmployed',
    'NumCreditLines',
    'HasMortgage',
    'HasDependents',
    'HasCoSigner',
]


def render_batch_assessment(encoder, model, feature_names, threshold: float):
    st.markdown(
        """
        <div class="section-block">
            <div class="section-label">Portfolio view</div>
            <div class="section-title">Batch Applicant Assessment</div>
            <div class="section-caption">
                Upload a CSV or Excel file.
                File structure must match the model’s required input schema.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    summary_col, template_col = st.columns([1.8, 1.2], gap="large")

    with summary_col:
        st.markdown(
            """
            <div class="card-quiet">
                <div class="card-header">File specification</div>
                <div class="card-title">Required input fields</div>
                <div class="card-subtitle">
                    The following columns must be present for the model to accept the file.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write(
            ", ".join(
                [
                    "`Age`",
                    "`Income`",
                    "`Education`",
                    "`EmploymentType`",
                    "`MaritalStatus`",
                    "`LoanAmount`",
                    "`InterestRate`",
                    "`LoanTerm`",
                    "`LoanPurpose`",
                    "`CreditScore`",
                    "`DTIRatio`",
                    "`MonthsEmployed`",
                    "`NumCreditLines`",
                    "`HasMortgage`",
                    "`HasDependents`",
                    "`HasCoSigner`",
                ]
            )
        )

    with template_col:
        template_csv = pd.DataFrame(columns=REQUIRED_COLS).to_csv(index=False)
        st.markdown(
            """
            <div class="card">
                <div class="card-header">Template</div>
                <div class="card-title">Download empty file</div>
                <div class="card-subtitle">
                    Use this as a starting point for batch scoring templates.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.download_button(
            "Download CSV template",
            data=template_csv,
            file_name="applicant_template.csv",
            mime="text/csv",
        )

    st.markdown("---")

    up_left, up_right = st.columns([1.4, 1.6], gap="large")

    with up_left:
        st.markdown(
            """
            <div class="card-quiet">
                <div class="card-header">File upload</div>
                <div class="card-title">Load applicant dataset</div>
                <div class="card-subtitle">
                    Supports CSV (.csv) and Excel (.xlsx) formats.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        uploaded = st.file_uploader(
            "Select applicant file",
            type=["csv", "xlsx"],
            label_visibility="visible",
        )

    batch_df = None
    if uploaded is not None:
        try:
            batch_df = load_uploaded_table(uploaded)
        except Exception as e:
            st.error(f"Unable to read file. Details: {e}")

    if batch_df is not None:
        missing = [c for c in REQUIRED_COLS if c not in batch_df.columns]
        if missing:
            st.error(f"Missing columns in uploaded file: {missing}")
        else:
            with up_right:
                st.markdown(
                    f"**{len(batch_df):,} applicants loaded.** Preview of first 10 rows:"
                )
                st.dataframe(batch_df.head(10), use_container_width=True, height=280)

            st.markdown("")
            run_batch = st.button("Run batch assessment", type="primary")

            if run_batch:
                with st.spinner(f"Scoring {len(batch_df):,} applicants..."):
                    probs, _ = predict_default(encoder, model, feature_names, batch_df)
                    preds = apply_threshold(probs, threshold)
                    risk_labels = [risk_label(p)[0] for p in probs]

                results_df = batch_df.copy()
                results_df['Default_Probability'] = (probs * 100).round(1)
                results_df['Risk_Band'] = risk_labels
                results_df['Decision'] = np.where(
                    preds == 1, 'Flag for Review', 'Approve'
                )

                total_applicants = len(results_df)
                flagged_count = int(preds.sum())
                approval_rate = (1 - preds.mean())
                avg_default_prob = probs.mean()

                st.markdown(
                    """
                    <div class="section-block">
                        <div class="section-label">Portfolio summary</div>
                        <div class="section-title">Executive overview</div>
                        <div class="section-caption">
                            High-level indicators for the batch, suitable for portfolio and credit committee views.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                m1, m2, m3, m4 = st.columns(4)
                m1.metric("Total applicants", f"{total_applicants:,}")
                m2.metric("Flagged for review", f"{flagged_count:,}")
                m3.metric("Approval rate", f"{approval_rate:.1%}")
                m4.metric("Average default probability", f"{avg_default_prob:.1%}")

                st.markdown("")
                st.markdown(
                    """
                    <div class="section-block">
                        <div class="section-label">Row-level results</div>
                        <div class="section-title">Scored applicant records</div>
                        <div class="section-caption">
                            Each row in the file is scored independently using the unchanged production model.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.dataframe(
                    results_df[
                        ['Default_Probability', 'Risk_Band', 'Decision'] + REQUIRED_COLS
                    ],
                    use_container_width=True,
                    height=420,
                )

                st.download_button(
                    "Download scored results (CSV)",
                    data=results_df.to_csv(index=False),
                    file_name="loan_risk_results.csv",
                    mime="text/csv",
                )

                st.markdown("---")

                st.markdown(
                    """
                    <div class="section-block">
                        <div class="section-label">Risk distribution</div>
                        <div class="section-title">Risk band breakdown</div>
                        <div class="section-caption">
                            Distribution of applicants across risk bands, based on modelled probability of default.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                band_counts = (
                    pd.Series(risk_labels)
                    .value_counts()
                    .reindex(['Low', 'Medium', 'High'], fill_value=0)
                )
                fig2, ax2 = plt.subplots(figsize=(5, 3))
                ax2.bar(
                    band_counts.index,
                    band_counts.values,
                    color=['#22c55e', '#f97316', '#ef4444'],
                )
                ax2.set_ylabel('Number of applicants')
                ax2.set_title('Applicants by risk band')
                plt.tight_layout()
                st.pyplot(fig2)
                plt.close(fig2)

                st.markdown("")
                st.markdown(
                    """
                    <div class="section-block">
                        <div class="section-label">Global explanation</div>
                        <div class="section-title">What is driving risk across this file?</div>
                        <div class="section-caption">
                            SHAP summary based on a sample of up to 200 applicants from the uploaded portfolio.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                with st.spinner("Computing SHAP values for batch sample..."):
                    fig3 = shap_batch_fig(encoder, model, feature_names, batch_df)
                st.pyplot(fig3)
                plt.close(fig3)