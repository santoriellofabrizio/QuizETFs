import random
import streamlit as st

def generate_question():
    big = random.randint(1, int(1e6))
    small_num = random.randint(1, 100)
    small_scale = random.choice([1, 0.1, 0.01, 0.001, 0.0001])
    small = small_scale * small_num
    return big, small

def main():
    st.title("Guess game")

    big, small = generate_question()
    st.write(f"Prodotto di {big} X {small} ?")

    ans = big * small

    # Utilizza st.text_input per permettere all'utente di inserire la risposta
    user_answer = st.text_input("Inserisci la tua risposta", key="user_answer")

    if user_answer:
        if user_answer[-1].lower() == "k":
            user_answer = float(user_answer[:-1])*1000
        elif user_answer[-2].lower() == "bp":
            user_answer = float(user_answer[:-2])/10000
        else:
            user_answer = float(user_answer)

        st.write(f"answer: {ans}")
        error_perc = round(abs(ans - user_answer)/ans,2)
        st.write(f"error perc: {error_perc*100}%")
        if error_perc < 0.1:
            st.success("right!")
        else:
            st.error("wrong!")

if __name__ == "__main__":
    main()
