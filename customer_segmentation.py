# 📌 Customer Segmentation & Prediction Pipeline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# -------------------------------
# Step 1: Load Data
# -------------------------------
df = pd.read_csv("customer_churn.csv")
print("Data Shape:", df.shape)
print(df.head())

# -------------------------------
# Step 2: Encode Categorical Features
# -------------------------------
binary_cols = ['PaperlessBilling','Churn']
multi_cols = ['Contract','PaymentMethod']

# Label Encoding for binary
for col in binary_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# One-Hot Encoding for multi-class
df = pd.get_dummies(df, columns=multi_cols, drop_first=True)

# -------------------------------
# Step 3: Scale Numerical Features
# -------------------------------
num_cols = ['Tenure','MonthlyCharges','TotalCharges']
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[num_cols])

# -------------------------------
# Step 4: K-Means Clustering (Elbow Method)
# -------------------------------
inertia = []
for k in range(2, 10):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(scaled_data)
    inertia.append(km.inertia_)

plt.plot(range(2, 10), inertia, marker='o')
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of clusters")
plt.ylabel("Inertia")
plt.show()

# Fit KMeans with chosen K (example: 3)
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster_KMeans'] = kmeans.fit_predict(scaled_data)

# -------------------------------
# Step 5: Advanced Clustering
# -------------------------------
hier = AgglomerativeClustering(n_clusters=3)
df['Cluster_Hier'] = hier.fit_predict(scaled_data)

dbscan = DBSCAN(eps=1.5, min_samples=5)
df['Cluster_DBSCAN'] = dbscan.fit_predict(scaled_data)

# -------------------------------
# Step 6: Segment Analysis
# -------------------------------
segment_profiles = df.groupby('Cluster_KMeans')[num_cols].mean()
print("Segment Profiles:\n", segment_profiles)

segment_names = {
    0: "Premium Spenders",
    1: "Budget Conscious",
    2: "Young Professionals"
}
df['Segment_Name'] = df['Cluster_KMeans'].map(segment_names)

# -------------------------------
# Step 7: Prediction Models per Segment
# -------------------------------
results = []

for seg in df['Cluster_KMeans'].unique():
    seg_data = df[df['Cluster_KMeans'] == seg]
    
    X = seg_data.drop(columns=['CustomerID','Churn','Segment_Name','Cluster_KMeans','Cluster_Hier','Cluster_DBSCAN'])
    y = seg_data['Churn']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc = roc_auc_score(y_test, y_pred)
    
    results.append([segment_names[seg], acc, prec, rec, f1, roc])

results_df = pd.DataFrame(results, columns=["Segment","Accuracy","Precision","Recall","F1","ROC-AUC"])
results_df.to_csv("model_evaluation_results.csv", index=False)
print(results_df)

# -------------------------------
# Step 8: Hyperparameter Tuning
# -------------------------------
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [5, 10, None],
    'min_samples_split': [2, 5]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring='f1')
grid_search.fit(X_train, y_train)

print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)
