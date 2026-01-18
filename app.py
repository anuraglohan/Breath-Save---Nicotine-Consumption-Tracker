import streamlit as st
from pages.auth import login_page
from pages.overview import overview_page
from pages.analytics import analytics_page
from pages.predictions import predictions_page
from pages.rewards import rewards_page
from pages.settings import settings_page
from utils.data_loader import load_data

# Page configuration
st.set_page_config(
    page_title="Breath & Save Dashboard",
    page_icon="🚭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #10b981;
        margin-bottom: 2rem;
    }
    .metric-card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

# Display login or dashboard
if not st.session_state.logged_in:
    login_page()
else:
    # Load data
    notifications_df, milestones_df, rewards_df = load_data()
    
    if milestones_df is not None:
        # Sidebar navigation
        st.sidebar.markdown(f"## Welcome, {st.session_state.username}! 👋")
        st.sidebar.divider()
        
        page = st.sidebar.radio(
            "Navigation",
            ["📊 Overview", "🤖 Analytics", "🔮 Predictions", "🏆 Rewards", "⚙️ Settings"]
        )
        
        st.sidebar.divider()
        
        if st.sidebar.button("Logout", use_container_width=True, type="secondary"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()
        
        # Render selected page
        if "Overview" in page:
            overview_page(milestones_df)
        elif "Analytics" in page:
            analytics_page(milestones_df)
        elif "Predictions" in page:
            predictions_page(milestones_df)
        elif "Rewards" in page:
            rewards_page(milestones_df, rewards_df)
        elif "Settings" in page:
            settings_page()
