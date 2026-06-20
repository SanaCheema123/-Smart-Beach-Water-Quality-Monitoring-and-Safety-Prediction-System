import streamlit as st

def metric_card(title, value, icon="🌊"):
    st.markdown(
        f'''
        <div class="metric-card">
            <div class="metric-icon">{icon}</div>
            <p>{title}</p>
            <h2>{value}</h2>
        </div>
        ''',
        unsafe_allow_html=True
    )

def section_card(title, text):
    st.markdown(
        f'''
        <div class="content-card">
            <h3>{title}</h3>
            <p>{text}</p>
        </div>
        ''',
        unsafe_allow_html=True
    )
