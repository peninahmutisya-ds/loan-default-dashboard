import os

import matplotlib.pyplot as plt
import streamlit as st

from core.shap_utils import feature_importance_fig


def render_feature_importance(model, feature_names):
    st.markdown(
        """
        <div class="section-block">
            <div class="section-label">Model diagnostics</div>
            <div class="section-title">Feature Importance and Explainability</div>
            <div class="section-caption">
                Global importance views for the deployed model, combining native feature importances and SHAP-based insights.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    upper_col1, upper_col2 = st.columns([1.5, 1.2], gap="large")

    with upper_col1:
        st.markdown(
            """
            <div class="card-quiet">
                <div class="card-header">Global importance</div>
                <div class="card-title">Random Forest built-in importance</div>
                <div class="card-subtitle">
                    Mean decrease in impurity across all trees. Indicates overall contribution of each engineered feature.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        fig4 = feature_importance_fig(model, feature_names)
        st.pyplot(fig4)
        plt.close(fig4)

    with upper_col2:
        st.markdown(
            """
            <div class="card-quiet">
                <div class="card-header">Usage notes</div>
                <div class="card-title">How to read these views</div>
                <div class="card-subtitle">
                    Use built-in importance for model monitoring and feature governance; use SHAP views for deeper
                    interpretability at both portfolio and applicant level.
                </div>
                <div style="font-size:0.8rem;color:#9ca3af;margin-top:0.5rem;">
                    • Built-in importance is model-specific and reflects how frequently features are used in splits.<br/>
                    • SHAP bar charts summarise mean absolute Shapley value per feature across a reference dataset.<br/>
                    • SHAP beeswarm plots show the distribution of feature impact for individual observations.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    shap_col1, shap_col2 = st.columns(2, gap="large")

    with shap_col1:
        st.markdown(
            """
            <div class="card-quiet">
                <div class="card-header">SHAP global bar</div>
                <div class="card-title">Mean absolute SHAP value</div>
                <div class="card-subtitle">
                    Average magnitude of impact each feature has on predicted default probability.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("Based on an offline reference dataset used during model validation.")
        if os.path.exists('shap_bar.png'):
            st.image('shap_bar.png', caption='SHAP bar chart', width="stretch")
        else:
            st.info(
                "File `shap_bar.png` not found. Place the image in the same folder as `app.py` to display the global SHAP bar chart."
            )

    with shap_col2:
        st.markdown(
            """
            <div class="card-quiet">
                <div class="card-header">SHAP beeswarm</div>
                <div class="card-title">Feature impact distribution</div>
                <div class="card-subtitle">
                    For each feature, the spread of SHAP values across many observations.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("Highlights which features drive high and low risk outcomes across a reference sample.")
        if os.path.exists('shap_summary.png'):
            st.image('shap_summary.png', caption='SHAP beeswarm summary', width="stretch")
        else:
            st.info(
                "File `shap_summary.png` not found. Place the image in the same folder as `app.py` to display the SHAP beeswarm summary."
            )