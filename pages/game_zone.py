import streamlit as st
import random
import json
import os

#st.set_page_config(page_title="Games & Knowledge Check", layout="centered")
def main():    
    st.title("🌱 Games / Entertainment / Knowledge Check 🎮")
    st.markdown("Let's test your plant knowledge and daily gardening tasks! Win points and climb the leaderboard.")

    # ---------------------------
    # Sample Quiz Questions
    # ---------------------------

    quiz_questions = [
        {
            "question": "Which nutrient is essential for leafy vegetable growth?",
            "options": ["Nitrogen", "Phosphorus", "Potassium", "Calcium"],
            "answer": "Nitrogen"
        },
        {
            "question": "What is the ideal pH for most vegetable garden soil?",
            "options": ["3.0-4.0", "5.5-7.0", "7.5-9.0", "8.0-10.0"],
            "answer": "5.5-7.0"
        },
        {
            "question": "Which method uses water and nutrients without soil?",
            "options": ["Hydroponics", "Aeration", "Composting", "Fertilization"],
            "answer": "Hydroponics"
        },
        {
            "question": "Which plant is best suited for vertical gardening?",
            "options": ["Spinach", "Cucumber", "Potato", "Beetroot"],
            "answer": "Cucumber"
        },
        {
            "question": "What’s the best time to water plants?",
            "options": ["Noon", "Early morning", "Late night", "Afternoon"],
            "answer": "Early morning"
        }
    ]

    # ---------------------------
    # Score tracking
    # ---------------------------

    def load_scores():
        if os.path.exists("scores.json"):
            with open("scores.json", "r") as f:
                return json.load(f)
        return {}

    def save_scores(scores):
        with open("scores.json", "w") as f:
            json.dump(scores, f)

    # ---------------------------
    # User Profile
    # ---------------------------

    st.subheader("👤 Enter Your Player Info")
    username = st.text_input("Enter your name to join the game and earn points:", max_chars=20)

    if username:
        scores = load_scores()
        if username not in scores:
            scores[username] = 0

        st.success(f"Welcome {username}! Let's begin 🌿")

        # ---------------------------
        # Quiz Section
        # ---------------------------

        st.subheader("🧠 Daily Plant Knowledge Quiz")
        question = random.choice(quiz_questions)

        selected = st.radio(question["question"], question["options"], key="quiz")

        if st.button("Submit Answer"):
            if selected == question["answer"]:
                st.success("Correct! 🎉 +10 points")
                scores[username] += 10
            else:
                st.error(f"Oops! Correct answer was: **{question['answer']}**")

            save_scores(scores)

        # ---------------------------
        # Daily Plant Task
        # ---------------------------

        st.subheader("🌿 Daily Gardening Challenge")
        tasks = [
            "Check soil moisture and water accordingly",
            "Clean dry leaves and check for pests",
            "Fertilize plants lightly today",
            "Harvest mature veggies",
            "Rotate your pots for balanced sunlight"
        ]
        task = random.choice(tasks)
        st.info(f"Today's Task: **{task}** ✅")

        if st.button("Task Completed"):
            st.success("Well done! +5 points added.")
            scores[username] += 5
            save_scores(scores)

        # ---------------------------
        # Leaderboard
        # ---------------------------

        st.subheader("🏆 Community Leaderboard")

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for rank, (user, score) in enumerate(sorted_scores[:10], 1):
            st.write(f"**{rank}. {user}** - 🌟 {score} points")

        # ---------------------------
        # Rewards Section
        # ---------------------------

        st.subheader("🎁 Rewards")

        if scores[username] >= 50:
            st.balloons()
            st.success("You've earned a reward! 🎁 Claim your discount on next compost/seeds order!")
        elif scores[username] >= 30:
            st.info("Almost there! Earn 50 points to unlock your first reward!")
        else:
            st.warning("Keep playing and completing tasks to earn rewards!")

    else:
        st.warning("👆 Please enter your name to play.")
