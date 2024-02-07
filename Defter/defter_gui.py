from tkinter import *
from tkinter import messagebox


def azalt():
    global tane
    tane -= 1
    if tane == 0:
        bilgi = f"""1-{bitis} nolu defter istenilen kadar yazdırılmıştır.\nYazdırma işlemi bitmiştir."""

        messagebox.showinfo("Bitti", bilgi)
        ent1.delete(0, "end")
        ent2.delete(0, "end")

    elif tane < 0:
        messagebox.showwarning("Fazla", "Defter fazladan yazdırılmıştır.")


def yaz():
    if tane > 0:
        kalan = f"1-{bitis} nolu defterden {tane} tane daha yazdırılmalıdır."
        messagebox.showinfo("Kalan", kalan)

    elif tane < 0:
        kalan = f"Defterden {tane} tane fazladan yazdırılmıştır."
        messagebox.showinfo("Fazla", kalan)

    else:
        messagebox.showinfo("Bitti", "Defter istenilen kadar yazdırılmıştır.")


def basla():
    global tane
    global bitis

    if ent1.get() == "" or ent2.get() == "":
        messagebox.showwarning("Uyarı", "Lütfen alanları boş bırakmayınız.")

    elif not (ent1.get().isnumeric()) or not (ent2.get().isnumeric()):
        messagebox.showwarning("Uyarı", "Lütfen sadece sayısal değer giriniz.")

    elif tane > 0:
        rsp = messagebox.askokcancel("Dikkat", "Değerleri değiştirmek ister misiniz?")

        if rsp == True:
            bitis = int(ent1.get())
            tane = int(ent2.get())

    else:
        bitis = int(ent1.get())
        tane = int(ent2.get())

        Button(
            main,
            text="Eksikler",
            padx=5,
            pady=5,
            bd=5,
            activebackground="blue",
            relief=GROOVE,
            command=yaz,
        ).place(x=300, y=250)
        Button(
            main,
            text="Yazıldı",
            padx=5,
            pady=5,
            bd=5,
            activebackground="green",
            relief=GROOVE,
            command=azalt,
        ).place(x=50, y=250)


main = Tk()
main.title("Defter Sayaci")
main.geometry("600x400")

main.resizable(True, True)
main.bind("<Escape>", lambda event: main.destroy())
main.bind("<Return>", lambda event: basla())
main.bind("<Control_L>", lambda event: azalt())

Label(main, text="Lütfen bitiş değirini giriniz:").place(x=50, y=100)
Label(main, text="Lütfen kaç tane olduğunu giriniz:").place(x=50, y=200)
ent1 = Entry(main)
ent1.place(x=300, y=100)
ent2 = Entry(main)
ent2.place(x=300, y=200)

tane = 0

Button(
    main,
    text="Başla",
    padx=5,
    pady=5,
    bd=5,
    activebackground="yellow",
    relief=GROOVE,
    command=basla,
).place(x=400, y=250)

main.mainloop()
