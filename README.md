Hotel/Restaurant Billing System (Tkinter + Python)
📌 Overview

This project is a Hotel/Restaurant Billing System built with Python (Tkinter) for the front-end and ReportLab for PDF bill generation.
It allows restaurants to manage orders, calculate bills with GST, and generate printable invoices.

The project is designed in a dark theme UI for better user experience.
Currently, the menu includes 10 food items, but it can be easily extended.

🚀 Features

🖥️ Dark theme GUI using Tkinter.

🍔 Food menu with 10 items (easily customizable).

📝 Take customer orders with multi-item selection.

💰 Auto-calculates bill + GST (5%).

📄 Save/Print bill as PDF using ReportLab.

🔄 Reset/clear orders instantly.

⚡ Lightweight and beginner-friendly.

🛠️ Tech Stack

Python 3.x

Tkinter (Front-end GUI)

ReportLab (for PDF invoice generation)

(Optional) MySQL/SQLite (for advanced version with database support)

📂 Project Structure
Hotel-Billing-System/
│-- billing_system.py    # Main Tkinter application
│-- invoices/            # Folder where generated PDF bills are saved
│-- README.md            # Project documentation
│-- requirements.txt     # Dependencies



🔧 Installation & Setup

Clone the repository:

git clone https://github.com/your-username/hotel-billing-system.git
cd hotel-billing-system


Install dependencies:

pip install reportlab


Run the project:

python billing_system.py

📑 Future Enhancements

✅ Add Database support (MySQL/SQLite) for storing orders & sales history.

✅ Add Admin Panel to manage menu & prices dynamically.

✅ Daily/Monthly sales report generation.

✅ Multi-user login (Admin/Waiter/Cashier).
