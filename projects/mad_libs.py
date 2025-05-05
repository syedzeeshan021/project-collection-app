import streamlit as st

def run():
    """Generates a Mad Libs story with explanations of word types."""

    st.title("Mad Libs Generator 🤪")
    st.write("Let's create a fun story! Please fill in the blanks below:")

    # Explanations of word types
    st.markdown("""
        **Word Types:**
        *   **Adjective:** Describes a noun (e.g., big, small, happy, sad, colorful)
        *   **Verb (ending in -ing):**  An action word in its continuous form (e.g., running, jumping, singing, dancing)
        *   **Verb:** An action word (e.g., run, jump, sing, dance)
        *   **Noun:** A person, place, thing, or idea (e.g., cat, dog, house, tree, happiness)
        *   **Place:** A location (e.g., park, school, city, country)
        *   **Exclamation:** A sudden cry or remark (e.g., Wow!, Oh no!, Help!, Hooray!)
    """)

    # Input fields
    adjective = st.text_input("Adjective:", key="adjective")
    verb_ing = st.text_input("Verb (ending in -ing):", key="verb_ing")
    verb = st.text_input("Verb:", key="verb")
    noun = st.text_input("Noun:", key="noun")
    place = st.text_input("Place:", key="place")
    exclamation = st.text_input("Exclamation:", key="exclamation")

    # Story generation
    if st.button("Generate Story 🎉"):
        if not all([adjective, verb_ing, verb, noun, place, exclamation]):
            st.warning("Please fill in all the blanks!")
        else:
            story = f"""{exclamation}! I went to the {place} and saw a {adjective} {noun}.  It was {verb_ing} excitedly and then suddenly {verb}! What a day!"""
            st.markdown(f"<h3 style='color:green;'>{story}</h3>", unsafe_allow_html=True)
