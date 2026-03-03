# MindEase — Mental Health Chatbot

A conversational mental health assistant powered by a fine-tuned large language model. MindEase provides a private, empathetic space for users to express their feelings and receive supportive responses.

---

## Overview

MindEase is built on a causal language model fine-tuned specifically for mental health conversations. The application exposes a clean, distraction-free chat UI via Streamlit and can be run locally or deployed as a Docker container.

| Component | Technology |
|-----------|-----------|
| Model | [`huzaifashahid/mental-health-bot`](https://huggingface.co/huzaifashahid/mental-health-bot) (Hugging Face) |
| Inference | Hugging Face `transformers` + PyTorch |
| Frontend | Streamlit (custom dark theme) |
| Containerization | Docker |

---

## Project Structure

```
LLM_Project/
├── app/
│   ├── chatbot.py          # Model loading & response generation logic
│   └── streamlit_app.py    # Streamlit chat UI
├── models/                 # (Optional) local model cache
├── notebooks/
│   └── Fine_tuning.ipynb   # Fine-tuning experiment notebook
├── Dockerfile              # Container build instructions
├── requirements.txt        # Python dependencies
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10 or 3.11
- pip
- (Optional) Docker

---

### 1. Local Setup

**Clone the repository**

```bash
git clone https://github.com/huzaifashahid2003/mental-health-chatbot-finetuned
```

**Create and activate a virtual environment**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

**Install dependencies**

```bash
pip install -r requirements.txt
```

**Run the app**

```bash
streamlit run app/streamlit_app.py
```

The app will be available at `http://localhost:8501`.

---

### 2. Docker Setup

**Build the image**

```bash
docker build -t mindease .
```

**Run the container**

```bash
docker run -p 8501:8501 mindease
```

Open `http://localhost:8501` in your browser.

---

## How It Works

1. **Model Loading** — `chatbot.py` lazily loads the fine-tuned causal LM from Hugging Face Hub on the first user message.
2. **Prompt Construction** — Each user message is formatted as:
   ```
   User: <message>
   Bot:
   ```
3. **Text Generation** — The model generates a response using nucleus sampling (`temperature=0.7`) with repetition penalties to keep replies coherent and non-repetitive.
4. **UI** — `streamlit_app.py` maintains a conversation history in `st.session_state` and renders a bubble-style chat interface with a dark Catppuccin Mocha-inspired theme.

---

## Model Details

| Parameter | Value |
|-----------|-------|
| Model ID | `huzaifashahid/mental-health-bot` |
| Architecture | Causal LM (GPT-style) |
| Max input length | 256 tokens |
| Max new tokens | 100 |
| Temperature | 0.7 |
| Repetition penalty | 1.8 |
| No-repeat n-gram size | 3 |

The model was fine-tuned on mental health dialogue data. See `notebooks/Fine_tuning.ipynb` for the full training pipeline.

---

## Dependencies

```
sentence-transformers >= 2.7.0
numpy               >= 1.24.0
pandas              >= 2.0.0
streamlit           >= 1.35.0
python-dotenv       >= 1.0.0
torch               >= 2.1.0
transformers        (latest)
```

> **GPU support:** The default `requirements.txt` installs the CPU wheel of PyTorch. For GPU inference, replace the `torch` entry with the appropriate CUDA wheel from [pytorch.org](https://pytorch.org/get-started/locally/).

---

## Fine-Tuning

The `notebooks/Fine_tuning.ipynb` notebook documents the complete fine-tuning workflow:

- Dataset preparation and preprocessing
- Tokenization
- Training configuration (learning rate, epochs, batch size)
- Evaluation and model upload to Hugging Face Hub

---

## Configuration

Environment variables can be placed in a `.env` file at the project root (loaded via `python-dotenv`):

```env
# Example — add any API keys or custom settings here
HUGGINGFACE_TOKEN=your_token_here
```

---

## Disclaimer

MindEase is an AI assistant intended for **general emotional support only**. It is **not** a substitute for professional mental health care. If you or someone you know is in crisis, please contact a licensed mental health professional or a crisis helpline.

---

## Author

**Huzaifa Shahid** — [Hugging Face](https://huggingface.co/huzaifashahid)
