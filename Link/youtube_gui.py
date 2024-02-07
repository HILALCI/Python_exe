from tkinter import *
from tkinter import messagebox
import numpy as np
import pyperclip as pc


def kontrol():
    try:
        sureler = np.array(ent2.get().split(":")).astype(int)
        link = ent1.get().split("/")
        chk = ["https:", "youtu.be", "www.youtube.com"]
        chks = 0

        for linkpar in link:
            for chkp in chk:
                if linkpar == chkp:
                    chks += 1

        if sureler.dtype.kind == "i" and chks == 2:
            convert(ent2.get())

        else:
            messagebox.showwarning("Uyarı", "URL hatali girildi.")

    except ValueError:
        messagebox.showwarning("Uyarı", "Sure degeri hatali girildi.")


def convert(sure):
    if sure.count(":") == 2:
        h, m, s = sure.split(":")
        sec = int(h) * 3600 + int(m) * 60 + int(s)

    elif sure.count(":") == 1:
        m, s = sure.split(":")
        sec = int(m) * 60 + int(s)

    elif sure.count(":") == 0:
        sec = int(sure)

    url = ent1.get() + "&t=" + str(sec)

    pc.copy(url)

    messagebox.showinfo("URL", url + "\n\nLink kopyalandi.")


def basla():
    if ent1.get() == "" or ent2.get() == "":
        messagebox.showwarning("Uyarı", "Lütfen alanları boş bırakmayınız.")

    else:
        kontrol()


main = Tk()
main.title("Youtube Link Olusturma")
main.geometry("500x400")

main.resizable(True, True)
main.bind("<Escape>", lambda event: main.destroy())
main.bind("<Return>", lambda event: basla())

Label(main, text="Lütfen URL giriniz:").place(x=50, y=100)
Label(main, text="Lütfen süre giriniz:").place(x=50, y=200)

ent1 = Entry(main)
ent1.place(x=200, y=100)
ent2 = Entry(main)
ent2.place(x=200, y=200)


Button(
    main,
    text="Oluştur",
    padx=5,
    pady=5,
    bd=5,
    activebackground="yellow",
    relief=GROOVE,
    command=basla,
).place(x=250, y=250)

main.mainloop()
