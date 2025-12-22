import streamlit as st
import joblib
import nltk
import os
NLTK_DIR = os.path.join(os.getcwd(), "nltk_data")
nltk.data.path.append(NLTK_DIR)

@st.cache_resource
def download_nltk():
    nltk.download("punkt", download_dir=NLTK_DIR, quiet=True)
    nltk.download("stopwords", download_dir=NLTK_DIR, quiet=True)

download_nltk()
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer




ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    
    tokens = [
        ps.stem(word)
        for word in tokens
        if word.isalnum() and word not in stop_words
    ]
    
    return " ".join(tokens)

# Load trained pipeline
model = joblib.load("phishing_model.pkl")

# Page config
st.set_page_config(
    page_title="Phishing Email Detector",
    page_icon="🚨",
    layout="centered"
)

# ---------- UI STYLING (NO LOGIC CHANGE) ----------
st.markdown("""
<style>

/* =======================
   APP BACKGROUND
======================= */
.stApp {
    background: #020617;
}

/* =======================
   SIDEBAR
======================= */
section[data-testid="stSidebar"] {
    background: #080e20;
    backdrop-filter: blur(18px);
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}



/* =======================
   TITLES & HEADINGS
======================= */




[data-testid="stMarkdown"] h2 {
    
    color: #3C82F6 !important;
   
}



/* =======================
   TEXT / PARAGRAPHS
======================= */
[data-testid="stMarkdown"] p {
    font-size: 0.95rem;
    line-height: 1.65;
    color: #cbd5e1;
}

/* =======================
   TEXT AREA
======================= */
textarea[data-testid="stTextArea"] {
    background: rgba(255,255,255,0.06) !important;
    color: #f8fafc !important;
    border-radius: 16px !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    padding: 16px !important;
    font-size: 15px !important;
}

textarea[data-testid="stTextArea"]:focus {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 0 2px rgba(56,189,248,0.3);
}

/* =======================
   BUTTON (st.button)
======================= */
div[data-testid="stButton"] > button {
    background: #3C82F6 !important;
    color: white !important;
    border-radius: 16px !important;
    padding: 0.65rem 1.6rem !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    border: none !important;
    transition: all 0.25s ease;
}

div[data-testid="stButton"] > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 10px 28px rgba(56,189,248,0.45);
}

div[data-testid="stButton"] > button:active {
    transform: scale(0.97);
}
      





</style>
""", unsafe_allow_html=True)


with st.sidebar:
    

    st.markdown("## 🛡️ Project Overview")
    st.write(
        """
        This application detects **phishing emails** using 
        **machine learning and natural language processing (NLP)**.
        

        """
    )
    st.markdown("---")
    st.markdown("## ⚙️ Model Details")
    st.write(
        """
        **Algorithm:** Linear Support Vector Classifier (LinearSVC)  
        **Vectorization:** TF-IDF  
        **Preprocessing:**  
        - Lowercasing  
        - Tokenization  
        - Stopword removal  
        - Stemming  
        """
    )
    st.markdown("---")
    st.markdown("## 📈 Model Performance")
    st.write(
        """
        - **Accuracy:** ~98%  
        - **Recall (Phishing):** ~98%  
        
        Recall is prioritized to ensure that phishing emails
        are rarely misclassified as legitimate.
        """
    )
    st.markdown("---")
    st.markdown("## ⚠️ Important Note")
    st.info(
        """
        This tool is intended for **educational and demonstration purposes**.
        Always verify suspicious emails through official channels.
        """
    )

    st.markdown("---")
    st.caption("Built with using Streamlit & Scikit-learn")

# Title & description
st.markdown(
    """
    <h1>
        Stop <span style="color:#3C82F6;">Phishing</span> Before It Strikes.
    </h1>
    """,
    unsafe_allow_html=True
)
st.write(
    "Paste an email message below and the model will predict "
    "whether it is **Phishing** or **Legitimate**."
)

# Text input
email_text = st.text_area(
    "📩 Enter Email Content",
    height=220,
    placeholder="Paste the email text here..."
)

st.markdown(
    "<p style='color: white; background: #192A48 ; padding:12px 16px; "
    "border-radius:12px; font-weight:550; '>"
    "ℹ️ <strong>Note:</strong> For best results, provide a longer email. "
    "Very short messages may reduce detection accuracy."
    "</p>",
    unsafe_allow_html=True
)



import time
# Predict button
if st.button("🔍 Detect"):
    if email_text.strip() == "":
        st.warning("Please enter some email text.")
    else:
        with st.spinner("🔎 Analyzing ..."):
            time.sleep(1.5)  # gives a smooth loading feel
            prediction = model.predict([preprocess(email_text)])[0]

        if prediction == 1:
            st.error("⚠️ Phishing Email Detected!")
        else:
            st.success("✅ Legitimate Email")

# Footer
st.markdown("---")
st.caption("Model: TF-IDF + Linear SVM | Built with Streamlit")
