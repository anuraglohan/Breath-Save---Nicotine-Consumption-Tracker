# Breath & Save - ML-Powered Dashboard

A comprehensive Streamlit application for tracking smoking cessation with machine learning analytics, user authentication, and reward management.

## Features

- **Secure Login & Registration**: Password-protected authentication with SHA-256 hashing
- **Dashboard Overview**: Real-time metrics and visualizations of user progress
- **ML Analytics**: K-Means clustering for user segmentation and correlation analysis
- **Predictions**: Linear regression model for savings forecasting
- **Rewards Tracking**: Monitor redemptions and reward distribution
- **Account Settings**: Change password, view account info, and more

## Installation

1. Clone the repository and install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

2. Run the application:
\`\`\`bash
streamlit run app.py
\`\`\`

3. Open your browser and navigate to `http://localhost:8501`

## Usage

### Login/Register
- Create a new account with username and password
- Login with your credentials
- Minimum password length: 6 characters

### Pages
- **Overview**: Key metrics and distribution charts
- **Analytics**: 3D clustering visualization and correlation heatmap
- **Predictions**: Linear regression model for savings prediction
- **Rewards**: Track reward redemptions and performance
- **Settings**: Manage account and password

## Data Files

The dashboard uses three CSV files located in the `/data` directory:
- `breathsave_notifications_schedule.csv` - Notification logs
- `breathsave_savings_milestones.csv` - User savings and progress
- `breathsave_rewards_wallet.csv` - Reward information

## Machine Learning Models

- **K-Means Clustering**: Segments users into 3 categories based on performance
- **Linear Regression**: Predicts money saved based on cigarettes avoided

## Security

- Passwords are hashed using SHA-256
- User credentials stored locally in `users.json`
- Session-based authentication
