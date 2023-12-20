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
        
        
        
# file_text = open("Codes/data.txt","r")

# a = file_text.read()
# list_a = []
# for item in a.split(","):
#     if int(item)%2 == 0:
#         list_a.append(int(item))
    
# file_text_2 = open("Codes/netice.txt","w")

# for item in list_a:
#     file_text_2.write(str(item)+",")

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"



class JackRussellTerrier(Dog):
    def speak(self):
        return f"{self.name} mew mew"

class Dachshund(Dog):
    def speak(self):
        return f"{self.name} says how how"