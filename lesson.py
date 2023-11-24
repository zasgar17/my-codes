# def sort_list(*list_a):
#     list_a=list(list_a)
#     for a in list_a:
#         for i in range(len(list_a)-1):
#             if list_a[i]>list_a[i+1]:
#                 list_a[i], list_a[i+1]=list_a[i+1],list_a[i]
#     print(list_a)
# # list_a=[5,1,9,3,6,2]
# # sort_list(list_a)
# list_b=[3,2,7,5,8,9,0]
# sort_list(list_b)
# sort_list(1,5,2,8,3,0,4)

# list_c=[3,4,5]
# a,b,c=list_c

# class menyu:
#     def __init__(self, yem_1, qiym_1, yem_2, qiym_2):
#         self.yem_1 = yem_1
#         self.qiym_1 = qiym_1
#         self.yem_2 = yem_2
#         self.qiym_2 = qiym_2
    
#     def exhibit(self):
#         print(self.yem_1+ ":",self.qiym_1)
#         print(self.yem_2+ ":",self.qiym_2)
        
# menyu_1=menyu("duyu", 10, "toyuq", 18)
# menyu_1.exhibit()
# menyu_1.yem_1="qarabasaq"
# menyu_1.qiym_1=7
# menyu_1.exhibit()

# 1)bir menyu var, menyuda 3 kateqoriya var,yemekler, ickiler, salatlar. Her kateqoriyada 3 secim var, her secimin muxtelif qiymetleri var.
# run edende butun menyu ekranda gorsensin ve menden hansini istediyimi sorusun. bunu bele etsin: ilk olaraq 3 kateqoriyadan birini secir.
# birini secdikden sonra hemin kateqoriyadaki yemekler print olsun. Men de yemek secim, ya da hec birini secim. Sonra yene butun menyu acilsin ve o da secsin.
# Bu bele davam etsin. secim bitdikden sonra finis yazsin ve secdikleri ve umumi qiymet ekrana yazilsin. 
# Extra xususiyyet: secdikleri yemeklerin ve ickilerin falan sayi. 
        
        
        
class Menu:
    
    def menyu_goster(self, kategoriya):
        if kategoriya in self.kategoriyalar:
            self.kategoriyalar[kategoriya].cesid_exhibit()  
        else:
            print("Geçersiz kategoriya!")

    def sifaris_gotur(self):
        toplam_mebleg = 0
        while True:
            secilen_kategoriya = self.kategoriya_sec()
            if secilen_kategoriya == 'Finish':
                break
            else:
                self.menyu_goster(secilen_kategoriya)
                secilen_yemek = int(input("Zehmet olmasa bir yemek nomresi seçin ve ya '0' yazaraq bitirin: "))
                if secilen_yemek == 0:
                    break
                elif secilen_yemek <= len(self.kategoriyalar[secilen_kategoriya].cesidler):
                    qiymet = self.kategoriyalar[secilen_kategoriya].cesidler[secilen_yemek - 1]['qiymet']
                    yemek_adi = self.kategoriyalar[secilen_kategoriya].cesidler[secilen_yemek - 1]['ad']
                    print(f"{yemek_adi} seçildi. Qiymeti: {qiymet} AZN")
                    toplam_mebleg += qiymet  
                else:
                    print("Olmayan yemek nomresi!")
        
        print(f"Sifarişinizin toplam miqdari: {toplam_mebleg} AZN")

menu = Menu()
menu.sifaris_gotur()






 