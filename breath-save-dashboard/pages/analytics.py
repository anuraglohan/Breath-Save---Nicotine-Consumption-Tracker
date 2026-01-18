import streamlit as st
import plotly.express as px
from ml_models.clustering import UserSegmentationModel

def analytics_page(milestones_df):
    """ML analytics with K-Means clustering and correlations."""
    st.title("🤖 ML Analytics - User Segmentation")
    
    # Initialize and run clustering model
    segmentation_model = UserSegmentationModel(n_clusters=3)
    clusters = segmentation_model.fit_predict(milestones_df)
    milestones_df['cluster'] = clusters
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("3D User Segmentation (K-Means)")
        st.info("This visualization uses K-Means clustering to segment users into 3 groups based on:\n"
                "- Cigarettes avoided\n- Money saved\n- Cigarettes smoked")
        
        fig_3d = px.scatter_3d(
            milestones_df,
            x='total_cigs_avoided',
            y='money_saved',
            z='total_cigs_smoked',
            color='cluster',
            title='K-Means Clustering (3 User Segments)',
            color_discrete_sequence=['#ef4444', '#3b82f6', '#10b981'],
            hover_data=['user_id', 'points']
        )
        st.plotly_chart(fig_3d, use_container_width=True)
    
    with col2:
        st.subheader("Feature Correlations")
        st.info("Correlation matrix shows relationships between features:\n"
                "1.0 = Perfect positive relationship\n"
                "-1.0 = Perfect negative relationship\n"
                "0.0 = No relationship")
        
        corr_data = milestones_df[['total_cigs_avoided', 'money_saved', 'total_cigs_smoked', 'points']]
        corr_matrix = corr_data.corr()
        fig_heatmap = px.imshow(
            corr_matrix,
            title='Correlation Heatmap',
            color_continuous_scale='RdBu',
            zmin=-1, zmax=1,
            labels=dict(color='Correlation')
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)
    
    st.divider()
    
    # Cluster Analysis with statistics
    st.subheader("Cluster Analysis & Statistics")
    cluster_stats = segmentation_model.get_cluster_stats(milestones_df, clusters)
    
    cluster_cols = st.columns(3)
    for idx, (cluster_name, stats) in enumerate(cluster_stats.items()):
        with cluster_cols[idx]:
            with st.container(border=True):
                st.markdown(f"### {cluster_name}")
                st.metric("Users", stats['users'])
                st.metric("Avg Savings", f"${stats['avg_savings']:.0f}")
                st.metric("Avg Cigs Avoided", f"{stats['avg_cigs_avoided']:.0f}")
