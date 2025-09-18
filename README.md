# 🔒 True-Echo-AI – Multimodal Fraud Detection System  

A robust AI-powered system that detects fraudulent activities across **Audio, SMS, and Email communications**.  
This project was built to tackle **voice spoofing, phishing emails, and SMS scams** using advanced AI/ML models.  

---

## ⚠️ Key Fraud Risks  
- 🗣️ **Voice Spoofing & Deepfakes** – AI can mimic real voices to fool security checks and customer support.  
- 📧 **Advanced Phishing Attacks** – Fake emails that closely resemble real ones, tricking users into sharing private information.  
- 💰 **Financial Risks** – A single impersonation can lead to massive financial and reputational damage.  
- 🔗 **Multi-Channel Attacks** – Scammers use a combination of email + phone + SMS to bypass isolated detection systems.  

---

## 🧩 Project Modules  

### 🎤 1) Audio Spam Detection  
- **Dataset:** Fake-or-Real (FoR) Audio Dataset  
- **Input:** `.wav` audio samples (raw waveform)  
- **Model:** Fine-tuned **Wav2Vec2** Transformer (Hugging Face)  
- **Output:** Real ✅ / Fake ❌  

### 💬 2) SMS Spam Detection  
- **Dataset:** SMS Spam Collection (Kaggle)  
- **Input:** SMS message text  
- **Model:** **SVM classifier with TF-IDF vectorization**  
- **Output:** Spam 📵 / Ham 📨  

### 📩 3) Email Phishing Detection  
- **Dataset:** Phishing Email Dataset (Kaggle)  
- **Input:** Email body, subject line, sender domain  
- **Model:** **SVM classifier with TF-IDF vectorization**  
- **Output:** Spam ⚠️ / Ham ✔️  

---

## 🛠️ Tech Stack  

**Languages & Frameworks**  
- Python (NumPy, Pandas, Scikit-learn)  
- Hugging Face Transformers (Wav2Vec2)  
- Flask (Backend)  

**ML Models**  
- Wav2Vec2 (Audio classification)  
- SVM + TF-IDF (SMS & Email classification)  

**Tools**  
- Jupyter Notebook  
- Git/GitHub  

---

## ✨ Features  
- 🛡️ Multi-channel fraud detection (Audio, SMS, Email)  
- 🎧 Real-time **voice deepfake detection** using Wav2Vec2  
- 📊 Spam filtering with **TF-IDF + SVM** pipelines  
- 🌐 Unified detection pipeline with Flask backend  

---

## 📊 Results & Insights  
✅ Achieved high accuracy in detecting fraudulent **audio, SMS, and email communications**  
✅ Showed the importance of **multimodal fraud detection systems**  
✅ Built a **scalable pipeline** for real-time deployment  

---

##Screenshots
🎤 Audio Spam Detection
<img width="595" height="582" alt="Screenshot 2025-09-18 232405" src="https://github.com/user-attachments/assets/9c001530-9b98-4345-ab70-0ff490438ef5" />
💬 SMS Spam Detection 
<img width="753" height="697" alt="Screenshot 2025-09-18 232527" src="https://github.com/user-attachments/assets/d6d79a99-1e6a-4fd4-83e9-1c29fa826c3f" />
📩 Email Phishing Detection
![WhatsApp Image 2025-09-16 at 21 38 59_8edeb241](https://github.com/user-attachments/assets/9ff3904a-79f0-4ef9-9244-da1b276ba10b)
![WhatsApp Image 2025-09-16 at 21 39 16_819860f3](https://github.com/user-attachments/assets/cc621cb1-d3c2-4445-8ab2-5e819d4126c8)

## 🚀 Getting Started  

### 📌 Prerequisites  
Install required dependencies:  

```bash
pip install -r Requirement.txt


