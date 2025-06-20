import plotly.graph_objects as go
import streamlit as st

def show_skill_radar(matched, missing):
    labels = matched + missing
    values = [1]*len(matched) + [0]*len(missing)
    fig = go.Figure(data=go.Scatterpolar(r=values, theta=labels, fill='toself'))
    st.plotly_chart(fig, use_container_width=True)