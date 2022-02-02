print("-+-+-+-+-+-+-+-+-+-+-+-+-+NOT HESAPLAMA PROGRAMI-+-+-+-+-+-+-+-+-+-+-+-+-+")
vizekat=0.4
finalkat=0.6

ograd=input("Ogrenci adini giriniz= ").upper()
ogrsoyad=input("Ogrenci soyadini giriniz= ").upper()
ogrnu=input("Ogrenci numarasini giriniz= ")

dersbir=input("1. dersin adini giriniz=").upper()
dersiki=input("2. dersin adini giriniz=").upper()
dersuc=input("3. dersin adini giriniz=").upper()
dersdort=input("4. dersin adini giriniz=").upper()

vizbir=int(input("Lutfen {} vize notunu giriniz :".format(dersbir)))
finbir=int(input("Lutfen {} final notunu giriniz :".format(dersbir)))
ortbir=(vizbir*vizekat)+(finbir*finalkat)

viziki=int(input("Lutfen {} vize notunu giriniz :".format(dersiki)))
finiki=int(input("Lutfen {} final notunu giriniz :".format(dersiki)))
ortiki=(viziki*vizekat)+(finiki*finalkat)

vizuc=int(input("Lutfen {} vize notunu giriniz :".format(dersuc)))
finuc=int(input("Lutfen {} final notunu giriniz :".format(dersuc)))
ortuc=(vizuc*vizekat)+(finuc*finalkat)

vizdort=int(input("Lutfen {} vize notunu giriniz :".format(dersdort)))
findort=int(input("Lutfen {} final notunu giriniz :".format(dersdort)))
ortdort=(vizdort*vizekat)+(findort*finalkat)

ogrliste=[ograd,ogrsoyad,ogrnu]
dersliste=[dersbir,dersiki,dersuc,dersdort]
ortliste=[ortbir,ortiki,ortuc,ortdort]

print("\nAdi:{}\nSoyadi:{}\nNumarasi:{}\n".format(ogrliste[0],ogrliste[1],ogrliste[2]))
if ortliste[0]>=50:
    print("{} Dersinin ortalamasi {} : GECTI\n".format(dersliste[0],ortliste[0]))
else:
    print("{} Dersinin ortalamasi {} : KALDI\n".format(dersliste[0],ortliste[0]))

if ortliste[1]>=50:
    print("{} Dersinin ortalamasi {} : GECTI\n".format(dersliste[1],ortliste[1]))
else:
    print("{} Dersinin ortalamasi {} : KALDI\n".format(dersliste[1],ortliste[1]))

if ortliste[2]>=50:
    print("{} Dersinin ortalamasi {} : GECTI\n".format(dersliste[2],ortliste[2]))
else:
    print("{} Dersinin ortalamasi {} : KALDI\n".format(dersliste[2],ortliste[2]))

if ortliste[3]>=50:
    print("{} Dersinin ortalamasi {} : GECTI".format(dersliste[3],ortliste[3]))
else:
    print("{} Dersinin ortalamasi {} : KALDI".format(dersliste[3],ortliste[3]))