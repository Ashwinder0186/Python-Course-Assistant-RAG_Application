# 🐍 Python Course Assistant - RAG Application

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![RAG](https://img.shields.io/badge/RAG-Enabled-purple.svg)

**An intelligent AI-powered assistant that answers questions about Python programming using Retrieval-Augmented Generation (RAG)**

[Demo](#demo) • [Features](#features) • [Installation](#installation) • [Usage](#usage) • [Architecture](#architecture)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Demo](#demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **Python Course Assistant** is a production-ready RAG (Retrieval-Augmented Generation) application that helps users learn Python programming by providing contextual answers from video course content. The system automatically processes YouTube playlists, transcribes audio, creates embeddings, and uses semantic search to retrieve relevant information.

This project demonstrates proficiency in:
- **Natural Language Processing (NLP)**
- **Vector Embeddings & Semantic Search**
- **RAG Architecture Implementation**
- **Full-Stack ML Application Development**
- **API Integration & Deployment**

---

## 🎥 Demo

<div align="center">

### Chat Interface
*Ask questions and get instant, contextual answers with video references*

### Video References with Timestamps
*Direct links to specific moments in course videos*

</div>

---

## ✨ Features

### 🤖 Core Functionality
- **Intelligent Q&A System**: Natural language understanding for Python-related queries
- **Semantic Search**: Uses BGE-M3 embeddings for accurate context retrieval
- **Video Reference System**: Provides precise timestamps for video content
- **Conversational Interface**: Chat-based UI with conversation history

### 🔧 Technical Features
- **Automated Pipeline**: End-to-end automation from YouTube to deployment
- **Embedding Generation**: Utilizes Ollama's BGE-M3 model for vector representations
- **Efficient Retrieval**: Cosine similarity-based search with top-k results
- **LLM Integration**: GPT-4o via OpenRouter for response generation
- **Scalable Architecture**: Modular design for easy extension

---

## 🛠️ Tech Stack

### Machine Learning & NLP
- **Embeddings**: BGE-M3 (via Ollama)
- **LLM**: GPT-4o (via OpenRouter API)
- **Vector Search**: Scikit-learn (Cosine Similarity)
- **Audio Processing**: OpenAI Whisper

### Backend & Data Processing
- **Framework**: Streamlit
- **Data Manipulation**: Pandas, NumPy
- **Serialization**: Joblib
- **HTTP Requests**: Requests library

### External Services
- **Video Processing**: yt-dlp
- **Transcription**: Whisper (Base Model)
- **LLM API**: OpenRouter

---

## 🏗️ Architecture

```
┌─────────────────┐
│  YouTube Video  │
│    Playlist     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   yt-dlp        │
│ Audio Extract   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Whisper       │
│  Transcription  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   BGE-M3        │
│   Embeddings    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Vector Store   │
│   (Joblib)      │
└────────┬────────┘
         │
         ▼
    ┌────┴────┐
    │  Query  │
    └────┬────┘
         │
         ▼
┌─────────────────┐
│ Semantic Search │
│ (Top-K Results) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   GPT-4o via    │
│   OpenRouter    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Response     │
│  with Sources   │
└─────────────────┘
```

---

## 📥 Installation

### Prerequisites
- Python 3.8 or higher
- Ollama installed locally ([Installation Guide](https://ollama.ai/))
- OpenRouter API key ([Get it here](https://openrouter.ai/))

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ashwinder0186/python-course-assistant.git
cd python-course-assistant
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Install Ollama Model
```bash
ollama pull bge-m3
```

### Step 4: Set Up API Keys
Create a `.env` file or update `app.py` with your OpenRouter API key:
```python
api_key = "your-openrouter-api-key-here"
```

### Step 5: Download and Process Course Data
```bash
# Download videos
jupyter notebook Yt_to_mp3.ipynb

# Transcribe audio
jupyter notebook mp3_to_Json.ipynb

# Generate embeddings
jupyter notebook Json_to_embeddings.ipynb
```

---

## 🚀 Usage

### Running the Application
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Using the Assistant
1. Type your Python-related question in the chat input
2. Receive detailed answers with:
   - Conceptual explanations
   - Video references (number, title, timestamp)
   - Recommendations for related content

### Example Queries
- "How do I use lists in Python?"
- "Explain dictionaries with examples"
- "What are user-defined functions?"
- "How to iterate over a list?"

---

## 📁 Project Structure

```
python-course-assistant/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
│
├── Yt_to_mp3.ipynb            # YouTube playlist downloader
├── mp3_to_Json.ipynb          # Audio transcription
├── Json_to_embeddings.ipynb   # Embedding generation
├── Emb_to_RAG.ipynb           # RAG testing notebook
│
├── audios/                     # Downloaded audio files
├── jsons/                      # Transcription outputs
├── embeddings.joblib           # Serialized embeddings
│
└── README.md                   # This file
```

---

## 🔍 How It Works

### 1. Data Collection
- Downloads audio from YouTube playlist using yt-dlp
- Extracts audio in MP3 format for each video
- Currently processes **24 Python course videos** from [this playlist](https://www.youtube.com/playlist?list=PLYmlEoSHldN46dpxzEgcG83VxcEr_L9zq)

### 2. Transcription
- Uses Whisper base model to transcribe audio
- Creates timestamped segments for precise referencing
- Outputs structured JSON files

### 3. Embedding Generation
- Processes transcripts through BGE-M3 model
- Generates 1024-dimensional vector embeddings
- Stores embeddings with metadata in Joblib format

### 4. Query Processing
- User query is embedded using the same BGE-M3 model
- Cosine similarity computed against all stored embeddings
- Top-5 most relevant chunks retrieved

### 5. Response Generation
- Retrieved context sent to GPT-4o via OpenRouter
- LLM generates comprehensive answer with:
  - Direct answer to question
  - Video references with timestamps
  - Learning recommendations

---

## 🔮 Future Enhancements

- [ ] **Multi-Course Support**: Expand to support multiple programming courses (JavaScript, Java, Data Science) from different YouTube playlists, creating a comprehensive learning assistant
- [ ] **Dynamic Course Addition**: Implement a feature to add new courses dynamically through the UI without reprocessing the entire dataset
- [ ] **Cross-Course Learning**: Enable the system to draw connections between different courses and provide comparative explanations (e.g., "Python lists vs JavaScript arrays")
- [ ] **Advanced Retrieval**: Implement hybrid search combining dense embeddings with keyword-based sparse retrieval for improved accuracy
- [ ] **Fine-Tuned Embeddings**: Train custom embedding models specifically optimized for educational content and programming concepts
- [ ] **Multi-Modal Support**: Add support for code snippets, diagrams, and slides from videos
- [ ] **Interactive Code Execution**: Integrate code sandbox for users to test Python examples directly
- [ ] **Progress Tracking**: User learning path and completion tracking across multiple courses
- [ ] **Quiz Generation**: Automatically generate practice questions from course content
- [ ] **Docker Deployment**: Containerized application for easy deployment and scalability

---

## 📊 Performance Metrics

- **Average Query Time**: ~2-3 seconds
- **Embedding Dimension**: 1024
- **Retrieval Accuracy**: Top-5 relevant chunks
- **Current Dataset**: 24 Python course videos
- **Total Embeddings**: ~500+ chunks
- **Supported Topics**: Python basics, data structures, functions, loops, OOP

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Ashwinder Singh**
- **GitHub**: [@Ashwinder0186](https://github.com/Ashwinder0186)
- **LinkedIn**: [singh-ashwinder](https://linkedin.com/in/singh-ashwinder)
- **Email**: singhashwinder0186@gmail.com
- **Education**: MS in Computer Science, University of Texas at Arlington (GPA: 4.0/4.0)

### Background
Data-driven Software Developer with 2+ years of experience in quantitative analytics, machine learning, and financial technology solutions. Previously worked at Tata Consultancy Services developing Python-based automation tools for JPMorgan Chase financial systems.

---

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for transcription
- [Ollama](https://ollama.ai/) for local embedding generation
- [OpenRouter](https://openrouter.ai/) for LLM API access
- [Streamlit](https://streamlit.io/) for the web framework
- Course content from [Learn Python Playlist](https://www.youtube.com/playlist?list=PLYmlEoSHldN46dpxzEgcG83VxcEr_L9zq)

---

<div align="center">

**⭐ If you found this project helpful, please consider giving it a star!**

Made with ❤️ and Python

</div>