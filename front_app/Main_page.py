import streamlit as st
import requests

st.set_page_config(
    page_title="PowerLearn - Generate Content",
)


def generate_content_api(keywords, description):
    api_endpoint = "http://127.0.0.1:5000/generate_all"  # Replace with your API endpoint
    data = {
        'keywords': keywords,
        'topic_description': description
    }
    response = requests.post(api_endpoint, json=data)
    return response.json()



keywords = st.sidebar.text_input(label='Enter 2-4 Keywords (comma-separated)')
description = st.sidebar.text_area(label='Description')

if st.sidebar.button('Generate Content'):
    if keywords and description:
        keyword_list = [word.strip() for word in keywords.split(',')]
        content = generate_content_api(keyword_list, description)

        st.header("Summary")
        st.write(content['summary'])

        st.header("Example")
        st.write(content['example'])

        st.header("In-depth Explanation")
        st.write(content['in_depth_explanation'])

        st.header("Practice Questions")
        st.write(content['practice_questions'])


    else:
        st.error('Please enter keywords and description.')
