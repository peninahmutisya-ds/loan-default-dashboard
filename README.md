Loan Default Risk Assessment Dashboard
Project Overview
The Loan Default Risk Assessment Dashboard is a machine learning–powered decision support system designed to help financial institutions evaluate borrower risk and predict the likelihood of loan default.
This project combines a trained credit risk model with an interactive Streamlit dashboard that allows banks and SACCOs to assess both individual applicants and entire customer portfolios in real time.
The system focuses on improving lending decisions through data-driven risk analysis while maintaining model transparency and usability for non-technical users.

Problem Statement
Financial institutions face significant losses due to loan defaults caused by inaccurate risk evaluation and manual assessment processes. Traditional credit evaluation methods may fail to capture complex relationships between borrower characteristics and repayment behavior.

This project aims to:
- Predict loan default probability using machine learning
- Provide interpretable insights for credit officers
- Support faster and more consistent lending decisions

The application provides an interactive dashboard where users can:
- Enter borrower information manually
- Upload datasets for batch risk evaluation
- View default probability scores
- Classify borrowers into risk categories
- Understand model decisions through explainability tools

The machine learning model remains unchanged during deployment and is used strictly for inference.
Key Features
- Individual Loan Assessment
- Manual borrower input form
- Real-time prediction
- Default probability score
- Risk classification indicator
- Batch Processing
- CSV and spreadsheet uploads
- Individual predictions for each borrower
- Portfolio risk analysis
- Explainable AI
- Feature contribution visualization
- Transparent model reasoning
- Supports trust in automated decisions
- Professional Dashboard UI
- Banking-style interface
- Modular architecture
- Clean and scalable code structure
- Machine Learning Model

The model pipeline includes:
- Custom preprocessing encoder (LoanEncoder)
- Binary and ordinal feature encoding
- One-hot encoding for categorical variables
- Feature alignment validation
- Random Forest Classifier
- Optimized decision threshold

The trained model is stored as a serialized pipeline (model.pkl) and loaded directly by the application.

Programming & Data Analysis
- Python: Core programming language.
- Pandas: Data manipulation, cleaning, and DataFrame management.
- NumPy: Numerical computing and array operations.

Machine Learning & Explainability (XAI)
- Scikit-learn: Implementation of the Random Forest classifier and preprocessing pipelines.
- SHAP (Shapley Additive Explanations): Model interpretability for global and local (individual applicant) risk drivers.
- Joblib: Serialization and loading of the production model and encoder bundles.

Web Application & UI
- Streamlit: Framework for building the interactive risk assessment dashboard.
- HTML5 & CSS3: Custom interface styling and layout injection for a fintech-grade user experience.
- Matplotlib: Generation of risk distribution charts and analytical visualizations.

