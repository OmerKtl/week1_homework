print("\n"+" * "*10+"\n    TAS KAGIT MAKAS OYUNU\n"+" * "*10+"\n")

adbir=input("BIRINCI OYUNCUNUN ADINI GIRINIZ :").upper()
adiki=input("IKINCI OYUNCUNUN ADINI GIRINIZ :").upper()
tas="T"
kagit="K"
makas="M"
puanbir=0
puaniki=0
sayac=1

while sayac<=10:
    cbir=input("\n{} CEVAPLAYACAK :\nTAS MI?  ---> ( T )\nKAGIT MI?---> ( K )\nMAKAS MI?---> ( M )\n:".format(adbir)).upper()
    ciki=input("\n{} CEVAPLAYACAK :\nTAS MI?  ---> ( T )\nKAGIT MI?---> ( K )\nMAKAS MI?---> ( M )\n:".format(adiki)).upper()

    if (cbir==tas and ciki==tas) or (cbir==kagit and ciki==kagit) or (cbir==makas and ciki==makas):
        print("\n{}.EL BERABERE...".format(sayac))
        sayac+=1
    elif (cbir==tas and ciki==kagit) or (cbir==kagit and ciki==makas) or (cbir==makas and ciki==tas):
        print("\n{}.Elin Kazanani:".format(sayac),adiki)
        sayac+=1
        puaniki+=1
    elif (ciki==tas and cbir==kagit) or (ciki==kagit and cbir==makas) or (ciki==makas and cbir==tas):
        print("\n{}.Elin Kazanani:".format(sayac),adbir)
        sayac+=1
        puanbir+=1
    else:
        print("GECERSIZ GIRIS... SADECE ( T- K - M ) GIRINIZ!")

if puanbir>puaniki:
    print("\nOYUNUN KAZANANI :{}\nPUANI           :{}\nOYUNUN KAYBEDENI:{}\nPUANI           :{}".format(adbir,puanbir,adiki,puaniki))
elif puaniki>puanbir:
    print("\nOYUNUN KAZANANI :{}\nPUANI           :{}\nOYUNUN KAYBEDENI:{}\nPUANI           :{}".format(adiki,puaniki,adbir,puanbir))
elif puaniki==puanbir:
    print("\nOYUN {} - {} BERABERE BITMISTIR".format(puanbir,puaniki))