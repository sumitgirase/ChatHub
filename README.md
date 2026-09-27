# OpenRouter Chatbot 🤖

A Streamlit-based chat application that connects to [OpenRouter](https://openrouter.ai)'s API, allowing you to chat with multiple AI models (Gemini, GPT, Claude, Llama, and more) through a single unified interface.

## Features

- 💬 Clean, chat-style UI built with Streamlit
- 🔄 Persistent chat history within a session
- 🌐 Access to multiple LLM providers through OpenRouter's OpenAI-compatible API
- 🔑 Simple API key setup via environment variables
- ⚡ Easily swap between models by changing a single variable

## Tech Stack

- **Python**
- **Streamlit** — web app framework
- **OpenAI Python SDK** — used to call OpenRouter's OpenAI-compatible endpoint
- **python-dotenv** — environment variable management

## Setup

1. Clone the repo:
```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```
3. Create a `.env` file in the project root:

OPENROUTER_API_KEY=your_openrouter_api_key_here

4. Get your API key from [OpenRouter](https://openrouter.ai/keys).

5. Run the app:
```bash
   streamlit run app.py
```

## Usage

- Open the app in your browser (Streamlit will give you a local URL).
- Type your question in the chat box.
- The app sends your full conversation history to the selected model and displays the response.
- Change the model anytime by editing the `MODEL_NAME` variable in `app.py` — browse available models at [openrouter.ai/models](https://openrouter.ai/models).

## Configuration

You can control response length and cost by adjusting `max_tokens` in the API call inside `app.py`.

## Attribution

This project was originally based on [Gemini-ChatBot](https://github.com/KalyanM45/Gemini-ChatBot) by Hema Kalyan Murapaka, and has been substantially modified to use OpenRouter's multi-model API instead of Google's native Gemini SDK, including a rewritten backend integration and chat history handling.

## License

This project is licensed under GPL-3.0 — see the [LICENSE](LICENSE) file for details.

3. Create a `.env` file in the project root:
