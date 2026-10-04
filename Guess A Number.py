import streamlit as st
import random

st.title(":rainbow[Guess a Number]")

if "num" not in st.session_state:
    st.session_state["num"] = random.randint(1, 100)
    st.session_state["number of guesses"] = 0
    st.session_state["game_over"] = False

st.write("Guess a number from 1 to 100")

guess = st.number_input("Please enter a number from 1 - 100", min_value=1, max_value=100)
button = st.button("Guess")

if button:
    st.session_state["number of guesses"] += 1
    
    if guess < st.session_state["num"]:
        st.warning(f"Your number is smaller than the number given. Retry! Guessed {st.session_state['number of guesses']} times.")
        
    elif guess > st.session_state["num"]: 
        st.warning(f"Your number is bigger than the number given. Retry! Guessed {st.session_state['number of guesses']} times.")
        
    else:
        st.success(f"Congratulations! You have guessed the number given! Guessed {st.session_state['number of guesses']} times.")
        st.balloons()
        st.session_state["game_over"] = True
        if st.session_state["game_over"]:
            st.write(":blue[Click on the refresh button or Ctrl + R to reset the game]")
