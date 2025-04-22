import streamlit as st
st.title("BMI Calculator")
st.header("Calculate your Body Mass Index (BMI)")
weight_kg=st.slider("Select your weight (kg):", min_value=30, max_value=150, value=70, step=1)
height_cm=st.slider("Select your height in cm :", min_value=100, max_value=250, value=170, step=1)
bmi = weight_kg / ((height_cm / 100) ** 2)
st.subheader("Report")

if bmi < 18.5:
    st.write(f"BMI: {bmi:.2f} → You're **Underweight**.")
    st.write("Consider increasing your calorie intake and consulting a healthcare professional.")
elif 18.5 <= bmi < 25:
    st.write(f"BMI: {bmi:.2f} → You're in the **Normal weight** category. ✅")
    st.write("Keep up the good work with your balanced lifestyle! 💪")
elif 25 <= bmi < 30:
    st.write(f"BMI: {bmi:.2f} → You're in the **Overweight** category.")
    st.write("It’s not extremely high, but it’s a good time to focus on healthy habits like:")
    st.markdown("- Balanced diet 🍎")
    st.markdown("- Regular exercise 🏃‍♂️")
    st.markdown("- Good sleep and stress management 🧘")
else:
    st.write(f"BMI: {bmi:.2f} → You're in the **Obese** category.")
    st.write("It's advisable to consult with a doctor and adopt a structured health plan.")

    
st.write(f"Your BMI is: {bmi:.2f}")
st.subheader("BMI Categories")
st.write("• Underweight: BMI less than 18.5")
st.write("• Normal weight: BMI between 18.5 and 24.9")
st.write("• Overweight: BMI between 25 and 29.9")
st.write("• Obese: BMI 30 and above")


 

 
