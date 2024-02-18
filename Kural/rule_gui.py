from tkinter import *
from tkinter import messagebox


def hesap():
    if ent1.get().isnumeric() and int(ent1.get()) > 0:
        bilgi = f"Temel ihtiyac(x%50)= {int(ent1.get()) * 0.5}\nTasarruf(x%20)= {int(ent1.get()) * 0.2}\nIstekler(x%30)= {int(ent1.get()) * 0.3}"

        messagebox.showinfo("Bilgi", bilgi)

        ent1.delete(0, "end")

    else:
        messagebox.showwarning("Uyarı", "Gelir degeri hatali girildi.")
        ent1.delete(0, "end")


main = Tk()
main.title("50-20-30 Kurali")
main.geometry("500x400")

main.resizable(True, True)
main.bind("<Escape>", lambda event: main.destroy())
main.bind("<Return>", lambda event: hesap())

Label(main, text="Lütfen net gelirinizi giriniz:").place(x=50, y=100)

ent1 = Entry(main)
ent1.place(x=250, y=100)

Button(
    main,
    text="Hesapla",
    padx=5,
    pady=5,
    bd=5,
    activebackground="yellow",
    relief=GROOVE,
    command=hesap,
).place(x=340, y=150)

main.mainloop()
