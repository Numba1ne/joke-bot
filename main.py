from typing import Annotated, List, Literal
from pydantic import BaseModel
from langgraph.graph import StateGraph, END
from langgraph.graph.state import CompiledStateGraph
from langgraph.constants import START
from operator import add
from pyjokes import get_joke


# ============================================================
# STEP 1: Define the State
# ============================================================

class Joke(BaseModel):
    """Model for a single joke"""
    text: str
    category: str


class JokeState(BaseModel):
    """Main state for the joke bot workflow"""
    jokes: Annotated[List[Joke], add] = []  # Accumulates jokes using add reducer
    jokes_choice: Literal["n", "c", "q"] = "n"  # next joke, change category, or quit
    category: str = "neutral"
    language: str = "en"
    quit: bool = False


# ============================================================
# STEP 2: Write Node Functions
# ============================================================

def show_menu(state: JokeState) -> dict:
    """Display menu and capture user input"""
    print(f"\n🎭 Menu | Category: {state.category.upper()} | Jokes: {len(state.jokes)}")
    print("-" * 50)
    print("Pick an option:")
    print("[n] 🎭 Next Joke  [c] 📂 Change Category  [q] 🚪 Quit")
    user_input = input("User Input: ").strip().lower()
    return {"jokes_choice": user_input}


def fetch_joke(state: JokeState) -> dict:
    """Fetch a joke from pyjokes and add it to state"""
    joke_text = get_joke(language=state.language, category=state.category)
    new_joke = Joke(text=joke_text, category=state.category)
    print(f"\n😂 {joke_text}\n")
    print("=" * 60)
    return {"jokes": [new_joke]}


def update_category(state: JokeState) -> dict:
    """Allow user to change the joke category"""
    categories = ["neutral", "chuck", "all"]
    print("\n📂 Available Categories:")
    print("[0] Neutral  [1] Chuck Norris  [2] All")
    try:
        selection = int(input("Select category: ").strip())
        if 0 <= selection < len(categories):
            selected_category = categories[selection]
            print(f"✅ Category changed to: {selected_category.upper()}\n")
            print("=" * 60)
            return {"category": selected_category}
        else:
            print("⚠️ Invalid selection. Keeping current category.\n")
            print("=" * 60)
            return {}
    except ValueError:
        print("⚠️ Invalid input. Keeping current category.\n")
        print("=" * 60)
        return {}


def exit_bot(state: JokeState) -> dict:
    """Exit the bot gracefully"""
    print("\n🚪" + "=" * 58 + "🚪")
    print("    GOODBYE!")
    print("=" * 60)
    return {"quit": True}


# ============================================================
# Routing Logic
# ============================================================

def route_choice(state: JokeState) -> str:
    """Route to the appropriate node based on user choice"""
    if state.jokes_choice == "n":
        return "fetch_joke"
    elif state.jokes_choice == "c":
        return "update_category"
    elif state.jokes_choice == "q":
        return "exit_bot"
    # Default to exit if invalid input
    return "exit_bot"


# ============================================================
# STEPS 3 & 4: Create Graph and Add Nodes + Edges
# ============================================================

def build_joke_graph() -> CompiledStateGraph:
    """Build and compile the joke bot graph"""
    workflow = StateGraph(JokeState)

    # Add all nodes
    workflow.add_node("show_menu", show_menu)
    workflow.add_node("fetch_joke", fetch_joke)
    workflow.add_node("update_category", update_category)
    workflow.add_node("exit_bot", exit_bot)

    # Set entry point
    workflow.set_entry_point("show_menu")

    # Add conditional edges from show_menu based on user choice
    workflow.add_conditional_edges(
        "show_menu",
        route_choice,
        {
            "fetch_joke": "fetch_joke",
            "update_category": "update_category",
            "exit_bot": "exit_bot",
        }
    )

    # Add edges back to menu from fetch_joke and update_category
    workflow.add_edge("fetch_joke", "show_menu")
    workflow.add_edge("update_category", "show_menu")
    
    # Add edge from exit_bot to END
    workflow.add_edge("exit_bot", END)

    return workflow.compile()


# ============================================================
# STEP 5: Run the Graph
# ============================================================

def main():
    """Main function to run the joke bot"""
    print("\n🎉" + "=" * 58 + "🎉")
    print("    WELCOME TO THE LANGGRAPH JOKE BOT!")
    print("    This example demonstrates agentic state flow without LLMs")
    print("=" * 60)
    print("\n🚀" + "=" * 58 + "🚀")
    print("    STARTING JOKE BOT SESSION...")
    print("=" * 60)
    
    # Build and run the graph
    graph = build_joke_graph()
    final_state = graph.invoke(JokeState(), config={"recursion_limit": 100})
    
    # Display session summary
    print("\n🎊" + "=" * 58 + "🎊")
    print("    SESSION COMPLETE!")
    print("=" * 60)
    print(f"    📈 You enjoyed {len(final_state['jokes'])} jokes during this session!")
    print(f"    📂 Final category: {final_state['category'].upper()}")
    print("    🙏 Thanks for using the LangGraph Joke Bot!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
