import streamlit as st

st.title("Even/Odd Number Checker")

# Number input with a nice label
number = st.number_input(
    "Enter a number:", 
    step=1,  # Allows only integer values
    format="%d"  # Displays as integer
)

# Button to check the number
if st.button("Check"):
    if number % 2 == 0:
        st.success(f"{int(number)} is Even")  # success message in green
    else:
        st.warning(f"{int(number)} is Odd")  # warning message in orange