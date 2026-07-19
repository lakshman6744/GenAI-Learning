# Topic-01: First LLM API using Groq

## 📌 Project Overview

This project demonstrates how to build a simple Large Language Model (LLM) application using the **Groq API** with Python. It sends a user prompt to the LLM and displays the generated response in the terminal.

---

## 🚀 Features

- Connects to the Groq API
- Uses Python SDK
- Loads API key securely from a `.env` file
- Accepts user input
- Displays AI-generated responses

---

## 🛠️ Tech Stack

- Python 3.x
- Groq API
- python-dotenv

---

## 📁 Project Structure

```
Topic-01-LLM-API/
│── app.py
│── .env          (Not uploaded to GitHub)
│── requirements.txt
│── README.md
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/lakshman6744/GenAI-Learning.git
```

### 2. Go to the project folder

```bash
cd GenAI-Learning/Topic-01-LLM-API
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the project folder.

```env
GROQ_API_KEY=your_api_key_here
```

> **Note:** Never upload your `.env` file to GitHub.

---

## ▶️ Run the Project

```bash
python app.py
```

Example:

```
Ask your question:

What is Artificial Intelligence?
```

Example Output:

```
Artificial Intelligence (AI) is the simulation of human intelligence by machines...
```

---

## 📚 Learning Outcomes

After completing this project, you will understand:

- How to use the Groq API
- How to make API requests
- How to use environment variables
- Basic prompt-response workflow
- Python project structure

---

## 👨‍💻 Author

**Lakshman Parpatakam**

GitHub: https://github.com/lakshman6744
