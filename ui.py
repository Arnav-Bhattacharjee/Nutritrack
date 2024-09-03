import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def setup_ui(root):
    root.title('NutriTrack')
    root.geometry('800x600')
    root.configure(bg='light blue')

    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=1, fill='both')

    nutrition_tab = ttk.Frame(tab_control)
    weight_tab = ttk.Frame(tab_control)
    calendar_tab = ttk.Frame(tab_control)

    tab_control.add(nutrition_tab, text='Nutrition')
    tab_control.add(weight_tab, text='Weight')
    tab_control.add(calendar_tab, text='Calendar')

    # Nutrition Tab
    tk.Label(nutrition_tab, text="Daily Nutrition Log", bg='light blue').pack()
    tk.Label(nutrition_tab, text="Calories:", bg='light blue').pack()
    tk.Entry(nutrition_tab).pack()

    tk.Label(nutrition_tab, text="Protein (g):", bg='light blue').pack()
    tk.Entry(nutrition_tab).pack()

    tk.Label(nutrition_tab, text="Fat (g):", bg='light blue').pack()
    tk.Entry(nutrition_tab).pack()

    tk.Label(nutrition_tab, text="Carbs (g):", bg='light blue').pack()
    tk.Entry(nutrition_tab).pack()

    tk.Button(nutrition_tab, text="Save").pack()

    # Weight Tab
    tk.Label(weight_tab, text="Daily Weight Log", bg='light blue').pack()
    tk.Label(weight_tab, text="Weight (kg):", bg='light blue').pack()
    tk.Entry(weight_tab).pack()
    tk.Button(weight_tab, text="Save").pack()

    # Calendar Tab
    tk.Label(calendar_tab, text="Calendar View", bg='light blue').pack()
    calendar = Calendar(calendar_tab, selectmode='day', year=2024, month=9, day=1)
    calendar.pack(pady=20)

