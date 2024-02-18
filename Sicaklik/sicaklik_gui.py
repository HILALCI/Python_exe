from tkinter import *
from tkinter import messagebox


def cevir():
    if ent1.get().isnumeric():
        if label_option.get() == "°K":
            messagebox.showinfo(
                "Bilgi", f"{int(ent1.get())} °C = {int(ent1.get()) + 273.15} °K"
            )

        elif label_option.get() == "°F":
            messagebox.showinfo(
                "Bilgi", f"{int(ent1.get())} °C = {(int(ent1.get()) * 9/5) + 32} °F"
            )

        else:
            messagebox.showwarning(
                "Uyarı", "Secim yapilmamistir lutfen bir birim seciniz."
            )

    else:
        messagebox.showwarning("Uyarı", "°C degeri hatali girildi.")
        ent1.delete(0, "end")


main = Tk()
main.title("Sicaklik Birim Donusturme")
main.geometry("500x400")

main.resizable(True, True)
main.bind("<Escape>", lambda event: main.destroy())
main.bind("<Return>", lambda event: cevir())

Label(main, text="Lütfen °C degerini giriniz:").place(x=50, y=100)

ent1 = Entry(main)
ent1.place(x=250, y=100)

label_option = StringVar(main)
label_open_menu = OptionMenu(main, label_option, "°K", "°F").place(x=250, y=150)

Button(
    main,
    text="Donustur",
    padx=5,
    pady=5,
    bd=5,
    activebackground="yellow",
    relief=GROOVE,
    command=cevir,
).place(x=330, y=150)

main.mainloop()
