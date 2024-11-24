# ism ="rustamjon"
# ish ="hech qayerda"
# yosh =20
# print(ism)
# print(ish)
# print(yosh)

# print (f"Salom men {ism} men {ish} da ishlayman menni yoshim {yosh} da")


# Uzunlik L santimetrda berilgan. Undagi metrlar sonini aniqlang. (1 metr = 100 santimetr)

# l=int(input("sm qiymatni kiriting: "))
# print("Metrlar soni:",l/100)
  
"""  Og'irlik M kilogrammda berilgan. Undagi to'liq tonnalar sonini aniqlovchi dastur tuzilsin.
(1 tonna = 1000 kg)"""


# m=int(input("Kg qiymatni kiriting: "))
# print("Tonnada: ",m/1000)

# # Faylning hajmi baytlarda berilgan. Fayl hajmini to'liq kilobaytlarda ifodalovchi dastur tuzing.(1024 bayt = 1kb)

# kb=int(input("bayt qiymatni kiriting: "))
# print("Kb: ",kb/1024)

# """ Ikki xonali son berilgan. Oldin uning o'nliklar xonasidagi raqamni, so'ng, birlar xonasidagi raqamni chiqaruvchi
# dastur tuzing. Masalan: n = 25; Natija: 2, 5"""

# n=int(input("son kiriting: "))
# print("uning o'nliklar xonasidagi raqam: ",n//10)
# print("sonning birlar xonasidagi raqam: ",n%10)

# """
# Ikki xonali son berilgan. Oldin uning o'nliklar xonasidagi raqamni, so'ng, 
# birlar xonasidagi raqamni chiqaruvchi dastur tuzing. Masalan: n = 25; Natija: 2, 5
# """
# k=int(input("son kiriting: "))
# onlik=k//10
# birlar=k%10
# print(onlik+birlar)

# Ikki xonali son berilgan. Uning raqamlar o'rni almashtirishdan hosil bo'lgan sonni aniqlovchi dastur tuzing.
# Masalan: n = 25; Natija: 52

# so=int(input("ikki xonali sonni kiriting: "))
# onlar=so//10
# birlar=so%10
# k=birlar*10+onlar    
# print(k)

# print('7-masla')
# son=int(input("uch honali son kiriting: "))
# yuzlar=son//100*100
# print(yuzlar)

# print('8-masla')
# son=int(input("uch xonali sonni kiriting: "))
# onlar=son//10%10
# birlar=son%10
# print(birlar)
# print(onlar)
# print('9-masla')
# son=int(input("uch xonali son kiriting: "))
# yuzlar=son//100%10
# onlar=son//10%10
# birlar=son%10
# print(yuzlar+onlar+birlar)

# print('10-masla')
# son=int(input("uch xonali son kiriting: "))
# yuzlar=son//100%10
# onlar=son//10%10
# birlar=son%10
# almash=birlar*100+onlar*10+yuzlar
# print(almash)

# print('11-masla')
# son=int(input("uch xonali son kiriting: "))
# yuzlar=son//100%10
# k=son%100*10+yuzlar
# print(k)

# print('12-masla')
# son=int(input("uch xonali son kiriting: "))
# birlar=son%10
# k=son//10+birlar*100
# print(k)

# print('13-masla')
# son=int(input("uch xonali son kiriting: "))
# birlar=son%10
# onlar=son//10%10
# yuzlar=son//100%10
# almash=birlar+onlar*100+yuzlar*10
# print(almash)


# print('15-masla')
# son=int(input("999 dan katta son kiriting: "))
# yuzlar=son//100%10
# print(yuzlar)

# print('16-masla')
# son=int(input("999 dan katta son kiriting: "))
# minglar=son//1000%10
# print(minglar)
# print('17-masla')
# sekund=int(input("sekund kiriting: "))
# minut=sekund//60
# print(f"{str(minut)} min")

# print('18-masla')
# sekund=int(input("sekund kiriting: "))
# soat=sekund//3600
# print(f"{str(soat)} soat")

# print('19-masla')
# sekund=int(input("sekund kiriting: "))
# minut=sekund//60%60
# soat=sekund//3600
# sek=sekund%60
# print(f"{str(soat)} soat {str(minut)} minut {str(sek)} sekund")

print('20-masla')
sekund=int(input("sekund kiriting: "))
minut=sekund//60%60
sek=sekund%60
print(f"{str(minut)} minut {str(sek)} sekund")