import json
import streamlit as st
import utils

utils.init_session_state()

st.set_page_config(layout="wide")

test_page = st.Page("test.py", title="Take test", default=True)
list_page = st.Page("question_list.py", title="Questions list")

pg = st.navigation([test_page, list_page])

if __name__ == "__main__":
    pg.run()
