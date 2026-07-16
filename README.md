# 🧾 Electro Billing Software

A desktop-based **Billing Management System** built using **Python, Tkinter, and MySQL**. The application allows users to generate electronic product bills, calculate taxes automatically, store customer records, and search previously generated invoices through a simple graphical interface.

---

## 📌 Overview

Electro Billing Software is designed to simplify billing operations for an electronics store. It provides an easy-to-use interface for entering customer details, selecting products, calculating taxes, generating invoices, and maintaining billing records.

This project demonstrates GUI development, database integration, file handling, and object-oriented programming in Python.

---

## ✨ Features

- 👤 Customer Information Management
- 💻 Laptop Billing
- 📱 Mobile Phone Billing
- 📺 LED TV Billing
- 🧮 Automatic Price Calculation
- 💰 Automatic Tax Calculation
- 🧾 Bill Generation
- 💾 Save Bills as Text Files
- 🗂 Store Customer Data in MySQL Database
- 🔍 Search Bills by
  - Bill Number
  - Customer Name
  - Phone Number
- 📋 View All Saved Bills
- 🧹 Clear Form
- 🚪 Exit Application

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Tkinter | Graphical User Interface |
| MySQL | Database |
| MySQL Connector | Database Connectivity |
| File Handling | Store Generated Bills |
| OOP | Application Structure |

---

## 📂 Project Structure

```
Billing-Software/
│
├── main.py
├── bills/
├── README.md

```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/student-kosha/Billing-software.git
```

### 2. Open the project

```bash
cd Billing-software
```

### 3. Install dependencies

```bash
pip install mysql-connector-python
```

### 4. Configure MySQL

Create a database:

```sql
CREATE DATABASE data_storage;
```

Create the required tables:

- customer
- Laptop
- Phones
- LEDs

Update the database credentials inside the project if required.

### 5. Run the application

```bash
python main.py
```

---

## 🖥 Application Workflow

1. Enter customer details.
2. Select product quantities.
3. Click **Total** to calculate prices and taxes.
4. Click **Generate Bill**.
5. Save the bill.
6. Search previously saved bills anytime.

---

## 📸 Screenshots

### Home Screen

> [BILLING SOFTWARE](image.png)

```
screenshots/home.png
```

### Generated Bill

> [Bill]({E0042D36-5935-40FA-98CA-59B4BF9122B7}.png)

```
screenshots/bill.png
```

---

## 💡 Concepts Used

- Object-Oriented Programming
- GUI Development
- Event Handling
- MySQL Database Connectivity
- File Handling
- Exception Handling
- Data Validation
- Random Bill Number Generation

---

## 🚀 Future Improvements

- PDF Invoice Generation
- Barcode / QR Code Support
- Product Inventory Management
- User Login System
- Admin Dashboard
- Sales Analytics
- GST Invoice Export
- Email Bill to Customer
- Receipt Printing
- SQLite Support
- Modern UI using CustomTkinter

---

## 🎯 Learning Outcomes

Through this project I learned:

- Building desktop applications using Tkinter
- Designing user-friendly graphical interfaces
- Connecting Python with MySQL
- Managing customer and billing records
- Working with file handling
- Applying Object-Oriented Programming concepts
- Error handling and validation techniques

---

## 👨‍💻 Author

**Kosha Bante**

BCA Graduate • Python Developer

GitHub: https://github.com/student-kosha

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.
