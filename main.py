### 1
# import threading
#
# data = "Bu faylga parallel yozilayotgan ma'lumot.\n" * 100
#
# def write_to_file(filename):
#     with open(filename, 'w') as f:
#         f.write(data)
#         print(f"{filename} ga yozish tugatildi")
#
#
# file_names = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']
#
# threads = []
#
# for name in file_names:
#     t = threading.Thread(target=write_to_file, args=(name,))
#     threads.append(t)
#     t.start()
#
#
# for t in threads:
#     t.join()
#
# print("Barcha fayllarga yozish tugadi.")


### 2
# import threading
# import math
#
# def kvadrat(x):
#     print(f"{x} ning kvadrati: {x ** 2}")
#
# def kub(x):
#     print(f"{x} ning kubi: {x ** 3}")
#
# def ildiz(x):
#     print(f"{x} ning ildizi: {math.sqrt(x)}")
#
# son = 9
#
# thread1 = threading.Thread(target=kvadrat, args=(son,))
# thread2 = threading.Thread(target=kub, args=(son,))
# thread3 = threading.Thread(target=ildiz, args=(son,))
#
# thread1.start()
# thread2.start()
# thread3.start()
#
# thread1.join()
# thread2.join()
# thread3.join()

### 3
# import threading
#
# def juft_son(x):
#     for i in x:
#         if i % 2 == 0:
#             print(f"Juft sonlar: {i}")
#
# def toq_son(x):
#     for i in x:
#         if i % 2 == 1:
#             print(f"Toq sonlar: {i}")
#
# list = [1, 2, 3, 4, 5, 6, 7, 8]
#
# thread1 = threading.Thread(target=juft_son, args=(list, ))
# thread2 = threading.Thread(target=toq_son, args=(list, ))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()


### 4
# import threading
# import time
#
# def hello_de():
#     while True:
#         print('Hello')
#         time.sleep(2)
#
# def world_de():
#     while True:
#         print('World')
#         time.sleep(3)
#
# t1 = threading.Thread(target=hello_de)
# t2 = threading.Thread(target=world_de)
#
# t1.daemon = True
# t2.daemon = True
#
# t1.start()
# t2.start()
#
# time.sleep(10)
# print("Dastur tugadi.")

### 5
# import threading
# import time
#
# def fayl_oqish(nomi):
#     with open(nomi, 'r') as file:
#         for qator in file:
#             print(f"Fayl oqildi {qator.strip()}")
#             time.sleep(1)
#
# fayl_thread = threading.Thread(target = fayl_oqish, args=('data.txt', ) )
#
# fayl_thread.start()
#
# fayl_thread.join()


### 6
# import threading
# import time
#
# def xabar_ber(matn):
#     time.sleep(1)
#     print(matn)
#
# matnlar = [
#     "Xabar 1",
#     "Xabar 2",
#     "Xabar 3",
#     "Xabar 4",
#     "Xabar 5"
# ]
#
# threadlar = []
#
#
# for matn in matnlar:
#     t = threading.Thread(target=xabar_ber, args=(matn ,))
#     threadlar.append(t)
#     t.start()
#
# for t in threadlar:
#     t.join()
#
# print("Barcha xabarlar chiqarildi.")

###Stringy Strings
# def stringy(size):
#     return ''.join('1' if i % 2 == 0 else '0' for i in range(size) )


### Capitalization and Mutability
# def capitalize_word (word : str) -> str:
#     return word[0].upper() + word[1:]


###Well of Ideas - Easy Version
# def well(x):
#     good_count = x.count('good')
#
#     if good_count == 0:
#         return 'Fail!'
#     elif good_count <= 2:
#         return 'Publish!'
#     else:
#         return 'I smell a series!'

### Exclamation marks series #1: Remove an exclamation mark from the end of string
# def remove(s):
#     if s.endswith('!'):
#         return s[:-1]
#     else:
#         return s




















# import threading
# import time
#
# def salom_de():
#     for _ in range(5):
#         print('salom')
#         time.sleep(1)
#
# def xayr_de():
#     for _ in range(5):
#         print('Xayr')
#         time.sleep(1)
#
# t1 = threading.Thread(target=salom_de)
# t2 = threading.Thread(target=xayr_de)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

###
# import threading
#
#
# def umumiy_yigindi():
#     s = sum(range(1, 11))
#     print("Umumiy yigindi", s)
#
# def juft_yigindi():
#     s = sum(i for i in range(1, 11) if i % 2 == 0)
#     print("Juft yigindi:", s)
#
# t1 = threading.Thread(target=umumiy_yigindi)
# t2 = threading.Thread(target=juft_yigindi)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

###
# import threading
#
# def salom_ber(ism):
#     print(f"Salom {ism}")
#
# userlar = ['Asadbek', 'Ali', 'Vali']
#
# threadlar = []
#
# for ism in userlar:
#     t = threading.Thread(target=salom_ber, args=(ism,))
#     t.start()
#     threadlar.append(t)
#
# for t in threadlar:
#     t.join()


###
# import threading
# import time
#
# def vaqtni_kuzat():
#     for i in range(5):
#         print('Sekunt otdi...')
#         time.sleep(1)
#
# t = threading.Thread(target=vaqtni_kuzat)
# t.start()
#
# t.join()
# print("Dastur tugadi")

###
# import threading
#
# lock = threading.Lock()
#
# def faylga_yozish(ism):
#     with lock:
#         with open("data.txt", "a") as f:
#             f.write(f"{ism} faylga yozdi.\n")
#
# userlar = ["Asadbek", "Ali", "Vali"]
#
# threadlar = []
# for ism in userlar:
#     t = threading.Thread(target=faylga_yozish, args=(ism,))
#     t.start()
#     threadlar.append(t)
#
# for t in threadlar:
#     t.join()


