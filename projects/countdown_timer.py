# Project 6: Countdown Timer Python Project
import streamlit as st
import time

def countdown(hours, minutes, seconds):
    """Performs a countdown with hours, minutes, and seconds, updating the display dynamically."""
    total_seconds = hours * 3600 + minutes * 60 + seconds  # Convert to total seconds
    
    placeholder = st.empty()  # Placeholder for dynamic updates
    progress_bar = st.progress(0)  # Progress bar

    for remaining in range(total_seconds, -1, -1):
        hrs, rem = divmod(remaining, 3600)
        mins, secs = divmod(rem, 60)
        timer_display = f"{hrs:02d}:{mins:02d}:{secs:02d}"

        placeholder.markdown(f"## ⏳ Time Left: `{timer_display}`")  # Update countdown display
        progress_bar.progress((total_seconds - remaining) / total_seconds)  # Update progress
        
        time.sleep(1)

    placeholder.success("🎉 **Time's Up!**")  # Display completion message
    progress_bar.empty()  # Remove progress bar

def run():
    st.title("⏳ Digital Countdown Timer")
    st.write("Set your timer with hours, minutes, and seconds.")

    # User input fields
    hours = st.number_input("Enter Hours:", min_value=0, step=1, value=0)
    minutes = st.number_input("Enter Minutes:", min_value=0, step=1, value=0)
    seconds = st.number_input("Enter Seconds:", min_value=1, step=1, value=10)

    if st.button("Start Timer 🚀"):
        countdown(hours, minutes, seconds)
