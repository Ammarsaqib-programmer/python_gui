from tkinter import *

# Function for clearing the contents of all entry boxes
def clear_all():
    principal_field.delete(0, END)
    rate_field.delete(0, END)
    time_field.delete(0, END)
    compound_field.delete(0, END)
    interest_field.delete(0, END)
    principal_field.focus_set()

# Function to find compound interest
def calculate_ci():
    principal = int(principal_field.get())
    rate = float(rate_field.get())
    time = int(time_field.get())
    
    # Calculates compound interest
    CI = principal * (pow((1 + rate / 100), time))
    interest_amount = CI - principal
    
    # Insert values into text entry boxes
    compound_field.insert(10, round(CI, 2))
    interest_field.insert(10, round(interest_amount, 2))

# Driver code
if __name__ == "__main__":
    root = Tk()
    root.configure(background='#2E4053')  # Dark blue-grey background
    root.geometry("450x300")
    root.title("Compound Interest Calculator")
    
    # Labels
    label1 = Label(root, text="Principal Amount (Rs):", fg='white', bg='#1ABC9C', font=('Arial', 10, 'bold'))
    label2 = Label(root, text="Rate (%):", fg='white', bg='#1ABC9C', font=('Arial', 10, 'bold'))
    label3 = Label(root, text="Time (years):", fg='white', bg='#1ABC9C', font=('Arial', 10, 'bold'))
    label4 = Label(root, text="Compound Interest:", fg='white', bg='#1ABC9C', font=('Arial', 10, 'bold'))
    label5 = Label(root, text="Interest Amount:", fg='white', bg='#1ABC9C', font=('Arial', 10, 'bold'))
    
    label1.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=2, column=0, padx=10, pady=10)
    label3.grid(row=3, column=0, padx=10, pady=10)
    label4.grid(row=5, column=0, padx=10, pady=10)
    label5.grid(row=6, column=0, padx=10, pady=10)
    
    # Entry fields
    principal_field = Entry(root, bg='white', font=('Arial', 10))
    rate_field = Entry(root, bg='white', font=('Arial', 10))
    time_field = Entry(root, bg='white', font=('Arial', 10))
    compound_field = Entry(root, bg='white', font=('Arial', 10))
    interest_field = Entry(root, bg='white', font=('Arial', 10))
    
    principal_field.grid(row=1, column=1, padx=10, pady=10)
    rate_field.grid(row=2, column=1, padx=10, pady=10)
    time_field.grid(row=3, column=1, padx=10, pady=10)
    compound_field.grid(row=5, column=1, padx=10, pady=10)
    interest_field.grid(row=6, column=1, padx=10, pady=10)
    
    # Buttons
    button1 = Button(root, text="Submit", bg="#3498DB", fg="white", font=('Arial', 10, 'bold'), command=calculate_ci)
    button2 = Button(root, text="Clear", bg="#E74C3C", fg="white", font=('Arial', 10, 'bold'), command=clear_all)
    
    button1.grid(row=4, column=1, pady=10)
    button2.grid(row=7, column=1, pady=10)
    
    root.mainloop()
