import streamlit as st
import numpy as np
import plotly.graph_objects as go
from ml_models.regression import SavingsPredictionModel

def predictions_page(milestones_df):
    """ML predictions using linear regression model."""
    st.title("🔮 Savings Predictions (Linear Regression)")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.info("This model uses Linear Regression to predict savings based on cigarettes avoided.\n"
                "Formula: Money Saved = Coefficient × Cigarettes Avoided + Intercept")
        
        # Train model
        prediction_model = SavingsPredictionModel()
        prediction_model.fit(milestones_df)
        
        # Get prediction range for visualization
        X_range, y_pred = prediction_model.get_prediction_range(
            max_value=milestones_df['total_cigs_avoided'].max(),
            num_points=100
        )
        
        fig_pred = go.Figure()
        fig_pred.add_trace(go.Scatter(
            x=milestones_df['total_cigs_avoided'],
            y=milestones_df['money_saved'],
            mode='markers',
            name='Actual Data',
            marker=dict(size=8, color='#3b82f6', opacity=0.6, line=dict(width=1, color='white'))
        ))
        fig_pred.add_trace(go.Scatter(
            x=X_range,
            y=y_pred,
            mode='lines',
            name='Prediction Model',
            line=dict(color='#ef4444', width=3)
        ))
        fig_pred.update_layout(
            title='Savings vs Cigarettes Avoided (Linear Regression)',
            xaxis_title='Cigarettes Avoided',
            yaxis_title='Money Saved ($)',
            hovermode='closest',
            height=400
        )
        st.plotly_chart(fig_pred, use_container_width=True)
    
    with col2:
        st.subheader("Model Performance")
        metrics = prediction_model.get_metrics()
        st.metric("R² Score", f"{metrics['r2_score']:.3f}")
        st.metric("Coefficient ($/cig)", f"${metrics['coefficient']:.2f}")
        st.metric("Intercept ($)", f"${metrics['intercept']:.2f}")
        st.info(metrics['interpretation'], icon="💡")
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Personal Prediction Tool")
        cigs_goal = st.slider("Cigarettes you plan to avoid", 0, int(milestones_df['total_cigs_avoided'].max()), 500, step=50)
    
    with col2:
        predicted = prediction_model.predict(cigs_goal)[0]
        st.metric("Predicted Savings", f"${predicted:.2f}", delta=f"${predicted/max(cigs_goal, 1):.2f} per cig")
    
    with col3:
        days_estimate = max(0, predicted / 10)
        st.metric("Estimated Timeline", f"{days_estimate:.0f} days")
