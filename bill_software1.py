from tkinter import *
import os, random
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class bill_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1300x760")
        # self.root.minsize(1200, 760)
        self.root.title("Billing Software")
        bg_color = "#006078"
        title = Label(self.root, text="ELECTRO BILLING SOFTWARE", bg=bg_color, fg="white",
                      font="roboto 20 bold", bd=12, relief=GROOVE)
        title.pack(fill=X)

        # =====initializing variable=============
        # =======laptop============
        self.hp_l = IntVar()
        self.Asus_l = IntVar()
        self.lenovo_l = IntVar()
        self.samsung_l = IntVar()
        self.apple_l = IntVar()
        self.jiobook_l = IntVar()
        # ========phone===========
        self.samsung_p = IntVar()
        self.vivo_p = IntVar()
        self.oneplus_p = IntVar()
        self.realme_p = IntVar()
        self.google_p = IntVar()
        self.apple_p = IntVar()
        # =========led=========
        self.croma_le = IntVar()
        self.samsung_le = IntVar()
        self.xiaomi_le = IntVar()
        self.tcl_le = IntVar()
        self.lg_le = IntVar()
        self.sony_le = IntVar()

        # ========total product price=========
        self.laptops_price = StringVar()
        self.phones_price = StringVar()
        self.leds_price = StringVar()

        # ==========tax=======
        self.laptops_tax = StringVar()
        self.phones_tax = StringVar()
        self.leds_tax = StringVar()

        # =======customer info========
        self.c_name = StringVar()
        self.c_address = StringVar()
        self.c_phno = StringVar()
        self.bill_no = StringVar()
        self.bill_no.set(str(random.randint(1000, 9999)))
        self.search_bill = StringVar()

        # running totals, populated by self.total() -- initialize so bill_area()
        # # can never be called against stale/missing data
        self._reset_computed_totals()

        sb = Scrollbar(self.root)
        sb.pack(side=RIGHT, fill=Y)

        # customer detail
        c1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", bg=bg_color, fg="white",
                        font="roboto 15 bold")
        c1.place(x=0, y=61, relwidth=1)
        Label(c1, text="Customer Name", bg=bg_color, fg="white", font="roboto 16 bold ").grid(
            row=0, column=0, padx=20, pady=5)
        Entry(c1, width=15, textvariable=self.c_name, font="arial 14", bd=3, relief=SOLID).grid(
            row=0, column=1, pady=5, padx=10)

        Label(c1, text="Phone No:", bg=bg_color, fg="white", font="roboto 16 bold").grid(
            row=0, column=2, padx=20, pady=5)
        Entry(c1, width=15, textvariable=self.c_phno, font="arial 14", bd=3, relief=SOLID).grid(
            row=0, column=3, pady=5, padx=10)

        Label(c1, text="Address", bg=bg_color, fg="white", font="roboto 16 bold").grid(
            row=0, column=4, padx=20, pady=5)
        Entry(c1, width=17, textvariable=self.c_address, font="arial 14", bd=3, relief=SOLID).grid(
            row=0, column=5, pady=5, padx=10)

        Label(c1, text="Search (Bill No / Name / Phone):", bg=bg_color, fg="white",
              font="roboto 14 bold").grid(row=1, column=0, columnspan=2, padx=10, pady=8, sticky="e")
        Entry(c1, width=18, textvariable=self.search_bill, font="arial 14", bd=3, relief=SOLID).grid(
            row=1, column=2, pady=8, padx=10, sticky="w")
        Button(c1, text="Search", width=10, bd=3, relief=SOLID, font="arial 14", fg="white", bg=bg_color,
               command=self.find_bill).grid(row=1, column=3, padx=10, pady=8)

        Button(c1, text="View All Bills", width=14, bd=3, relief=SOLID, font="arial 14", fg="white",
               bg=bg_color, command=self.view_all_bills).grid(row=1, column=4, padx=10, pady=8)
        
          # =========first appliances======
        c2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Laptops", font="roboto 16 bold", bg=bg_color,
                         fg="black")
        c2.place(x=5, y=198, width=300, height=335)

        Label(c2, text="Hp Laptop:", bg=bg_color, fg="light green", font="roboto 15 bold").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        Entry(c2, width=8, textvariable=self.hp_l, font="arial 13", bd=3, relief=SOLID).grid(
            row=0, column=1, padx=10, pady=10)

        Label(c2, text="Asus Laptop:", bg=bg_color, fg="light green", font="roboto 15 bold").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        Entry(c2, textvariable=self.Asus_l, font="arial 13", bd=3, relief=SOLID, width=8).grid(
            row=1, column=1, padx=10, pady=10)

        Label(c2, text="Lenovo Laptop:", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        Entry(c2, width=8, textvariable=self.lenovo_l, font="arial 13", bd=3, relief=SOLID).grid(
            row=2, column=1, padx=10, pady=10)

        Label(c2, text="Samsung Laptop:", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=3, column=0, padx=10, pady=10)
        Entry(c2, width=8, textvariable=self.samsung_l, font="arial 13", bd=3, relief=SOLID).grid(
            row=3, column=1, padx=10, pady=10)

        Label(c2, text="Apple Laptop:", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        Entry(c2, width=8, textvariable=self.apple_l, font="arial 13", bd=3, relief=SOLID).grid(
            row=4, column=1, padx=10, pady=10)

        Label(c2, text="Jiobook Laptop:", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        Entry(c2, width=8, textvariable=self.jiobook_l, font="arial 13", bd=3, relief=SOLID).grid(
            row=5, column=1, padx=10, pady=10)

        # ========second appliances
        c3 = LabelFrame(self.root, text="phones", font="roboto 16 bold", bg=bg_color, fg="black", bd=10,
                        relief=GROOVE)
        c3.place(x=308, y=198, width=300, height=335)

        Label(c3, text="Samsung Phone:", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        Entry(c3, width=8, textvariable=self.samsung_p, bd=3, relief=SOLID, font="arial 13").grid(
            row=0, column=1, padx=10, pady=10)

        Label(c3, text="Vivo Phone:", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        Entry(c3, width=8, textvariable=self.vivo_p, bd=3, relief=SOLID, font="arial 13").grid(
            row=1, column=1, padx=10, pady=10)

        Label(c3, text="OnePlus Phone:", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        Entry(c3, width=8, textvariable=self.oneplus_p, bd=3, relief=SOLID, font="arial 13").grid(
            row=2, column=1, padx=10, pady=10)

        Label(c3, text="Realme Phone:", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        Entry(c3, width=8, textvariable=self.realme_p, bd=3, relief=SOLID, font="arial 13").grid(
            row=3, column=1, padx=10, pady=10)

        Label(c3, text="Google Phone:", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        Entry(c3, width=8, textvariable=self.google_p, bd=3, relief=SOLID, font="arial 13").grid(
            row=4, column=1, padx=10, pady=10)

        Label(c3, text="Apple Phone:", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        Entry(c3, width=8, textvariable=self.apple_p, bd=3, relief=SOLID, font="arial 13").grid(
            row=5, column=1, padx=10, pady=10)

        # =======third appliances========
        c4 = LabelFrame(self.root, font="roboto 16 bold", fg="black", bg=bg_color, text="LEDs", bd=10,
                        relief=GROOVE)
        c4.place(x=612, y=198, width=300, height=335)

        Label(c4, text="Croma LED", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        Entry(c4, textvariable=self.croma_le, font="arial 13", bd=3, width=8, relief=SOLID).grid(
            row=0, column=1, padx=10, pady=10)

        Label(c4, text="Samsung LED", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=1, column=0, padx=10, pady=10, sticky="w")
        Entry(c4, textvariable=self.samsung_le, font="arial 13", bd=3, width=8, relief=SOLID).grid(
            row=1, column=1, padx=10, pady=10)

        Label(c4, text="TCL LED", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        Entry(c4, textvariable=self.tcl_le, font="arial 13", bd=3, width=8, relief=SOLID).grid(
            row=2, column=1, padx=10, pady=10)

        Label(c4, text="Xiaomi LED", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        Entry(c4, textvariable=self.xiaomi_le, font="arial 13", bd=3, width=8, relief=SOLID).grid(
            row=3, column=1, padx=10, pady=10)

        Label(c4, text="LG LED", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        Entry(c4, textvariable=self.lg_le, font="arial 13", bd=3, width=8, relief=SOLID).grid(
            row=4, column=1, padx=10, pady=10)

        Label(c4, text="Sony LED", fg="light green", bg=bg_color, font="roboto 15 bold").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        Entry(c4, textvariable=self.sony_le, font="arial 13", bd=3, width=8, relief=SOLID).grid(
            row=5, column=1, padx=10, pady=10)
        
        c5 = LabelFrame(self.root, bd=7, relief=GROOVE)
        c5.place(x=914, y=198, width=350, height=335)
        Label(c5, text="BILL AREA", bg="light grey", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        sb2 = Scrollbar(c5)
        sb2.pack(side=RIGHT, fill=Y)
        self.textarea = Text(c5, yscrollcommand=sb2.set)
        sb2.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # ============Button Frame========
        c7 = LabelFrame(self.root, bd=3, relief=GROOVE, bg=bg_color)
        c7.place(x=2, y=525, height=135)
        c6 = LabelFrame(c7, relief=GROOVE, text=" ", font="roboto 16 bold", fg="black", bg=bg_color)
        c6.pack(side=LEFT, fill=BOTH, pady=1)

        Label(c6, text="Total Laptop Price", bg=bg_color, fg="white", font="roboto 14 bold").grid(
            row=0, column=0, padx=10, pady=0, sticky="w")
        Entry(c6, width=11, textvariable=self.laptops_price, font="arial 12", bd=3, relief=SOLID).grid(
            row=0, column=1, padx=10, pady=1)

        Label(c6, text="Total Phone Price", font="roboto 14 bold", bg=bg_color, fg="white").grid(
            row=1, column=0, padx=10, pady=1, sticky="w")
        Entry(c6, width=11, textvariable=self.phones_price, font="arial 12", bd=3, relief=SOLID).grid(
            row=1, column=1, padx=10, pady=2)

        Label(c6, text="Total LEDs Price", font="roboto 14 bold", bg=bg_color, fg="white").grid(
            row=2, column=0, padx=10, pady=1, sticky="w")
        Entry(c6, width=11, textvariable=self.leds_price, font="arial 12", bd=3, relief=SOLID).grid(
            row=2, column=1, padx=10, pady=2)

        Label(c6, text="Laptop Tax", font="roboto 14 bold", fg="white", bg=bg_color).grid(
            row=0, column=2, padx=12, pady=0, sticky="w")
        Entry(c6, width=10, textvariable=self.laptops_tax, font="arial 12", bd=3, relief=SOLID).grid(
            row=0, column=3, padx=6, pady=1)

        Label(c6, text="Phones Tax", font="roboto 14 bold", fg="white", bg=bg_color).grid(
            row=1, column=2, padx=12, pady=0, sticky="w")
        Entry(c6, width=10, textvariable=self.phones_tax, font="arial 12", bd=3, relief=SOLID).grid(
            row=1, column=3, padx=6, pady=1)

        Label(c6, text="LEDs Tax", font="roboto 14 bold", fg="white", bg=bg_color).grid(
            row=2, column=2, padx=12, pady=0, sticky="w")
        Entry(c6, width=10, textvariable=self.leds_tax, font="arial 12", bd=3, relief=SOLID).grid(
            row=2, column=3, padx=6, pady=1)

        b_f = Frame(c7, bd=3, relief=GROOVE)
        b_f.pack(side=RIGHT, fill=Y, pady=2, padx=20)

        Button(b_f, text="Total", command=self.total, font="roboto 12 bold", bg="cadetblue", fg="white", bd=3,
               width=15, height=3, relief=GROOVE).grid(row=0, column=0, padx=2, pady=12)
        Button(b_f, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="white",
               font="roboto 12 bold", bd=3, relief=GROOVE, width=15, height=3).grid(row=0, column=1, padx=2,
                                                                                     pady=12)
        Button(b_f, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", font="roboto 12 bold",
               bd=3, relief=GROOVE, width=15, height=3).grid(row=0, column=2, padx=2, pady=12)
        Button(b_f, text="Exit", command=self.Exit_app, bg="cadetblue", fg="white", font="roboto 12 bold",
               bd=3, relief=GROOVE, width=15, height=3).grid(row=0, column=3, padx=2, pady=12)
        
         # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------
    def _reset_computed_totals(self):
        """Keeps every per-item / per-category price attribute defined,
        so bill_area() can never crash from a skipped 'Total' click."""
        for attr in ("hp_l_p", "Asus_l_p", "lenovo_l_p", "samsung_l_p", "apple_l_p", "jiobook_l_p",
                     "samsung_p_p", "vivo_p_p", "oneplus_p_p", "realme_p_p", "google_p_p", "apple_p_p",
                     "croma_le_p", "samsung_le_p", "tcl_le_p", "xiaomi_le_p", "lg_le_p", "sony_le_p",
                     "total_l_p", "total_p_p", "total_le_p", "total_bill"):
            setattr(self, attr, 0)

    def total(self):
        self.hp_l_p = self.hp_l.get() * 47100
        self.Asus_l_p = self.Asus_l.get() * 62990
        self.lenovo_l_p = self.lenovo_l.get() * 84999
        self.samsung_l_p = self.samsung_l.get() * 94990
        self.apple_l_p = self.apple_l.get() * 144900
        self.jioBook_l_p = self.jiobook_l.get() * 10490

        self.total_l_p = float(self.hp_l_p + self.Asus_l_p + self.lenovo_l_p +
                                self.samsung_l_p + self.apple_l_p + self.jioBook_l_p)
        self.laptops_price.set("Rs. " + str(self.total_l_p))
        laptops_tax = round(self.total_l_p * 0.05, 2)
        self.laptops_tax.set("Rs. " + str(laptops_tax))

        self.samsung_p_p = self.samsung_p.get() * 11999
        self.vivo_p_p = self.vivo_p.get() * 19999
        self.oneplus_p_p = self.oneplus_p.get() * 23999
        self.realme_p_p = self.realme_p.get() * 33999
        self.google_p_p = self.google_p.get() * 43310
        self.apple_p_p = self.apple_p.get() * 82900

        self.total_p_p = float(self.samsung_p_p + self.vivo_p_p + self.oneplus_p_p +
                                self.realme_p_p + self.google_p_p + self.apple_p_p)
        self.phones_price.set("Rs. " + str(self.total_p_p))
        phones_tax = round(self.total_p_p * 0.1, 2)
        self.phones_tax.set("Rs. " + str(phones_tax))

        self.croma_le_p = self.croma_le.get() * 10990
        self.samsung_le_p = self.samsung_le.get() * 14750
        self.tcl_le_p = self.tcl_le.get() * 16990
        self.xiaomi_le_p = self.xiaomi_le.get() * 16990
        self.lg_le_p = self.lg_le.get() * 34990
        self.sony_le_p = self.sony_le.get() * 52240

        self.total_le_p = (self.croma_le_p + self.samsung_le_p + self.tcl_le_p +
                            self.xiaomi_le_p + self.lg_le_p + self.sony_le_p)
        self.leds_price.set("Rs. " + str(self.total_le_p))
        leds_tax = round(self.total_le_p * 0.05, 2)
        self.leds_tax.set("Rs. " + str(leds_tax))

        self.total_bill = (self.total_l_p + self.total_p_p + self.total_le_p +
                            laptops_tax + phones_tax + leds_tax)

    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\t ELECTRO BILLING AREA \n")
        self.textarea.insert(END, f"\n BILL NUMBER : {self.bill_no.get()}")
        self.textarea.insert(END, f"\n CUSTOMER NAME : {self.c_name.get()}")
        self.textarea.insert(END, f"\n PHONE NUMBER : {self.c_phno.get()}")
        self.textarea.insert(END, f"\n ADDRESS : {self.c_address.get()}")
        self.textarea.insert(END, "\n==============================================")
        self.textarea.insert(END, "\n PRODUCTS \t QTY \t PRICE")
        self.textarea.insert(END, "\n==============================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phno.get() == "" or self.c_address.get() == "":
            messagebox.showerror("Error", "Customer detail are must ")
            return

        # make sure totals reflect the current form state, regardless of
        # whether the user remembered to click "Total" first
        self.total()

        if (self.laptops_price.get() == "Rs. 0.0" and
                self.phones_price.get() == "Rs. 0.0" and
                self.leds_price.get() == "Rs. 0.0"):
            messagebox.showerror("Error", "No purchased")
            return

        self.welcome_bill()

        try:
            myconn = mysql.connector.connect(
                host="localhost",
                user="root",
                password=os.environ.get("BILLING_DB_PASSWORD", " "),
                database="data_storage"
            )
            cur = myconn.cursor()
            cur.execute(
                "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.bill_no.get(), self.c_name.get(), self.c_phno.get(), self.c_address.get(),
                 self.total_l_p, self.total_p_p, self.total_le_p,
                 self.laptops_tax.get(), self.phones_tax.get(), self.leds_tax.get(), self.total_bill),
            )
            cur.execute(
                "insert into Laptop values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.bill_no.get(), self.c_name.get(), self.c_phno.get(), self.c_address.get(),
                 self.hp_l_p, self.lenovo_l_p, self.Asus_l_p, self.samsung_l_p, self.apple_l_p,
                 self.jiobook_l_p, self.total_l_p, self.laptops_tax.get(), self.total_bill),
            )
            cur.execute(
                "insert into Phones values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.bill_no.get(), self.c_name.get(), self.c_phno.get(), self.c_address.get(),
                 self.samsung_p_p, self.vivo_p_p, self.oneplus_p_p, self.realme_p_p, self.google_p_p,
                 self.apple_p_p, self.total_p_p, self.phones_tax.get(), self.total_bill),
            )
            cur.execute(
                "insert into LEDs values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.bill_no.get(), self.c_name.get(), self.c_phno.get(), self.c_address.get(),
                 self.croma_le_p, self.samsung_le_p, self.tcl_le_p, self.xiaomi_le_p, self.lg_le_p,
                 self.sony_le_p, self.total_le_p, self.leds_tax.get(), self.total_bill),
            )
            myconn.commit()
            print(cur.rowcount, "Data Inserted")
            myconn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Could not save bill to database:\n{err}")

        # =========laptop======
        if self.hp_l.get() != 0:
            self.textarea.insert(END, f"\n Hp Laptop\t\t{self.hp_l.get()}\t\t{self.hp_l_p}")
        if self.Asus_l.get() != 0:
            self.textarea.insert(END, f"\n Asus Laptop\t\t{self.Asus_l.get()}\t\t{self.Asus_l_p}")
        if self.lenovo_l.get() != 0:
            self.textarea.insert(END, f"\n Lenovo Laptop\t\t{self.lenovo_l.get()}\t\t{self.lenovo_l_p}")
        if self.samsung_l.get() != 0:
            self.textarea.insert(END, f"\n Samsung Laptop\t\t{self.samsung_l.get()}\t\t{self.samsung_l_p}")
        if self.apple_l.get() != 0:
            self.textarea.insert(END, f"\n Apple Laptop\t\t{self.apple_l.get()}\t\t{self.apple_l_p}")
        if self.jiobook_l.get() != 0:
            self.textarea.insert(END, f"\n Jiobook Laptop\t\t{self.jiobook_l.get()}\t\t{self.jioBook_l_p}")

        # ==========phones========
        if self.samsung_p.get() != 0:
            self.textarea.insert(END, f"\n Samsung Phone\t\t{self.samsung_p.get()}\t\t{self.samsung_p_p}")
        if self.vivo_p.get() != 0:
            self.textarea.insert(END, f"\n Vivo Phone\t\t{self.vivo_p.get()}\t\t{self.vivo_p_p}")
        if self.oneplus_p.get() != 0:
            self.textarea.insert(END, f"\n Oneplus Phone\t\t{self.oneplus_p.get()}\t\t{self.oneplus_p_p}")
        if self.realme_p.get() != 0:
            self.textarea.insert(END, f"\n Realme Phone\t\t{self.realme_p.get()}\t\t{self.realme_p_p}")
        if self.google_p.get() != 0:
            self.textarea.insert(END, f"\n Google Phone\t\t{self.google_p.get()}\t\t{self.google_p_p}")
        if self.apple_p.get() != 0:
            self.textarea.insert(END, f"\n Apple Phone\t\t{self.apple_p.get()}\t\t{self.apple_p_p}")

        # ======leds=======
        if self.croma_le.get() != 0:
            self.textarea.insert(END, f"\n Croma LEDs\t\t{self.croma_le.get()}\t\t{self.croma_le_p}")
        if self.samsung_le.get() != 0:
            self.textarea.insert(END, f"\n Samsung LEDs\t\t{self.samsung_le.get()}\t\t{self.samsung_le_p}")
        if self.tcl_le.get() != 0:
            self.textarea.insert(END, f"\n TCL LEDs\t\t{self.tcl_le.get()}\t\t{self.tcl_le_p}")
        if self.xiaomi_le.get() != 0:
            self.textarea.insert(END, f"\n Xiaomi LEDs\t\t{self.xiaomi_le.get()}\t\t{self.xiaomi_le_p}")
        if self.lg_le.get() != 0:
            self.textarea.insert(END, f"\n LG LEDs\t\t{self.lg_le.get()}\t\t{self.lg_le_p}")
        if self.sony_le.get() != 0:
            self.textarea.insert(END, f"\n Sony LEDs\t\t{self.sony_le.get()}\t\t{self.sony_le_p}")

        self.textarea.insert(END, "\n----------------------------------------------")
        if self.laptops_tax.get() != "Rs. 0.0":
            self.textarea.insert(END, f"\n Laptops Tax\t\t\t{self.laptops_tax.get()}")
        if self.phones_tax.get() != "Rs. 0.0":
            self.textarea.insert(END, f"\n Phones Tax\t\t\t{self.phones_tax.get()}")
        if self.leds_tax.get() != "Rs. 0.0":
            self.textarea.insert(END, f"\n LEDs Tax\t\t\t{self.leds_tax.get()}")
        self.textarea.insert(END, f"\n Total Bill : \t\t\t Rs. {str(self.total_bill)}")
        self.textarea.insert(END, "\n----------------------------------------------")
        self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if not op:
            return
        os.makedirs("bills", exist_ok=True)
        self.bill_data = self.textarea.get('1.0', END)
        filepath = os.path.join("bills", str(self.bill_no.get()) + ".txt")
        with open(filepath, "w") as f1:
            f1.write(self.bill_data)
        messagebox.showinfo("Saved", f"Bill no. {self.bill_no.get()} Saved Successfully")

    def _load_bill_file(self, bill_no):
        """Loads a saved bill .txt file straight into the BILL AREA."""
        path = os.path.join("bills", f"{bill_no}.txt")
        with open(path, "r") as f1:
            self.textarea.delete('1.0', END)
            for line in f1:
                self.textarea.insert(END, line)

    def find_bill(self):
        """Searches by exact bill number first. If that doesn't match,
        falls back to a case-insensitive search across customer name /
        phone number inside every saved bill, so you don't have to
        remember the random bill number at all."""
        os.makedirs("bills", exist_ok=True)
        target = self.search_bill.get().strip()
        if not target:
            messagebox.showerror("Error", "Enter a bill number, customer name, or phone number")
            return

        # 1) exact bill-number match
        exact_path = os.path.join("bills", f"{target}.txt")
        if os.path.isfile(exact_path):
            self._load_bill_file(target)
            return

        # 2) fall back to matching customer name / phone inside saved bills
        target_lower = target.lower()
        matches = []  # (bill_no, customer_name, phone, mtime)
        for fname in os.listdir("bills"):
            if not fname.endswith(".txt"):
                continue
            bill_no = os.path.splitext(fname)[0]
            path = os.path.join("bills", fname)
            cust_name, phone = "", ""
            with open(path, "r") as f1:
                content = f1.read()
                for line in content.splitlines():
                    if "CUSTOMER NAME" in line:
                        cust_name = line.split(":", 1)[1].strip()
                    elif "PHONE NUMBER" in line:
                        phone = line.split(":", 1)[1].strip()
            if target_lower in content.lower():
                matches.append((bill_no, cust_name, phone, os.path.getmtime(path)))

        if not matches:
            messagebox.showerror("Error", "No bill found matching that number, name, or phone")
            return

        if len(matches) == 1:
            self._load_bill_file(matches[0][0])
            return

        # multiple matches -> let the user pick one from a list
        self._show_bill_picker(matches, title=f"Bills matching '{target}'")

    def _show_bill_picker(self, entries, title="Saved Bills"):
        """entries: list of (bill_no, customer_name, phone, mtime), most
        recent first. Shows a pick-list; double-click loads that bill."""
        entries = sorted(entries, key=lambda e: e[3], reverse=True)

        win = Toplevel(self.root)
        win.title(title)
        win.geometry("560x420")

        Label(win, text=title, font="arial 13 bold").pack(pady=6)

        list_frame = Frame(win)
        list_frame.pack(fill=BOTH, expand=1, padx=8, pady=8)
        sb = Scrollbar(list_frame)
        sb.pack(side=RIGHT, fill=Y)
        lb = Listbox(list_frame, font="consolas 11", yscrollcommand=sb.set)
        lb.pack(fill=BOTH, expand=1)
        sb.config(command=lb.yview)

        for bill_no, cust_name, phone, mtime in entries:
            date_str = datetime.fromtimestamp(mtime).strftime("%d-%b-%Y %I:%M %p")
            lb.insert(END, f"Bill #{bill_no}   |   {cust_name:<20}   |   {phone:<12}   |   {date_str}")

        def load_selected(event=None):
            sel = lb.curselection()
            if not sel:
                return
            bill_no = entries[sel[0]][0]
            self._load_bill_file(bill_no)
            win.destroy()

        lb.bind("<Double-Button-1>", load_selected)
        Button(win, text="Open Selected Bill", bg="cadetblue", fg="white", font="arial 12 bold",
               command=load_selected).pack(pady=6)

    def view_all_bills(self):
        """Browse every saved bill without needing to know its number --
        sorted with the most recently saved bill first."""
        os.makedirs("bills", exist_ok=True)
        entries = []
        for fname in os.listdir("bills"):
            if not fname.endswith(".txt"):
                continue
            bill_no = os.path.splitext(fname)[0]
            path = os.path.join("bills", fname)
            cust_name, phone = "", ""
            with open(path, "r") as f1:
                for line in f1:
                    if "CUSTOMER NAME" in line:
                        cust_name = line.split(":", 1)[1].strip()
                    elif "PHONE NUMBER" in line:
                        phone = line.split(":", 1)[1].strip()
            entries.append((bill_no, cust_name, phone, os.path.getmtime(path)))

        if not entries:
            messagebox.showinfo("Bills", "No bills have been saved yet")
            return

        self._show_bill_picker(entries, title="All Saved Bills")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if not op:
            return

        # ==========Laptops============
        self.hp_l.set(0)
        self.Asus_l.set(0)
        self.lenovo_l.set(0)
        self.samsung_l.set(0)
        self.apple_l.set(0)
        self.jiobook_l.set(0)
        # ==========Phones============
        self.samsung_p.set(0)
        self.vivo_p.set(0)
        self.oneplus_p.set(0)
        self.realme_p.set(0)
        self.google_p.set(0)
        self.apple_p.set(0)
        # ===========LEDs=============
        self.croma_le.set(0)
        self.samsung_le.set(0)
        self.tcl_le.set(0)
        self.xiaomi_le.set(0)
        self.lg_le.set(0)
        self.sony_le.set(0)

        # ===========Total Product Price & Tax Variable==========
        self.laptops_price.set("")
        self.phones_price.set("")
        self.leds_price.set("")

        self.laptops_tax.set("")
        self.phones_tax.set("")
        self.leds_tax.set("")

        # ==========Customer===========
        self.c_name.set("")
        self.c_phno.set("")
        self.c_address.set("")

        self.bill_no.set(str(random.randint(1000, 9999)))
        self.search_bill.set("")

        self._reset_computed_totals()
        self.wellcome_bill()

    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = bill_app(root)
    root.mainloop()
