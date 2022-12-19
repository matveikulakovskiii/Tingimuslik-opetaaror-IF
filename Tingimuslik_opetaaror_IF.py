
#try:
#    nimi=str(input("Sisestage oma nimi "))


#    if nimi.upper() == "JUKU":

#        print("Lähme kinno.")
#        a = float(input("Kui vana sa oled? ->"))
#        if a<0 or a>100:
#            print("viga andmetega")
#        elif a<6 :
#            print("siis on pilet tasuta")
#        elif a>=6 and a<=14:
#            print("siis on lastepilet")
#        elif a>=15 and a<65:
#            print("siis on täispilet")
#        elif a>=65:
#            print("siis on sooduspilet")
#        elif a<0 or a>100:
#            print("viga andmetega")
#    else:
#        print("Otsime Juku")

#except:
#    print("Vale andmetüüp")




#a=input("Esimese inimese nimi ->")
#b=input("Esimese teise nimi -> ")
#if a.isalpha() and b.isalpha():

#    if a.lower()=="matvei" and b.lower()=="anna":
#        print(f"{a} ja {b} on täna pinginaabrid")
#    else:
#        print()
#else:
#    print("Vale andmetüüp")


#try:
#    a=float(input("määrake ristkülikukujulise ruumi pikkus ->"))
#    b=float(input("määrake ristkülikukujulise ruumi laius ->"))
#    if a>0 and b>0:
#        S=a*b
#        print(f"ristküliku pindala on {S}")
#        c=int(input("Kas soovite remonti teha? kui 1-jah või 0-ei: "))
#        if c==1:
#            print("kui palju maksab ruutmeeter ja mitu põranda vahetamise hind?")
#            h=float(input("Ruutmeeter on ->"))
#            põrand=S*h 
#            print(f"Põranda hind on {põrand}")
#        else:
#            print("Hüvasti")
#    else:
#        print("Vale andmetüüp")
#except:
#    print("Vale andmetüüp")



#print("Vaja leida hind 30% allahindlusega, kui alghind on üle 700")
#try:
#    a=float(input("Määra hind ->"))
#    if a>700:
#        b=700-(700*0.3)
#        print(f"Vastus on {b}")
#    else:
#        print("Error")
#except:
#    print("Vale andmetüüp")



