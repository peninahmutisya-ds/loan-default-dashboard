import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from core.predict import predict_default, apply_threshold
from core.shap_utils import shap_waterfall_fig
from utils.risk_labels import risk_label


def render_single_applicant(encoder, model, feature_names, threshold: float):
    st.markdown(
        """
        <div class="section-block">
            <div class="section-title">Single Applicant Risk Assessment</div>
            <div class="section-caption">
                Capture applicant, loan, and financial details to obtain a model-backed decision with full
                SHAP-based explanation.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_inputs, col_outputs = st.columns([1.5, 1.1], gap="large")

    with col_inputs:
        st.markdown(
            """
            <div class="card">
                <div class="card-header">Input capture</div>
                <div class="card-title">Applicant details</div>
                <div class="card-subtitle">
                    All fields are required. Values are passed directly into the production preprocessing pipeline.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("**Personal profile**")
            age = st.number_input("Age", min_value=18, max_value=80, value=35)
            income = st.number_input(
                "Annual Income (KES)", min_value=0, max_value=5000000, value=60000, step=1000
            )
            education = st.selectbox(
                "Education",
                ["High School", "Bachelor's", "Master's", "PhD"],
            )
            employment = st.selectbox(
                "Employment Type",
                ["Full-time", "Part-time", "Self-employed", "Unemployed"],
            )
            marital_status = st.selectbox(
                "Marital Status",
                ["Single", "Married", "Divorced"],
            )

        with c2:
            st.markdown("**Loan Information**")
            loan_amount = st.number_input(
                "Loan Amount (KES)", min_value=0, max_value=10000000, value=20000, step=500
            )
            interest_rate = st.number_input(
                "Interest Rate (%)", min_value=0.0, max_value=30.0, value=8.5, step=0.1
            )
            loan_term = st.number_input(
                "Loan Term (months)", min_value=6, max_value=360, value=60
            )
            loan_purpose = st.selectbox(
                "Loan Purpose", ["Home", "Auto", "Education", "Business", "Personal"]
            )
            credit_score = st.number_input(
                "Credit Score", min_value=300, max_value=850, value=680
            )

        with c3:
            st.markdown("**Financial position**")
            dti_ratio = st.number_input(
                "Debt-to-Income Ratio", min_value=0.0, max_value=1.0, value=0.35, step=0.01
            )
            months_employed = st.number_input(
                "Months Employed", min_value=0, max_value=600, value=60
            )
            num_credit_lines = st.number_input(
                "No. of Credit Lines", min_value=0, max_value=20, value=3
            )
            has_mortgage = st.selectbox("Has Mortgage?", ["No", "Yes"])
            has_dependents = st.selectbox("Has Dependents?", ["No", "Yes"])
            has_cosigner = st.selectbox("Has Co-Signer?", ["No", "Yes"])

        st.markdown("")
        assess_btn = st.button("Run underwriting decision", type="primary")

    with col_outputs:
        st.markdown(
            """
            <div class="card-quiet">
                <div class="card-header">Decision engine</div>
                <div class="card-title">Model output</div>
                <div class="card-subtitle">
                    Underwriting recommendation based purely on model estimate of default probability.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        default_placeholder = st.empty()

    if assess_btn:
        applicant = pd.DataFrame(
            [
                {
                    'Age': age,
                    'Income': income,
                    'Education': education,
                    'EmploymentType': employment,
                    'MaritalStatus': marital_status,
                    'LoanAmount': loan_amount,
                    'InterestRate': interest_rate,
                    'LoanTerm': loan_term,
                    'LoanPurpose': loan_purpose,
                    'CreditScore': credit_score,
                    'DTIRatio': dti_ratio,
                    'MonthsEmployed': months_employed,
                    'NumCreditLines': num_credit_lines,
                    'HasMortgage': has_mortgage,
                    'HasDependents': has_dependents,
                    'HasCoSigner': has_cosigner,
                }
            ]
        )

        with st.spinner("Running prediction through production pipeline..."):
            probs, _ = predict_default(encoder, model, feature_names, applicant)
            prob = probs[0]
            preds = apply_threshold(probs, threshold)
            risk, color = risk_label(prob)
            decision = "Flag for Review" if preds[0] == 1 else "Proceed to Approval"

        with col_outputs:
            with default_placeholder.container():
                c_decision, c_risk, c_prob = st.columns(3)
                c_prob.metric("Default probability", f"{prob:.1%}")
                c_risk.metric("Risk band", risk)
                c_decision.metric("Recommendation", decision)

                if preds[0] == 1:
                    st.error(
                        f"This application exceeds the risk threshold ({threshold:.2f}). "
                        "Recommend escalation to senior credit officer."
                    )
                else:
                    st.success(
                        f"Application is within acceptable risk limits. "
                        f"Default probability {prob:.1%} is below the threshold ({threshold:.2f})."
                    )

        st.markdown("---")
        st.markdown(
            """
            <div class="section-block">
                <div class="section-label">Explainability</div>
                <div class="section-title">What drove this specific decision?</div>
                <div class="section-caption">
                    Positive SHAP contributions push the probability of default higher; negative contributions reduce it.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        exp_col1, exp_col2 = st.columns([1.6, 1.0], gap="large")

        with exp_col1:
            with st.spinner("Generating SHAP waterfall explanation..."):
                fig, _ = shap_waterfall_fig(encoder, model, feature_names, applicant)
            st.pyplot(fig)
            plt.close(fig)
            
        with exp_col2:
            with st.expander("View submitted applicant record", expanded=True):
                # We add .astype(str) so Arrow treats everything uniformly
                st.dataframe(
                    applicant.T.rename(columns={0: 'Value'}).astype(str),
                    width="stretch",
                )