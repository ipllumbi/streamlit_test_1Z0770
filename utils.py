import json
import streamlit as st



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
def parse_test_data():
    test = './docs/1z0770.json'
    with open(test, 'r') as file:
        questions = json.load(file)
        return questions


def init_session_state():
    if "current_question_indx" not in st.session_state:
        st.session_state["current_question_indx"] = 0

    question_list = parse_test_data()

    for question in question_list:
        question['confirmed'] = 'N'
        question['correct'] = 'N'
        for answer in question['answers']:
            answer['selected'] = "N"

    if "question_list" not in st.session_state:
        st.session_state["question_list"] = question_list

def get_question_list():
    return st.session_state["question_list"]

def increment_current_question_indx():
    if st.session_state["current_question_indx"] == len(st.session_state['question_list']) - 1:
        st.session_state["current_question_indx"] = 0
    else:
        st.session_state["current_question_indx"] += 1

def decrement_current_question_indx():
   if st.session_state["current_question_indx"] == 0:
        st.session_state["current_question_indx"] = len(st.session_state['question_list']) - 1
   else:
        st.session_state["current_question_indx"] -= 1

def get_current_question_indx():
    return st.session_state["current_question_indx"]

def set_current_question_indx(val):
     st.session_state["current_question_indx"] = val


def get_question_list_len():
    return len(st.session_state['question_list'])

def get_current_question():
    return st.session_state['question_list'][get_current_question_indx()]

def get_current_question_value_from_key(key):
    current_question = get_current_question()
    return current_question[key]

def set_current_question_value_from_key(key, val):
    current_question = get_current_question()
    current_question[key] = val

def get_current_question_answers():
    return get_current_question_value_from_key("answers")

def count_correct_answers():
    questions_correct = 0
    for item in get_question_list():
        if item["correct"] == "Y":
            questions_correct += 1

    return questions_correct

def count_incorrect_answers():
    questions_incorrect = 0
    for item in get_question_list():
        if item["correct"] == "N" and item["confirmed"] == "Y":
            questions_incorrect += 1

    return questions_incorrect

def count_no_answer_questions():
    questions_no_answers = 0
    for item in get_question_list():
        if item["confirmed"] == "N":
            questions_no_answers += 1

    return questions_no_answers

def write_results():
    col1, col2 = st.columns(2)
    with col1:
        percentage = count_correct_answers() / get_question_list_len()
        st.text(f"Total questions: {get_question_list_len()} / {percentage:.2f}%")
        st.text(f"Not answerd questions: {count_no_answer_questions()}")
    with col2:
        st.text(f"Correct answers: {count_correct_answers()}")
        st.text(f"Incorrect answer: {count_incorrect_answers()}")

@st.dialog("Results")
def popup_results():
    write_results()


