import streamlit as st
from datetime import datetime
from utils.auth import update_password

def settings_page():
    """Account settings and data management."""
    st.title("⚙️ Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Account Information")
        st.write(f"**Username:** `{st.session_state.username}`")
        if hasattr(st.session_state, 'login_time'):
            st.write(f"**Login Time:** {st.session_state.login_time.strftime('%Y-%m-%d %H:%M:%S')}")
        st.write(f"**Account Status:** Active ✓")
    
    with col2:
        st.subheader("Session Info")
        st.info(f"You are securely logged in. Your data is encrypted and protected.", icon="🔒")
    
    st.divider()
    
    st.subheader("Change Password")
    current_pass = st.text_input("Current Password", type="password")
    new_pass = st.text_input("New Password", type="password")
    confirm_pass = st.text_input("Confirm New Password", type="password")
    
    if st.button("Update Password", use_container_width=True):
        if len(new_pass) < 6:
            st.error("New password must be at least 6 characters")
        elif new_pass != confirm_pass:
            st.error("New passwords don't match")
        else:
            success, message = update_password(st.session_state.username, current_pass, new_pass)
            if success:
                st.success(message)
            else:
                st.error(message)
