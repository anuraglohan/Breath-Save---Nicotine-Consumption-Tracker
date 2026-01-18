"""
K-MEANS CLUSTERING MODEL
========================

Purpose: Segment users into 3 distinct groups based on their behavior

Algorithm Explanation:
1. Features Used: total_cigs_avoided, money_saved, total_cigs_smoked
2. Preprocessing: StandardScaler normalizes features to zero mean and unit variance
3. K-Means: Groups users into 3 clusters based on similarity
4. Distance: Uses Euclidean distance in scaled feature space

Cluster Interpretation:
- Cluster 0 (Red): High Achievers - Maximum savings and cigs avoided
- Cluster 1 (Blue): Steady Performers - Moderate progress, consistent efforts
- Cluster 2 (Green): New Members - Early stage users with growing momentum

Mathematical Formula:
    J = Σ Σ ||x_i - c_j||^2
    where x_i = data point, c_j = cluster center
"""

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

class UserSegmentationModel:
    def __init__(self, n_clusters=3, random_state=42):
        """
        Initialize K-Means clustering model.
        
        Args:
            n_clusters (int): Number of segments (default: 3)
            random_state (int): For reproducible results
        """
        self.n_clusters = n_clusters
        self.scaler = StandardScaler()
        self.model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
        self.cluster_names = ['High Achievers', 'Steady Performers', 'New Members']
        
    def fit_predict(self, df):
        """
        Fit model and predict clusters.
        
        Args:
            df (pd.DataFrame): Data with columns: total_cigs_avoided, money_saved, total_cigs_smoked
            
        Returns:
            np.array: Cluster assignments for each user
        """
        features = ['total_cigs_avoided', 'money_saved', 'total_cigs_smoked']
        X = df[features].values
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        # Fit and predict
        clusters = self.model.fit_predict(X_scaled)
        
        return clusters
    
    def get_cluster_stats(self, df, clusters):
        """
        Calculate statistics for each cluster.
        
        Args:
            df (pd.DataFrame): Original data
            clusters (np.array): Cluster assignments
            
        Returns:
            dict: Statistics for each cluster
        """
        df_copy = df.copy()
        df_copy['cluster'] = clusters
        
        stats = {}
        for cluster_id in range(self.n_clusters):
            cluster_data = df_copy[df_copy['cluster'] == cluster_id]
            stats[self.cluster_names[cluster_id]] = {
                'users': len(cluster_data),
                'avg_savings': cluster_data['money_saved'].mean(),
                'avg_cigs_avoided': cluster_data['total_cigs_avoided'].mean(),
                'avg_cigs_smoked': cluster_data['total_cigs_smoked'].mean()
            }
        
        return stats
