"""
Student Management System
GUI-based application for managing student records.
Modules: tkinter, pandas, numpy, time
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd
import numpy as np
import time
import os

DATA_FILE = "students.csv"
ADMIN_USER = "admin"
ADMIN_PASS = "password"

# Initialize data file if not exists
def init_data_file():
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["Roll", "Name", "Address", "DOB"])
        df.to_csv(DATA_FILE, index=False)

# Login Window
def login_window():
    login = tk.Tk()
    login.title("Admin Login")
    login.geometry("300x150")

    tk.Label(login, text="Username:").pack()
    username_entry = tk.Entry(login)
    username_entry.pack()
    tk.Label(login, text="Password:").pack()
    password_entry = tk.Entry(login, show="*")
    password_entry.pack()

    def check_login():
        user = username_entry.get()
        pwd = password_entry.get()
        if user == ADMIN_USER and pwd == ADMIN_PASS:
            login.destroy()
            main_window()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!")

    tk.Button(login, text="Login", command=check_login).pack(pady=10)
    login.mainloop()

# Main Window
def main_window():
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("400x400")

    def add_student():
        df = pd.read_csv(DATA_FILE)
        name = simpledialog.askstring("Add Student", "Enter Name:")
        address = simpledialog.askstring("Add Student", "Enter Address:")
        dob = simpledialog.askstring("Add Student", "Enter DOB (YYYY-MM-DD):")
        roll = int(df["Roll"].max()) + 1 if not df.empty else 1
        df = df.append({"Roll": roll, "Name": name, "Address": address, "DOB": dob}, ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        messagebox.showinfo("Success", f"Student added with Roll No: {roll}")

    def update_student():
        df = pd.read_csv(DATA_FILE)
        roll = simpledialog.askinteger("Update Student", "Enter Roll No:")
        if roll in df["Roll"].values:
            idx = df.index[df["Roll"] == roll][0]
            name = simpledialog.askstring("Update Student", "Enter New Name:")
            address = simpledialog.askstring("Update Student", "Enter New Address:")
            dob = simpledialog.askstring("Update Student", "Enter New DOB (YYYY-MM-DD):")
            df.at[idx, "Name"] = name
            df.at[idx, "Address"] = address
            df.at[idx, "DOB"] = dob
            df.to_csv(DATA_FILE, index=False)
            messagebox.showinfo("Success", "Student info updated!")
        else:
            messagebox.showerror("Error", "Roll No not found!")

    def delete_student():
        df = pd.read_csv(DATA_FILE)
        roll = simpledialog.askinteger("Delete Student", "Enter Roll No:")
        if roll in df["Roll"].values:
            df = df[df["Roll"] != roll]
            df.to_csv(DATA_FILE, index=False)
            messagebox.showinfo("Success", "Student deleted!")
        else:
            messagebox.showerror("Error", "Roll No not found!")

    def search_student():
        df = pd.read_csv(DATA_FILE)
        search_by = simpledialog.askstring("Search Student", "Search by 'roll' or 'name':")
        if search_by == "roll":
            roll = simpledialog.askinteger("Search Student", "Enter Roll No:")
            result = df[df["Roll"] == roll]
        elif search_by == "name":
            name = simpledialog.askstring("Search Student", "Enter Name:")
            result = df[df["Name"].str.lower() == name.lower()]
        else:
            messagebox.showerror("Error", "Invalid search type!")
            return
        if not result.empty:
            info = result.to_string(index=False)
            messagebox.showinfo("Student Found", info)
        else:
            messagebox.showinfo("Not Found", "No student found!")

    tk.Button(root, text="Add Student", command=add_student, width=25).pack(pady=10)
    tk.Button(root, text="Update Student", command=update_student, width=25).pack(pady=10)
    tk.Button(root, text="Delete Student", command=delete_student, width=25).pack(pady=10)
    tk.Button(root, text="Search Student", command=search_student, width=25).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy, width=25).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    init_data_file()
    login_window()
