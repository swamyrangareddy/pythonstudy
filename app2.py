import streamlit as st

# Title of the app
st.title("Python Quiz App")

# Sample quiz questions
questions = [
    {
        "question": "What is the output of `print(2 ** 3)`?",
        "options": ["6", "8", "9", "4"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "What is the result of `3 + 4 * 2`?",
        "options": ["14", "11", "10", "7"],
        "answer": "11"
    },
    {
        "question": "Which of the following is a valid way to create a list in Python?",
        "options": ["list = [1, 2, 3]", "list = {1, 2, 3}", "list = (1, 2, 3)", "list = <1, 2, 3>"],
        "answer": "list = [1, 2, 3]"
    },
    {
        "question": "What is the output of `print('Hello, World!')`?",
        "options": ["Hello, World!", "Hello World!", "Hello, World", "Hello World"],
        "answer": "Hello, World!"
    }
]

# Store the user's answers
user_answers = {}

# Loop through each question
for idx, q in enumerate(questions):
    st.subheader(f"Question {idx + 1}")
    st.write(q["question"])

    # Radio buttons with no default selection
    selected_option = st.radio(
        f"Choose an answer for Question {idx + 1}:",
        q["options"],
        key=idx,
        index=0
    )
    user_answers[idx] = selected_option

# Submit button
if st.button("Submit"):
    for idx, q in enumerate(questions):
        if user_answers[idx] == "Select an option":
            st.warning(f"Please select an option for Question {idx + 1}")
        elif user_answers[idx] == q["answer"]:
            st.success(f"Correct! {q['question']} -> {user_answers[idx]}")
        else:
            st.error(f"Incorrect. {q['question']} -> Your answer: {user_answers[idx]}, Correct answer: {q['answer']}")