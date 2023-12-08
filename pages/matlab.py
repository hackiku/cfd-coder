import streamlit as st
import os

# Function to read content from a file
def load_content_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Main Streamlit UI for matlab.py
def main():
    st.title('MATLAB zadaci/primeri')

    # List all .m files in the matlab_code directory
    matlab_files = [file for file in os.listdir('./matlab_code') if file.endswith('.m')]
    problem_titles = [file.replace('.m', '').replace('_', ' ') for file in matlab_files]

    # Problem selector
    selected_title = st.selectbox("Select Problem", problem_titles)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"{selected_title}")

    text_file_path = f"./matlab_code/{selected_title.replace(' ','_')}.txt"
    if os.path.exists(text_file_path):
        text_content = load_content_from_file(text_file_path)
        st.markdown(text_content, unsafe_allow_html=True)

    matlab_file_path = f"./matlab_code/{selected_title.replace(' ', '_')}.m"
    if os.path.exists(matlab_file_path):
        matlab_code = load_content_from_file(matlab_file_path)
        st.code(matlab_code, language='matlab')
    else:
        st.error(f'MATLAB file not found: {matlab_file_path}')

    # markdown explanation
    markdown_file_path = f"./matlab_code/{selected_title.replace(' ', '_')}.md"
    if os.path.exists(markdown_file_path):
        markdown_content = load_content_from_file(markdown_file_path)
        st.markdown(markdown_content, unsafe_allow_html=True)

    # ================= #

    st.markdown("***")
    
    col1, col2 = st.columns(2)

    # MATLAB code on the left
    with col1:
        matlab_file_path = f"./matlab_code/{selected_title.replace(' ', '_')}.m"
        if os.path.exists(matlab_file_path):
            matlab_code = load_content_from_file(matlab_file_path)
            st.code(matlab_code, language='matlab')
        else:
            st.error(f'MATLAB file not found: {matlab_file_path}')

    # Markdown with LaTeX on the right
    with col2:
        markdown_file_path = f"./matlab_code/{selected_title.replace(' ', '_')}.md"
        if os.path.exists(markdown_file_path):
            markdown_content = load_content_from_file(markdown_file_path)
            st.markdown(markdown_content, unsafe_allow_html=True)

if __name__ == "__main__":
    main()