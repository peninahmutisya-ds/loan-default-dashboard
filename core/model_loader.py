import joblib
import sys
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


class LoanEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, binary_cols=None, education_map=None, ohe_cols=None):
        self.binary_cols = binary_cols or ['HasMortgage', 'HasDependents', 'HasCoSigner']
        self.education_map = education_map or {
            'High School': 0, "Bachelor's": 1, "Master's": 2, 'PhD': 3
        }
        self.ohe_cols = ohe_cols or ['EmploymentType', 'MaritalStatus', 'LoanPurpose']

    def fit(self, X, y=None):
        X_ = self._apply_binary(X.copy())
        X_ = self._apply_ordinal(X_)
        self.ohe_ = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
        self.ohe_.fit(X_[self.ohe_cols])
        self.ohe_feature_names_ = self.ohe_.get_feature_names_out(self.ohe_cols).tolist()
        return self

    def transform(self, X, y=None):
        X_ = self._apply_binary(X.copy())
        X_ = self._apply_ordinal(X_)
        ohe_array = self.ohe_.transform(X_[self.ohe_cols])
        ohe_df    = pd.DataFrame(ohe_array, columns=self.ohe_feature_names_, index=X_.index)
        X_        = X_.drop(columns=self.ohe_cols)
        X_        = pd.concat([X_, ohe_df], axis=1)
        bool_cols = X_.select_dtypes(include='bool').columns
        X_[bool_cols] = X_[bool_cols].astype(int)
        return X_

    def _apply_binary(self, X_):
        for col in self.binary_cols:
            X_[col] = X_[col].map({'Yes': 1, 'No': 0})
        return X_

    def _apply_ordinal(self, X_):
        X_['Education'] = X_['Education'].map(self.education_map)
        return X_


sys.modules['__main__'].LoanEncoder = LoanEncoder


def load_model():
    bundle = joblib.load("model.pkl")
    return bundle['pipeline'], bundle['threshold'], bundle['feature_names']