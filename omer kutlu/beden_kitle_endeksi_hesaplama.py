print("*"*10,"BEDEN KITLE ENDEKSI HESAPLAMA PROGRAMI","*"*10)

ad=input("ADINIZI GIRINIZ : ")
boy=int(input("BOYUNUZU GIRINIZ (CM cinsinden) : "))
kilo=int(input("KILONUZU GIRINIZ (KG cinsinden) : "))
bke=kilo/((boy*0.01)**2)
liste=[ad,boy,kilo,bke]
durum=["NORMAL","FAZLA KILOLU","OBEZ","ASIRI SISMAN"]

if bke<25:
    print("\nADI :{}\nBOYU :{} cm\nKILOSU :{} kg\nBEDEN KITLE ENDEKSI :{}\nSONUC :{}".format(liste[0],liste[1],liste[2],liste[3],durum[0]))
if bke>=25 and bke<30:
    print("\nADI :{}\nBOYU :{} cm\nKILOSU :{} kg\nBEDEN KITLE ENDEKSI :{}\nSONUC :{}".format(liste[0],liste[1],liste[2],liste[3],durum[1]))
if bke>=30 and bke<40:
    print("\nADI :{}\nBOYU :{} cm\nKILOSU :{} kg\nBEDEN KITLE ENDEKSI :{}\nSONUC :{}".format(liste[0],liste[1],liste[2],liste[3],durum[2]))
if bke>=40:
    print("\nADI :{}\nBOYU :{} cm\nKILOSU :{} kg\nBEDEN KITLE ENDEKSI :{}\nSONUC :{}".format(liste[0],liste[1],liste[2],liste[3],durum[3]))