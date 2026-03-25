import streamlit as st
with st.form("My_Form"):
    col1,col2=st.columns(2)
    name1=col1.text_input("First Name")
    name2=col2.text_input("Last Name")
    email=st.text_input("Email")
    password=st.text_input("password",type="password")
    confirm_password=st.text_input("Confirm password",type="password")
    address=st.text_area("Address")
    submit=st.form_submit_button("Submit")

# After submission, handle the output

if submit:
    if password != confirm_password:
        st.error("Passwords do not match!")
    else:
        st.success("Form submitted successfully!")
        st.write("### Entered Details")
        st.write(f"**First Name:** {name1}")
        st.write(f"**Last Name:** {name2}")
        st.write(f"**Email:** {email}")
        st.write(f"**Address:** {address}")