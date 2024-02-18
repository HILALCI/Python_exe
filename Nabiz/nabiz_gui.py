"""
        Heart Rate  Calculate

Source
    1-) https://www.health.harvard.edu/heart-health/hows-your-heart-rate-and-why-it-matters
    2-) https://www.health.harvard.edu/staying-healthy/feel-the-beat-of-heart-rate-training
    3-) https://www.health.harvard.edu/heart-health/what-your-heart-rate-is-telling-you
    4-) https://www.health.harvard.edu/blog/your-resting-heart-rate-can-reflect-your-current-and-future-health-201606172482

Not : 4. kaynagimizi ek saglik kontrolu icin eklenmistir.Dinlenme durumundaki kalp atis hizini kapsadigi icin projeye eklenmemistir.
Not : %80 uzerindeki durumlar icin makale henuz bulamadigim icin eklenmemistir.Simdilik sagliginiz icin cok yuksek degerlere cikilmamasi onerilir. 
"""

from tkinter import *
from tkinter import messagebox


def heart_rate():
    if ent1.get().isnumeric() and int(ent1.get()) > 0:
        ratep50 = (220 - int(ent1.get())) * 0.5
        ratep60 = (220 - int(ent1.get())) * 0.6
        ratep75 = (220 - int(ent1.get())) * 0.75
        ratep80 = (220 - int(ent1.get())) * 0.8

        bilgi = f"""MAX Nabiz = {220 - int(ent1.get())}
        Yeni baslayanlar icin %50 = {ratep50} kademeli olarak arttirilip %70-%80 araligan gelinmelidir.
        Orta yogunluk icin %60 - %75 = {ratep60} - {ratep75} arasinda olmalidir.
        Harbi Egzersiz icin %75 - %80 = {ratep75} - {ratep80} arasinda olmalidir.
        """

        messagebox.showinfo("Bilgi", bilgi)

        ent1.delete(0, "end")

    else:
        messagebox.showwarning("Uyarı", "Yas degeri hatali girildi.")
        ent1.delete(0, "end")


main = Tk()
main.title("Nabiz Araligi Hesaplama")
main.geometry("500x400")

main.resizable(True, True)
main.bind("<Escape>", lambda event: main.destroy())
main.bind("<Return>", lambda event: heart_rate())

Label(main, text="Lütfen yaşınızı giriniz:").place(x=50, y=100)

ent1 = Entry(main)
ent1.place(x=200, y=100)

Button(
    main,
    text="Hesapla",
    padx=5,
    pady=5,
    bd=5,
    activebackground="yellow",
    relief=GROOVE,
    command=heart_rate,
).place(x=290, y=150)

main.mainloop()
