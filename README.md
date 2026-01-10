# 🎭 Agentic LangGraph Joke Bot

An advanced, multilingual joke bot built with LangGraph that features an LLM-powered **Writer-Critic loop**. This bot doesn't just fetch static jokes; it generates, evaluates, and refines them to ensure high-quality software engineering humor.

## ✨ Features

- 🤖 **Writer-Critic Loop**: An agentic loop where a Writer LLM generates jokes and a Critic LLM evaluates them.
- 🌀 **Repetition Avoidance**: The bot remembers past jokes and ensures new ones are unique and fresh.
- 📂 **Dynamic Categories**: Specify categories like Neutral, Chuck Norris, or All for tailored humor.
- 🌐 **Multilingual Support**: Generate jokes in English, German, Spanish, and more.
- 🔁 **Reset History**: Clear session history while maintaining the agentic state.
- 📊 **Session Tracking**: Track joke count, final category, and language choices.

## 🏗️ Architecture: The Writer-Critic Loop

This bot demonstrates the **Reason, Reflect, and Revise** pattern:

1. **Writer Node**: Uses GPT-4o-mini to draft a joke based on the selected category and past history.
2. **Critic Node**: Evaluates the joke for quality and uniqueness. It can reject jokes up to 5 times.
3. **Looping**: If rejected, the Writer tries again with awareness of why the previous attempt failed (implicitly by being told what to avoid).

### State Structure
```python
class JokeState(BaseModel):
    jokes: List[Joke] = []           # History of approved jokes
    jokes_choice: str = "n"          # User menu selection
    category: str = "neutral"        # Selected category
    language: str = "en"             # Selected language
    latest_joke: str = ""            # Current draft being evaluated
    approved: bool = False           # Critic's approval flag
    retry_count: int = 0             # Current loop iteration
```

## 📦 Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd joke-bot
```

2. Install dependencies using `uv` (recommended):
```bash
uv sync
```

3. Set up your environment variables:
Create a `.env` file in the root directory and add your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
```

## 🚀 Usage

Run the bot:
```bash
uv run main.py
```

### Menu Options
- **[n] 🎭 Next Joke** - Trigger the Writer-Critic loop for a fresh joke.
- **[c] 📂 Change Category** - Switch themes (Neutral, Chuck Norris, All).
- **[l] 🌐 Change Language** - Select from supported languages.
- **[r] 🔁 Reset History** - Wipe the session's joke history.
- **[q] 🚪 Quit** - Exit and see your session stats.

## 📂 Project Structure
- `main.py`: The core LangGraph workflow and node definitions.
- `prompts.yaml`: Centralized management for Agent system and user prompts.
- `utils.py`: Utility functions for loading and formatting dynamic prompts.
- `.env`: (User-created) For API credentials.

## 🛠️ Technical Details
- **Framework**: LangGraph
- **LLM**: OpenAI GPT-4o-mini
- **Validation**: Pydantic
- **Environment**: python-dotenv, PyYAML

## 📄 License
MIT License.

## 🙏 Acknowledgments
- Built with [LangGraph](https://github.com/langchain-ai/langgraph)
- Powered by [OpenAI](https://openai.com/)
