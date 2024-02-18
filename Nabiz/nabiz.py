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
age = int(input("Please enter age : "))
maxHeartRate = 220 - age
print("MAX Heart Rate = ", maxHeartRate)
print(
    "Yeni baslayanlar icin %50 = {} kademeli olarak arttirilip %70-%80 araligan gelinmelidir.".format(
        maxHeartRate * 0.5
    )
)
print(
    "Orta yogunluk icin %60 = {} ile %75 = {} arasinda olmalidir.".format(
        maxHeartRate * 0.6, maxHeartRate * 0.75
    )
)
print(
    "Harbi Egzersiz icin %75 = {} ile %80 = {} arasinda olmalidir.".format(
        maxHeartRate * 0.75, maxHeartRate * 0.8
    )
)
