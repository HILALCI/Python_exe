while True:
    print(
        "     ========================\n     50-20-30 Kurali\n     ========================"
    )
    netGeliriniz = float(input("Net Gelirinizi Giriniz: "))
    if netGeliriniz < 0:
        break
    need50 = float(float(netGeliriniz * 50) / 100)
    save20 = float(float(netGeliriniz * 20) / 100)
    want30 = float(float(netGeliriniz * 30) / 100)
    print("\n€£€£€£€£€£€£€£€£€£€£€£€£€£€£€£€\n")
    print("Temel ihtiyac(x%50)= {}\n".format(need50))
    print("Tasarruf(x%20)= {}\n".format(save20))
    print("Istekler(x%30)= {}\n".format(want30))
    print("\n€£€£€£€£€£€£€£€£€£€£€£€£€£€£€£€\n")
