import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas
import datetime

# ---------------------------
# Restaurant Billing System
# ---------------------------

# Food Menu (10 items with price)
menu_items = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
    "Sandwich": 100,
    "French Fries": 80,
    "Momos": 90,
    "Cold Coffee": 70,
    "Tea": 20,
    "Paneer Tikka": 200,
    "Ice Cream": 60
}

# Dictionary to store user selected quantities
order_quantities = {}


# Function to calculate bill
def generate_bill():
    total = 0
    bill_details = "------ BILL RECEIPT ------\n"
    bill_details += f"Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}\n\n"

    for item, price in menu_items.items():
        qty = order_quantities[item].get()
        if qty > 0:  # Only add if quantity > 0
            subtotal = qty * price
            bill_details += f"{item} x {qty} = Rs {subtotal}\n"
            total += subtotal

    gst = round(total * 0.05, 2)  # 5% GST
    grand_total = total + gst

    bill_details += "\n-------------------------\n"
    bill_details += f"Total: Rs {total}\n"
    bill_details += f"GST (5%): Rs {gst}\n"
    bill_details += f"Grand Total: Rs {grand_total}\n"
    bill_details += "-------------------------\n"

    # Show in messagebox
    messagebox.showinfo("Bill Generated", bill_details)

    # Save bill as PDF
    save_bill_pdf(bill_details)


# Function to save bill as PDF
def save_bill_pdf(text):
    file_name = f"Bill_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(file_name)
    c.drawString(100, 800, "Restaurant Bill")

    # Print bill line by line
    y = 760
    for line in text.split("\n"):
        c.drawString(100, y, line)
        y -= 20
    c.save()
    messagebox.showinfo("PDF Saved", f"Bill saved as {file_name}")


# ---------------------------
# Tkinter GUI
# ---------------------------
root = tk.Tk()
root.title("Restaurant Billing System")
root.geometry("600x600")
root.config(bg="#222")  # Dark theme background

# Heading
heading = tk.Label(root, text="Restaurant Billing System", font=("Arial", 20, "bold"), fg="white", bg="#222")
heading.pack(pady=10)

# Frame for menu
menu_frame = tk.Frame(root, bg="#333")
menu_frame.pack(pady=20)

# Create labels and spinboxes for each item
for item, price in menu_items.items():
    frame = tk.Frame(menu_frame, bg="#333")
    frame.pack(fill="x", pady=5)

    lbl = tk.Label(frame, text=f"{item} - Rs {price}", font=("Arial", 12), fg="white", bg="#333", anchor="w")
    lbl.pack(side="left", padx=20)

    qty_var = tk.IntVar(value=0)
    spin = tk.Spinbox(frame, from_=0, to=10, textvariable=qty_var, width=5)
    spin.pack(side="right", padx=20)

    order_quantities[item] = qty_var

# Button to generate bill
btn = tk.Button(root, text="Generate Bill", command=generate_bill, font=("Arial", 14), bg="#444", fg="white")
btn.pack(pady=20)

root.mainloop()
