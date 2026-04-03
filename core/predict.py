import numpy as np
import pandas as pd


def predict_default(encoder, model, feature_names, input_df: pd.DataFrame):
    X_enc = encoder.transform(input_df.copy())
    X_enc = X_enc.reindex(columns=feature_names, fill_value=0)

    probs = model.predict_proba(X_enc)[:, 1]
    preds = (probs >= 0).astype(int)  # placeholder, will be overridden

    # Thresholding is intentionally performed outside this function
    return probs, preds  # preds will not be used from here directly


def apply_threshold(probs: np.ndarray, threshold: float):
    preds = (probs >= threshold).astype(int)
    return preds