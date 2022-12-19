
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




#try:
#    a=float(input("Mis on teie toatemperatuur: "))
#    if a>=18:
#        print("Teie toatemperatuur on keskmisest kõrgem, 18 kraadi Celsiuse järgi.")
#    else:
#        print("Teie toatemperatuur on keskmisest madalam, 18 kraadi Celsiuse järgi.")
#except:
#    print("Vale Andmetüüp")



#try:
#    a=float(input("Mis on su pikkus?(Sentimeetrites): "))
#    if a<=0:
#        print("Error")
#    else:
#        if a<=165:
#            print("Teie pikkus on madal")
#        elif a>165 and a<180:
#            print("Teie pikkus on keskmine")
#        elif a>=180:
#            print("Teie pikkus on kõrge")
#except:
#    print("Vale Andmetüüp")




#try:
#    a=float(input("Mis on su pikkus?(Sentimeetrites): "))
#    try:
#        b=int(input("Mis on sinu sugu?(mees-1 või naine-0): "))
#        if b>1:
#            print("Error")
#        else:
#            if b==1:
#                if a<=0:
#                     print("Error")
#                else:
#                     if a<170:
#                         print("Teie pikkus on madal")
#                     elif a>=170 and a<180:
#                         print("Teie pikkus on keskmine")
#                     elif a>=180:
#                         print("Teie pikkus on kõrge")
#            else:
#                if a<=0:
#                    print("Error")
#                else:
#                    if a<160:
#                        print("Teie pikkus on madal")
#                    elif a>=160 and a<170:
#                        print("Teie pikkus on keskmine")
#                    elif a>=170:
#                        print("Teie pikkus on kõrge")
#    except:
#        print("Vale Andmetüüp")
#except:
#    print("Vale Andmetüüp")


#try:
#    a=int(input("Kas soovite piima osta?(jah-1 või ei-0): "))
#    b=int(input("Kas soovite saia osta?(jah-1 või ei-0): "))
#    c=int(input("Kas soovite leiba osta?(jah-1 või ei-0): "))
#    if a==1 and b==0 and c==0:
#        piim=0.79
#        sai=0
#        leib=0
#        S=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {S}")
#    elif a==0 and b==1 and c==0:
#        piim=0
#        sai=0.8
#        leib=0
#        P=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {P}")
#    elif a==0 and b==0 and c==1:
#        piim=0
#        sai=0
#        leib=0.8
#        F=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {F}")
#    elif a==1 and b==1 and c==0:
#        piim=0.79
#        sai=0.8
#        leib=0
#        L=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {L}")
#    elif a==0 and b==1 and c==1:
#        piim=0
#        sai=0.8
#        leib=0.8
#        O=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {O}")
#    elif a==1 and b==0 and c==1:
#        piim=0.79
#        sai=0
#        leib=0.8
#        U=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {U}")
#    elif a==1 and b==1 and c==1:
#        piim=0.79
#        sai=0.8
#        leib=0.8
#        A=piim+sai+leib
#        print(f"Kõik ostetud asjad maksavad {A}")
#except:
#    print("Vale Andmetüüp")

#try:
#    a=float(input("Utle pool a "))
#    b=float(input("Utle pool b "))
#    if a==b:
#        print("See on ruut")
#    else:
#        print("See ei ole ruut")
#except:
#    print("Value Error")


#try:
#    a=float(input("1 number "))
#    b=float(input("1 number "))
#    c=input("mis märk sa oled +-/ \n ")
#    if c==("+"):
#        print(a+b)
#    elif c==("-"):
#        print(a-b)
#    elif c==(""):
#        print(a*b)
#    elif c==("/"):
#        if b==0:
#            print("Väiksem kui 0")
#        else:
#            print(a/b)
#except:
#    print("Value Error")



#now = datetime.datetime.now()
#try:
#    a=int(input("Sisesta sünniaasta. "))
#except:
#    print("Value Error")
#b=int(now.year)
#c=int(b-a)
#print(c)
#f=c%5
#if f==0:
#    print("teil on juubel")
#else:
#    print("Kui kaju")

#try:
#    a=float(input("sisesta toote hind "))
#    if a<=10:
#        print("sul on soodus 10%",a-a0.1)
#    elif a>10:
#        print("sul on soodus 20%",a-a0.2)
#except:
#    print("Value Error")


#try:
#    a=int(input("Kas sa oled mees?(jah-1 või ei-0)"))
#    if a==1:
#        b=int(input("Kui vana sa oled? "))
#        if b>=16 and b<=18:
#            print("sa sobid")
#    else:
#        print("sa oled naine sest, et sa ei sobi")
#except:
#    print("Value Error")
