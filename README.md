
# True-Echo-AI


Key Fraud Risks
Voice Spoofing & Deepfakes – AI can copy someone’s voice so well that it fools security checks and even customer service agents.

Advanced Phishing Attacks – Fake emails look very real and are carefully designed to trick people into sharing private information.

Financial Risk – Just one fake impersonation can cause big money losses and harm the company’s reputation.

Multi-Channel Attacks – Scammers use more than one method (like email + phone call) together, making them harder to catch if systems don’t share information.

This project consists of 3 modules to detect fraudulent content across three communication mediums:
  1)Audio Emails (voice messages)
  2)SMS (text messages)
  3)Emails (phishing detection)

The three main modules are as follows:
  1)Audio Spam Detection
  Dataset: Fake-or-Real (FoR) Audio Dataset
  Input: .wav audio samples (raw waveform)
  Model: Wav2Vec2 (fine-tuned)
  Output: Real / Fake 

  2)SMS Spam Detection
  Dataset: SMS Spam Collection Dataset (Kaggle)
  Input: SMS message text
  Model: SVM classifier with TF-IDF vectorization
  Output: Spam / Ham
  
  3)Email Phishing Detection
  Dataset: Kaggle – Phishing Email Dataset
  Input: Email body, subject line, sender domain
  Model: SVM classifier with TF-IDF vectorization
  Output: Spam/ Ham
