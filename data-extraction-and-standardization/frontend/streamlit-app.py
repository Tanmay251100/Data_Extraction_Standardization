import streamlit as st
import requests
import json

st.title('Welcome to Pytract-UI')
st.markdown('---')
st.subheader('Upload a PDF ')

uploaded_file = st.file_uploader("Choose a file ", label_visibility="hidden")
submit_btn = st.button("Upload")
api_url = "https://fastapi-service-741843712518.us-central1.run.app/docs"
upload_object_endpoint = "/upload"


if submit_btn and uploaded_file is not None:
    if uploaded_file.name.endswith(".pdf"):
        try:
            body = {"file":uploaded_file}
            response = requests.post(api_url+upload_object_endpoint,files=body)
            if response.status_code == 200 :
                st.success(f"PDF live @ {response.json()['url']}")
            else :
                st.error(response.json()['detail'])
        except requests.exceptions.RequestException as e :
            st.error(e)
    else:
        st.warning(f"Input Document is not a PDF")
elif submit_btn and (uploaded_file is None) :
    st.warning(f"Choose a File to upload")           

        