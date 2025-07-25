import tkinter as tk
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
import names


class NameGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Name Generator")
        self.root.geometry("500x400")  # Increased window size
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f4f4")

        self.setup_ui()

    def setup_ui(self):
        # Title Label
        title = tk.Label(self.root, text="Name Generator", font=("Verdana", 16, "bold"),
                         bg="#333", fg="white", pady=10)
        title.pack(fill=tk.X)

        # Frame for dropdowns
        input_frame = tk.Frame(self.root, bg="#f4f4f4")
        input_frame.pack(pady=15)

        # Gender Dropdown
        tk.Label(input_frame, text="Gender:", font=("Verdana", 10, "bold"),
                 bg="#f4f4f4").grid(row=0, column=0, padx=10, sticky='w')
        self.gender_var = tk.StringVar()
        self.gender_box = Combobox(input_frame, textvariable=self.gender_var,
                                   values=["Male", "Female"], state="readonly", width=15,
                                   font=("Verdana", 10))
        self.gender_box.grid(row=1, column=0, padx=10)
        self.gender_box.current(0)

        # Type Dropdown
        tk.Label(input_frame, text="Type:", font=("Verdana", 10, "bold"),
                 bg="#f4f4f4").grid(row=0, column=1, padx=10, sticky='w')
        self.type_var = tk.StringVar()
        self.type_box = Combobox(input_frame, textvariable=self.type_var,
                                 values=["Full Name", "First Name", "Last Name"], state="readonly",
                                 width=15, font=("Verdana", 10))
        self.type_box.grid(row=1, column=1, padx=10)
        self.type_box.current(0)

        # Generate Button
        generate_btn = tk.Button(self.root, text="Generate", font=("Verdana", 10, "bold"),
                                 command=self.generate_name, bg="#007acc", fg="white",
                                 relief=tk.RAISED, padx=10, pady=5)
        generate_btn.pack(pady=5)

        # Output Text Box with increased height
        self.output_box = ScrolledText(self.root, width=60, height=12,
                                       font=("Verdana", 10), wrap=tk.WORD)
        self.output_box.pack(pady=10)

    def generate_name(self):
        gender = self.gender_var.get().lower()
        name_type = self.type_var.get()

        try:
            if name_type == "Full Name":
                name = names.get_full_name(gender=gender)
            elif name_type == "First Name":
                name = names.get_first_name(gender=gender)
            elif name_type == "Last Name":
                name = names.get_last_name()
            else:
                name = "Invalid selection."

            self.output_box.insert(tk.END, f"{name}\n")
            self.output_box.see(tk.END)
        except Exception as e:
            self.output_box.insert(tk.END, f"Error: {str(e)}\n")
            self.output_box.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = NameGeneratorApp(root)
    root.mainloop()
