import numpy as np
import pandas as pd
import streamlit as st
from random import randrange


# python -m streamlit run C:\Users\GBS08935\AppData\Roaming\JetBrains\PyCharm2023.1\scratches\scratch_3.py
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def diff(lst1, lst2):
    lst3 = [value for value in lst1 if value not in lst2]
    return lst3


submit: bool = False

st.title("ETFs quiz web app")
corp_gov_col = ["CORPORATE"] * 170 + ["GOV"] * 146

data = [
    ['XTC5', 'HY EU'],
    ['XHY1', 'HY EU'],
    ['HYS', 'HY EU'],
    ['EUHI', 'HY EU'],
    ['IHYG', 'HY EU'],
    ['XHYG', 'HY EU'],
    ['JNKE', 'HY EU'],
    ['HY', 'HY EU'],
    ['AHYE', 'HY EU'],
    ['HYBB', 'HY EU'],
    ['FLES', 'IG EU'],
    ['ERNE', 'IG EU'],
    ['AFRN', 'IG EU'],
    ['ECRP3', 'IG EU'],
    ['SEUC', 'IG EU'],
    ['SUSE', 'IG EU'],
    ['SRIC3', 'IG EU'],
    ['LDCE', 'IG EU'],
    ['XZE5', 'IG EU'],
    ['EBBB', 'IG EU'],
    ['JR15', 'IG EU'],
    ['SE15', 'IG EU'],
    ['CBEU5', 'IG EU'],
    ['SRIC5', 'IG EU'],
    ['IQEC', 'IG EU'],
    ['IEBB', 'IG EU'],
    ['XDEP', 'IG EU'],
    ['CC4', 'IG EU'],
    ['ICOV', 'IG EU'],
    ['ECRP', 'IG EU'],
    ['XB4F', 'IG EU'],
    ['SUOE', 'IG EU'],
    ['ETFCOR', 'IG EU'],
    ['EUCR', 'IG EU'],
    ['PSFE', 'IG EU'],
    ['XBLC', 'IG EU'],
    ['IEAC', 'IG EU'],
    ['IRCP', 'IG EU'],
    ['VECP', 'IG EU'],
    ['VECA', 'IG EU'],
    ['CRPE', 'IG EU'],
    ['EUCO', 'IG EU'],
    ['SRIC', 'IG EU'],
    ['IBCX', 'IG EU'],
    ['IEXF', 'IG EU'],
    ['CBEF', 'IG EU'],
    ['ECOEUA', 'IG EU'],
    ['CBSEU', 'IG EU'],
    ['FLRG', 'IG EU'],
    ['YLD', 'IG EU'],
    ['EYLD', 'IG EU'],
    ['CLIM', 'IG EU'],
    ['STHE', 'HY US'],
    ['STHY', 'HY US'],
    ['SDHY', 'HY US'],
    ['IHYU', 'HY US'],
    ['IHYE', 'HY US'],
    ['XUHY', 'HY US'],
    ['USHY', 'HY US'],
    ['USYH', 'HY US'],
    ['HYFA', 'HY US'],
    ['FAEU', 'HY US'],
    ['MINT', 'IG US'],
    ['USFRN', 'IG US'],
    ['HFRN', 'IG US'],
    ['FLOE', 'IG US'],
    ['FLTR', 'IG US'],
    ['IU0E', 'IG US'],
    ['SUSC', 'IG US'],
    ['VDCA', 'IG US'],
    ['VUSC', 'IG US'],
    ['LDCU', 'IG US'],
    ['CBUS5', 'IG US'],
    ['CBUS5E', 'IG US'],
    ['IUCB', 'IG US'],
    ['XYLD', 'IG US'],
    ['SUOU', 'IG US'],
    ['UCRP', 'IG US'],
    ['USIG', 'IG US'],
    ['USIH', 'IG US'],
    ['VUCP', 'IG US'],
    ['VUCE', 'IG US'],
    ['ETFUSC', 'IG US'],
    ['PUIG', 'IG US'],
    ['FLUC', 'IG US'],
    ['LQDE', 'IG US'],
    ['XDGU', 'IG US'],
    ['XDGE', 'IG US'],
    ['CBSUS', 'IG US'],
    ['CBSUSE', 'IG US'],
    ['CBUS', 'IG US'],
    ['CBUSE', 'IG US'],
    ['CBSUSA', 'IG US'],
    ['LUSC', 'IG US'],
    ['ECR1', 'IG GLOBAL'],
    ['ECMS', 'IG GLOBAL'],
    ['ECMD', 'IG GLOBAL'],
    ['UBBB', 'IG GLOBAL'],
    ['ECMA', 'IG GLOBAL'],
    ['ECMF', 'IG GLOBAL'],
    ['ETFCRP', 'IG GLOBAL'],
    ['COOL', 'IG GLOBAL'],
    ['JREB', 'IG GLOBAL'],
    ['XCO2E', 'IG GLOBAL'],
    ['TCBT', 'IG GLOBAL'],
    ['V3GF', 'IG GLOBAL'],
    ['V3GE', 'IG GLOBAL'],
    ['VDCE', 'IG GLOBAL'],
    ['JRUB', 'IG GLOBAL'],
    ['CORP', 'IG GLOBAL'],
    ['XZBU', 'IG GLOBAL'],
    ['ECE', 'IG GLOBAL'],
    ['ECO', 'IG GLOBAL'],
    ['USCE', 'IG GLOBAL'],
    ['THEP', 'HY GLOBAL'],
    ['XZHE', 'HY GLOBAL'],
    ['HYC', 'HY GLOBAL'],
    ['EHYA', 'HY GLOBAL'],
    ['HYLD', 'HY GLOBAL'],
    ['SJNK', 'HY GLOBAL'],
    ['SJNE', 'HY GLOBAL'],
    ['FAMUSS', 'HY GLOBAL'],
    ['GHYEH', 'HY GLOBAL'],
    ['GHYE', 'HY GLOBAL'],
    ['JGHY', 'HY GLOBAL'],
    ['JYEH', 'HY GLOBAL'],
    ['UHYE', 'HY GLOBAL'],
    ['XZHY', 'HY GLOBAL'],
    ['WING', 'HY GLOBAL'],
    ['USHYC', 'HY GLOBAL'],
    ['GFA', 'HY GLOBAL'],
    ['CCBO', 'AT1'],
    ['COBO', 'AT1'],
    ['AT1', 'AT1'],
    ['XAT1', 'AT1'],
    ['AT1D', 'AT1'],
    ['EHYB', 'AT1'],
    ['EHBA', 'AT1'],
    ['EMHE', 'EM'],
    ['EMH5', 'EM'],
    ['SHEMB', 'EM'],
    ['SHEME', 'EM'],
    ['HYEM', 'EM'],
    ['EMCR', 'EM'],
    ['SBEM', 'EM'],
    ['SBEME', 'EM'],
    ['EMIG', 'EM'],
    ['EMIGE', 'EM'],
    ['VEMT', 'EM'],
    ['VDEA', 'EM'],
    ['EMSA', 'EM'],
    ['CATHEM', 'EM'],
    ['JPMB', 'EM'],
    ['JMBE', 'EM'],
    ['JMBA', 'EM'],
    ['IEMB', 'EM'],
    ['EMBE', 'EM'],
    ['PEMD', 'EM'],
    ['XEMB', 'EM'],
    ['XUEM', 'EM'],
    ['AGEB', 'EM'],
    ['EMKTB', 'EM'],
    ['EMBHI', 'EM'],
    ['XQUA', 'EM'],
    ['XQUE', 'EM'],
    ['CGB', 'CHINA'],
    ['CIB', 'CHINA'],
    ['CBND', 'CHINA'],
    ['CNYB', 'CHINA'],
    ['DRGN', 'CHINA'],
    ['C3M', 'UE'],
    ['PEU', 'UE'],
    ['XBOT', 'UE'],
    ['IEGE', 'UE'],
    ['PJS1', 'UE'],
    ['EIB3', 'UE'],
    ['GOVS', 'UE'],
    ['X13E', 'UE'],
    ['IBGS', 'UE'],
    ['CSBGE3', 'UE'],
    ['C13', 'UE'],
    ['XYP1', 'UE'],
    ['BTP13', 'UE'],
    ['AAA13', 'UE'],
    ['EM13', 'UE'],
    ['JE13', 'UE'],
    ['X13G', 'UE'],
    ['TAT', 'UE'],
    ['EIB5', 'UE'],
    ['EU35', 'UE'],
    ['C33', 'UE'],
    ['X35E', 'UE'],
    ['EM35', 'UE'],
    ['AAA35', 'UE'],
    ['IBGX', 'UE'],
    ['SS1EUA', 'UE'],
    ['CSBGE7', 'UE'],
    ['C53', 'UE'],
    ['EM57', 'UE'],
    ['IBGY', 'UE'],
    ['EIB7', 'UE'],
    ['X57E', 'UE'],
    ['TGBT', 'UE'],
    ['IITB', 'UE'],
    ['XY4P', 'UE'],
    ['IEAG', 'UE'],
    ['C73', 'UE'],
    ['EM710', 'UE'],
    ['GEB', 'UE'],
    ['EIBX', 'UE'],
    ['IBGM', 'UE'],
    ['X710', 'UE'],
    ['SEGA', 'UE'],
    ['SECA', 'UE'],
    ['EIBB', 'UE'],
    ['JBEM', 'UE'],
    ['ETFGOV', 'UE'],
    ['EGOV', 'UE'],
    ['X1G', 'UE'],
    ['CB3', 'UE'],
    ['VETY', 'UE'],
    ['VGEA', 'UE'],
    ['XGLE', 'UE'],
    ['GOVY', 'UE'],
    ['GOVA', 'UE'],
    ['MTIG', 'UE'],
    ['EMG', 'UE'],
    ['BTP10', 'UE'],
    ['EMAAA', 'UE'],
    ['AM3A', 'UE'],
    ['WGOV', 'UE'],
    ['GOVE', 'UE'],
    ['IBGZ', 'UE'],
    ['C10', 'UE'],
    ['EM1015', 'UE'],
    ['EUBO', 'UE'],
    ['ERTH', 'UE'],
    ['LGOV', 'UE'],
    ['X15E', 'UE'],
    ['IBGL', 'UE'],
    ['EM15', 'UE'],
    ['X25E', 'UE'],
    ['BBIL', 'US'],
    ['XT01', 'US'],
    ['TREI', 'US'],
    ['IBTS', 'US'],
    ['TRS3', 'US'],
    ['UST1F', 'US'],
    ['UT1EUA', 'US'],
    ['CSBGU3', 'US'],
    ['JU13', 'US'],
    ['TRE3', 'US'],
    ['U13H', 'US'],
    ['US13', 'US'],
    ['MDBA', 'US'],
    ['MDBE', 'US'],
    ['CSBGU7', 'US'],
    ['TRE7', 'US'],
    ['US37', 'US'],
    ['TRS5', 'US'],
    ['VDTE', 'US'],
    ['TRES', 'US'],
    ['ETFUST', 'US'],
    ['VDTA', 'US'],
    ['VUTY', 'US'],
    ['TRSY', 'US'],
    ['XUTD', 'US'],
    ['XUTE', 'US'],
    ['BBTR', 'US'],
    ['IBTM', 'US'],
    ['TREX', 'US'],
    ['TRXE', 'US'],
    ['UT7EUA', 'US'],
    ['TRSX', 'US'],
    ['US10C', 'US'],
    ['UST10F', 'US'],
    ['LUTR', 'US'],
    ['U10H', 'US'],
    ['US10', 'US'],
    ['EGO', 'GLOBAL'],
    ['EGE', 'GLOBAL'],
    ['GGOV', 'GLOBAL'],
    ['GOVH', 'GLOBAL'],
    ['ETFGG', 'GLOBAL'],
    ['GOVG', 'GLOBAL'],
    ['XGSH', 'GLOBAL'],
    ['XGVD', 'GLOBAL'],
    ['XG7S', 'GLOBAL'],
    ['JT13', 'JAPAN'],
    ['JT13E', 'JAPAN'],
    ['XJSE', 'JAPAN'],
    ['JAPB', 'JAPAN'],
    ['INFL1', 'INFL UE'],
    ['INFL', 'INFL UE'],
    ['EMI', 'INFL UE'],
    ['IBCI', 'INFL UE'],
    ['CI3', 'INFL UE'],
    ['XEIN', 'INFL UE'],
    ['INFL10', 'INFL UE'],
    ['TIP1D', 'INFL US'],
    ['TIP1E', 'INFL US'],
    ['TIPU', 'INFL US'],
    ['TIPE', 'INFL US'],
    ['ATIP', 'INFL US'],
    ['ITPS', 'INFL US'],
    ['TIPS', 'INFL US'],
    ['BINFU', 'INFL US'],
    ['INFU', 'INFL US'],
    ['TIP10D', 'INFL US'],
    ['TIP10E', 'INFL US'],
    ['GIST', 'INFL GL'],
    ['GISE', 'INFL GL'],
    ['XGII', 'INFL GL'],
    ['XGIN', 'INFL GL'],
    ['XGIU', 'INFL GL'],
    ['INXG', 'INFL GL']
]

