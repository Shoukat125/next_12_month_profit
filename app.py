import streamlit as st
import pickle
import numpy as np
import pandas as pd
import plotly.express as px
from ui import apply_custom_css, display_header, display_result_card, display_prediction_graphs

# Page Settings
st.set_page_config(page_title="AI Business Dashboard", layout="wide")
apply_custom_css()

# 1. Models Load karna
@st.cache_resource
def load_assets():
    with open('scaler_X.pkl', 'rb') as f: sx = pickle.load(f)
    with open('scaler_y.pkl', 'rb') as f: sy = pickle.load(f)
    with open('final_multi_model.pkl', 'rb') as f: rm = pickle.load(f)
    with open('sarima_model.pkl', 'rb') as f: sm = pickle.load(f)
    return sx, sy, rm, sm

scaler_X, scaler_y, reg_model, sarima_model = load_assets()

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=100)
st.sidebar.title("Dashboard Menu")
choice = st.sidebar.selectbox("Select Analysis Type", ["Calculate Profit & Revenue", "Future Forecast"])

# --- PAGE 1: Calculate Profit & Revenue---
if choice == "Calculate Profit & Revenue":
    display_header("AI Profit, Revenue & Forecast Predictor")
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            qty = st.number_input("Enter Sales Quantity", min_value=0.0, value=100.0)
        with col2:
            cost = st.number_input("Enter Total Cost (£)", min_value=0.0, value=500.0)
        
        if st.button("Calculate Predictions"):
            # Scaling & Prediction
            inp = scaler_X.transform([[qty, cost]])
            pred_scaled = reg_model.predict(inp)
            res = scaler_y.inverse_transform(pred_scaled)
            
            profit, revenue = res[0][0], res[0][1]
            
            # UI Components from ui.py
            display_result_card(profit, revenue)
            display_prediction_graphs(profit, revenue)

# --- PAGE 2: FUTURE FORECAST ---
elif choice == "Future Forecast":
    display_header("12-Month Profit Forecasting")
    
    if st.button("Run SARIMA Model"):
        forecast = sarima_model.get_forecast(steps=12)
        df = forecast.summary_frame()
        
        # Plotly based Forecast Graph
        fig = px.line(df, x=df.index, y='mean', title="Projected Monthly Profit (2006)",
                     labels={'mean': 'Profit (£)', 'index': 'Date'})
        fig.add_scatter(x=df.index, y=df['mean_ci_upper'], fill=None, mode='lines', line_color='rgba(255,0,0,0)', showlegend=False)
        fig.add_scatter(x=df.index, y=df['mean_ci_lower'], fill='tonexty', mode='lines', line_color='rgba(255,0,0,0)', fillcolor='rgba(255,0,0,0.1)', name='Confidence Interval')
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Total Stats
        total_p = df['mean'].sum()
        st.markdown(f"""
            <div style="background-color:#022b8b; padding:20px; border-radius:15px; text-align:center;">
                <h2 style="color:white;">Grand Total Expected Profit: £{total_p:,.2f}</h2>
            </div>
        """, unsafe_allow_html=True)