# Not like anyone would but DO NOT USE THIS FOR ANYTHING BUT TESTING
# NO INFORMATION IS SAVED
# PUBLIC IP IS ONLY SHOWN LOCALLY

from tkinter import Tk, Toplevel, Label, Entry, Button, Menu, Canvas, messagebox
from urllib.request import urlopen
import re

def close_win(window):
    window.destroy()

def show_thanks_window(previous_window):
    previous_window.destroy()
    try:
        ip = urlopen('https://api.ipify.org').read().decode('utf8')
    except:
        ip = "Unable to fetch IP"

    thanks_window = Toplevel()
    thanks_window.title("Thank You!")
    thanks_window.geometry("350x150")
    thanks_window.configure(bg="#f4f4f4")

    Label(thanks_window, text="Thanks for the details!", font=('Segoe UI', 14, 'bold'), bg="#f4f4f4").pack(pady=10)
    Label(thanks_window, text=f"Your IP: {ip}", font=('Segoe UI', 12), bg="#f4f4f4").pack(pady=5)
    Button(thanks_window, text="Close", font=('Segoe UI', 10), command=thanks_window.destroy).pack(pady=10)

def chb(window):
    new_window = Toplevel(window)
    new_window.title("FREE $500 GIFTCARD!")
    new_window.geometry("400x300")
    new_window.configure(bg="#f9f9f9")

    Canvas(new_window, width=400, height=20, bg="#f9f9f9", highlightthickness=0).pack()

    Label(new_window, text="Claim Your Giftcard!", font=('Segoe UI', 12, 'bold'), bg="#f9f9f9").pack(pady=5)

    Label(new_window, text="Email:", bg="#f9f9f9", anchor='w').pack(pady=3)
    email_entry = Entry(new_window, bd=2, width=30)
    email_entry.pack()

    Label(new_window, text="Postcode:", bg="#f9f9f9", anchor='w').pack(pady=3)
    postcode_entry = Entry(new_window, bd=2, width=30)
    postcode_entry.pack()

    Label(new_window, text="Password:", bg="#f9f9f9", anchor='w').pack(pady=3)
    password_entry = Entry(new_window, bd=2, width=30, show="*")
    password_entry.pack()

    def validate_and_submit():
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email_entry.get()):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return
        show_thanks_window(new_window)

    Button(new_window, text="Submit", font=('Segoe UI', 10), command=validate_and_submit).pack(pady=15)

MMapp = Tk()
MMapp.geometry("600x200")
MMapp.title("FREE $500 GIFTCARD")
MMapp.configure(bg="#ffffff")

menubar = Menu(MMapp)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Close", command=lambda: close_win(MMapp))
MMapp.config(menu=menubar)

Label(MMapp, text="FREE $500 GIFTCARD!", font=('Segoe UI', 24, 'bold'), bg="#ffffff").pack(pady=10)
Label(MMapp, text="Click the button below to claim", font=('Segoe UI', 12), bg="#ffffff").pack(pady=5)
Button(MMapp, text="CLICK HERE", font=('Segoe UI', 11), command=lambda: chb(MMapp)).pack(pady=10)

MMapp.mainloop()
