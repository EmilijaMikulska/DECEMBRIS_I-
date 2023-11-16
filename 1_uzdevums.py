#Izveidojiet Python programmu, kas saskaita no 1 līdz lietotāja ievadītam skaitlim, izmantojot for ciklu.

skaitlis = int(input("Ievadi skaitli: "))

summa = 0
for i in range(1, skaitlis+1):
    summa += i

print("Summa no 1 līdz", skaitlis, "ir:", summa)