import random
import streamlit as st

st.set_page_config(page_title="Snake Water Gun", page_icon="🐍")

st.title("🐍 🌊 🔫 Snake Water Gun")

# State setup
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

yourD = {"Snake": 1, "Water": 2, "Gun": 3}
reverseD = {1: "Snake", 2: "Water", 3: "Gun"}
emojis = {"Snake": "🐍", "Water": "🌊", "Gun": "🔫"}

# Score Display
score_col1, score_col2 = st.columns(2)
score_col1.metric("You", st.session_state.user_score)
score_col2.metric("Computer", st.session_state.computer_score)

st.divider()


# Result popup modal (makes it feel snappy like an arcade game)
@st.dialog("Round Result")
def show_result(user_choice, computer_choice, outcome):
    st.write(
        f"You picked **{emojis[user_choice]} {user_choice}** | Computer picked **{emojis[computer_choice]} {computer_choice}**"
    )

    if outcome == "draw":
        st.info("🤝 It's a Draw!")
    elif outcome == "win":
        st.success("🎉 You Win!")
    else:
        st.error("💻 You Lose!")


# Player Move Buttons
st.subheader("Pick your move")
col1, col2, col3 = st.columns(3)

user_choice = None
with col1:
    if st.button("🐍 Snake", use_container_width=True):
        user_choice = "Snake"
with col2:
    if st.button("🌊 Water", use_container_width=True):
        user_choice = "Water"
with col3:
    if st.button("🔫 Gun", use_container_width=True):
        user_choice = "Gun"

# Game Processing
if user_choice:
    computer_num = random.choice([1, 2, 3])
    computer_choice = reverseD[computer_num]
    you_num = yourD[user_choice]

    if computer_num == you_num:
        outcome = "draw"
    elif (
        (you_num == 1 and computer_num == 2)
        or (you_num == 2 and computer_num == 3)
        or (you_num == 3 and computer_num == 1)
    ):
        outcome = "win"
        st.session_state.user_score += 1
    else:
        outcome = "loss"
        st.session_state.computer_score += 1

    show_result(user_choice, computer_choice, outcome)

st.divider()

if st.button("Reset Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.rerun()
