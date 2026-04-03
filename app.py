import streamlit as st
from core.model_loader import load_model
from ui.styles import inject_global_styles
from ui.header import render_header
from ui.single_view import render_single_applicant
from ui.batch_view import render_batch_assessment
from ui.feature_view import render_feature_importance
import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='sklearn.preprocessing')


st.set_page_config(
    page_title="Loan Default Risk Assessor",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)


@st.cache_resource
def _load_model():
    return load_model()


pipeline, threshold, feature_names = _load_model()
encoder = pipeline.named_steps['encoder']
model = pipeline.named_steps['model']

inject_global_styles()
render_header(threshold)

tab1, tab2, tab3 = st.tabs(
    [
        "Single Applicant Decisioning",
        "Batch File Assessment",
        "Model Drivers & Explainability",
    ]
)

with tab1:
    render_single_applicant(encoder, model, feature_names, threshold)

with tab2:
    render_batch_assessment(encoder, model, feature_names, threshold)

with tab3:
    render_feature_importance(model, feature_names)

    
    


