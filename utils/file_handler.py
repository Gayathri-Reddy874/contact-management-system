import pandas as pd
from pathlib import Path

DATA_PATH = Path("data")
DATA_PATH.mkdir(exist_ok=True)

FILE = DATA_PATH / "phone_directory.xlsx"


def initialize_excel():
    if not FILE.exists():
        with pd.ExcelWriter(FILE, engine="openpyxl") as writer:
            pd.DataFrame(columns=["Name", "Phone"]).to_excel(writer, sheet_name="contacts", index=False)
            pd.DataFrame(columns=["Name", "Phone", "Deleted_on"]).to_excel(writer, sheet_name="deleted", index=False)


def load_contacts():
    try:
        return pd.read_excel(FILE, sheet_name="contacts")
    except:
        return pd.DataFrame(columns=["Name", "Phone"])


def load_deleted_contacts():
    try:
        return pd.read_excel(FILE, sheet_name="deleted")
    except:
        return pd.DataFrame(columns=["Name", "Phone", "Deleted_on"])


def save_contacts(df):
    with pd.ExcelWriter(FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name="contacts", index=False)


def save_deleted_contacts(df):
    with pd.ExcelWriter(FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name="deleted", index=False)