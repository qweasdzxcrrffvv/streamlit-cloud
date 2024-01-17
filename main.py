import streamlit as st
# ==============================================================================
query_dict = st.experimental_get_query_params()
aid = query_dict['aid'][0]
if aid == 'drug_dosage':
    st.switch_page(f"pages/{aid}.py")
