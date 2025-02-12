import os
import random
from tkinter import *
from tkinter import messagebox

class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        self.bg_color = "#badc57"

        # Title Label
        title = Label(self.root, text="Billing Software", font=('Times New Roman', 30, 'bold'),
                      pady=2, bd=12, bg=self.bg_color, fg="Black", relief=GROOVE)
        title.pack(fill=X)

        # ----------------- Variables -----------------
        # Medical items
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.syrup = IntVar()
        self.cream = IntVar()
        self.thermal_gun = IntVar()

        # Grocery items
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.spices = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()

        # Cold drinks items
        self.sprite = IntVar()
        self.mineral = IntVar()
        self.juice = IntVar()
        self.coke = IntVar()
        self.lassi = IntVar()
        self.mountain_duo = IntVar()

        # Prices and Taxes
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()

        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()

        # Customer details
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        self.search_bill = StringVar()
        bill_number = random.randint(1000, 9999)
        self.bill_no.set(str(bill_number))

        # ----------------- Customer Details Frame -----------------
        F1 = LabelFrame(self.root, text="Customer Details", font=('Times New Roman', 15, 'bold'),
                        bd=10, fg="Black", bg=self.bg_color)
        F1.place(x=0, y=80, relwidth=1)

        Label(F1, text="Customer Name:", bg=self.bg_color, font=('Times New Roman', 15, 'bold')) \
            .grid(row=0, column=0, padx=20, pady=5)
        Entry(F1, width=15, textvariable=self.c_name, font='Arial 15', bd=7, relief=GROOVE) \
            .grid(row=0, column=1, pady=5, padx=10)

        Label(F1, text="Customer Phone:", bg=self.bg_color, font=('Times New Roman', 15, 'bold')) \
            .grid(row=0, column=2, padx=20, pady=5)
        Entry(F1, width=15, textvariable=self.c_phone, font='Arial 15', bd=7, relief=GROOVE) \
            .grid(row=0, column=3, pady=5, padx=10)

        Label(F1, text="Bill Number:", bg=self.bg_color, font=('Times New Roman', 15, 'bold')) \
            .grid(row=0, column=4, padx=20, pady=5)
        Entry(F1, width=15, textvariable=self.search_bill, font='Arial 15', bd=7, relief=GROOVE) \
            .grid(row=0, column=5, pady=5, padx=10)

        Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('Arial', 12, 'bold'),
               relief=GROOVE).grid(row=0, column=6, pady=5, padx=10)

        # ----------------- Medical Items Frame -----------------
        F2 = LabelFrame(self.root, text="Medical Items", font=('Times New Roman', 15, 'bold'),
                        bd=10, fg="Black", bg=self.bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        Label(F2, text="Sanitizer", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=0, column=0, padx=10, pady=10, sticky='W')
        Entry(F2, width=10, textvariable=self.sanitizer, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=0, column=1, padx=10, pady=10)

        Label(F2, text="Mask", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=1, column=0, padx=10, pady=10, sticky='W')
        Entry(F2, width=10, textvariable=self.mask, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=1, column=1, padx=10, pady=10)

        Label(F2, text="Hand Gloves", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=2, column=0, padx=10, pady=10, sticky='W')
        Entry(F2, width=10, textvariable=self.hand_gloves, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=2, column=1, padx=10, pady=10)

        Label(F2, text="Syrup", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=3, column=0, padx=10, pady=10, sticky='W')
        Entry(F2, width=10, textvariable=self.syrup, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=3, column=1, padx=10, pady=10)

        Label(F2, text="Cream", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=4, column=0, padx=10, pady=10, sticky='W')
        Entry(F2, width=10, textvariable=self.cream, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=4, column=1, padx=10, pady=10)

        Label(F2, text="Thermal Gun", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=5, column=0, padx=10, pady=10, sticky='W')
        Entry(F2, width=10, textvariable=self.thermal_gun, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=5, column=1, padx=10, pady=10)

        # ----------------- Grocery Items Frame -----------------
        F3 = LabelFrame(self.root, text="Grocery Items", font=('Times New Roman', 15, 'bold'),
                        bd=10, fg="Black", bg=self.bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        Label(F3, text="Rice", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=0, column=0, padx=10, pady=10, sticky='W')
        Entry(F3, width=10, textvariable=self.rice, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=0, column=1, padx=10, pady=10)

        Label(F3, text="Food Oil", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=1, column=0, padx=10, pady=10, sticky='W')
        Entry(F3, width=10, textvariable=self.food_oil, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=1, column=1, padx=10, pady=10)

        Label(F3, text="Wheat", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=2, column=0, padx=10, pady=10, sticky='W')
        Entry(F3, width=10, textvariable=self.wheat, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=2, column=1, padx=10, pady=10)

        Label(F3, text="Spices", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=3, column=0, padx=10, pady=10, sticky='W')
        Entry(F3, width=10, textvariable=self.spices, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=3, column=1, padx=10, pady=10)

        Label(F3, text="Flour", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=4, column=0, padx=10, pady=10, sticky='W')
        Entry(F3, width=10, textvariable=self.flour, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=4, column=1, padx=10, pady=10)

        Label(F3, text="Maggi", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=5, column=0, padx=10, pady=10, sticky='W')
        Entry(F3, width=10, textvariable=self.maggi, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=5, column=1, padx=10, pady=10)

        # ----------------- Cold Drinks Frame -----------------
        F4 = LabelFrame(self.root, text="Cold Drinks", font=('Times New Roman', 15, 'bold'),
                        bd=10, fg="Black", bg=self.bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        Label(F4, text="Sprite", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=0, column=0, padx=10, pady=10, sticky='W')
        Entry(F4, width=10, textvariable=self.sprite, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=0, column=1, padx=10, pady=10)

        Label(F4, text="Mineral Water", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=1, column=0, padx=10, pady=10, sticky='W')
        Entry(F4, width=10, textvariable=self.mineral, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=1, column=1, padx=10, pady=10)

        Label(F4, text="Juice", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=2, column=0, padx=10, pady=10, sticky='W')
        Entry(F4, width=10, textvariable=self.juice, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=2, column=1, padx=10, pady=10)

        Label(F4, text="Coke", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=3, column=0, padx=10, pady=10, sticky='W')
        Entry(F4, width=10, textvariable=self.coke, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=3, column=1, padx=10, pady=10)

        Label(F4, text="Lassi", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=4, column=0, padx=10, pady=10, sticky='W')
        Entry(F4, width=10, textvariable=self.lassi, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=4, column=1, padx=10, pady=10)

        Label(F4, text="Mountain Duo", font=('Times New Roman', 16, 'bold'), bg=self.bg_color, fg="Black") \
            .grid(row=5, column=0, padx=10, pady=10, sticky='W')
        Entry(F4, width=10, textvariable=self.mountain_duo, font=('Times New Roman', 16, 'bold'),
              bd=5, relief=GROOVE).grid(row=5, column=1, padx=10, pady=10)

        # ----------------- Bill Area Frame -----------------
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)
        Label(F5, text="Bill Area", font='Arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ----------------- Billing Menu Frame -----------------
        F6 = LabelFrame(self.root, text="Billing Menu", font=('Times New Roman', 14, 'bold'),
                        bd=10, fg="Black", bg=self.bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        Label(F6, text="Total Medical Price", font=('Times New Roman', 14, 'bold'),
              bg=self.bg_color, fg="Black").grid(row=0, column=0, padx=20, pady=1, sticky='W')
        Entry(F6, width=18, textvariable=self.medical_price, font='Arial 10 bold',
              bd=7, relief=GROOVE).grid(row=0, column=1, padx=18, pady=1)

        Label(F6, text="Total Grocery Price", font=('Times New Roman', 14, 'bold'),
              bg=self.bg_color, fg="Black").grid(row=1, column=0, padx=20, pady=1, sticky='W')
        Entry(F6, width=18, textvariable=self.grocery_price, font='Arial 10 bold',
              bd=7, relief=GROOVE).grid(row=1, column=1, padx=18, pady=1)

        Label(F6, text="Total Cold Drinks Price", font=('Times New Roman', 14, 'bold'),
              bg=self.bg_color, fg="Black").grid(row=2, column=0, padx=20, pady=1, sticky='W')
        Entry(F6, width=18, textvariable=self.cold_drinks_price, font='Arial 10 bold',
              bd=7, relief=GROOVE).grid(row=2, column=1, padx=18, pady=1)

        Label(F6, text="Medical Tax", font=('Times New Roman', 14, 'bold'),
              bg=self.bg_color, fg="Black").grid(row=0, column=2, padx=20, pady=1, sticky='W')
        Entry(F6, width=18, textvariable=self.medical_tax, font='Arial 10 bold',
              bd=7, relief=GROOVE).grid(row=0, column=3, padx=18, pady=1)

        Label(F6, text="Grocery Tax", font=('Times New Roman', 14, 'bold'),
              bg=self.bg_color, fg="Black").grid(row=1, column=2, padx=20, pady=1, sticky='W')
        Entry(F6, width=18, textvariable=self.grocery_tax, font='Arial 10 bold',
              bd=7, relief=GROOVE).grid(row=1, column=3, padx=18, pady=1)

        Label(F6, text="Cold Drinks Tax", font=('Times New Roman', 14, 'bold'),
              bg=self.bg_color, fg="Black").grid(row=2, column=2, padx=20, pady=1, sticky='W')
        Entry(F6, width=18, textvariable=self.cold_drinks_tax, font='Arial 10 bold',
              bd=7, relief=GROOVE).grid(row=2, column=3, padx=18, pady=1)

        # ----------------- Buttons Frame -----------------
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)
        Button(btn_f, command=self.total, text="Total", bg="#535C68", bd=2, fg="white",
               pady=15, width=12, font='Arial 13 bold').grid(row=0, column=0, padx=5, pady=5)
        Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="white",
               pady=12, width=12, font='Arial 13 bold').grid(row=0, column=1, padx=5, pady=5)
        Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white",
               pady=15, width=12, font='Arial 13 bold').grid(row=0, column=2, padx=5, pady=5)
        Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="white",
               pady=15, width=12, font='Arial 13 bold').grid(row=0, column=3, padx=5, pady=5)

        self.welcome_bill()

    def total(self):
        # ---- Calculate Medical Prices ----
        sanitizer_price = self.sanitizer.get() * 2
        mask_price = self.mask.get() * 5
        hand_gloves_price = self.hand_gloves.get() * 12
        syrup_price = self.syrup.get() * 30
        cream_price = self.cream.get() * 5
        thermal_gun_price = self.thermal_gun.get() * 15
        total_medical = (sanitizer_price + mask_price + hand_gloves_price +
                         syrup_price + cream_price + thermal_gun_price)
        self.medical_price.set("Rs. " + str(total_medical))
        medical_tax_val = round(total_medical * 0.05, 2)
        self.medical_tax.set("Rs. " + str(medical_tax_val))

        # ---- Calculate Grocery Prices ----
        rice_price = self.rice.get() * 10
        food_oil_price = self.food_oil.get() * 10
        wheat_price = self.wheat.get() * 10
        spices_price = self.spices.get() * 6
        flour_price = self.flour.get() * 8
        maggi_price = self.maggi.get() * 5
        total_grocery = (rice_price + food_oil_price + wheat_price +
                         spices_price + flour_price + maggi_price)
        self.grocery_price.set("Rs. " + str(total_grocery))
        grocery_tax_val = round(total_grocery * 0.05, 2)
        self.grocery_tax.set("Rs. " + str(grocery_tax_val))

        # ---- Calculate Cold Drinks Prices ----
        sprite_price = self.sprite.get() * 10
        mineral_price = self.mineral.get() * 10
        juice_price = self.juice.get() * 10
        coke_price = self.coke.get() * 10
        lassi_price = self.lassi.get() * 10
        mountain_duo_price = self.mountain_duo.get() * 10
        total_cold_drinks = (sprite_price + mineral_price + juice_price +
                             coke_price + lassi_price + mountain_duo_price)
        self.cold_drinks_price.set("Rs. " + str(total_cold_drinks))
        cold_drinks_tax_val = round(total_cold_drinks * 0.1, 2)
        self.cold_drinks_tax.set("Rs. " + str(cold_drinks_tax_val))

        # ---- Calculate Total Bill ----
        self.total_bill = (total_medical + total_grocery + total_cold_drinks +
                           medical_tax_val + grocery_tax_val + cold_drinks_tax_val)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to Billing Software")
        self.txtarea.insert(END, f"\nBill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, "\n================================")
        self.txtarea.insert(END, "\nProducts\t\tQty\t\tPrice")

    def bill_area(self):
        # Validate customer details and product selection
        if not self.c_name.get().strip() or not self.c_phone.get().strip():
            messagebox.showerror("Error", "Customer details are required!")
            return
        if (self.medical_price.get() == "Rs. 0" and 
            self.grocery_price.get() == "Rs. 0" and 
            self.cold_drinks_price.get() == "Rs. 0"):
            messagebox.showerror("Error", "No product purchased!")
            return

        self.welcome_bill()
        # ---- Medical Items ----
        if self.sanitizer.get() != 0:
            self.txtarea.insert(END, f"\nSanitizer\t\t{self.sanitizer.get()}\t\t{self.sanitizer.get()*2}")
        if self.mask.get() != 0:
            self.txtarea.insert(END, f"\nMask\t\t{self.mask.get()}\t\t{self.mask.get()*5}")
        if self.hand_gloves.get() != 0:
            self.txtarea.insert(END, f"\nHand Gloves\t\t{self.hand_gloves.get()}\t\t{self.hand_gloves.get()*12}")
        if self.syrup.get() != 0:
            self.txtarea.insert(END, f"\nSyrup\t\t{self.syrup.get()}\t\t{self.syrup.get()*30}")
        if self.cream.get() != 0:
            self.txtarea.insert(END, f"\nCream\t\t{self.cream.get()}\t\t{self.cream.get()*5}")
        if self.thermal_gun.get() != 0:
            self.txtarea.insert(END, f"\nThermal Gun\t\t{self.thermal_gun.get()}\t\t{self.thermal_gun.get()*15}")
        # ---- Grocery Items ----
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\nRice\t\t{self.rice.get()}\t\t{self.rice.get()*10}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\nFood Oil\t\t{self.food_oil.get()}\t\t{self.food_oil.get()*10}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\nWheat\t\t{self.wheat.get()}\t\t{self.wheat.get()*10}")
        if self.spices.get() != 0:
            self.txtarea.insert(END, f"\nSpices\t\t{self.spices.get()}\t\t{self.spices.get()*6}")
        if self.flour.get() != 0:
            self.txtarea.insert(END, f"\nFlour\t\t{self.flour.get()}\t\t{self.flour.get()*8}")
        if self.maggi.get() != 0:
            self.txtarea.insert(END, f"\nMaggi\t\t{self.maggi.get()}\t\t{self.maggi.get()*5}")
        # ---- Cold Drinks Items ----
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\nSprite\t\t{self.sprite.get()}\t\t{self.sprite.get()*10}")
        if self.mineral.get() != 0:
            self.txtarea.insert(END, f"\nMineral Water\t\t{self.mineral.get()}\t\t{self.mineral.get()*10}")
        if self.juice.get() != 0:
            self.txtarea.insert(END, f"\nJuice\t\t{self.juice.get()}\t\t{self.juice.get()*10}")
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\nCoke\t\t{self.coke.get()}\t\t{self.coke.get()*10}")
        if self.lassi.get() != 0:
            self.txtarea.insert(END, f"\nLassi\t\t{self.lassi.get()}\t\t{self.lassi.get()*10}")
        if self.mountain_duo.get() != 0:
            self.txtarea.insert(END, f"\nMountain Duo\t\t{self.mountain_duo.get()}\t\t{self.mountain_duo.get()*10}")

        self.txtarea.insert(END, "\n--------------------------------")
        if self.medical_tax.get() != 'Rs. 0.0':
            self.txtarea.insert(END, f"\nMedical Tax\t\t\t{self.medical_tax.get()}")
        if self.grocery_tax.get() != 'Rs. 0.0':
            self.txtarea.insert(END, f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != 'Rs. 0.0':
            self.txtarea.insert(END, f"\nCold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")
        self.txtarea.insert(END, f"\nTotal Bill:\t\t\tRs. {self.total_bill}")
        self.txtarea.insert(END, "\n--------------------------------")

        self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op:
            bill_data = self.txtarea.get('1.0', END)
            # Ensure the bills directory exists
            if not os.path.exists("bills"):
                os.makedirs("bills")
            with open(f"bills/{self.bill_no.get()}.txt", "w") as f:
                f.write(bill_data)
            messagebox.showinfo("Saved", f"Bill no: {self.bill_no.get()} saved successfully!")

    def find_bill(self):
        found = False
        for file in os.listdir("bills"):
            if file.split('.')[0] == self.search_bill.get():
                with open(f"bills/{file}", "r") as f:
                    self.txtarea.delete("1.0", END)
                    self.txtarea.insert(END, f.read())
                found = True
                break
        if not found:
            messagebox.showerror("Error", "Invalid Bill Number")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear the data?")
        if op:
            # Reset all fields and variables
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.syrup.set(0)
            self.cream.set(0)
            self.thermal_gun.set(0)
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.spices.set(0)
            self.flour.set(0)
            self.maggi.set(0)
            self.sprite.set(0)
            self.mineral.set(0)
            self.juice.set(0)
            self.coke.set(0)
            self.lassi.set(0)
            self.mountain_duo.set(0)
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")
            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")
            self.c_name.set("")
            self.c_phone.set("")
            self.search_bill.set("")
            new_bill_no = random.randint(1000, 9999)
            self.bill_no.set(str(new_bill_no))
            self.txtarea.delete("1.0", END)
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = BillApp(root)
    root.mainloop()
