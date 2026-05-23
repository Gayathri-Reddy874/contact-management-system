# 📱 Phone Directory Manager

A simple and efficient Phone Directory Management System built using **Python**, **Streamlit**, and **Pandas**.
This application allows users to add, search, view, and delete contacts with persistent Excel-based storage.

---

## 🚀 Features

* ➕ Add New Contacts
* 🔍 Search Contacts by Name or Phone Number
* 🗑️ Delete Contacts
* 📋 View All Saved Contacts
* 🕒 Deleted Contacts History
* ✅ Phone Number Validation
* 💾 Excel-Based Data Storage
* ⚡ Interactive Streamlit UI

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit ⚡
* Pandas 📊
* OpenPyXL 📁

---

## 📂 Project Structure

```bash
phone-directory-app/
│
├── app.py                     # Main Streamlit application
├── requirements.txt           # Project dependencies
├── README.md                  # Documentation
│
├── utils/
│   ├── file_handler.py        # Excel read/write operations
│   └── validators.py          # Input validation functions
│
└── data/
    └── phone_directory.xlsx   # Auto-created Excel database
```
## 🌐 Live Demo

🚀 Try the application here:  
[Phone Directory Manager](https://contact-management-system-sdjvkjbrvkbeveug7zd4cl.streamlit.app/)

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Gayathri-Reddy874/contact-management-system.git
cd contact-management-system
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Application Modules

### ➕ Add Contact

Add new contacts with validation and duplicate checking.

### 🔍 Search Contact

Search contacts using name or phone number.

### 🗑️ Delete Contact

Delete contacts and maintain deleted history.

### 📋 View Contacts

Display all saved contacts in tabular format.

### 🕒 Deleted History

Track deleted contacts with timestamps.

---

## 📦 Requirements

```txt
streamlit
pandas
openpyxl
```

---

## 🎯 Future Enhancements

* ✏️ Update/Edit Contact Feature
* 📤 Export Contacts to CSV/PDF
* 🔐 User Authentication
* ☁️ Cloud Database Integration
* 📱 Mobile Responsive UI

---

## 👨‍💻 Author

**Mallareddygari Gayathri**

Aspiring AI/ML Engineer & Data Science Enthusiast

---

## 📄 License

This project is developed for educational and learning purposes.
