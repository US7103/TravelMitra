# 🧳 Travel Mitra

**Travel Mitra** is your AI-powered travel planner designed to help you plan unforgettable and budget-friendly trips across India!  
Interact with a friendly chatbot UI to get instant, personalized trip suggestions, itineraries, and travel tips—whether you want a quick city break, a cultural tour, or an adventure-packed getaway.

---

## ✨ Features

- **Conversational AI**: Chat with "Mitra", your personal travel assistant, for recommendations and planning.
- **Budget Planning**: Get suggestions tailored to your budget and preferences.
- **Indian Destinations**: Specialized for exploring destinations all across India.
- **User-friendly Interface**: Beautiful and responsive UI built with Streamlit.
- **Custom AI Model**: Integrates with Ollama and custom fine-tuned models for Indian travel data.

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/US7103/TravelMitra.git
cd TravelMitra
```

### 2. Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Requests](https://docs.python-requests.org/)
- Ollama (for running local LLMs): https://ollama.com/

Install dependencies:

```bash
pip install -r requirements.txt
```
*(Create `requirements.txt` if not present: `streamlit requests`)*

### 3. Set Up Ollama Model

- Place your model file, e.g. `ModelFile`, in the project directory.
- Create a new model in Ollama:

  ```bash
  ollama create TRAVELMITRA -f ModelFile
  ```

- Run the model with your data:

  ```bash
  ollama run TRAVELMITRA < indiandata.jsonl
  ```

  *(Make sure your data is in JSONL format.)*

### 4. Launch the TravelMitra UI

```bash
cd Ready
streamlit run ollamachat.py
```

The web UI should open in your browser. Start chatting and planning your next trip!

---

## 🏗 Project Structure

```
TravelMitra/
├── Ready/
│   └── ollamachat.py        # Main Streamlit chat UI
├── ModelFile                # (Your Ollama model file)
├── indiandata.jsonl         # (Travel data for fine-tuning)
├── Readme.txt               # Technical quick notes
└── README.md                # You're reading it!
```

---

## 🧩 How It Works

- The chat UI (`Ready/ollamachat.py`) uses Streamlit for a modern, interactive web experience.
- Messages are sent to a locally running Ollama server (`http://localhost:11434/api/chat`).
- The backend leverages a custom model called **TravelMitra** trained on Indian travel data.
- The assistant ("Mitra") guides users in planning trips, suggesting itineraries, and answering travel queries.

---

## 💡 Example Usage

> **You:** Plan a 3-day trip from Jaipur to Mumbai  
> **Mitra:** (Shows a day-wise plan, places to visit, and estimated costs)

---

## 🛠 Customization

- **Model:** Swap or fine-tune your own LLM with Ollama.
- **Data:** Replace `indiandata.jsonl` with your own travel dataset.
- **UI:** Tweak the Streamlit app for additional features or different themes.

---

## ❤️ Credits

Built with [Streamlit](https://streamlit.io/) and [Ollama](https://ollama.com/).  
Crafted by Travel Mitra · Explore India your way! 🌏

---

## 📄 License

This project is for personal or educational use. Please check with the author before using for commercial purposes.

---

*Ready to explore India? Fire up Travel Mitra and let the journey begin!*

