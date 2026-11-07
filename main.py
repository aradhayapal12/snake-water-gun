import random
import streamlit as st

st.set_page_config(page_title="Snake Water Gun", page_icon="🐍")

st.title("🐍 🌊 🔫 Snake Water Gun")
st.write("Pick your move below:")

# Keep track of scores
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

yourD = {"Snake": 1, "Water": 2, "Gun": 3}
reverseD = {1: "Snake", 2: "Water", 3: "Gun"}

# Show nice score cards at the top
score_col1, score_col2 = st.columns(2)
score_col1.metric("Your Score", st.session_state.user_score)
score_col2.metric("Computer Score", st.session_state.computer_score)

st.write("---")

# Buttons for your move
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

# Game outcome logic
if user_choice:
    computer_num = random.choice([1, 2, 3])
    computer_choice = reverseD[computer_num]
    you_num = yourD[user_choice]

    st.write(
        f"You picked **{user_choice}** | Computer picked **{computer_choice}**"
    )

    if computer_num == you_num:
        st.info("🤝 It's a Draw!")
    elif (
        (you_num == 1 and computer_num == 2)
        or (you_num == 2 and computer_num == 3)
        or (you_num == 3 and computer_num == 1)
    ):
        st.success("🎉 You Win!")
        st.session_state.user_score += 1
    else:
        st.error("💻 You Lose!")
        st.session_state.computer_score += 1

st.write("---")

if st.button("Reset Score"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.rerun()
