import pyshorteners
import tkinter as tk

def store_input():
    global url
    global short_url
    url = input_entry.get()
    short_url = s.tinyurl.short(url)
    label1.pack()
    label2 = tk.Label(window, text=short_url)  
    label2.pack()


s = pyshorteners.Shortener()

window=tk.Tk()
window.title("URL Shortner")
window.geometry('500x200')
window.configure(bg="#FD3A54")

label=tk.Label(text='Enter URL')
label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

submit_button = tk.Button(window, text="Submit", command=store_input)
submit_button.pack()

label1=tk.Label(window,text="Shortened URL :")
window.mainloop()
