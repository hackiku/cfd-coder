import streamlit as st
import json
from PIL import Image
import os

# Function to load data from db.json
def load_data():
    with open('db.json', 'r') as file:
        data = json.load(file)
    return data

# Function to read markdown from a file
def load_markdown_from_file(file_path):
    with open(file_path, 'r') as file:
        markdown_content = file.read()
    return markdown_content

# Main Streamlit UI
def main():
    st.title('Proracunska aerodinamika')

    # Initialize the current slide in session state
    if 'current_slide' not in st.session_state:
        st.session_state.current_slide = 1

    # Load data from JSON
    data = load_data()

    # Static subject selection since each subject has its own page
    selected_subject = "proracunska aerodinamika"

    # Lesson Selection with Number
    lessons = data[selected_subject]
    lesson_numbers = [lesson["lesson_number"] for lesson in lessons]
    lesson_titles = [lesson["title"] for lesson in lessons]
    col1, col2 = st.columns([1, 4])
    with col1:
        selected_lesson_number = st.selectbox("Lesson:", lesson_numbers)
    with col2:
        selected_lesson_title = st.selectbox("Select Lesson Title", lesson_titles)

    # Find the selected lesson
    selected_lesson = next(lesson for lesson in lessons if lesson["title"] == selected_lesson_title)

    # slider
    slide_numbers = [slide["slide_number"] for slide in selected_lesson["slides"]]
    st.session_state.current_slide = st.slider("Select Slide", min_value=min(slide_numbers), max_value=max(slide_numbers), value=st.session_state.current_slide)

    # nav
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button('Previous'):
            if st.session_state.current_slide > 1:
                st.session_state.current_slide -= 1

    with col2:
        st.write(f"Slide {st.session_state.current_slide} of {len(slide_numbers)}")

    with col3:
        if st.button('Next'):
            if st.session_state.current_slide < len(slide_numbers):
                st.session_state.current_slide += 1

    # slide show
    current_slide = selected_lesson["slides"][st.session_state.current_slide - 1]
    col1, col2 = st.columns([3, 2])
    with col1:
        st.image(current_slide["image_path"], use_column_width=True)
    with col2:
        st.code("""
        clear all, clc
        nu=0.002; h=0.04; ug=20; rho=1000; dpdx = 20000;
        Ny = 11;
        y=linspace(0,h,Ny);
        dy=y(2)-y(1);
        t=0;
        tfinal=1;
        dt=1e-3;
        d=nu*dt/dy^2;
        u00 = zeros(1,Ny);
        u00(Ny) = ug;
        t=t+dt;
        u0=zeros(1,Ny);
        u0(1)=0;
        u0(2:Ny-1) = u00(2:Ny-1) + d*(u00(3:Ny) - 2*u00(2:Ny-1) + u00(1:Ny-2)) - dt/rho * dpdx;
        uo(Ny) = ug;
        while (t < tfinal)
            t = t + dt;
            u(1) = 0;
            u(Ny) = ug;
            u(2:Ny-1) = (1-2*d) / (1+2*d)*u00(2:Ny-1) + 2*d/(1+2*d)*(u0(3:Ny)+u0(1:Ny-2))-2*dt/(rho*(1+2*d))*dpdx;
            u00=u0;
            plot(u,u0,y),drawnow;
        end
        """)

        if isinstance(current_slide["description"], str) and current_slide["description"].endswith('.md'):
            # Check if the file exists
            if os.path.exists(current_slide["description"]):
                markdown_content = load_markdown_from_file(current_slide["description"])
                st.markdown(markdown_content, unsafe_allow_html=True)
            else:
                st.error(f'Markdown file not found: {current_slide["description"]}')
        else:
            st.markdown(current_slide["description"])
    

if __name__ == "__main__":
    main()
