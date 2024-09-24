import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

selected_row = st.session_state.get('selected_row')


def on_select():
    # Handle the selected row here
    selectedrow = st.session_state['selected_row']["selection"]["rows"]
    st.session_state["qi"] = selectedrow[0]


df = pd.DataFrame(st.session_state['test'], columns=(['question_description', 'confirmed', 'correct']))

st.dataframe(df, use_container_width=True, hide_index=True, selection_mode="single-row", on_select=on_select, key='selected_row', column_config={
    "question_description": "Question",
    "confirmed": "Cofirmed",
    "correct": "Correct"}
             )

if st.button("Review"):
    st.switch_page("test.py")