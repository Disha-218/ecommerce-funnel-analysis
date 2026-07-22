import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.title("🛒 Live E-Commerce Funnel Analysis")
st.write("An interactive analytics dashboard examining conversion rates and drop-offs.")

# Generate/Load Data
np.random.seed(42)
n_sessions = 10000

df = pd.DataFrame({
    'session_id': [f"SESS_{i:05d}" for i in range(1, n_sessions + 1)],
    'device': np.random.choice(['Desktop', 'Mobile', 'Tablet'], size=n_sessions, p=[0.5, 0.4, 0.1]),
    'viewed_product': np.random.choice([1, 0], size=n_sessions, p=[0.85, 0.15]),
})
df['added_to_cart'] = df['viewed_product'] * np.random.choice([1, 0], size=n_sessions, p=[0.50, 0.50])
df['reached_checkout'] = df['added_to_cart'] * np.random.choice([1, 0], size=n_sessions, p=[0.55, 0.45])
df['completed_purchase'] = df['reached_checkout'] * np.random.choice([1, 0], size=n_sessions, p=[0.80, 0.20])

# Funnel Calculation
funnel_data = pd.DataFrame({
    'Stage': ['1. Sessions', '2. View Product', '3. Add to Cart', '4. Checkout', '5. Purchase'],
    'Users': [len(df), df['viewed_product'].sum(), df['added_to_cart'].sum(), df['reached_checkout'].sum(), df['completed_purchase'].sum()]
})

# Interactive Chart
fig = go.Figure(go.Funnel(
    y=funnel_data['Stage'],
    x=funnel_data['Users'],
    textinfo="value+percent initial+percent previous"
))
st.plotly_chart(fig)