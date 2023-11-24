# 1
# def list_max(list_1):
#     max=list_1[0]
#     for item in list_1:
#         if item>max:
#             max=item
#     return max
# misal_list=input("bir list yazin:" )
# misal_list=misal_list.split(" ")
# misal_list=[int(item) for item in misal_list]
# print(misal_list)
# # //misal_list=[1,5,3,8,7,5]
# netice=list_max(misal_list)
# print(netice)

# 2
# def list_text(text, soz):
#     counter=0
#     for word in text.split():
#         if word==soz:
#             counter+=1
#     return counter
# example_text= "men ders edire, men youluram, men dincelirem, men yene ders edirem."
# lazimi="men"
# netice=list_text(example_text, lazimi)
# print(f"'{lazimi}' sozu metnde '{netice}' defe var ")

# 3
# def faktoryal(say):
#     if say==0 or say==1:
#         return 1
#     else:
#         return say*faktoryal(say-1)
    
# say=10
# netice=faktoryal(say)
# print(netice)

# 4
# def sort_list(*list_a):
#     list_a=list(list_a)
#     for a in list_a:
#         for i in range(len(list_a)-1):
#             if list_a[i]>list_a[i+1]:
#                 temp=list_a[i]
#                 list_a[i]=list_a[i+1]
#                 list_a[i+1]=temp
#     print(list_a)
# # / list_a=[5,1,9,3,6,2]
# # / sort_list(list_a)
# # /list_b=[3,2,7,5,8,9,0]
# # / sort_list(list_b)
# sort_list(1,5,2,8,3,0,4)

# 5 ?
# def sade_ededler(ilk, son):
#     eded=[]
#     for say in range(ilk, son+1):
#         if say>1:
#             for i in range(2, int(say**0.5)+1):
#                 if say%i==0:
#                     break
#             else:
#                 eded.append(say)
#     return eded

# ilk_eded=int(input("bir eded yazin:" ))
# son_eded=int(input("digerinden boyuk bir eded yazin:" ))
# sade_ededler_list=sade_ededler(ilk_eded, son_eded)
# print(sade_ededler_list)


# 6
# def list_text(text):
#     sozler=text.split()
#     return len(sozler)

# numune_text="bu sadece misal bir yazidir."
# soz_sayi=list_text(numune_text)
# print(soz_sayi)

# 7
# def list(list_eded):
#     tek_ededler=[]
#     for eded in list_eded:
#         if eded%2!=0:
#             tek_ededler.append(eded)
#     return tek_ededler

# numune=[3, 78, 90, 9, 15, 6 , 89, 98]
# tekler_listi=list(numune)
# print(tekler_listi)

# 8
# def ikisibirarada(metn1, metn2):
#     birlesmis=", ".join([metn1, metn2])
#     return birlesmis

# birinci="men gedirem Istanbula"
# ikinci="ehtiyacim vardi pula"
# netice=ikisibirarada(birinci, ikinci)
# print(netice)

# 9
# def ededi_orta(siyahi):
#     cem=sum(siyahi)
#     ortalama=cem/len(siyahi)
#     return ortalama
# siyahi=[4, 6,7,8,9,23,45,67]
# netice=ededi_orta(siyahi)
# print(netice)

# siyahi=[4, 6, 7, 8, 90, 87, 56, 45]
# cem=0
# for eded in siyahi:
#     cem+=eded
# print(eded)

# sinif
# def salam_ver(*ad):
#     print(f"salam, {ad}")
    
# salam_ver("Hesen","Eli")
# # salam_ver()
