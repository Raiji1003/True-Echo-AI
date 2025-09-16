
import joblib
import librosa
import torch
import torch.nn.functional as F
from transformers import Wav2Vec2Processor, Wav2Vec2ForSequenceClassification
import streamlit as st
from datetime import datetime

# =======================
# Load Models
# =======================

# ---- Email Model ----
email_pipeline = joblib.load("/content/drive/MyDrive/Colab Notebooks/email_pipeline.pkl")

def process_email(email_text: str):
    pred = email_pipeline.predict([email_text])[0]
    proba = email_pipeline.predict_proba([email_text])[0]
    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input": email_text,
        "prediction": "SPAM" if pred == 1 else "NON-SPAM",
        "spam_probability": float(proba[1]),
        "nonspam_probability": float(proba[0])
    }

# ---- SMS Model ----
sms_model_data = joblib.load("/content/drive/MyDrive/sms_mufg_combined.pkl")
sms_svc = sms_model_data['svc']
sms_tfidf = sms_model_data['tfidf']

def process_sms(sms_text: str):
    sms_features = sms_tfidf.transform([sms_text]).toarray()
    prediction = sms_svc.predict(sms_features)[0]
    probabilities = sms_svc.predict_proba(sms_features)[0]
    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input": sms_text,
        "prediction": "SPAM" if prediction == 1 else "NOT SPAM",
        "spam_probability": float(probabilities[1]),
        "nonspam_probability": float(probabilities[0])
    }

# ---- Audio Model ----
checkpoint = "facebook/wav2vec2-base"
processor = Wav2Vec2Processor.from_pretrained(checkpoint)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Wav2Vec2ForSequenceClassification.from_pretrained(
    checkpoint,
    num_labels=2,
    gradient_checkpointing=True,
    attention_dropout=0.1,
    hidden_dropout=0.1,
    feat_proj_dropout=0.1,
    mask_time_prob=0.05
).to(device)

def process_audio(file):
    speech, sr = librosa.load(file, sr=16000)
    inputs = processor(speech, sampling_rate=16000, return_tensors="pt", padding=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        logits = model(**inputs).logits
        probs = F.softmax(logits, dim=-1)

    real_prob = probs[0][0].item()
    fake_prob = probs[0][1].item()

    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input": file.name,
        "prediction": "REAL" if fake_prob < real_prob else "FAKE",
        "REAL_probability": real_prob,
        "FAKE_probability": fake_prob
    }

# =======================
# Streamlit UI with Tabs
# =======================
st.title("📊 True Echo AI")

# Initialize session state with history lists
if "email_results" not in st.session_state:
    st.session_state.email_results = []
if "sms_results" not in st.session_state:
    st.session_state.sms_results = []
if "audio_results" not in st.session_state:
    st.session_state.audio_results = []

tab1, tab2, tab3, tab4 = st.tabs(["📧 Email", "📱 SMS", "🎤 Audio", "📊 Dashboard"])

# ========== EMAIL ==========
with tab1:
    st.header("Email Classification")
    text_input = st.text_area("Paste your email here:", height=200)
    if st.button("Classify Email"):
        if text_input.strip():
            result = process_email(text_input)
            st.session_state.email_results.append(result)
            st.success("✅ Email classified!")
            st.json(result)  # show latest result instantly
        else:
            st.warning("⚠️ Please enter some text.")

# ========== SMS ==========
with tab2:
    st.header("SMS Classification")
    sms_input = st.text_area("Enter your SMS here:", height=150)
    if st.button("Classify SMS"):
        if sms_input.strip():
            result = process_sms(sms_input)
            st.session_state.sms_results.append(result)
            st.success("✅ SMS classified!")
            st.json(result)  # show latest result instantly
        else:
            st.warning("⚠️ Please enter an SMS message.")

# ========== AUDIO ==========
with tab3:
    st.header("Audio Classification")
    uploaded_file = st.file_uploader("Upload a .wav file", type=["wav"])
    if uploaded_file is not None and st.button("Classify Audio"):
        result = process_audio(uploaded_file)
        st.session_state.audio_results.append(result)
        st.success("✅ Audio classified!")
        st.json(result)  # show latest result instantly

# ========== DASHBOARD ==========
with tab4:
    st.header("📊 Dashboard Summary")

    if (len(st.session_state.email_results) == 0 and
        len(st.session_state.sms_results) == 0 and
        len(st.session_state.audio_results) == 0):
        st.info("No results yet. Please classify something in other tabs.")
    else:
        if len(st.session_state.email_results) > 0:
            st.subheader("📧 Email Results (History)")
            for res in reversed(st.session_state.email_results):
                st.json(res)

        if len(st.session_state.sms_results) > 0:
            st.subheader("📱 SMS Results (History)")
            for res in reversed(st.session_state.sms_results):
                st.json(res)

        if len(st.session_state.audio_results) > 0:
            st.subheader("🎤 Audio Results (History)")
            for res in reversed(st.session_state.audio_results):
                st.json(res)

        if st.button("🗑️ Clear All History"):
            st.session_state.email_results.clear()
            st.session_state.sms_results.clear()
            st.session_state.audio_results.clear()
            st.success("History cleared!")
