from tkinter import *
from tkinter import messagebox
import pyshorteners
import clipboard
import threading
import requests
from PIL import Image, ImageTk
import threading


'''
Made by:- Prathamesh Dhande
Version : 1.0
Since :-26/03/2022
if you get any error contact email me on prathameshdhande534@gmail.com
Distributed by: prathameshcode.blogspot.com
'''


class Url(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap("urllogo.ico")
        self.title("URL Shortener")
        self.geometry("500x400")
        self.resizable(False, False)
        self.configure(bg="white")

    # creates the gui of the window
    def gui(self):
        self.label = Label(self, text="URL SHORTENER", font=[
                           "segoe UI Black", "30"], bg='white')
        self.label.pack(side="top", anchor="n")

        self.label1 = Label(self, text="Enter The Link :", font=[
                            "Times New Roman", "14", "bold"], bg="white", fg="red")
        self.label1.place(x=7, y=70)

        # takes the link from the user
        self.inputfield = StringVar()
        self.input = Entry(self, font="Calibri 13", relief="solid",
                           width=53, textvariable=self.inputfield)
        self.input.focus()
        self.input.place(x=7, y=95)

        # sets the output of the link
        self.generated_link = StringVar(value="Link Will be Generated Here")
        self.output = Entry(self, textvariable=self.generated_link,
                            font="Calibri 13", relief="solid", width=53, justify="left")
        self.output.focus()
        self.output.place(x=7, y=170)

        # this button copys the output text in the clipboard
        self.copy_link = Button(text="Copy", font="Corbel 12 bold", width=10, bg="light blue",
                                relief="ridge", borderwidth=2, command=self.copy_to_clipboard)
        self.copy_link.place(x=7, y=200)
        self.copy_link['state'] = "disabled"

        # button for shorting the url
        Button(text="Convert", font=("Calibri Light", "12", "bold"), width=10, padx=3, pady=3,
               relief="raised", bd=3, bg="Light green", command=self.threa).place(x=10, y=250)

        # exits the window
        Button(text="Exit", font=("Calibri light", "12", "bold"), width=8, padx=3, pady=3,
               relief="raised", bd=3, bg="light blue", command=self.destroy).place(x=211, y=250)

        # get the url short
        self.option = ["Tinyurl", "Cuttly",
                       "Bitly", "Chilpit", "Clckru", "Dagd"]
        self.selected_opt = StringVar()
        self.selected_opt.set("Tinyurl")
        self.dropdown = OptionMenu(self, self.selected_opt, *self.option)
        self.dropdown.place(x=4, y=133)

        self.label2 = Label(
            text="Select the Shortening Url Domain", font="calibri 10 bold")
        self.label2.place(x=90, y=137)

        # button for clearing the input field
        Button(text="Clear", font=("Calibri light", "12", "bold"), width=8, padx=3, pady=3,
               relief="raised", bd=3, bg="Orange", command=self.clear).place(x=120, y=250)

        self.label3 = Label(text="Developed By Prathamesh Dhande",
                            font="arial 9 bold", bg="white")
        self.label3.place(x=300, y=378)

        # setting the button for dark and light theme
        self.lt = Image.open("light.png")  # setting the light theme
        self.resized_image = self.lt.resize(size=(60, 30))
        self.add_image = ImageTk.PhotoImage(self.resized_image)
        self.count = 0

        self.theme_change = Button(
            image=self.add_image, bg='white', relief="flat", command=self.theme)
        self.theme_change.place(x=430, y=5)

    def generate(self):
        if self.input.get() == "":
            messagebox.showerror("Error", "Please Enter the Url")
        else:
            if self.selected_opt.get() == "Tinyurl":
                try:
                    s = pyshorteners.Shortener().tinyurl.short(self.input.get())
                    self.generated_link.set(s)
                    self.copy_link["state"] = "normal"
                except pyshorteners.exceptions.ShorteningErrorException:
                    messagebox.showerror("Error", "Enter the Valid URL")
                except requests.exceptions.ConnectionError:
                    messagebox.showwarning(
                        'Network Error', "Please Connect to the Internet")
                except Exception:
                    messagebox.showinfo("Try Again", "Try again")

            elif self.selected_opt.get() == "Cuttly":
                try:
                    s = pyshorteners.Shortener(
                        api_key="49e25c5c38bf90484e469643fb200f7549820").cuttly.short(self.input.get())
                    self.generated_link.set(s)
                    self.copy_link["state"] = "normal"
                except requests.exceptions.ConnectionError:
                    messagebox.showwarning(
                        'Network Error', "Please Connect to the Internet")
                except pyshorteners.exceptions.ShorteningErrorException:
                    messagebox.showerror("Error", "Enter the Valid URL")
                except pyshorteners.exceptions.BadAPIResponseException:
                    messagebox.showinfo("Error", "Some Error Occurred")
                except Exception:
                    messagebox.showinfo("Try Again", "Try Again")

            elif self.selected_opt.get() == "Bitly":
                try:
                    s = pyshorteners.Shortener(
                        api_key="ed152315eacaf661e193ce3005cab32a2955bd19").bitly.short(self.input.get())
                    self.generated_link.set(s)
                    self.copy_link["state"] = "normal"
                except requests.exceptions.ConnectionError:
                    messagebox.showwarning(
                        'Network Error', "Please Connect to the Internet")
                except pyshorteners.exceptions.BadAPIResponseException:
                    messagebox.showinfo("Error", "Some Error Occurred")
                except pyshorteners.exceptions.ShorteningErrorException:
                    messagebox.showerror("Error", "Enter the Valid URL")
                except Exception:
                    messagebox.showinfo("Try Again", "Try Again")

            elif self.selected_opt.get() == "Chilpit":
                try:
                    s = pyshorteners.Shortener().chilpit.short(self.input.get())
                    self.generated_link.set(s)
                    self.copy_link["state"] = "normal"
                except requests.exceptions.ConnectionError:
                    messagebox.showwarning(
                        'Network Error', "Please Connect to the Internet")
                except pyshorteners.exceptions.ShorteningErrorException:
                    messagebox.showerror("Error", "Enter the Valid URL")
                except Exception:
                    messagebox.showinfo("Try Again", "Try Again")

            elif self.selected_opt.get() == "Clckru":
                try:
                    s = pyshorteners.Shortener().clckru.short(self.input.get())
                    self.generated_link.set(s)
                    self.copy_link["state"] = "normal"
                except pyshorteners.exceptions.ShorteningErrorException:
                    messagebox.showerror("Error", "Enter the Valid URL")
                except requests.exceptions.ConnectionError:
                    messagebox.showwarning(
                        'Network Error', "Please Connect to the Internet")
                except Exception:
                    messagebox.showinfo("Try Again", "Try again")

            elif self.selected_opt.get() == "Dagd":
                try:
                    s = pyshorteners.Shortener().dagd.short(self.input.get())
                    self.generated_link.set(s)
                    self.copy_link["state"] = "normal"
                except pyshorteners.exceptions.ShorteningErrorException:
                    messagebox.showerror("Error", "Enter the Valid URL")
                except requests.exceptions.ConnectionError:
                    messagebox.showwarning(
                        'Network Error', "Please Connect to the Internet")
                except Exception:
                    messagebox.showinfo("Try Again", "Try again")

    def copy_to_clipboard(self):
        clipboard.copy(self.generated_link.get())

    def clear(self):
        self.inputfield.set("")
        self.generated_link.set("Link Will be Generated Here")
        self.copy_link["state"] = "disabled"

    def theme(self):

        self.count += 1

        if self.count == 1:
            self.lt = Image.open("dark.png")  # setting the light theme
            self.resized_image = self.lt.resize(size=(60, 30))
            self.add_image = ImageTk.PhotoImage(self.resized_image)
            self.theme_change.config(image=self.add_image)
            self.dark()
            self.count = 1

        elif self.count == 2:
            self.lt = Image.open("light.png")  # setting the light theme
            self.resized_image = self.lt.resize(size=(60, 30))
            self.add_image = ImageTk.PhotoImage(self.resized_image)
            self.theme_change.config(image=self.add_image)
            self.light()
            self.count = 0

    def dark(self):
        self.config(bg="black")
        self.label.config(bg='black', fg='white')
        self.theme_change.config(bg='black')
        self.label1.config(bg='black', fg='white')
        self.label2.config(bg='black', fg='white')
        self.label3.config(bg='black', fg='white')

    def light(self):
        self.config(bg="white")
        self.label.config(fg='black', bg='white')
        self.theme_change.config(bg='white')
        self.label1.config(fg='black', bg='white')
        self.label2.config(fg='black', bg='white')
        self.label3.config(fg='black', bg='white')

    def threa(self):
        threading.Thread(target=self.generate).start()


if __name__ == "__main__":
    ur = Url()
    t1 = threading.Thread(target=ur.gui)
    t1.start()

    ur.mainloop()
