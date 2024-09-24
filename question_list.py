import streamlit as st
import pandas as pd

selected_row = st.session_state.get('selected_row')


def count_correct_keys(data):
    """Counts the number of keys with a "correct_flag" value of "Y" in a JSON object.

    Args:
        data (dict): The JSON data containing the keys.

    Returns:
        int: The number of keys with the specified value.
    """

    correct_key_count = 0

    if isinstance(data, dict):
        for key, value in data.items():
            if key == "correct" and value == "Y":
                correct_key_count += 1
            if isinstance(value, dict):
                correct_key_count += count_correct_keys(value)
            elif isinstance(value, list):
                for item in value:
                    correct_key_count += count_correct_keys(item)

    return correct_key_count


def on_select():
    # Handle the selected row here
    selectedrow = st.session_state['selected_row']["selection"]["rows"]
    st.session_state["qi"] = selectedrow[0]


df = pd.DataFrame(st.session_state['test'], columns=(['question_description', 'confirmed', 'correct']))

df['confirmed'] = df['confirmed'].replace('N', '🚨')
df['confirmed'] = df['confirmed'].replace('Y', '✅')

df['correct'] = df['correct'].replace('N', '🚨')
df['correct'] = df['correct'].replace('Y', '✅')

questions_total = len(st.session_state['test'])
questions_correct = 0
questions_wrong = 0
questions_no_anwer = 0

for item in st.session_state["test"]:
    if item["correct"] == "Y":
        questions_correct += 1

    if item["correct"] == "N" and item["confirmed"] == "Y":
        questions_wrong += 1

    if item["confirmed"] == "N":
        questions_no_anwer += 1

percentage = questions_correct / questions_total * 100

col1, col2 = st.columns(2)
with col1:
    st.text(f"Total questions: {questions_total} Perc.: {percentage:.2f}")
    st.text(f"Not answerd questions: {questions_no_anwer}")

with col2:
    st.text(f"Correct answers: {questions_correct}")
    st.text(f"Incorrect answer: {questions_wrong}")

st.dataframe(df, use_container_width=True, hide_index=True, selection_mode="single-row", on_select=on_select, key='selected_row', column_config={
    "question_description": "Question",
    "confirmed": "Cofirmed",
    "correct": "Correct"}
             )

if st.button("Review"):
    st.switch_page("test.py")
