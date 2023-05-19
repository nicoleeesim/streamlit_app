import streamlit as st

def process_text(input_text):
    # Perform some processing on the input text and generate the output
    output_text = f"You entered: {input_text}"
    return output_text

def main():
    st.title("Text Input and Output Demo")

    # Text input
    input_text = st.text_input("Enter some text:")

    # Submit button
    if st.button("Submit"):
        # Process the input and get the output
        output_text = process_text(input_text)
        # Display the output
        st.write("Output:")
        st.write(output_text)

if __name__ == "__main__":
    main()