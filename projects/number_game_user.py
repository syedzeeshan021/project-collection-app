import streamlit as st
import random

def run():
    st.title("🔢 Number Guessing Game")
    st.write("Try to guess the number chosen by the computer!")

    # Select difficulty range
    max_number = st.slider("Select the range (1 to X):", min_value=10, max_value=1000, value=100)

    # Generate a random number
    if "random_number" not in st.session_state:
        st.session_state["random_number"] = random.randint(1, max_number)
        st.session_state["attempts"] = 0

    user_guess = st.number_input("Enter your guess:", min_value=1, max_value=max_number, step=1)
    
    if st.button("Guess! 🎯"):
        st.session_state["attempts"] += 1
        if user_guess < st.session_state["random_number"]:
            st.warning("Too low! Try again. ⬆️")
        elif user_guess > st.session_state["random_number"]:
            st.warning("Too high! Try again. ⬇️")
        else:
            st.success(f"🎉 Congratulations! You guessed the number {st.session_state['random_number']} in {st.session_state['attempts']} attempts!")
            st.session_state["random_number"] = random.randint(1, max_number)  # Reset for a new game
            st.session_state["attempts"] = 0
