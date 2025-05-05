import streamlit as st
import os

# Import your project modules from the 'projects' directory
from projects import (
    bmi_calculator,
    countdown_timer,
    hangman,
    mad_libs,
    rock_paper_scissors,
    sample_data_dashboard,
    password_generator,
    number_game_user,
    number_game_computer
)

# Set page configuration
st.set_page_config(page_title="Multi-Project App", layout="wide")

# Sidebar Navigation Title
st.sidebar.title("🚀 Navigation")

# Dark/Light Mode Toggle
theme = st.sidebar.radio("Select Theme:", ["🌞 Light Mode", "🌙 Dark Mode"])

# Apply theme styles
if theme == "🌙 Dark Mode":
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] { background-color: #212121; color: #e0e0e0; }
        [data-testid="stSidebar"] { background-color: #2c2c2c; color: #e0e0e0; }
        input, textarea, select { background-color: #333333 !important; color: #e0e0e0 !important; }
        button { background-color: #4CAF50 !important; color: white !important; }
        pre, code { background-color: #333333 !important; color: #e0e0e0 !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] { background-color: #ffffff; color: #000000; }
        [data-testid="stSidebar"] { background-color: #f5f5f5; color: #000000; }
        input, textarea, select { background-color: #ffffff !important; color: #000000 !important; }
        button { background-color: #4CAF50 !important; color: white !important; }
        pre, code { background-color: #ffffff !important; color: #000000 !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Sidebar options
options = {
    "🏠 Home": "Home",
    "📏 BMI Calculator": "BMI Calculator",
    "⏳ Countdown Timer": "Countdown Timer",
    "🔤 Hangman": "Hangman",
    "🎭 Mad Libs": "Mad Libs",
    "✊ Rock Paper Scissors": "Rock Paper Scissors",
    "🌐 Sample Data Dashboard": "Sample Data Dashboard",
    "🔑 Password Generator": "Password Generator",
    "🔢 Number Game (User)": "Number Game (User)",
    "🤖 Number Game (Computer)": "Number Game (Computer)",
    "👁️ View Code": "View Code",
    "💬 Comment": "Comment",
}

choice = st.sidebar.selectbox("Select an option", list(options.keys()))

# Home Page
if options[choice] == "Home":
    st.title("🎉 Welcome to the Multi-Project App!")
    st.markdown("#### Explore different interactive Python projects! Select an option from the sidebar to get started. 🚀")
    st.markdown("#### Feel free to comment on the app or suggest improvements. 📝")
    st.markdown("#### Enjoy exploring! 🌟")
    st.markdown("---")

# Run project modules
elif options[choice] == "BMI Calculator":
    bmi_calculator.run()
elif options[choice] == "Countdown Timer":
    countdown_timer.run()
elif options[choice] == "Hangman":
    hangman.run()
elif options[choice] == "Mad Libs":
    mad_libs.run()
elif options[choice] == "Rock Paper Scissors":
    rock_paper_scissors.run()
elif options[choice] == "Sample Data Dashboard":
    sample_data_dashboard.run()
elif options[choice] == "Password Generator":
    password_generator.run()
elif options[choice] == "Number Game (User)":
    number_game_user.run()
elif options[choice] == "Number Game (Computer)":
    number_game_computer.run()

# View Code Section
elif options[choice] == "View Code":
    st.title("👁️ View Code")
    st.markdown("#### View the code for the selected project:")

    # Define relative paths for each project module
    project_files = {
        "🏠 Home": None,
        "📏 BMI Calculator": "projects/bmi_calculator.py",
        "⏳ Countdown Timer": "projects/countdown_timer.py",
        "🔤 Hangman": "projects/hangman.py",
        "🎭 Mad Libs": "projects/mad_libs.py",
        "✊ Rock Paper Scissors": "projects/rock_paper_scissors.py",
        "🌐 Sample Data Dashboard": "projects/sample_data_dashboard.py",
        "🔑 Password Generator": "projects/password_generator.py",
        "🔢 Number Game (User)": "projects/number_game_user.py",
        "🤖 Number Game (Computer)": "projects/number_game_computer.py",
    }

    selected_project_name = st.selectbox("Select a project", list(project_files.keys()))
    selected_project_file = project_files[selected_project_name]

    if selected_project_file:
        try:
            with open(selected_project_file, "r", encoding="utf-8") as file:
                code = file.read()
                st.code(code, language="python")
        except UnicodeDecodeError as e:
            st.error(f"Error: Unable to decode file as UTF-8. Original error: {e}")
            with open(selected_project_file, "r", encoding="latin-1") as file:
                code = file.read()
                st.code(code, language="python")
        except FileNotFoundError:
            st.error(f"Error: File not found at {selected_project_file}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.info("ℹ️ No code available for the Home screen.")

# Comment Section
elif options[choice] == "Comment":
    st.title("💬 Comment")
    st.markdown("#### Leave a comment about the selected project:")
    comment = st.text_area("Your comment", height=100)
    if st.button("Submit Comment"):
        st.success("Thank you for your comment!")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Created with ❤️ by Syed Zeeshan Iqbal")
