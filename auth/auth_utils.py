import streamlit as st
from .supabase_client import supabase

# Sign up a new user
def sign_up(email, password):
    response = supabase.auth.sign_up({"email": email, "password": password})
    return response

# Login existing user
def login(email, password):
    response = supabase.auth.sign_in_with_password({"email": email, "password": password})
    return response

# Send reset password email
def forgot_password(email):
    response = supabase.auth.reset_password_email(email)
    return response

# Logout
def logout():
    supabase.auth.sign_out()
    st.session_state["user"] = None
