import streamlit as st
import random

# Game choices with emojis
choices = {
    "Rock": "🪨 Rock",
    "Paper": "📜 Paper",
    "Scissors": "✂️ Scissors"
}

# Function to determine the winner
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "🤝 It's a Tie!", "gray", "tie"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "🎉 You Win!", "green", "user"
    else:
        return "😢 Computer Wins!", "red", "computer"

# Streamlit UI
def run():
    st.title("🎮 Rock, Paper, Scissors Game!")
    st.write("Choose your move and try to beat the computer!")

    # Initialize scores in session state
    if "user_score" not in st.session_state:
        st.session_state["user_score"] = 0
    if "computer_score" not in st.session_state:
        st.session_state["computer_score"] = 0

    # User selection
    user_choice = st.radio("Make your choice:", list(choices.keys()), format_func=lambda x: choices[x])

    if st.button("Play! 🚀"):
        computer_choice = random.choice(list(choices.keys()))

        st.subheader("🆚 Results:")
        st.write(f"👤 You chose: {choices[user_choice]}")
        st.write(f"🤖 Computer chose: {choices[computer_choice]}")

        result, color, winner = get_winner(user_choice, computer_choice)
        st.markdown(f"<h3 style='color:{color};'>{result}</h3>", unsafe_allow_html=True)

        # Update scores based on winner
        if winner == "user":
            st.session_state["user_score"] += 1
        elif winner == "computer":
            st.session_state["computer_score"] += 1

    # Scoreboard
    st.subheader("📊 Scoreboard:")
    st.write(f"👤 **Your Score:** {st.session_state['user_score']}  |  🤖 **Computer Score:** {st.session_state['computer_score']}")

    if st.button("Reset Scores 🔄"):
        st.session_state["user_score"] = 0
        st.session_state["computer_score"] = 0
        st.rerun()

# Run the app
if __name__ == "__main__":
    run()
