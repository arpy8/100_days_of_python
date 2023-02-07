from tkinter import *
from tkinter import messagebox
from random import *
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10) )]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    pswrd_entry.insert(0, password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    email = email_entry.get()
    pswrd = pswrd_entry.get()
    website = website_entry.get()
    new_data = {website : {"email":email, "password" : pswrd}}
    
    if len(email) == 0 or len(pswrd) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        try:
            with open("Day-30\Password Manager\data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("Day-30\Password Manager\data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("Day-30\Password Manager\data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
                website_entry.delete(0, END)
                pswrd_entry.delete(0,END)

# ---------------------------- FINDING PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("Day-30\Password Manager\data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="error", message= "no data file found.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message= f"email : {email}\npassword : {password}")
        else:
            messagebox.showinfo(title="error", message= f"no details for {website} exists.")
               
    # except KeyError:

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)
root.resizable(False,False)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file = "C:/Users/asus/Desktop/repos/100_days_of_python/Day-29/logo.png")
canvas.create_image(120,90,image = logo_img)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
pswrd_label = Label(text="Password:")
pswrd_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(row=1,column=1)
email_entry = Entry(width=53)
email_entry.insert(0, "arpitsengar99@gmail.com")
email_entry.grid(row=2,column=1, columnspan=2)
pswrd_entry = Entry(width=34)
pswrd_entry.grid(row=3,column=1, sticky="nsew")

#Buttons
search_button = Button(text = "Search", relief=RAISED, command=find_password, borderwidth=0.5)
search_button.grid(row=1,column=2, sticky="nsew")
generate_button = Button(text = "Generate Password", relief=RAISED, command=password_generator, borderwidth=0.5)
generate_button.grid(row=3,column=2, sticky="nsew")
add_button = Button(text = "Add", width=45, relief=RAISED, command=save, borderwidth=0.5)
add_button.grid(row=4,column=1, columnspan=2)
root.mainloop() 