#Izveidojiet Python programmu, kas aprēķina lietotāja ievadīta skaitļa faktoriālu, izmantojot for ciklu.

c=int(input("Ieraksti skaitli: "))      #c=cipars

fa=1                       #fa=faktoriāls
for i in range (1,c+1):
    fa*=i

print("Skaitļa", c, "faktoriāls ir:", fa)