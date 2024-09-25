import streamlit as st
import pandas as pd
import utils


def on_select():
    selected_row = st.session_state.get('selected_row')
    selection_index = st.session_state['selected_row']["selection"]["rows"][0]
    utils.set_current_question_indx(selection_index)


df = utils.get_question_list_df()

df['confirmed'] = df['confirmed'].replace('N', '🚨')
df['confirmed'] = df['confirmed'].replace('Y', '✅')

df['correct'] = df['correct'].replace('N', '🚨')
df['correct'] = df['correct'].replace('Y', '✅')

utils.write_results()

st.dataframe(df, use_container_width=True, hide_index=True, selection_mode="single-row", on_select=on_select, key='selected_row', height=700, column_config={
    "question_description": "Question",
    "confirmed": "Cofirmed",
    "correct": "Correct"}
             )

if st.button("Go to selected question", use_container_width=True):
    st.switch_page("test.py")
