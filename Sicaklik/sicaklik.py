while True:
    a=float(input("°C Girin="))
    b=int(input("K icin 1 ,°F icin 2 ,Çıkmak için 3 Girin="))
    if b==1:
        c=a+273.15   #(0°C + 273.15 formülüdür.
        print("{} °C --> {} °K" .format(a,c))
    elif b==2:
        d=(a*9/5)+32  #(0°C × 9/5) + 32 formülüdür.
        print("{} °C --> {} °F " .format(a,d))
    elif b==3:
        break
    else:
        print("Yanliş girdi")
