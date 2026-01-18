# Breath & Save ML Dashboard - Complete Documentation

## Overview
A comprehensive Streamlit-based smoking cessation tracking dashboard featuring machine learning analytics, user authentication, and reward management.

## Architecture

### Directory Structure
\`\`\`
breath-save-dashboard/
├── app.py                          # Main application entry point
├── requirements.txt                # Python dependencies
├── users.json                      # User credentials (auto-generated)
├── data/
│   ├── breathsave_notifications_schedule.csv
│   ├── breathsave_savings_milestones.csv
│   └── breathsave_rewards_wallet.csv
├── utils/
│   ├── auth.py                    # Authentication logic
│   └── data_loader.py             # Data loading utilities
├── ml_models/
│   ├── clustering.py              # K-Means clustering model
│   └── regression.py              # Linear regression prediction model
└── pages/
    ├── auth.py                    # Login/registration page
    ├── overview.py                # Dashboard overview
    ├── analytics.py               # ML analytics & clustering
    ├── predictions.py             # Savings predictions
    ├── rewards.py                 # Rewards tracking
    └── settings.py                # User settings
\`\`\`

## Machine Learning Models

### 1. K-Means Clustering (User Segmentation)
**Location:** `ml_models/clustering.py`

**Purpose:** Segment users into 3 distinct behavioral categories

**Algorithm:**
- Unsupervised learning algorithm
- Groups similar users together based on features
- Minimizes within-cluster distances using Euclidean distance

**Features Used:**
1. `total_cigs_avoided` - Cigarettes successfully avoided
2. `money_saved` - Total financial savings
3. `total_cigs_smoked` - Cigarettes still smoked

**How It Works:**
1. Normalize features using StandardScaler (mean=0, std=1)
2. Initialize 3 random cluster centers
3. Assign each user to nearest cluster
4. Recalculate cluster centers
5. Repeat until convergence

**Cluster Interpretation:**
- **Cluster 0 (Red) - High Achievers:** Maximum savings, most cigarettes avoided
- **Cluster 1 (Blue) - Steady Performers:** Moderate progress, consistent efforts
- **Cluster 2 (Green) - New Members:** Early stage, growing momentum

**Mathematical Formula:**
\`\`\`
J = Σ Σ ||x_i - c_j||²
where:
  x_i = individual data point
  c_j = cluster center j
  J = Total within-cluster sum of squares
\`\`\`

**Output:** User cluster assignments for visualization and analysis

---

### 2. Linear Regression (Savings Prediction)
**Location:** `ml_models/regression.py`

**Purpose:** Predict future savings based on cigarettes avoided

**Algorithm:**
- Supervised learning algorithm
- Fits a linear line through data points
- Minimizes squared errors between actual and predicted values

**Features:**
- **Independent Variable (X):** total_cigs_avoided
- **Dependent Variable (y):** money_saved

**Linear Equation:**
\`\`\`
y = mx + b
where:
  y = predicted money saved
  m = coefficient ($ per cigarette avoided)
  x = cigarettes avoided
  b = intercept (base savings)
\`\`\`

**Example Prediction:**
\`\`\`
If coefficient = 0.15 and intercept = 50:
- 100 cigs avoided → $65 saved (0.15 × 100 + 50)
- 500 cigs avoided → $125 saved (0.15 × 500 + 50)
- 1000 cigs avoided → $200 saved (0.15 × 1000 + 50)
\`\`\`

**Model Performance Metrics:**
- **R² Score:** Measures goodness of fit (0-1 scale)
  - 1.0 = Perfect prediction
  - 0.5 = Model explains 50% of variance
  - 0.0 = Model performs no better than average

**Limitations:**
- Assumes linear relationship (may not hold in all cases)
- Sensitive to outliers
- Cannot capture sudden behavioral changes

**Output:** 
- Prediction line for visualization
- R² score and coefficients
- Individual savings predictions

---

## Authentication System

**Location:** `utils/auth.py`

**Security Features:**
1. **Password Hashing:** SHA-256 encryption
2. **User Storage:** JSON file with encrypted passwords
3. **Session Management:** Streamlit session state

**Authentication Flow:**
\`\`\`
User Input → hash_password() → Compare with stored hash
   ↓
  IF Match → Login successful
  IF No match → Login failed
\`\`\`

**Functions:**
- `hash_password()` - One-way encryption
- `verify_user()` - Check credentials
- `register_user()` - Create new account
- `update_password()` - Change password securely

---

## Data Flow

\`\`\`
CSV Files → load_data() → Cache → Pages
    ↓
Notifications Schedule
Savings Milestones → ML Models → Visualizations → Dashboard
Rewards Wallet
\`\`\`

**Caching Strategy:** @st.cache_data decorator prevents redundant data reloading

---

## How to Run

1. **Install Dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

2. **Prepare Data Files:**
   - Place CSV files in `data/` directory:
     - breathsave_notifications_schedule.csv
     - breathsave_savings_milestones.csv
     - breathsave_rewards_wallet.csv

3. **Run Application:**
   \`\`\`bash
   streamlit run app.py
   \`\`\`

4. **Access Dashboard:**
   - Open browser to `http://localhost:8501`
   - Create account or login
   - Explore dashboard pages

---

## Page Descriptions

### Overview
- Key statistics (users, avg savings, etc.)
- Distribution histograms
- Top savers leaderboard

### Analytics
- 3D K-Means clustering visualization
- Correlation heatmap
- Cluster statistics and profiles

### Predictions
- Linear regression model visualization
- Savings prediction tool
- Model performance metrics

### Rewards
- Reward redemption status
- Reward types distribution
- Top reward earners

### Settings
- Account information
- Password management
- Session details

---

## Technical Stack

- **Frontend:** Streamlit
- **Data Processing:** Pandas, NumPy
- **ML Libraries:** scikit-learn (KMeans, LinearRegression)
- **Visualization:** Plotly
- **Authentication:** SHA-256 hashing
- **Storage:** JSON files
