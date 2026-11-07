import random
import streamlit as st

st.set_page_config(page_title="Snake Water Gun", page_icon="🐍")

st.title("Snake Water Gun Game")
st.write("Pick your move:")

# Session state to keep track of scores
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

yourD = {"Snake": 1, "Water": 2, "Gun": 3}
reverseD = {1: "Snake", 2: "Water", 3: "Gun"}

# Move buttons
col1, col2, col3 = st.columns(3)
user_choice = None

with col1:
    if st.button("🐍 Snake"):
        user_choice = "Snake"
with col2:
    if st.button("🌊 Water"):
        user_choice = "Water"
with col3:
    if st.button("🔫 Gun"):
        user_choice = "Gun"

if user_choice:
    computer = random.choice([1, 2, 3])
    you = yourD[user_choice]

    st.write(
        f"You chose: **{user_choice}** | Computer chose: **{reverseD[computer]}**"
    )

    if computer == you:
        st.write("It's a draw!")
    elif (
        (you == 1 and computer == 2)
        or (you == 2 and computer == 3)
        or (you == 3 and computer == 1)
    ):
        st.write("You win!")
        st.session_state.user_score += 1
    else:
        st.write("You lose!")
        st.session_state.computer_score += 1

st.write("---")
st.write(
    f"Score — You: {st.session_state.user_score} | Computer: {st.session_state.computer_score}"
)

if st.button("Reset Score"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.rerun()