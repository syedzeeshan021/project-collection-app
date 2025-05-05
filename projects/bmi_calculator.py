import streamlit as st
import pandas as pd

def run():
    st.title("🏋️‍♀️ BMI (Body Mass Index) Calculator 🏋️‍♂️")
    st.write("Calculate your BMI and get personalized health advice! 😊")

    # Height input in feet and inches
    st.subheader("📏 Your Height")
    height_feet = st.slider("Enter your height (feet):", min_value=4, max_value=8, value=5, step=1)
    height_inches = st.slider("Enter your height (inches):", min_value=0, max_value=11, value=6, step=1)

    # Convert height to meters
    height_in_meters = (height_feet * 0.3048) + (height_inches * 0.0254)

    # Weight input
    st.subheader("⚖️ Your Weight")
    weight = st.slider("Enter your weight (kg):", min_value=30, max_value=300, value=70, step=1)

    # Calculate BMI
    if height_in_meters > 0:
        bmi = weight / (height_in_meters**2)
    else:
        bmi = None  # Invalid height case

    # Display BMI Result
    st.subheader("📊 Your BMI Result")
    if bmi is None:
        st.warning("Height must be greater than zero!")
    else:
        st.write(f"### Your BMI is: **{bmi:.2f}**")

        # BMI Classification & Advice
        bmi_categories = [
            ("Underweight", 18.5, "⚠️ Consider gaining weight with a healthy diet."),
            ("Normal weight", 24.9, "✅ Great job! Maintain a balanced lifestyle."),
            ("Overweight", 29.9, "⚠️ Consider healthier habits to manage weight."),
            ("Obesity (Class I)", 34.9, "🚨 Consider a structured weight loss plan."),
            ("Obesity (Class II)", 39.9, "⚠️ High risk! Consult a healthcare provider."),
            ("Obesity (Class III)", float('inf'), "🚨 Serious risk! Immediate medical advice needed.")
        ]

        for category, limit, advice in bmi_categories:
            if bmi <= limit:
                st.markdown(f"### 📌 **Category:** {category}")
                st.info(f"💡 **Advice:** {advice}")
                break

        # Display BMI Chart
        st.write("### 📊 BMI Categories Overview")
        bmi_df = pd.DataFrame(
            {
                "Category": [cat[0] for cat in bmi_categories],
                "BMI Range": ["<18.5", "18.5 - 24.9", "25.0 - 29.9", "30.0 - 34.9", "35.0 - 39.9", "40+"]
            }
        )
        st.dataframe(bmi_df, hide_index=True)