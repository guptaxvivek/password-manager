import tkinter as tk
from tkinter import messagebox
import random
import json

WHITE = "#FFFFFF"
EMAIl = "ENTER YOUR EMAIL"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_random_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(5, 7)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for sym in range(nr_symbols)]
    password_list += [random.choice(numbers) for num in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    pwd.delete(0, tk.END)
    pwd.insert(0, f"{password}")
    pwd.clipboard_clear()
    pwd.clipboard_append(password)

# ---------------------------- SAVED PASSWORDS ------------------------------ #
def find_password():
    website = web.get().capitalize()
    try:
        data_file = open("data.json", "r")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        data = json.load(data_file)
        try:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']} \nPassword: {data[website]['password']}")
        except KeyError:
            messagebox.showerror(title="Oops", message="No saved Data Found!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web.get().capitalize()
    email = em.get()
    password = pwd.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) > 0 and len(email) > 0 and len(password) > 0:
        is_ok = messagebox.askokcancel(title=f"{website}",
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: {password} "
                                               f"\nIs that correct?")
        if is_ok:
            try:
                data_file = open("data.json", "r")
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data = json.load(data_file)
                data.update(new_data)
                with open("data.json","w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                web.delete(0, tk.END)
                pwd.delete(0, tk.END)
    else:
        messagebox.showwarning(title="Oops", message="Please Don't Leave any empty fields")


# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("Password Manager")
image = tk.PhotoImage(file="logo.png")
root.config(bg=WHITE, padx=50, pady=50)
canvas = tk.Canvas(height=200, width=200, bg=WHITE, highlightthickness=0)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)
w = tk.Label(text="Website: ", bg=WHITE)
w.grid(row=1, column=0)
e = tk.Label(text="Email/Username: ", bg=WHITE)
e.grid(row=2, column=0)
p = tk.Label(text="Password: ", bg=WHITE)
p.grid(row=3, column=0)
web = tk.Entry(width=17)
web.grid(column=1, row=1)
search_btn = tk.Button(text="Search", width=14, relief="groove",bg=WHITE,command=find_password)
search_btn.grid(column=2,row=1)
web.focus()
em = tk.Entry(width=35)
em.grid(column=1, row=2, columnspan=2)
em.insert(0, EMAIl)
pwd = tk.Entry(width=17)
pwd.grid(column=1, row=3)
gen_pwd_btn = tk.Button(text="Generate Password", relief="groove", bg="white", command=gen_random_pwd)
gen_pwd_btn.grid(column=2, row=3)
add_btn = tk.Button(text="Add", width=30, relief="groove", bg=WHITE, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

root.mainloop()
