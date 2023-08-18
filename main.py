import streamlit as st
import pandas as pd
from random import randrange

st.title("ETFs quiz web app")

etf_col = ["XTC5", "XHY1", "HYS", "EUHI", "IHYG", "XHYG", "JNKE", "HY", "AHYE", "HYBB", "FLES", "ERNE", "AFRN", "ECRP3", "SEUC", "SUSE", "SRIC3", "LDCE", "XZE5", "EBBB", "JR15", "SE15", "CBEU5", "SRIC5", "IQEC", "IEBB", "XDEP", "CC4", "ICOV", "ECRP", "XB4F", "SUOE", "ETFCOR", "EUCR", "PSFE", "XBLC", "IEAC", "IRCP", "VECP", "VECA", "CRPE", "EUCO", "SRIC", "IBCX", "IEXF", "CBEF", "ECOEUA", "CBSEU", "FLRG", "YLD", "EYLD", "CLIM", "STHE", "STHY", "SDHY", "IHYU", "IHYE", "XUHY", "USHY", "USYH", "HYFA", "FAEU", "MINT", "USFRN", "HFRN", "FLOE", "FLTR", "IU0E", "SUSC", "VDCA", "VUSC", "LDCU", "CBUS5", "CBUS5E", "IUCB", "XYLD", "SUOU", "UCRP", "USIG", "USIH", "VUCP", "VUCE", "ETFUSC", "PUIG", "FLUC", "LQDE", "XDGU", "XDGE", "CBSUS", "CBSUSE", "CBUS", "CBUSE", "CBSUSA", "LUSC", "ECR1", "ECMS", "ECMD", "UBBB", "ECMA", "ECMF", "ETFCRP", "COOL", "JREB", "XCO2E", "TCBT", "V3GF", "V3GE", "VDCE", "JRUB", "CORP", "XZBU", "ECE", "ECO", "USCE", "THEP", "XZHE", "HYC", "EHYA", "HYLD", "SJNK", "SJNE", "FAMUSS", "GHYEH", "GHYE", "JGHY", "JYEH", "UHYE", "XZHY", "WING", "USHYC", "GFA", "CCBO", "COBO", "AT1", "XAT1", "AT1D", "EHYB", "EHBA", "EMHE", "EMH5", "SHEMB", "SHEME", "HYEM", "EMCR", "SBEM", "SBEME", "EMIG", "EMIGE", "VEMT", "VDEA", "EMSA", "CATHEM", "JPMB", "JMBE", "JMBA", "IEMB", "EMBE", "PEMD", "XEMB", "XUEM", "AGEB", "EMKTB", "EMBHI", "XQUA", "XQUE", "CGB", "CIB", "CBND", "CNYB", "DRGN", "C3M", "PEU", "XBOT", "IEGE", "PJS1", "EIB3", "GOVS", "X13E", "IBGS", "CSBGE3", "C13", "XYP1", "BTP13", "AAA13", "EM13", "JE13", "X13G", "TAT", "EIB5", "EU35", "C33", "X35E", "EM35", "AAA35", "IBGX", "SS1EUA", "CSBGE7", "C53", "EM57", "IBGY", "EIB7", "X57E", "TGBT", "IITB", "XY4P", "IEAG", "C73", "EM710", "GEB", "EIBX", "IBGM", "X710", "SEGA", "SECA", "EIBB", "JBEM", "ETFGOV", "EGOV", "X1G", "CB3", "VETY", "VGEA", "XGLE", "GOVY", "GOVA", "MTIG", "EMG", "BTP10", "EMAAA", "AM3A", "WGOV", "GOVE", "IBGZ", "C10", "EM1015", "EUBO", "ERTH", "LGOV", "X15E", "IBGL", "EM15", "X25E", "BBIL", "XT01", "TREI", "IBTS", "TRS3", "UST1F", "UT1EUA", "CSBGU3", "JU13", "TRE3", "U13H", "US13", "MDBA", "MDBE", "CSBGU7", "TRE7", "US37", "TRS5", "VDTE", "TRES", "ETFUST", "VDTA", "VUTY", "TRSY", "XUTD", "XUTE", "BBTR", "IBTM", "TREX", "TRXE", "UT7EUA", "TRSX", "US10C", "UST10F", "LUTR", "U10H", "US10", "EGO", "EGE", "GGOV", "GOVH", "ETFGG", "GOVG", "XGSH", "XGVD", "XG7S", "JT13", "JT13E", "XJSE", "JAPB", "INFL1", "INFL", "EMI", "IBCI", "CI3", "XEIN", "INFL10", "TIP1D", "TIP1E", "TIPU", "TIPE", "ATIP", "ITPS", "TIPS", "BINFU", "INFU", "TIP10D", "TIP10E", "GIST", "GISE", "XGII", "XGIN", "XGIU", "INXG"]
corp_gov_col = ["CORPORATE"]*170 + ["GOV"]*146
group_col = ["HY EU"]*10 \
            + ["IG EU"]*42\
            + ["HY US"]*10\
            + ["IG US"]*32\
            + ["IG GLOBAL"]*20\
            + ["HY GLOBAL"]*17\
            + ["AT1"]*7\
            + ["EM"]*27\
            + ["CHINA"]*5\
            + ["UE"]*71\
            + ["US"]*37\
            + ["GLOBAL"]*9\
            + ["JAPAN"]*4\
            + ["INFL EU"]*6\
            + ["INFL US"]*9\
            + ["INFL GL"]*6
ETFs = pd.DataFrame( [corp_gov_col,group_col],index=["CORP-GOV","Group"],columns=etf_col)
ETFs = ETFs.T


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

if "etf" not in st.session_state:

  st.session_state.etf = ETFs.index[randrange(0, len(ETFs), 1)]

corp_gov_answer = ETFs.loc[st.session_state.etf,"CORP-GOV"]
group_answer = ETFs.loc[st.session_state.etf,"Group"]

st.header(f"{st.session_state.etf}")

corp_gov_guess = st.selectbox("is corporate or gov?",
                          options=ETFs["CORP-GOV"].unique())

group_guess = st.selectbox(f"what is {st.session_state.etf} group?",
                       options=ETFs.loc[ETFs["CORP-GOV"] == corp_gov_guess, "Group"].unique())

submit = st.button("submit")
if submit:

    if corp_gov_answer == corp_gov_guess:
        if group_guess == group_answer:
            st.success("Right!")
            st.session_state.score += 1
        else:
            st.write(f"Wrong group, {st.session_state.etf} belongs to {group_answer}, but is {corp_gov_answer}")
            st.session_state.score += 0.5
    else:
        st.write(f"Wrong! {st.session_state.etf} is {corp_gov_answer}")
    st.session_state.etf = ETFs.index[randrange(0, len(ETFs), 1)]
    st.session_state.current_question += 1
    if st.session_state.current_question >= int(n_question):
        st.success(f"score: {st.session_state.score /n_question}")
        restart = st.button("restart")
        if restart:
            st.experimental_rerun()

next = st.button("Next")

