import streamlit as st

def sidebar_header():
    st.sidebar.markdown(
        '''
        <div class="sidebar-brand">
            <div class="brand-icon">🌊</div>
            <h2>OceanAI</h2>
            <p>Coastal Intelligence Center</p>
        </div>
        ''',
        unsafe_allow_html=True
    )
