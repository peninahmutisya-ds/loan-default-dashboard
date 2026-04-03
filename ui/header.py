import streamlit as st


def render_header(threshold: float):
    st.markdown(
        f"""
        <div class="top-nav">
            <div class="top-nav-left">
                <div class="brand-pill">CRI</div>
                <div class="brand-title">
                    <div class="brand-title-main">CREDIT RISK INTELLIGENCE</div>
                    <div class="brand-title-sub">Loan Default Decision Platform</div>
                </div>
            </div>
            <div class="top-nav-right">
                <div class="metric-pill">
                    <div>
                        <div class="metric-pill-label">Decision Threshold</div>
                        <div class="metric-pill-value">{threshold:.2f}</div>
                    </div>
                </div>
                <div class="metric-pill">
                    <div>
                        <div class="metric-pill-label">Model</div>
                        <div class="metric-pill-value">Random Forest</div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="page-header">
            <div class="page-title-block">
                <div class="page-eyebrow">Credit Risk Operations</div>
                <div class="page-title">Loan Default Risk Assessor</div>
                <div class="page-subtitle">
                    Score individual loan applications or entire files against the production default model.
                    Designed for Banks and Saccos.
                </div>
            </div>
            <div class="page-header-right">
                <div class="legend-pill">
                    Risk band thresholds based on predicted probability of default:
                </div>
                <div class="legend-pill">
                    <span class="legend-key">
                        <span class="legend-dot-low"></span>
                        <span>Low &dash; below 20%</span>
                    </span>
                    <span class="legend-key">
                        <span class="legend-dot-med"></span>
                        <span>Medium &dash; 20–40%</span>
                    </span>
                    <span class="legend-key">
                        <span class="legend-dot-high"></span>
                        <span>High &dash; above 40%</span>
                    </span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )