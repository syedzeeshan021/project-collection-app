import streamlit as st
import random

def run():
    st.title("🎯 Number Guessing Game (User)")
    st.write("Try to guess the computer's number!")

    max_number = st.slider("Select the range (1 to X):", min_value=10, max_value=100, value=50)

    if "random_number" not in st.session_state:
        st.session_state["random_number"] = random.randint(1, max_number)
        st.session_state["attempts"] = 0

    user_input = st.number_input("Enter your guess:", min_value=1, max_value=max_number, step=1)

    if st.button("Guess! 🎯"):
        st.session_state["attempts"] += 1
        if user_input < st.session_state["random_number"]:
            st.warning("Too low! Try again. ⬆️")
        elif user_input > st.session_state["random_number"]:
            st.warning("Too high! Try again. ⬇️")
        else:
            st.success(f"🎉 Correct! You guessed {st.session_state['random_number']} in {st.session_state['attempts']} attempts!")
            st.session_state["random_number"] = random.randint(1, max_number)  # Reset for a new game
            st.session_state["attempts"] = 0

def computer_guess():
    st.title("🖥️ Computer Guessing Game")
    st.write("Think of a number, and the computer will try to guess it!")

    max_number = st.slider("Choose the guessing range:", min_value=10, max_value=100, value=50)

    if "low" not in st.session_state:
        st.session_state["low"], st.session_state["high"] = 1, max_number
        st.session_state["computer_guess"] = random.randint(1, max_number)

    st.subheader(f"Is your number {st.session_state['computer_guess']}? 🤔")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Too High 📈"):
            st.session_state["high"] = st.session_state["computer_guess"] - 1
    with col2:
        if st.button("Too Low 📉"):
            st.session_state["low"] = st.session_state["computer_guess"] + 1
    with col3:
        if st.button("Correct! 🎉"):
            st.success(f"Yay! The computer guessed your number {st.session_state['computer_guess']} correctly!")
            st.session_state.clear()

    if st.session_state["low"] <= st.session_state["high"]:
        st.session_state["computer_guess"] = random.randint(st.session_state["low"], st.session_state["high"])
        st.experimental_rerun()
