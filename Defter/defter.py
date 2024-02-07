def azalt():
    global tane
    tane -= 1
    if tane == 0:
        print(f"1-{bitis} nolu defter istenilen kadar yazdırılmıştır.")
        print("Yazdırma işlemi bitmiştir.")
        print("..........SON..........")


def yaz():
    print(f"1-{bitis} nolu defterden {tane} tane daha yazdırılmalıdır.")


print("..........BAŞLA..........")
bitis = int(input("Lütfen bitiş değirini giriniz: "))
tane = int(input("Lütfen kaç tane olduğunu giriniz: "))
