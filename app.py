import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import pickle

st.set_page_config(page_title="SARS-CoV-2 AI Screen", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif !important;
    }
    
    /* Sleek Blue-to-Pink Gradient Button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #1E3A8A 0%, #DB2777 100%);
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(219, 39, 119, 0.3);
        color: white;
    }
    
    /* Metric styling */
    [data-testid="stMetricValue"] {
        color: #DB2777 !important;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("🧬 About This Project")
    st.write("Built to accelerate early-stage drug discovery by predicting chemical potency ($pIC_{50}$) before physical lab testing.")
    st.divider()
    st.write("**Tech Stack:**")
    st.write("Python, XGBoost, RDKit, Streamlit, Pandas")
    st.divider()
    st.write("👤 **Syed Mu’azzam**")
    st.write("Bridging Biotechnology & Data Science")

@st.cache_resource
def load_model():
    with open('sars_cov_2_model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

st.title("SARS-CoV-2 3CL-Protease Inhibitor Screen")
st.markdown("Predict the binding affinity of chemical compounds using a machine learning model trained on historical ChEMBL bioassay data.")
st.divider()

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("Target Compound")
    smiles_input = st.text_input("Enter SMILES String:", "CC(=O)Nc1ccc(O)cc1", help="Enter a valid SMILES chemical structure.")
    predict_btn = st.button("Run AI Prediction", use_container_width=True)

with col2:
    st.subheader("Analysis Results")
    if predict_btn:
        mol = Chem.MolFromSmiles(smiles_input)
        
        if mol is None:
            st.error("Invalid SMILES string. Please check the chemical format.")
        else:
            fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
            features = pd.DataFrame([list(fp)])
            features.columns = features.columns.astype(str)
            prediction = model.predict(features)[0]
            
            st.metric(label="Predicted pIC50 Potency", value=f"{prediction:.2f}")
            
            if prediction >= 6.0:
                st.success("High Potential: Strong predicted binding affinity.")
            elif prediction >= 5.0:
                st.warning("Moderate Potential: Weak binding affinity.")
            else:
                st.error("Low Potential: Likely inactive against the target.")
            
            st.markdown("**Molecular Structure:**")
            img = Draw.MolToImage(mol, size=(300, 300))
            st.image(img)
