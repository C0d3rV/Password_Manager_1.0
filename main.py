from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(*args):
    with open("saved_passwords.txt", "a") as file:
        file.write(f"{web_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
        web_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website = Label(text="Website:", bg="white", highlightthickness=0)
web_entry = Entry(width=35)
website.grid(row=1, column=0)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email = Label(text="Email/Username:", bg="white", highlightthickness=0)
email_entry = Entry(width=35)
email_entry.insert(0, "vasuthec0der@gmail.com")
email.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2)

password = Label(text="Password:", bg="white", highlightthickness=0)
password_entry = Entry(width=35, show="*")
password.grid(row=3, column=0)
password_entry.grid(row=3, column=1, columnspan=2)
gen_pass = Button(text="Generate Password", width=15, bg="white", fg="black")
gen_pass.grid(row=3, column=2)

add_pass = Button(text="Add", width=30, bg="white", fg="black", command=save)
add_pass.grid(row=4, column=1, columnspan=2)

window.mainloop()