import streamlit as st
from datetime import datetime
from utils.auth import verify_user, register_user

def login_page():
    """Display login and registration page."""
    st.markdown('<div class="main-header"><h1>🚭 Breath & Save</h1></div>', 
                unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 18px; color: #666;">Your Journey to a Smoke-Free Life</p>', 
                unsafe_allow_html=True)
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Login")
        login_username = st.text_input("Username", key="login_user", placeholder="Enter your username")
        login_password = st.text_input("Password", type="password", key="login_pass", placeholder="Enter your password")
        
        if st.button("Login", key="login_btn", use_container_width=True):
            if verify_user(login_username, login_password):
                st.session_state.logged_in = True
                st.session_state.username = login_username
                st.session_state.login_time = datetime.now()
                st.success("Login successful! Redirecting...")
                st.rerun()
            else:
                st.error("Invalid username or password")
    
    with col2:
        st.subheader("Create Account")
        reg_username = st.text_input("New Username", key="reg_user", placeholder="Choose a username")
        reg_password = st.text_input("New Password", type="password", key="reg_pass", placeholder="Create a password")
        reg_confirm = st.text_input("Confirm Password", type="password", key="reg_confirm", placeholder="Confirm password")
        
        if st.button("Register", key="reg_btn", use_container_width=True):
            if not reg_username or not reg_password:
                st.error("Username and password are required")
            elif len(reg_password) < 6:
                st.error("Password must be at least 6 characters")
            elif reg_password != reg_confirm:
                st.error("Passwords don't match")
            else:
                success, message = register_user(reg_username, reg_password)
                if success:
                    st.success(message)
                    st.balloons()
                else:
                    st.error(message)
