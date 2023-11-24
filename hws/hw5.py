# 1
# list_str="Salamlasmaq lazimdir, Salam ehemmiyetlidir"
# istifadeciAdi=list_str.split(" ")
# print(istifadeciAdi)
# istifadeciAdi=[item for item in istifadeciAdi if item.startswith("Salam")]
# print(istifadeciAdi)
# //lazimi=istifadeciAdi.startswith("Salam")
#// print(lazimi)

# 2
# list_str=input("Listi daxil edin: ")
# istifadeciAdi=list_str.split(" ")
# istifadeciAdi=[item for item in istifadeciAdi if item.endswith(".jpg")]
# print(istifadeciAdi)
#// while lazimi(istifadeciAdi.endswith(".jpg")):
#//     print(lazimi)

# 3
# metin = input("Xahiş olunur mətni daxil edin: ")
# kelime = input("Zehmet olmasa axtarmaq istediyiniz sozu daxil edin: ")
# counter = metin.lower().count(kelime.lower())
# print(f"'{kelime}' kelimesi metinde {counter} defe islenib.")

# 4
# metin = input("Xahiş olunur mətni daxil edin: ")
# ilk_kelime = input("Zehmet olmasa deyismek istediyiniz sozu daxil edin: ")
# ikinci_kelime= input("Zehmet olmasa evezine isletmek istediyiniz sozu daxil edin: ")
# düzeltilmiş_metin = metin.replace(ilk_kelime, ikinci_kelime)
# print("Düzeldilmiş Metin:")
# print(düzeltilmiş_metin)

# 4//
# metin ="biz gedirik istanbula"
# ilk_kelime = "biz"
# ikinci_kelime= "ailelikce"
# indi=metin.split(" ")
# for index in range(len(indi)-1):
#     if ilk_kelime==indi[index]: 
#         indi[index]=ikinci_kelime
# metin=" ".join(indi)
# print(metin)
   

# 5
# tarix = input("Zehmet olmasa bir tarix daxil edin: ")
# hisse = tarix.split(".")
# gun = hisse[0]
# ay = hisse[1]
# il = hisse[2]
# print("Gun: " + gun)
# print("Ay: " + ay)
# print("il: " + il)
# //
# tarix= "24.04.2023"
# gun="24"
# ay="04"
# il="2023"
# print("24\\04\\2023")

# 6
# metn_ad= input("Zehmet olmasa adinizi daxil edin: ")
# metn_yas= input("Zehmet olmasa yasinizi daxil edin: ")
# mesaj= f"Salam, {metn_ad}! Sen {metn_yas} yasindasan."
# //mesaj= "Salam, {metn_ad}! Sen {metn_yas} yasindasan.".format(metn_ad=metn_ad, metn_yas=metn_yas)
# print(mesaj)

# 7
ad= input("mehsulun adini qeyd edin: ")
miqdar_str= input("mehsulun miqdarini(kq,l,sm..) qeyd edin: ")
miqdar_list=miqdar_str.split(" ")
miqdar=int(miqdar_list[0]) 
qiymet= int(input("mehsulun qiymetini qeyd edin: "))
toplam_mebleg= miqdar*qiymet
netice=f"mehsul:{ad}, miqdar:{miqdar_str}, qiymet:{toplam_mebleg} manat."
print(netice)

# extra