import random
import streamlit as st

st.set_page_config(page_title="Snake Water Gun", page_icon="🐍")

st.title("🐍 🌊 🔫 Snake Water Gun")

# 1. State setup
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "last_result" not in st.session_state:
    st.session_state.last_result = ""

yourD = {"Snake": 1, "Water": 2, "Gun": 3}
reverseD = {1: "Snake", 2: "Water", 3: "Gun"}

# 2. Process Move FIRST (Fixes the 1-round score delay!)
st.subheader("Pick your move")
col1, col2, col3 = st.columns(3)

user_choice = None
with col1:
    if st.button("🐍 Snake", disabled=st.session_state.game_over):
        user_choice = "Snake"
with col2:
    if st.button("🌊 Water", disabled=st.session_state.game_over):
        user_choice = "Water"
with col3:
    if st.button("🔫 Gun", disabled=st.session_state.game_over):
        user_choice = "Gun"

if user_choice and not st.session_state.game_over:
    computer_num = random.choice([1, 2, 3])
    computer_choice = reverseD[computer_num]
    you_num = yourD[user_choice]

    if computer_num == you_num:
        st.session_state.last_result = f"🤝 **Draw!** Both picked {user_choice}."
    elif (
        (you_num == 1 and computer_num == 2)
        or (you_num == 2 and computer_num == 3)
        or (you_num == 3 and computer_num == 1)
    ):
        st.session_state.user_score += 1
        st.session_state.last_result = (
            f"🎉 **You Win!** {user_choice} beats {computer_choice}."
        )
    else:
        st.session_state.computer_score += 1
        st.session_state.last_result = (
            f"💻 **You Lose!** {computer_choice} beats {user_choice}."
        )

    # Check for First to 5 Winner
    if st.session_state.user_score == 5 or st.session_state.computer_score == 5:
        st.session_state.game_over = True

# 3. Render Updated Scoreboard (Instant Sync)
st.write("---")
score_col1, score_col2 = st.columns(2)
score_col1.metric("Your Score", st.session_state.user_score)
score_col2.metric("Computer Score", st.session_state.computer_score)

# 4. Display Round Status / Game Over Modal
if st.session_state.game_over:
    st.write("---")
    if st.session_state.user_score == 5:
        st.balloons()
        st.success("🏆 **GAME OVER — YOU WON THE MATCH!** (First to 5)")
    else:
        st.error("💀 **GAME OVER — COMPUTER WON THE MATCH!** (First to 5)")

    if st.button("🔄 Play Again", type="primary"):
        st.session_state.user_score = 0
        st.session_state.computer_score = 0
        st.session_state.game_over = False
        st.session_state.last_result = ""
        st.rerun()
elif st.session_state.last_result:
    st.info(st.session_state.last_result)

st.write("---")
if st.button("Reset Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.game_over = False
    st.session_state.last_result = ""
    st.rerun()
