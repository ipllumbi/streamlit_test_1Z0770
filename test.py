import json
import streamlit as st
import utils


st.markdown(f"<h1 style='text-align: center;'>Test 1Z0-770</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("Previous", use_container_width=True):
        utils.decrement_current_question_indx()

with col2:
    if st.button("Next", use_container_width=True):
        utils.increment_current_question_indx()


st.subheader(utils.get_current_question_value_from_key("question_description"))


correct_answers = []
selected_answers = []

current_question_answer_options = utils.get_current_question_answers()
for answer in current_question_answer_options:
    selected = st.checkbox(label=answer["answer_desc"], value=(True if answer['selected'] == 'Y' else False))
    if selected:
        answer["selected"] = "Y"
    else:
        answer["selected"] = "N"

    correct_answers.append(answer["correct_flag"] == "Y")
    selected_answers.append(answer["selected"] == "Y")

is_correct = False

if st.button("Confirm", use_container_width=True):
    is_correct = utils.are_equal(correct_answers, selected_answers)
    utils.set_current_question_value_from_key("confirmed", "Y")
    utils.set_current_question_value_from_key("correct", "Y" if is_correct else "N")

    if is_correct:
        st.success('Correct answer!', icon="✅")
    else:
        ra = []
        for answer in current_question_answer_options:
            if answer['correct_flag'] == 'Y':
                ra.append(answer['answer_code'])

        st.error(f"Wrong answer! correct option is {ra}", icon="🚨")

if st.button("Finish", use_container_width=True):
    utils.popup_results()

st.markdown(f"<p style='text-align: center;'>{utils.get_current_question_indx() + 1} of {utils.get_question_list_len()} questions</p>", unsafe_allow_html=True)


