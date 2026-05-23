import streamlit as st
import pandas as pd
from datetime import datetime

from utils.file_handler import (
    initialize_excel,
    load_contacts,
    load_deleted_contacts,
    save_contacts,
    save_deleted_contacts
)

from utils.validators import validate_phone

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Phone Directory", page_icon="📱")

initialize_excel()

contacts_df = load_contacts()
deleted_df = load_deleted_contacts()

st.title("📱 Phone Directory Manager")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Contact", "Search Contact", "Delete Contact", "View Contacts", "Deleted History"]
)

# =========================
# ADD CONTACT
# =========================
if menu == "Add Contact":

    st.subheader("Add Contact")

    name = st.text_input("Name")
    phone = st.text_input("Phone")

    if st.button("Save"):

        name = name.strip()
        phone = phone.strip()

        if not name or not phone:
            st.warning("Enter all fields")

        elif not validate_phone(phone):
            st.error("Invalid phone number")

        elif name in contacts_df["Name"].values:
            st.error("Name already exists")

        elif phone in contacts_df["Phone"].astype(str).values:
            st.error("Phone already exists")

        else:
            new = pd.DataFrame({"Name": [name], "Phone": [phone]})
            contacts_df = pd.concat([contacts_df, new], ignore_index=True)
            save_contacts(contacts_df)
            st.success("Contact added")
            st.rerun()

# =========================
# SEARCH
# =========================
elif menu == "Search Contact":

    st.subheader("Search")

    query = st.text_input("Search by name or phone")

    if st.button("Search") and query:

        result = contacts_df[
            contacts_df["Name"].str.contains(query, case=False, na=False) |
            contacts_df["Phone"].astype(str).str.contains(query)
        ]

        st.dataframe(result if not result.empty else pd.DataFrame())

# =========================
# DELETE
# =========================
elif menu == "Delete Contact":

    st.subheader("Delete Contact")

    if not contacts_df.empty:

        name = st.selectbox("Select Contact", contacts_df["Name"])

        if st.button("Delete"):

            deleted = contacts_df[contacts_df["Name"] == name].copy()
            deleted["Deleted_on"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            contacts_df = contacts_df[contacts_df["Name"] != name]
            deleted_df = pd.concat([deleted_df, deleted], ignore_index=True)

            save_contacts(contacts_df)
            save_deleted_contacts(deleted_df)

            st.success("Deleted successfully")
            st.rerun()

    else:
        st.info("No contacts")

# =========================
# VIEW CONTACTS
# =========================
elif menu == "View Contacts":
    st.subheader("All Contacts")
    st.dataframe(contacts_df)

# =========================
# HISTORY
# =========================
elif menu == "Deleted History":
    st.subheader("Deleted Contacts")
    st.dataframe(deleted_df)