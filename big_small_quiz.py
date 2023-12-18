import random
import streamlit as st

def generate_question():
    big = random.randint(1, int(1e3))
    big_scale = random.choice([1, 0.1, 0.01 10, 100, 1000, 10000])
    big *= big_scale
    small_num = random.randint(1, 100)
    small_scale = random.choice([1, 0.1, 0.01, 0.001, 0.0001, 0.00001])
    small = small_scale * small_num
    return big, small

def main():

    st.title("Guess game")
    if "submitted" not in st.session_state or  st.session_state.submitted:
        st.session_state.big, st.session_state.small = generate_question()

    st.write(f"Prodotto di {st.session_state.big} X {st.session_state.small} ?")
    st.session_state.ans = st.session_state.big * st.session_state.small

    user_answer = st.text_input("Inserisci la tua risposta", key="user_answer", placeholder="",value="")
    st.session_state.submitted = st.button("submit")
    if st.session_state.submitted:
        if user_answer[-1].lower() == "k":
            user_answer = float(user_answer[:-1])*1000
        elif user_answer[-2:].lower() == "bp":
            user_answer = float(user_answer[:-2])/10000
        elif user_answer[-1].lower() == "m":
            user_answer = float(user_answer[:-1])*1000000
        else:
            user_answer = float(user_answer)
        st.write(f"answer: {st.session_state.ans}")
        st.write(f"you answered {user_answer}")
        error_perc = round(abs(st.session_state.ans - user_answer)/st.session_state.ans, 2)
        st.write(f"error perc: {error_perc*100}%")
        if error_perc < 0.2:
            st.success("right!")
        else:
            st.error("wrong!")



    # Aggiungi un pulsante per aggiornare l'app
    if st.button("Refresh App"):
        st.session_state.submitted = False

        st.experimental_rerun()

if __name__ == "__main__":
    main()
