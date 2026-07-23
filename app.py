import streamlit as st
import numpy as np
import joblib
import pandas as pd
import plotly.express as px

model = joblib.load('customer_pulse_churn_model.pkl')
rfm = pd.read_csv('rfm_dashboard.csv')

st.set_page_config(page_title="CustomerPulse", layout="wide")
st.markdown("""
    <style>
    .stApp {
        background-color: #FAFAFA;
    }
    .stMetric {
        background-color: #F5F0DC;
        padding: 10px;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #C9A84C;
        color: white;
        border-radius: 8px;
        width: 100%;
        padding: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 16px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)
st.title("CustomerPulse — Churn Predictor")
st.write("Your Customer Retention Intelligence Partner")

tab1, tab2 = st.tabs(["Churn Predictor", "Dashboard"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Enter Customer RFM Scores")
        r_score = st.slider("Recency Score (1=Long ago, 4=Recent)", 1, 4, 2)
        f_score = st.slider("Frequency Score (1=Rare, 4=Frequent)", 1, 4, 2)
        m_score = st.slider("Monetary Score (1=Low spend, 4=High spend)", 1, 4, 2)
        predict_btn = st.button("Predict Churn Risk")
    
    with col2:
        st.subheader("Prediction Result")
        if predict_btn:
            input_data = np.array([[r_score, f_score, m_score]])
            prediction = model.predict(input_data)
            probability = model.predict_proba(input_data)[0][1]
            rfm_score = r_score + f_score + m_score
            
            if rfm_score >= 10:
                segment = "Champions"
            elif rfm_score >= 7:
                segment = "Loyal"
            elif rfm_score >= 5:
                segment = "At Risk"
            else:
                segment = "Lost"
            
            st.metric("Churn Probability", f"{probability*100:.1f}%")
            st.metric("Customer Segment", segment)
            
            if prediction[0] == 1:
                st.warning("⚠️ High Risk of Churn")
                st.write("**Recommended Action:** Send a personalized retention offer — discount voucher or loyalty reward.")
            else:
                st.success("✅ Low Risk of Churn")
                st.write("**Recommended Action:** Send new product updates and engagement reminders.")
with tab2:
    st.subheader("Customer Retention Dashboard")
    
    # KPI row
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Customers", len(rfm))
    col2.metric("Churned Customers", rfm['Churned'].sum())
    col3.metric("Churn Rate", f"{rfm['Churned'].mean()*100:.1f}%")
    col4.metric("Total Revenue", f"£{rfm['Monetary'].sum():,.0f}")
    
    st.divider()
    
    # Charts row
    col1, col2 = st.columns(2)
    
    with col1:
        # Segment distribution pie chart
        seg_counts = rfm['Segment'].value_counts().reset_index()
        seg_counts.columns = ['Segment', 'Count']
        fig1 = px.pie(seg_counts, values='Count', names='Segment',
                      title='Customer Distribution by Segment',
                      color_discrete_sequence=['#2E86AB','#C9A84C','#E84855','#3BB273'])
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Churn rate by segment
        churn_seg = rfm.groupby('Segment')['Churned'].mean()*100
        churn_seg = churn_seg.reset_index()
        churn_seg.columns = ['Segment', 'Churn Rate']
        fig2 = px.bar(churn_seg, x='Churn Rate', y='Segment',
                      title='Churn Rate by Segment',
                      orientation='h',
                      color='Churn Rate',
                      color_continuous_scale='RdYlGn_r')
        st.plotly_chart(fig2, use_container_width=True)
    
    st.divider()
    
    # RFM Table
    st.subheader("Customer RFM Summary")
    st.dataframe(rfm[['Recency','Frequency','Monetary','Segment','Churned']].head(50))      