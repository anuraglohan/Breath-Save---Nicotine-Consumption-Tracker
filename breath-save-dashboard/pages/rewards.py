import streamlit as st
import plotly.express as px

def rewards_page(milestones_df, rewards_df):
    """Rewards and wallet tracking with analytics."""
    st.title("🏆 Rewards & Wallet")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_points = milestones_df['points'].sum()
        st.metric("Total Points Earned", f"{total_points:,}")
    with col2:
        redeemed_count = len(rewards_df[rewards_df['redemption_status'] == 'redeemed'])
        st.metric("Rewards Redeemed", redeemed_count)
    with col3:
        pending_count = len(rewards_df[rewards_df['redemption_status'] == 'pending'])
        st.metric("Pending Rewards", pending_count)
    with col4:
        avg_points = milestones_df['points'].mean()
        st.metric("Avg Points/User", f"{avg_points:.0f}")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_status = px.pie(
            rewards_df,
            names='redemption_status',
            title='Reward Redemption Status',
            color_discrete_map={'redeemed': '#10b981', 'pending': '#f59e0b'}
        )
        st.plotly_chart(fig_status, use_container_width=True)
    
    with col2:
        reward_type_counts = rewards_df['reward_type'].value_counts()
        fig_types = px.bar(
            x=reward_type_counts.index,
            y=reward_type_counts.values,
            title='Reward Types Distribution',
            labels={'x': 'Reward Type', 'y': 'Count'},
            color_discrete_sequence=['#8b5cf6']
        )
        st.plotly_chart(fig_types, use_container_width=True)
    
    st.divider()
    st.subheader("Top Reward Earners")
    top_earners = milestones_df.nlargest(10, 'points')[['user_id', 'points', 'money_saved']]
    st.dataframe(top_earners, use_container_width=True, hide_index=True)