ETFs = pd.DataFrame(data, columns=['Code', 'Group'])
ETFs["CORP-GOV"] = corp_gov_col
group_col = ETFs["Group"].tolist()

ETFs.set_index("Code",inplace=True)
etf_col = ETFs.index.tolist()

ETFs = pd.DataFrame([corp_gov_col, group_col], index=["CORP-GOV", "Group"], columns=etf_col)
ETFs.to_excel("myETFlist.xlsx")
ETFs = ETFs.T
ETFs = ETFs.sample(frac=1)
subgroups = ["HY EU", "HY US", "IG EU", "IG US", "IG GLOBAL", "HY GLOBAL"]

ETFs = ETFs.loc[ETFs["Group"].isin(subgroups)].sample(frac=1)
rand_group = subgroups[randrange(0, len(subgroups))]
if "rand_group" not in st.session_state:
    st.session_state.rand_group = rand_group

with st.form(f"guessing elements"):
    st.title(f"{st.session_state.rand_group}")
    risp = st.multiselect('guessing the group ETFs?', etf_col)
    submit = st.form_submit_button("submit")
    if submit:
        answer = ETFs.loc[ETFs["Group"] == st.session_state.rand_group].index.tolist()
        right_answers = intersection(answer, risp)
        if len(right_answers) == 0:
            st.warning("everything wrong!")
        elif len(right_answers) == len(answer):
            st.success("everything right!")
        else:
            right_answers = right_answers
            wrong_answer = diff(risp, answer)
            missing_answer = diff(answer, risp)
            n_r,n_w,n_m = len(right_answers),len(wrong_answer),len(missing_answer)



            st.success(f"right:{n_r/(n_r+n_m):.2f}%")
            st.warning(f"wrong:{n_w/(n_r+n_m):.2f}%")
            tab1,tab2,tab3 = st.tabs(["right","wrong","missing"])

            with tab1:

                st.write(right_answers)


            with tab2:

                if n_w>0:
                    st.write(wrong_answer)
                else:
                    st.write("nothing wrong")


            with tab3:

                if n_m > 0:
                   st.write( missing_answer)
                else:
                    st.write("nothing wrong")


# displaying the selected options
