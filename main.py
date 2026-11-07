import random
import streamlit as st

st.set_page_config(page_title="Snake Water Gun", page_icon="🐍")

st.title("🐍 🌊 🔫 Snake Water Gun")
st.write("First to **5 points** wins the game!")

# Initialize state
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "last_msg" not in st.session_state:
    st.session_state.last_msg = ""
if "game_over" not in st.session_state:
    st.session_state.game_over = False

yourD = {"Snake": 1, "Water": 2, "Gun": 3}
reverseD = {1: "Snake", 2: "Water", 3: "Gun"}

# Move buttons
col1, col2, col3 = st.columns(3)
user_choice = None

with col1:
    if st.button(
        "🐍\n\nSnake",
        use_container_width=True,
        disabled=st.session_state.game_over,
    ):
        user_choice = "Snake"
with col2:
    if st.button(
        "🌊\n\nWater",
        use_container_width=True,
        disabled=st.session_state.game_over,
    ):
        user_choice = "Water"
with col3:
    if st.button(
        "🔫\n\nGun",
        use_container_width=True,
        disabled=st.session_state.game_over,
    ):
        user_choice = "Gun"

# Process game round only if game is active AND a button was clicked
if user_choice and not st.session_state.game_over:
    computer_num = random.choice([1, 2, 3])
    computer_choice = reverseD[computer_num]
    you_num = yourD[user_choice]

    if computer_num == you_num:
        result = "🤝 It's a Draw!"
    elif (
        (you_num == 1 and computer_num == 2)
        or (you_num == 2 and computer_num == 3)
        or (you_num == 3 and computer_num == 1)
    ):
        result = "🎉 You Win this round!"
        st.session_state.user_score += 1
    else:
        result = "💻 Computer Wins this round!"
        st.session_state.computer_score += 1

    st.session_state.last_msg = (
        f"You picked **{user_choice}** | Computer picked **{computer_choice}**\n\n{result}"
    )

    if st.session_state.user_score == 5 or st.session_state.computer_score == 5:
        st.session_state.game_over = True

st.write("---")

# Show score metric
score_col1, score_col2 = st.columns(2)
score_col1.metric("Your Score", st.session_state.user_score)
score_col2.metric("Computer Score", st.session_state.computer_score)

# Display last result
if st.session_state.last_msg:
    st.info(st.session_state.last_msg)

# Game Over Screen
if st.session_state.game_over:
    st.write("---")
    if st.session_state.user_score == 5:
        st.balloons()
        st.success("🏆 **ROUND OVER: YOU WON THE MATCH!**")
    else:
        st.error("💀 **ROUND OVER: COMPUTER WON THE MATCH!**")

    # Clean reset on Play Again button
    if st.button("🔄 Play Again", type="primary"):
        st.session_state.user_score = 0
        st.session_state.computer_score = 0
        st.session_state.game_over = False
        st.session_state.last_msg = ""
        st.rerun()

st.write("---")
if st.button("Reset Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.game_over = False
    st.session_state.last_msg = ""
    st.rerun()
