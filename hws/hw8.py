# class Kategoriyayalar:
#     def __init__(self, salat, yemek, icki):
#         self.salat = salat
#         self.yemek = yemek
#         self.icki = icki
        
#     def exhibit(self):
#         print(self.salat)
#         print(self.yemek)
#         print(self.icki)
        
# class Menyu:
#     def __init__(self, cesidler):
#         self.cesidler = cesidler
        
#     def cesid_exhibit(self):
#         for index, cesid in enumerate(self.cesidler, start=1):
#             print(f"Cesid numayis olunur: {index}")


class Kategoriya:
    def __init__(self, ad, cesidler):
        self.ad = ad
        self.cesidler = cesidler

    def cesid_exhibit(self):
        for index, cesid in enumerate(self.cesidler, start=1):
            print(f"{index}. {cesid['ad']} - {cesid['qiymet']} AZN")

class Menu:
    def __init__(self):
        self.kategoriyalar = {
            "salat": Kategoriya("salat", [
                {"ad": "Paytaxt salati", "qiymet": 15},
                {"ad": "Mimoza salati", "qiymet": 18},
                {"ad": "Suba salati", "qiymet": 20}
            ]),
            "Yemek": Kategoriya("Yemek", [
                {"ad": "Kotlet", "qiymet": 25},
                {"ad": "Toyuq sis", "qiymet": 22},
                {"ad": "Xussusi soslu Makaron", "qiymet": 20}
            ]),
            "İçki": Kategoriya("İçki", [
                {"ad": "Meyve Suyu", "qiymet": 8},
                {"ad": "Lionad", "qiymet": 5},
                {"ad": "Mojito", "qiymet": 12}
            ])
        }

    def kategoriya_sec(self):
        print("Kategoriyalar:")
        for index, kategoriya in enumerate(self.kategoriyalar, start=1):
            print(f"{index}. {kategoriya}")
        secim = input("Zehmet olmasa bir kategoriya seçin (Bitirmek ucun 'Finish' yazin): ")
        return secim

    def menyu_goster(self, kategoriya):
        if kategoriya in self.kategoriyalar:
            self.kategoriyalar[kategoriya].cesid_exhibit()
        else:
            print("Geçersiz kategoriya!")

    def sifaris_gotur(self):
        toplam_mebleg = 0
        report={}
        while True:
            secilen_kategoriya = self.kategoriya_sec()
            if secilen_kategoriya == 'Finish':
                break
            else:
                self.menyu_goster(secilen_kategoriya)
                secilen_yemek = int(input("Zehmet olmasa bir yemek nomresi seçin ve ya '0' yazaraq bitirin: "))
                if secilen_yemek == 0:
                    continue
                elif secilen_yemek <= len(self.kategoriyalar[secilen_kategoriya].cesidler):  
                    secilen_yemek=secilen_yemek-1
                    qiymet = self.kategoriyalar[secilen_kategoriya].cesidler[secilen_yemek]['qiymet']
                    yemek_adi = self.kategoriyalar[secilen_kategoriya].cesidler[secilen_yemek]['ad']
                    report[yemek_adi]=qiymet
                    print(f"{yemek_adi} seçildi. qiymeti: {qiymet} AZN")
                    toplam_mebleg += qiymet
                else:
                    print("Olmayan yemek nomresi!")
        print(f"Sizin cekiniz:",report)
        print(f"Sifarişinizin toplam miqdari: {toplam_mebleg} AZN")

# Menynu hazirdir
menu = Menu()
menu.sifaris_gotur()


       
        