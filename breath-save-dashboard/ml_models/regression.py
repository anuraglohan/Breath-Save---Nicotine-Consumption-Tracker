"""
LINEAR REGRESSION MODEL
=======================

Purpose: Predict future savings based on cigarettes avoided

Algorithm Explanation:
1. Independent Variable (X): total_cigs_avoided
2. Dependent Variable (y): money_saved
3. Model: y = mx + b
   - m (slope/coefficient): $ saved per cigarette avoided
   - b (intercept): Base savings value

How it works:
1. Fit: Find best-fit line minimizing squared errors
2. Predict: Use line equation to estimate future savings
3. R² Score: Measures how well the model explains variance (0-1)

Example:
If coefficient = 0.15 and intercept = 50:
- 100 cigs avoided → $65 saved (0.15 * 100 + 50)
- 500 cigs avoided → $125 saved (0.15 * 500 + 50)

Limitations:
- Linear relationship assumption
- May not capture behavior changes over time
- Outliers can affect model accuracy
"""

import numpy as np
from sklearn.linear_model import LinearRegression

class SavingsPredictionModel:
    def __init__(self):
        """Initialize Linear Regression model."""
        self.model = LinearRegression()
        self.X_train = None
        self.y_train = None
        
    def fit(self, df):
        """
        Fit regression model to data.
        
        Args:
            df (pd.DataFrame): Data with columns: total_cigs_avoided, money_saved
        """
        self.X_train = df['total_cigs_avoided'].values.reshape(-1, 1)
        self.y_train = df['money_saved'].values
        self.model.fit(self.X_train, self.y_train)
        
    def predict(self, cigs_avoided):
        """
        Predict savings for given cigarettes avoided.
        
        Args:
            cigs_avoided (float or np.array): Cigarettes avoided
            
        Returns:
            float or np.array: Predicted savings amount
        """
        if isinstance(cigs_avoided, (int, float)):
            cigs_avoided = np.array([[cigs_avoided]])
        else:
            cigs_avoided = np.array(cigs_avoided).reshape(-1, 1)
            
        return self.model.predict(cigs_avoided)
    
    def get_metrics(self):
        """
        Get model performance metrics.
        
        Returns:
            dict: R² score, coefficient, intercept
        """
        r2_score = self.model.score(self.X_train, self.y_train)
        
        return {
            'r2_score': r2_score,
            'coefficient': self.model.coef_[0],  # $ per cig avoided
            'intercept': self.model.intercept_,
            'interpretation': f"Each cigarette avoided = ${self.model.coef_[0]:.2f} saved"
        }
    
    def get_prediction_range(self, max_value=2500, num_points=100):
        """
        Generate prediction range for visualization.
        
        Args:
            max_value (int): Maximum cigarettes to predict for
            num_points (int): Number of prediction points
            
        Returns:
            tuple: (X values, y predictions)
        """
        X_range = np.linspace(0, max_value, num_points).reshape(-1, 1)
        y_pred = self.model.predict(X_range)
        return X_range.flatten(), y_pred
