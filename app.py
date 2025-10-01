import streamlit as st

st.set_page_config(page_title="Streamlit Supabase Auth", page_icon="🔑")

from auth.auth_utils import sign_up, login, forgot_password, logout

# Maintain session state
if "user" not in st.session_state:
    st.session_state["user"] = None

st.title("🔑 Streamlit + Supabase Auth")

if st.session_state["user"] is None:
    menu = ["Login", "Sign Up", "Forgot Password"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Sign Up":
        st.subheader("Create New Account")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Sign Up"):
            res = sign_up(email, password)
            if res.user:
                st.success("✅ Account created! Please check your email for verification.")
            else:
                st.error(res)

    elif choice == "Login":
        st.subheader("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            res = login(email, password)
            if res.user:
                st.session_state["user"] = res.user
                st.success(f"Welcome {res.user.email} 👋")
            else:
                st.error("❌ Invalid login credentials")

    elif choice == "Forgot Password":
        st.subheader("Reset Password")
        email = st.text_input("Enter your email")

        if st.button("Send Reset Link"):
            res = forgot_password(email)
            st.info("📧 Reset password email sent. Check your inbox.")

else:
    st.success(f"✅ Logged in as {st.session_state['user'].email}")
    if st.button("Logout"):
        logout()
        st.info("You have been logged out")
