import streamlit as st

def main():
    st.title("Summary of Your Answers")

    if 'answers' in st.session_state:
        for question_id, answer in st.session_state['answers'].items():
            st.write(f"**{question_id}:** {answer}")
    else:
        st.write("No answers submitted yet.")

if __name__ == "__main__":
    main()
