

# 👥 Customer Segment Profiles — Churn Prediction Project

## 1. Overview
Clustering analysis was performed using **K-Means (k=3)**, with additional comparisons to Hierarchical and DBSCAN methods. The final segmentation produced three distinct customer groups with clear behavioral differences. Each segment was analyzed for tenure, spending, and churn patterns, followed by predictive modeling and business recommendations.

---

## 2. Segment Profiles

### **Segment 1: Young Professionals**
- **Cluster Size:** ~33% of customers  
- **Average Tenure:** 31.8 months  
- **Monthly Charges:** \$126.9  
- **Total Charges:** \$1,870  
- **Model Performance:** Accuracy 94%, F1-score 0.77, ROC-AUC 0.85  
- **Characteristics:**  
  - Moderate tenure, relatively high monthly charges but low total charges.  
  - Likely newer customers with higher service usage.  
- **Business Insight:**  
  - Offer bundled digital-first services.  
  - Provide onboarding support and loyalty incentives to increase retention.  

---

### **Segment 2: Budget Conscious**
- **Cluster Size:** ~34% of customers  
- **Average Tenure:** 41.7 months  
- **Monthly Charges:** \$59.7  
- **Total Charges:** \$5,125  
- **Model Performance:** Accuracy 98%, F1-score 0.67, ROC-AUC 0.75  
- **Characteristics:**  
  - Long tenure, low monthly charges, steady total spend.  
  - Price-sensitive customers who value affordability.  
- **Business Insight:**  
  - Introduce flexible payment plans and targeted discounts.  
  - Focus on retention through cost-saving bundles.  

---

### **Segment 3: Premium Spenders**
- **Cluster Size:** ~33% of customers  
- **Average Tenure:** 36.0 months  
- **Monthly Charges:** \$156.5  
- **Total Charges:** \$5,762  
- **Model Performance:** Accuracy 98%, F1-score 0.93, ROC-AUC 0.99  
- **Characteristics:**  
  - Mid-tenure, high monthly charges, high total spend.  
  - Loyal, high-value customers with strong engagement.  
- **Business Insight:**  
  - Provide exclusive offers, VIP programs, and premium support.  
  - Focus on upselling and cross-selling additional services.  

---

## 3. Key Takeaways
- **Young Professionals** need engagement and loyalty programs to prevent early churn.  
- **Budget Conscious** customers respond best to affordability-driven strategies.  
- **Premium Spenders** are high-value customers who should be nurtured with exclusivity and premium experiences.  
