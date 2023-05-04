from PIL import Image, ImageTk
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import PySimpleGUI as sg


def browse_wm_image():
    sg.theme("DarkBrown2")
    layout = [[sg.T("")],
              [sg.Text("Browse the watermark image"), sg.Input(key="-IN2-", change_submits=True), sg.FileBrowse(key="-IN-")],
              [sg.Button("Submit")]]

    window = sg.Window('Watermark image browser', layout, size=(600, 150))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Submit":
            window.close()
            return values["-IN-"]


def open_file():
    browse_text.set("Loading...")
    photo_name = askopenfilename(title="Select A File", filetype=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    if photo_name:
        image = Image.open(photo_name).convert("RGBA")
        wm_image = Image.open(browse_wm_image()).convert("RGBA")

        # Size watermark relative to size of base image
        wm_resized = wm_image.resize((round(image.size[0] * .35), round(image.size[1] * .35)))
        wm_mask = wm_resized.convert("RGBA")

        # Set position to lower right corner
        position = (image.size[0] - wm_resized.size[0], image.size[1] - wm_resized.size[1])

        transparent = Image.new('RGBA', image.size, (0, 0, 0, 0))
        transparent.paste(image, (0, 0))
        transparent.paste(wm_mask, position, mask=wm_mask)
        transparent.show()


        # Save watermarked photo
        finished_img = transparent.convert("RGB")
        finished_img_name = photo_name[:-4] + "_watermarked.jpg"
        finished_img.save(finished_img_name)

        messagebox.showinfo("Success!", f"File saved:\n{finished_img_name}.")

        browse_text.set("Browse")


def quit_app():
    root.destroy()


# GUI
root = tk.Tk()
root.title("iWatermark")
root.geometry("700x400")
root.resizable(False, False)
root.configure(bg="#280001")

canvas = tk.Canvas(root, width=650, height=540)
canvas.configure(bg="#280001", highlightthickness=0, borderwidth=0)
canvas.grid(columnspan=5, rowspan=4)

logo = Image.open("assets/logo.png")
logo = logo.resize((500, 130))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, borderwidth=0, highlightthickness=0)
logo_label.image = logo
logo_label.grid(column=2, row=0, columnspan=2)

# Browse dialog button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, command=open_file, textvariable=browse_text, font="Ariel", bg="#DAAD28", fg="#280001",
                       height=2, width=19)
browse_text.set("Browse")
browse_btn.grid(column=2, row=1)

# Cancel Button
cancel_btn = tk.Button(root, text="Quit", command=quit_app, font="Ariel", bg="#DAAD28", fg="#280001", height=2, width=19)
cancel_btn.grid(column=3, row=1, padx=10)

root.mainloop()
