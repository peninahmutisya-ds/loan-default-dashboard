import pandas as pd
from streamlit.runtime.uploaded_file_manager import UploadedFile


def load_uploaded_table(uploaded_file: UploadedFile) -> pd.DataFrame:
    name = uploaded_file.name.lower()

    if name.endswith(".csv"):
        return pd.read_csv(uploaded_file)
    if name.endswith(".xlsx"):
        return pd.read_excel(uploaded_file)

    raise ValueError("Unsupported file format. Please upload a CSV or Excel (.xlsx) file.")