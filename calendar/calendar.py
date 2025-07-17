import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from tkcalendar import Calendar
from datetime import date
import json
import os

EVENTS_FILE = "calendar_events.json"


def get_selected_date():
    selected = cal.selection_get()
    if isinstance(selected, tuple):  # Range selection
        selected_date_label.config(
            text=f"Selected Range: {selected[0]} to {selected[-1]}"
        )
    else:
        selected_date_label.config(text=f"Selected Date: {selected}")


def set_today():
    today = date.today()
    cal.selection_set(today)


def clear_selection():
    cal.selection_clear()
    selected_date_label.config(text="Selected Date:")


def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()


def apply_theme():
    if dark_mode:
        root.config(bg="#333333")
        frame.config(style="DarkFrame.TFrame")
        cal.configure(
            background="#333333",
            foreground="#ffffff",
            selectbackground="#ffff00",
            selectforeground="#000000",
            headersbackground="#333333",
            headersforeground="#ffffff",
        )
        select_date_button.config(style="DarkButton.TButton")
        today_button.config(style="DarkButton.TButton")
        clear_button.config(style="DarkButton.TButton")
        event_button.config(style="DarkButton.TButton")
        view_events_button.config(style="DarkButton.TButton")
        selected_date_label.config(foreground="red")
    else:
        root.config(bg="#f2f2f2")
        frame.config(style="LightFrame.TFrame")
        cal.configure(
            background="#ffffff",
            foreground="#333333",
            selectbackground="#ffff00",
            selectforeground="#000000",
            headersbackground="#f2f2f2",
            headersforeground="#333333",
        )
        select_date_button.config(style="TButton")
        today_button.config(style="TButton")
        clear_button.config(style="TButton")
        event_button.config(style="TButton")
        view_events_button.config(style="TButton")
        selected_date_label.config(foreground="#0080ff")


def add_event():
    selected = cal.selection_get()
    if not selected:
        messagebox.showinfo("No Date Selected", "Please select a date or range first.")
        return
    if isinstance(selected, tuple):
        dates = [str(d) for d in selected]
    else:
        dates = [str(selected)]
    event_text = simpledialog.askstring("Add Event", "Enter event details:")
    if event_text:
        for d in dates:
            events.setdefault(d, []).append(event_text)
        save_events()
        messagebox.showinfo("Event Added", f"Event added for {', '.join(dates)}.")


def view_events():
    selected = cal.selection_get()
    if not selected:
        messagebox.showinfo("No Date Selected", "Please select a date or range first.")
        return
    if isinstance(selected, tuple):
        dates = [str(d) for d in selected]
    else:
        dates = [str(selected)]
    msg = ""
    for d in dates:
        if d in events:
            msg += f"{d}:\n"
            for idx, ev in enumerate(events[d], 1):
                msg += f"  {idx}. {ev}\n"
    if not msg:
        msg = "No events for selected date(s)."
    messagebox.showinfo("Events", msg)


def save_events():
    with open(EVENTS_FILE, "w") as f:
        json.dump(events, f)


def load_events():
    if os.path.exists(EVENTS_FILE):
        with open(EVENTS_FILE, "r") as f:
            return json.load(f)
    return {}


# Create the main window
root = tk.Tk()
root.title("Calendar")
root.geometry("520x480")

# Create a frame for the calendar and buttons
frame = ttk.Frame(root, padding=20)
frame.pack()

# Set the initial theme to dark
dark_mode = True

# Create a Calendar widget with range selection
cal = Calendar(
    frame,
    selectmode="day",  # Change to "day" or "range" for range selection
    date_pattern="yyyy-mm-dd",
    background="#333333",
    foreground="#ffffff",
    selectbackground="#ffff00",
    selectforeground="#000000",
    headersbackground="#333333",
    headersforeground="#ffffff",
    font=("Arial", 12),
    cursor="hand2",
)
cal.grid(row=0, column=0, columnspan=3, pady=10)

# Create a button to get the selected date
select_date_button = ttk.Button(
    frame, text="Get Selected Date", command=get_selected_date, cursor="hand2"
)
select_date_button.grid(row=1, column=0, pady=10)

# Create a label to display the selected date
selected_date_label = ttk.Label(
    frame, text="Selected Date: ", font=("Arial", 12, "bold"), foreground="white"
)
selected_date_label.grid(row=1, column=1, pady=10)

# Create a button to set today's date
today_button = ttk.Button(frame, text="Set Today", command=set_today, cursor="hand2")
today_button.grid(row=2, column=0, pady=10)

# Create a button to clear the selected date
clear_button = ttk.Button(
    frame,
    text="Clear Date",
    command=clear_selection,
    cursor="hand2",
)
clear_button.grid(row=2, column=1, pady=10)

# Add event button
event_button = ttk.Button(
    frame, text="Add Event", command=add_event, cursor="hand2"
)
event_button.grid(row=3, column=0, pady=10)

# View events button
view_events_button = ttk.Button(
    frame, text="View Events", command=view_events, cursor="hand2"
)
view_events_button.grid(row=3, column=1, pady=10)

# Create a button to toggle between dark and light themes
toggle_theme_button = ttk.Button(
    frame, text="Toggle Theme", command=toggle_theme, cursor="hand2"
)
toggle_theme_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create styles for dark and light frames
style = ttk.Style()
style.configure("DarkFrame.TFrame", background="#333333")
style.configure("LightFrame.TFrame", background="#f2f2f2")

# Create styles for dark-themed buttons
style.configure("DarkButton.TButton", foreground="#333333", background="#ffffff")

# Load events from file
events = load_events()

# Apply the initial dark theme
apply_theme()

# Start the main loop
root.mainloop()
