import json
import streamlit as st

st.set_page_config(layout="wide")
def scrape():
    with open('./docs/1z0770.json', 'r') as file:
        questions = json.load(file)

    return questions


if "qi" not in st.session_state:
    st.session_state["qi"] = 0

q = scrape()

for question in q:
    question['confirmed'] = 'N'
    question['correct'] = 'N'
    for answer in question['answers']:
        answer['selected'] = "N"

if "test" not in st.session_state:
    st.session_state["test"] = q

test_page = st.Page("test.py", title="Take test", default=True)
list_page = st.Page("question_list.py", title="Questions list")

pg = st.navigation([test_page, list_page])

if __name__ == "__main__":
    pg.run()
