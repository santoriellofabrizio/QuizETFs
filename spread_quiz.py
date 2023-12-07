import streamlit as st
import random

def generate_random_values():
    price = round(random.uniform(1, 150), random.randint(0, 3))
    quantity = random.randint(10, 9999)
    bp = 1 / 10000
    spread = random.uniform(1, 20)
    bid, ask = round(price * (1 - spread * bp), random.randint(2, 3)), round(price * (1 + spread * bp), random.randint(2, 3))
    return quantity, bid, ask

def display_input_values(quantity, bid, ask):
    st.write(f"Quantity: {quantity}")
    st.write(f"Bid: {bid}, Ask: {ask}")

def main():
    st.title("Spread Calculation App")

    # Initialize session state variables
    if 'responses' not in st.session_state:
        st.session_state.responses = []
        st.session_state.question = None
        st.session_state.form_submitted = False

    # Generate random values for bid, ask, and quantity

    with ((st.form("spread_form"))):

        if  not st.session_state.question:
            quantity, bid, ask = generate_random_values()
        else:
            quantity = st.session_state.question["Quantity"]
            bid = st.session_state.question["Bid"]
            ask = st.session_state.question["Ask"]

        display_input_values(quantity, bid, ask)

        st.session_state.question = {
            "Quantity": quantity,
            "Bid": bid,
            "Ask": ask}


        # Collect user input for mid and spread
        mid_ans = st.number_input("Enter mid price:", value=bid, step=0.001, format="%.3f")
        spread_ans = st.number_input("Enter spread in bp:", step=0.001, format="%.1f")

        # Store responses in session state
        st.session_state.responses = {
            "Quantity": quantity,
            "Bid": bid,
            "Ask": ask,
            "Mid Answer": mid_ans,
            "Real mid": (ask + bid) / 2,
            "Real spread": (ask - bid) / (ask + bid),
            "Spread Answer": spread_ans
        }

        # Use session state to track form submission
        form_submitted = st.form_submit_button("Submit Answers")

    if form_submitted:
        # Display responses if the form is submitted
        st.title("Responses")
        real_spread_bp = st.session_state.responses["Real spread"] * 10000
        error_in_bp = abs(real_spread_bp - st.session_state.responses["Spread Answer"])
        response = st.session_state.responses
        st.write(f"Real mid: {response['Real mid']:.3f}")
        st.write(f"Real spread: {response['Real spread'] * 10000:.3f}")
        if error_in_bp < 0.1:
            st.success(f"error in bp: {error_in_bp:.2f}")
        else:
            st.warning(f"error in bp: {error_in_bp:.2f}")
        st.write("--------------------------------------------------------")
        st.session_state.form_submitted = False

    # Add a button to refresh the page
    if st.button("Next"):

        st.session_state.question = None
        st.session_state.form_submitted = False
        st.session_state.responses = None

        st.experimental_rerun()

if __name__ == "__main__":
    main()
