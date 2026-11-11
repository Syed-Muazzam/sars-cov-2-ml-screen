# Machine Learning for Early Drug Discovery (SARS-CoV-2)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sars-cov-2-ai-screen.streamlit.app/)

An end-to-end machine learning web application built to accelerate early-stage drug discovery by predicting chemical binding affinity against the SARS-CoV-2 3CL-Protease target.

### Live Dashboard
**Experience the AI model here:** [SARS-CoV-2 AI Screen](https://sars-cov-2-ai-screen.streamlit.app/)

### Project Overview
Traditional drug discovery is time-consuming and resource-intensive. This project deploys a computational pipeline to screen potential molecular candidates in seconds. By inputting a valid chemical SMILES string, the model predicts the compound's potency ($pIC_{50}$) before physical laboratory synthesis is required, acting as a digital filter for Structure-Based Drug Design (SBDD).

### Methodology & Data
* **Data Source:** Curated historical bioassay data targeting the SARS-CoV-2 3CL-Protease (`CHEMBL1835`) extracted from the ChEMBL database.
* **Feature Engineering:** Transformed raw SMILES strings into digital molecular representations using **1,024-bit Morgan Fingerprints** (radius of 2).
* **Model Architecture:** Trained an **XGBoost Regression** model to predict $pIC_{50}$ values. 
* **Performance:** Achieved an $R^2$ score of 0.62 and an RMSE of 0.79 on unseen test data.

### Tech Stack
* **Core:** Python 3.11, Pandas, NumPy
* **Machine Learning:** Scikit-learn, XGBoost
* **Cheminformatics:** RDKit
* **Deployment:** Streamlit Community Cloud, Git/GitHub

### Author
**Syed Mu’azzam**  
*Bridging Life Sciences & Data*
