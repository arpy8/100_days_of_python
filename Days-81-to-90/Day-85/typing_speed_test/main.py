import tkinter as tk
from tkinter import messagebox


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Typing Test")
        self.geometry("300x172")
        self.configure(bg="#FF847C")
        self.create_widgets()
        self.timer_count = 31
        self.resizable(False, False)

    def create_widgets(self):
        self.create_timer()
        self.create_textbox()

    def create_timer(self):
        timer_label = tk.Label(text="Timer: ", bg="#FF847C", fg="#45171D")
        timer_label.grid(row=0, column=0)
        self.timer = tk.Label(text="", fg="#45171D", bg="#FF847C")
        self.timer.grid(row=0, column=1, padx=5, pady=5)

        self.start_btn = tk.Button(text="Start!", command=self.start_timer, width=17, padx=5, bg="#E84A5F", fg="#45171D")
        self.start_btn.grid(row=2, column=0)

        self.quit_btn = tk.Button(text="Quit!", command=self.quit_app, width=17, padx=5, bg="#E84A5F", fg="#45171D")
        self.quit_btn.grid(row=2, column=1, pady=7)

    def quit_app(self):
        app.destroy()

    def create_textbox(self):
        self.textbox = tk.Text(width=35, height=5, bg="#FECEA8", fg="#45171D", highlightthickness=0, borderwidth=1)
        self.textbox['state'] = 'disabled'
        self.textbox.grid(row=1, column=0, columnspan=4, padx=7, pady=7)

    def start_timer(self):
        self.start_btn["state"] = "disabled"
        self.textbox['state'] = 'normal'
        self.after(1000, self.update_timer)

    def update_timer(self):
        if self.timer_count != 0:
            self.after(1000, self.start_timer)
            self.timer_count -= 1
            self.timer.configure(text=self.timer_count)
        else:
            self.start_btn["state"] = "normal"
            self.reset_timer()
            self.get_info()

    def get_info(self):
        text_input = self.textbox.get("1.0", 'end-1c')
        words = text_input.split(" ")
        chars = "".join(words)
        self.calculate_wpm(len(chars))

    def calculate_wpm(self, number_of_chars):
        words_per_minute = round(number_of_chars/10)
        self.delete_text_field()
        self.display_wpm(words_per_minute)

    def delete_text_field(self):
        self.textbox.delete("1.0", "end")
        self.textbox['state'] = 'disabled'

    def display_wpm(self, wpm):
        messagebox.showinfo("WPM Score", f"Words per minute: {wpm}")

    def reset_timer(self):
        self.timer_count = 60


app = App()
app.mainloop()
