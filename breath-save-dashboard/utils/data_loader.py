import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    """
    Load and cache CSV data files for the dashboard.
    
    Returns:
        tuple: (notifications_df, milestones_df, rewards_df)
    """
    try:
        notifications = pd.read_csv('data/breathsave_notifications_schedule.csv')
        milestones = pd.read_csv('data/breathsave_savings_milestones.csv')
        rewards = pd.read_csv('data/breathsave_rewards_wallet.csv')
        return notifications, milestones, rewards
    except FileNotFoundError:
        st.error("Data files not found in /data directory")
        return None, None, None
