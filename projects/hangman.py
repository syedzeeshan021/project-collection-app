import streamlit as st
import random

def run():
    st.title("🎮 Hangman Game")
    st.markdown("Guess the hidden word one letter at a time!")

    # Initialize session state
    if "game_state" not in st.session_state:
        words = ["PYTHON", "STREAMLIT", "PROJECT", "CODING", "GAME"]
        st.session_state.game_state = {
            "word": random.choice(words).upper(),
            "guessed_letters": set(),
            "lives": 6,
            "hint_used": False
        }

    # Access game state
    word = st.session_state.game_state["word"]
    guessed_letters = st.session_state.game_state["guessed_letters"]
    lives = st.session_state.game_state["lives"]
    hint_used = st.session_state.game_state["hint_used"]

    # Display word
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    st.subheader(f"Word: {display_word}")
    st.write(f"Lives left: {lives} ❤️")

    # Hints
    st.write(f"Hint: The word starts with '{word[0]}' and ends with '{word[-1]}'")

    # Hint button
    if not hint_used:
        if st.button("Use Hint (reveal a letter) 💡"):
            unguessed_letters = set(word) - guessed_letters
            if unguessed_letters:
                letter_to_reveal = random.choice(list(unguessed_letters))
                guessed_letters.add(letter_to_reveal)
                st.success(f"Hint revealed: {letter_to_reveal}")
                st.session_state.game_state["hint_used"] = True
            else:
                st.warning("No more letters to reveal!")

    # Guess input
    guess = st.text_input("Guess a letter:", max_chars=1, key="guess").upper()

    if guess:
        if guess in guessed_letters:
            st.warning("You already guessed that letter!")
        elif guess in word:
            guessed_letters.add(guess)
            st.success(f"Good job! '{guess}' is in the word.")
        else:
            lives -= 1
            st.error(f"Oops! '{guess}' is not in the word.")
            if lives == 0:
                st.error(f"Game Over! The word was: {word}")
                reset_game()

        # Update game state
        st.session_state.game_state["guessed_letters"] = guessed_letters
        st.session_state.game_state["lives"] = lives

    # Win condition
    if set(word) <= guessed_letters:
        st.balloons()
        st.success(f"Congratulations! You guessed the word: {word}")
        reset_game()


def reset_game():
    """Resets the game state."""
    st.session_state.game_state = {
            "word": random.choice(["PYTHON", "STREAMLIT", "PROJECT", "CODING", "GAME"]).upper(),
            "guessed_letters": set(),
            "lives": 6,
            "hint_used": False
        }

