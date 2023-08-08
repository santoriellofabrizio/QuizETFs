import streamlit as st
import pandas as pd
from random import randrange

st.title("ETFs quiz web app")
filepath = "listETFs.xlsx"
ETFs = pd.read_excel(filepath,index_col=0)

def getRandom():
    random_etf_number = randrange(0, len(ETFs), 1)
    st.session_state.random = random_etf_number

if "options_group" not in st.session_state:
    st.session_state.options_group = []
if "corp_gov_guesses" not in st.session_state:
    st.session_state.corp_gov_guess = "CORPORATE"
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "n_question" not in st.session_state:
    n_question = st.selectbox("How many questions do you want to do?",[5,10,20])

def options_group():
    st.session_state.options_group = ETFs.loc[ETFs["CORP-GOV"] == st.session_state.corp_gov_guess, "Group"].unique()
    return

if "random" not in st.session_state:
    getRandom()

etf = ETFs.index[st.session_state.random]
corp_gov_answer = ETFs.loc[etf,"CORP-GOV"]
group_answer = ETFs.loc[etf,"Group"]

st.header(f"{etf}")

corp_gov_guess = st.selectbox("is corporate or gov?",
                          options=ETFs["CORP-GOV"].unique())

group_guess = st.selectbox(f"what is {etf} group?",
                       options=ETFs.loc[ETFs["CORP-GOV"] == corp_gov_guess, "Group"].unique())

finish = st.button("submit")
if finish:
    if corp_gov_answer == corp_gov_guess:
        if group_guess == group_answer:
            st.success("Right!")
            st.session_state.score += 1
        else:
            st.write(f"Wrong group, {etf} belongs to {group_answer}, but is {corp_gov_answer}")
            st.session_state.score += 0.5
    else:
        st.write(f"Wrong! {etf} is {corp_gov_answer}")

    st.session_state.current_question += 1
    if st.session_state.current_question >= int(n_question):
        st.success(f"score: {st.session_state.score /n_question}")
        restart = st.button("restart")
        if restart:
            st.experimental_rerun()

next = st.button("Next")
if next:
    getRandom()














