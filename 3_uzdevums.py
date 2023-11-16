#Izveidojiet Python programmu, kas pārbauda, vai ievadītais skaitlis ir nepāra, izmantojot if priekšrakstu.

cipars=int(input("Ieraksti skaitli: "))
if cipars % 2 !=0:
    print("Ievadītais skaitlis ir nepāra.")
else:
    print("Ievadītais skaitlis ir pāra.")