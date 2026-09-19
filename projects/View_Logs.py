import os
import pandas as pd
import streamlit as st

FILENAME = "../restock_log.csv"  # Goes up one folder to find the CSV log

st.set_page_config(page_title="Restock History Logs", page_icon="📋", layout="wide")

st.title("📋 Restock History Logs")
st.write("Here is the complete record of all submitted supply restocks.")

if os.path.exists(FILENAME):
    df_log = pd.read_csv(FILENAME)
    if not df_log.empty:
        # Display search filter or metrics if desired
        st.dataframe(df_log, use_container_width=True)
        
        # Optional: Add a download button for the CSV log
        csv_data = df_log.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Logs as CSV",
            data=csv_data,
            file_name="restock_log_export.csv",
            mime="text/csv",
        )
    else:
        st.info("The log file is currently empty.")
else:
    st.warning("No restock log file found yet. Submit an item from the main form first!")