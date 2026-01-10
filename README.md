# 🎭 LangGraph Joke Bot

A multilingual joke bot built with LangGraph that demonstrates agentic state flow without LLMs. This bot uses the `pyjokes` library to deliver jokes in multiple languages and categories.

## ✨ Features

- 🎭 **Fetch Jokes**: Get random jokes from different categories
- 📂 **Change Category**: Switch between Neutral, Chuck Norris, and All categories
- 🌐 **Multilingual Support**: Enjoy jokes in 6 different languages
- 🔁 **Reset History**: Clear your joke history anytime
- 📊 **Session Tracking**: Keep track of all jokes you've enjoyed

## 🌍 Supported Languages

- 🇬🇧 English (en)
- 🇩🇪 German (de)
- 🇪🇸 Spanish (es)
- 🇪🇸 Galician (gl)
- 🇪🇸 Basque (eu)
- 🇮🇹 Italian (it)

## 📦 Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd joke-bot
```

2. Install dependencies using uv (recommended) or pip:
```bash
# Using uv
uv sync

# Or using pip
pip install -e .
```

## 🚀 Usage

Run the bot:
```bash
python main.py
```

### Menu Options

When the bot starts, you'll see a menu with the following options:

- **[n] 🎭 Next Joke** - Fetch and display a new joke
- **[c] 📂 Change Category** - Switch between joke categories (Neutral, Chuck Norris, All)
- **[l] 🌐 Change Language** - Select from 6 supported languages
- **[r] 🔁 Reset History** - Clear all jokes from your current session
- **[q] 🚪 Quit** - Exit the bot and see your session summary

## 🏗️ Architecture

This bot is built using LangGraph and demonstrates:

- **State Management**: Using Pydantic models to define and manage state
- **Node Functions**: Modular functions for each bot action
- **Conditional Routing**: Dynamic routing based on user choices
- **Graph Compilation**: Building and compiling a state graph workflow
- **Looping Behavior**: Continuous interaction until user quits

### State Structure

```python
class JokeState(BaseModel):
    jokes: List[Joke] = []           # Accumulated jokes
    jokes_choice: str = "n"          # User's menu choice
    category: str = "neutral"        # Current joke category
    language: str = "en"             # Current language
    quit: bool = False               # Exit flag
```

### Graph Nodes

1. **show_menu** - Display menu and capture user input
2. **fetch_joke** - Fetch a joke from pyjokes
3. **update_category** - Change joke category
4. **update_language** - Change joke language
5. **reset_jokes** - Clear joke history
6. **exit_bot** - Exit gracefully

## 📝 Example Session

```
🎉==========================================================🎉
    WELCOME TO THE LANGGRAPH JOKE BOT!
    This example demonstrates agentic state flow without LLMs
============================================================

🎭 Menu | Category: NEUTRAL | Language: EN | Jokes: 0
----------------------------------------------------------------------
Pick an option:
[n] 🎭 Next Joke  [c] 📂 Change Category  [l] 🌐 Change Language
[r] 🔁 Reset History  [q] 🚪 Quit
User Input: n

😂 Why do programmers prefer dark mode? Because light attracts bugs!

============================================================

🎭 Menu | Category: NEUTRAL | Language: EN | Jokes: 1
----------------------------------------------------------------------
Pick an option:
[n] 🎭 Next Joke  [c] 📂 Change Category  [l] 🌐 Change Language
[r] 🔁 Reset History  [q] 🚪 Quit
User Input: l

🌐 Available Languages:
[0] English (en)
[1] German (de)
[2] Spanish (es)
[3] Galician (gl)
[4] Basque (eu)
[5] Italian (it)
Select language: 2
✅ Language changed to: Spanish

============================================================

🎭 Menu | Category: NEUTRAL | Language: ES | Jokes: 1
----------------------------------------------------------------------
Pick an option:
[n] 🎭 Next Joke  [c] 📂 Change Category  [l] 🌐 Change Language
[r] 🔁 Reset History  [q] 🚪 Quit
User Input: q

🚪==========================================================🚪
    GOODBYE!
============================================================

🎊==========================================================🎊
    SESSION COMPLETE!
============================================================
    📈 You enjoyed 1 jokes during this session!
    📂 Final category: NEUTRAL
    🌐 Final language: ES
    🙏 Thanks for using the LangGraph Joke Bot!
============================================================
```

## 🛠️ Technical Details

- **Framework**: LangGraph
- **Joke Source**: pyjokes library
- **State Management**: Pydantic BaseModel
- **Graph Type**: StateGraph with conditional routing
- **Python Version**: 3.8+

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 🙏 Acknowledgments

- Built with [LangGraph](https://github.com/langchain-ai/langgraph)
- Jokes provided by [pyjokes](https://github.com/pyjokes/pyjokes)
