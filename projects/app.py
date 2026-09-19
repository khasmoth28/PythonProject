from datetime import datetime
import os
import pandas as pd
import streamlit as st

FILENAME = "restock_log.csv"


def initialize_file():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILENAME):
        df = pd.DataFrame(columns=["Date/Time", "Item Name", "Quantity", "Supplier", "Notes"])
        df.to_csv(FILENAME, index=False)


st.set_page_config(page_title="Supply Restocking Form", page_icon="📦", layout="centered")

st.title("📦 Supply Restocking Form")
st.write("Fill out the details below to log new inventory items.")

initialize_file()

# Streamlit Form Container
with st.form("restock_form", clear_on_submit=True):
    item_name = st.text_input("Item Name *")
    quantity = st.number_input("Quantity to Restock *", min_value=1, step=1, value=1)
    supplier = st.text_input("Supplier Name *")
    notes = st.text_area("Notes (Optional)")

    submitted = st.form_submit_button("Submit Restock")

    if submitted:
        if not item_name.strip() or not supplier.strip():
            st.error("Please fill out all required fields (Item Name and Supplier Name).")
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_entry = pd.DataFrame([[timestamp, item_name, quantity, supplier, notes]],
                                     columns=["Date/Time", "Item Name", "Quantity", "Supplier", "Notes"])

            new_entry.to_csv(FILENAME, mode="a", header=False, index=False)
            st.success(f"Successfully logged {quantity}x '{item_name}' from {supplier}!")