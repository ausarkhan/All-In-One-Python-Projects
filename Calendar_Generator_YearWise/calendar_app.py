"""
Calendar Generator YearWise
Issue #106 for king04aman/All-In-One-Python-Projects
"""
import tkinter as tk
from tkinter import messagebox
import calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Yearly Calendar Generator")
        self.root.geometry("350x150")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        tk.Label(root, text="Enter Year:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
        self.year_entry = tk.Entry(root, font=("Arial", 12), width=15)
        self.year_entry.pack(pady=5)

        tk.Button(root, text="Show Calendar", command=self.show_calendar, font=("Arial", 12), bg="#4caf50", fg="white").pack(pady=10)
        tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="#f44336", fg="white").pack()

    def show_calendar(self):
        year = self.year_entry.get()
        if not year.isdigit() or int(year) < 1:
            messagebox.showerror("Invalid Input", "Please enter a valid positive year.")
            return
        year = int(year)
        cal = calendar.TextCalendar(calendar.SUNDAY)
        cal_str = cal.formatyear(year, 2, 1, 1, 3)
        self.display_calendar(year, cal_str)

    def display_calendar(self, year, cal_str):
        cal_win = tk.Toplevel(self.root)
        cal_win.title(f"Calendar for {year}")
        cal_win.geometry("600x600")
        cal_win.configure(bg="#e3f2fd")
        text = tk.Text(cal_win, font=("Consolas", 10), bg="#e3f2fd", fg="#212121")
        text.insert(tk.END, cal_str)
        text.pack(expand=True, fill=tk.BOTH)
        tk.Button(cal_win, text="Close", command=cal_win.destroy, font=("Arial", 12), bg="#1976d2", fg="white").pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
