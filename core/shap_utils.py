import matplotlib.pyplot as plt
import pandas as pd
import shap  # pyright: ignore[reportMissingImports]


def shap_waterfall_fig(encoder, model, feature_names, row_df: pd.DataFrame):
    X_enc = encoder.transform(row_df.copy())
    X_enc = X_enc.reindex(columns=feature_names, fill_value=0)
    explainer = shap.TreeExplainer(model)
    shap_vals = explainer.shap_values(X_enc)
    prob = model.predict_proba(X_enc)[:, 1][0]

    if isinstance(shap_vals, list):
        sv_default = shap_vals[1][0]
        base_val = explainer.expected_value[1]
    else:
        sv_default = shap_vals[0, :, 1]
        base_val = explainer.expected_value[1]

    shap_exp = shap.Explanation(
        values=sv_default,
        base_values=base_val,
        data=X_enc.iloc[0].values,
        feature_names=feature_names,
    )
    fig, _ = plt.subplots(figsize=(9, 5))
    shap.waterfall_plot(shap_exp, show=False)
    plt.title(f'SHAP Explanation  |  Predicted Default Probability: {prob:.1%}')
    plt.tight_layout()
    return fig, prob
def feature_importance_fig(model, feature_names):
    imp_df = (
        pd.DataFrame({'Feature': feature_names, 'Importance': model.feature_importances_})
        .sort_values('Importance', ascending=True)
    )
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(imp_df['Feature'], imp_df['Importance'], color='steelblue')
    ax.set_xlabel('Importance)')
    ax.set_title('Feature Importance — Random Forest')
    plt.tight_layout()
    return fig


def shap_batch_fig(encoder, model, feature_names, batch_df: pd.DataFrame, sample_size: int = 200):
    sample = batch_df.sample(min(sample_size, len(batch_df)), random_state=42)
    X_enc = encoder.transform(sample.copy())
    X_enc.columns = feature_names
    explainer = shap.TreeExplainer(model)
    sv = explainer.shap_values(X_enc)
    sv_d = sv[1] if isinstance(sv, list) else sv[:, :, 1]
    fig, _ = plt.subplots(figsize=(9, 5))
    shap.summary_plot(sv_d, X_enc, feature_names=feature_names, show=False)
    plt.title('SHAP Summary — Batch')
    plt.tight_layout()
    return fig