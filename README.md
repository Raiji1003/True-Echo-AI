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

## 📂 File Structure  

├── README.md # Project documentation 
├── Requirement.txt # Dependencies and packages 
├── app.py # Main application script (integration entry point) 
├── email_pipeline.pkl # Pre-trained email phishing detection pipeline 
├── True_Echo_AI.ipynb # Notebook for Audio Spam Detection (Wav2Vec2) 
├── wave2vec2 (2).ipynb # Another notebook for audio classification 
├── sms_spam_p1_mufg.ipynb # Notebook for SMS spam detection (TF-IDF + SVM) 
├── mufg_email (1).ipynb # Notebook for Email phishing detection (TF-IDF + SVM) 
├── sms_mufg_combined.zip # SMS dataset (compressed) 
├── True Echo AI (screencast).mp4 # Demo video of project


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

## 🚀 Getting Started  

### 📌 Prerequisites  
Install required dependencies:  

```bash
pip install -r Requirement.txt
flask run

## Screenshots
<img width="595" height="582" alt="Screenshot 2025-09-18 232405" src="https://github.com/user-attachments/assets/e7c594c3-5132-4953-a5e9-c0f0ea0759fc" />
<img width="753" height="697" alt="Screenshot 2025-09-18 232527" src="https://github.com/user-attachments/assets/dcae38c0-2043-4dfa-b9d0-d345acb05083" />
![WhatsApp Image 2025-09-16 at 21 38 59_9d9a4288](https://github.com/user-attachments/assets/fe5b4cf1-b346-4117-ba99-695deeead56f)
![WhatsApp Image 2025-09-16 at 21 39 16_9ebdd1d5](https://github.com/user-attachments/assets/447cd2d3-21e3-40f6-9f81-50bf31f07497)

