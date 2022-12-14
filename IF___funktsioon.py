
from math import *
from random import *
try:
    päev=int(input("Mis päev ja mitu tundi täna on?")) 
    if päev==1:
        n="Esmaspäev"
        n="6 tundi"
    elif päev==2:
        n="Teisipäev"
        n="8 tundi"
    elif päev==3:
        n="Kolmapäev"
        n="6 tundi"
    elif päev==4:
        n="Neljapäev"
        n="5 tundi"
    elif päev==5:
        n="Reede"
        n="7 tundi"
    elif päev==6:
        n="Laupäev"
        n="0 tundi"
    elif päev==7:
        n="Puhapäev"
        n="0 tundi"
    else:
        n="vale number"
    print(n)
except:
    print("! ! ! ! ! ! !")









#13/12/22
print("Sisselogimine tahvel")
try: 
    vanus=int(input("Kui vana sa oled?"))
    if vanus<=18:
        print("Kas te annate vanematele loa oma tahvelit vaadata?")
        o=(input("Jah või ei. "))
        if o.lower()=="jah":
            print ({o})
            print("See on ligipääs teie vanematele. ")
            print("Tahvel on kinni. ")
        elif o.upper()=="Ei":
            print("Sissepääs puudub. ")
            print("Tahvel on kinni. ")
    if vanus>18:
        print("Juurdepääs vanematele on automaatselt antud.")
except:
    print("Tahvel on kinni. ")