import streamlit as st

st.title("Password Safety Checker")

password = st.text_input(
    "Enter your password:",
type="password"
)
if len(password) < 8:
    st.error("The password is too weak!")
elif len(password) >= 8 and len(password) < 14:
    st.error("The password is not recommended to use!")
elif len(password) >= 14:
    is_pattern_found = False
    standard_route = [
    "abcdefghijklmnopqrstuvwxyz",
    "zyxwvutsrqponmlkjihgfedcba",
    "01234567890123456789",
    "98765432109876543210"
]
    for i in range(len(password) - 2):
            sedutan = password[i:i+3].lower()
            for laluan in standard_route:
                if sedutan in laluan:
                    is_pattern_found = True
                    break

    if password.isalpha() or password.isdigit() or is_pattern_found:
        st.error("The password is too weak!")
    else:
        st.success("The password is strong!")
st.markdown("### :rainbow[Note: This is just for reference!]")
