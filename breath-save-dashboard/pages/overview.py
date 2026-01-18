import streamlit as st
import plotly.express as px

def overview_page(milestones_df):
    """Dashboard overview with key metrics and distributions."""
    st.title("📊 Dashboard Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Active Users", len(milestones_df), delta="Community")
    with col2:
        avg_cigs_avoided = milestones_df['total_cigs_avoided'].mean()
        st.metric("Avg Cigarettes Avoided", f"{avg_cigs_avoided:.0f}")
    with col3:
        total_savings = milestones_df['money_saved'].sum()
        st.metric("Total Collective Savings", f"${total_savings:,.0f}")
    with col4:
        avg_days = milestones_df['total_days'].mean()
        st.metric("Avg Days in Program", f"{avg_days:.0f}")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_savings = px.histogram(
            milestones_df, 
            x='money_saved', 
            nbins=40,
            title='Money Saved Distribution (All Users)',
            color_discrete_sequence=['#10b981'],
            labels={'money_saved': 'Money Saved ($)', 'count': 'Number of Users'}
        )
        fig_savings.update_layout(showlegend=False)
        st.plotly_chart(fig_savings, use_container_width=True)
    
    with col2:
        fig_cigs = px.histogram(
            milestones_df, 
            x='total_cigs_avoided', 
            nbins=40,
            title='Cigarettes Avoided Distribution',
            color_discrete_sequence=['#3b82f6'],
            labels={'total_cigs_avoided': 'Cigarettes Avoided', 'count': 'Number of Users'}
        )
        fig_cigs.update_layout(showlegend=False)
        st.plotly_chart(fig_cigs, use_container_width=True)
    
    st.divider()
    
    top_savers = milestones_df.nlargest(15, 'money_saved')[['user_id', 'money_saved', 'total_cigs_avoided']]
    fig_top = px.bar(
        top_savers, 
        x='user_id', 
        y='money_saved',
        title='Top 15 Money Savers',
        hover_data=['total_cigs_avoided'],
        color='money_saved',
        color_continuous_scale='Viridis'
    )
    fig_top.update_layout(showlegend=False)
    st.plotly_chart(fig_top, use_container_width=True)
