import tkinter as tk
from tkinter import messagebox
from database import create_connection, create_tables
from ui import setup_ui
from auth import register_user, login_user

def main():
    conn = create_connection()
    create_tables(conn)

    def register():
        username = username_entry.get()
        password = password_entry.get()
        if register_user(conn, username, password):
            messagebox.showinfo("Success", "Registration successful!")
        else:
            messagebox.showerror("Error", "Username already exists!")

    def login():
        username = username_entry.get()
        password = password_entry.get()
        if login_user(conn, username, password):
            root.destroy()
            app = tk.Tk()
            setup_ui(app)
            app.mainloop()
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    root = tk.Tk()
    root.title('NutriTrack Login')
    root.geometry('300x200')
    root.configure(bg='light blue')

    tk.Label(root, text="Username:", bg='light blue').pack(pady=10)
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password:", bg='light blue').pack(pady=10)
    password_entry = tk.Entry(root, show='*')
    password_entry.pack()

    tk.Button(root, text="Register", command=register).pack(pady=5)
    tk.Button(root, text="Login", command=login).pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
