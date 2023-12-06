import streamlit as st
import random

def main():
    st.title("Spread Calculation App")

    # Inizializza la variabile di sessione
    if 'responses' not in st.session_state:
        st.session_state.responses = []
        st.session_state.form_submitted = False

    with st.form("spread_form"):
        price = round(random.uniform(1, 150), random.randint(0, 3))
        quantity = random.randint(10, 9999)
        bp = 1 / 10000
        spread = random.uniform(1, 20)
        bid, ask = round(price * (1 - spread * bp), random.randint(2, 3)), round(price * (1 + spread * bp), random.randint(2, 3))
        st.write(f"Quantity: {quantity}")
        st.write(f"Bid: {bid}, Ask: {ask}")

        mid_ans = st.number_input("Enter mid price:", value=bid, step=0.001, format="%.3f")
        spread_ans = st.number_input("Enter spread in bp:", step=0.001, format="%.1f")

        st.session_state.responses = {
                "Quantity": quantity,
                "Bid": bid,
                "Ask": ask,
                "Mid Answer": mid_ans,
                "Real mid": (ask + bid) / 2,
                "Real spread": (ask - bid) / (ask + bid),
                "Spread Answer": spread_ans
            }

        # Utilizza una variabile di stato per tenere traccia dello stato di invio del modulo
        st.session_state.form_submitted = st.form_submit_button("Submit Answers")

        if st.session_state.form_submitted:
            # Visualizza le risposte solo se il modulo è stato effettivamente inviato
            st.title("Responses")
            response = st.session_state.responses
            st.write(f"Real mid: {response['Real mid']:.3f}")
            st.write(f"Real spread: {response['Real spread'] * 10000:.3f}")
            st.write("--------------------------------------------------------")
            st.session_state.form_submitted = False

    # Add a button to refresh the page
    if st.button("Refresh Page"):
        st.caching.clear_cache()
        st.experimental_rerun()

if __name__ == "__main__":
    main()

