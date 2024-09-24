import json
import streamlit as st


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


def are_equal(list1, list2):
    """Checks if two lists are equal in length and values.

    Args:
        list1: The first list.
        list2: The second list.

    Returns:
        True if the lists are equal, False otherwise.
    """

    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True


@st.dialog("Results")
def results(questions_total, questions_correct, questions_wrong, questions_no_anwer):
    st.text(f"Total questions: {questions_total}")
    st.text(f"Correct answers: {questions_correct}")
    st.text(f"Incorrect answer: {questions_wrong}")
    st.text(f"Not answerd questions: {questions_no_anwer}")
    percentage = count_correct_keys(questions_correct) / questions_total
    st.text(f"Percentage: {percentage:.2f}")


st.markdown(f"<h1 style='text-align: center;'>Test 1Z0-770</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("Previous", use_container_width=True):
        st.session_state["qi"] -= 1
        if st.session_state["qi"] < 0:
            st.session_state["qi"] = len(st.session_state['test']) - 1
with col2:
    if st.button("Next", use_container_width=True):
        st.session_state["qi"] += 1
        if st.session_state["qi"] > len(st.session_state['test']) - 1:
            st.session_state["qi"] = 0

st.markdown(f"<p style='text-align: center;'>{st.session_state["qi"] + 1} of {len(st.session_state['test'])} questions</p>", unsafe_allow_html=True)

st.subheader(st.session_state["test"][st.session_state["qi"]]["question_description"])
st.write()

correct_answers = []
selected_answers = []

for answer in st.session_state["test"][st.session_state["qi"]]["answers"]:
    ansr = st.checkbox(label=answer["answer_desc"], value=(True if answer['selected'] == 'Y' else False))
    if ansr:
        answer["selected"] = "Y"
    else:
        answer["selected"] = "N"

    correct_answers.append(answer["correct_flag"] == "Y")
    selected_answers.append(answer["selected"] == "Y")

is_correct = False

if st.button("Confirm", use_container_width=True):
    is_correct = are_equal(correct_answers, selected_answers)
    st.session_state["test"][st.session_state["qi"]]["confirmed"] = 'Y'
    st.session_state["test"][st.session_state["qi"]]["correct"] = 'Y' if is_correct else 'N'

    if is_correct:
        st.success('Correct answer!', icon="✅")
    else:
        ra = []
        for answer in st.session_state["test"][st.session_state["qi"]]["answers"]:
            if answer['correct_flag'] == 'Y':
                ra.append(answer['answer_code'])

        st.error(f"Wrong answer! correct option is {ra}", icon="🚨")

if st.button("Finish", use_container_width=True):
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

    results(questions_total, questions_correct, questions_wrong, questions_no_anwer)

# st.write(correct_answers)
# st.write(selected_answers)
# st.write(is_correct)
# st.write(st.session_state["test"])
