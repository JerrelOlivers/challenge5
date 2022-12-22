#RPG
import time
import sys
import random

HP = int(100)

hoofdpoppetje = input("Welke naam wil je aan je karakter meegeven?: ")
print("Lang geleden leefde er een schattig konijntje genaamd Flappie")
time.sleep(3)
print("--------------------")
print("Flappie was bezig met zijn favoriete bezigheid: lekker springen door het grasveldje")
time.sleep(3)
print("--------------------")
print("Het was Kerstochtend toen Flappie op brute wijze van het leven werd beroofd.")
time.sleep(3)
print("--------------------")
print("Flappie werd op brute wijze gedood voor het kerstdiner")
time.sleep(3)
print("--------------------")
print("Vele jaren later is", hoofdpoppetje, 'deze horrordaad nog niet vergeten en wil Flappie wreken.')
time.sleep(3)
print("--------------------")
print("Dit is het verhaal van", hoofdpoppetje)

print("Hoe gaat", hoofdpoppetje, "wraaknemen?")
def eerste_keuze1():
    eerste_keuze = input("Kies 1 voor de vader ombrengen met een kerstboom, kies 2 voor vader ombrengen met behulp van de kerstman zijn elfjes of kies 3 voor vader ombrengen met een rendier:  ")

    if eerste_keuze == "1":
        print("De kerstboom was te zwaar om op te tillen, probeer iets anders!")
        eerste_keuze1()
    elif eerste_keuze == "2":
        print("Het is de elfjes van de kerstman gelukt!")
    elif eerste_keuze == "3":
        print("De kerstman is enorm teleurgesteld in je, probeer iets anders!")
        eerste_keuze1()

eerste_keuze1()


print("----------------")
print("De elfjes hadden met een ding echter geen rekening gehouden met het feit dat de babyfoon nog aanstond")
time.sleep(3)
print("---------------")
print("Een hele tijd later is", hoofdpoppetje, "schuldig verklaard en moet voor 21 jaar de gevangenis in!")
time.sleep(3)
print("------------")
print(hoofdpoppetje, "heeft daar geen zin in en besluit te gaan ontsnappen uit de gevangenis, met een wapen ontvangen tijdens een eerder gesprek met de advocaat.")
tweede_keuze = input("Kies 1 om tijdens de lunch te gaan, kies 2 om te sprinten of kies 3 om met anderen te ontsnappen:  ")
if tweede_keuze == "1":
    print(hoofdpoppetje, "schiet 2 bewakers neer en loopt naar buiten, omdat de voordeur altijd al open bleek te zijn")
if tweede_keuze == "2":
    print(hoofdpoppetje, "trekt een sprint naar de hoogste verdieping, om daar via de luchtschacht te ontsnappen")
if tweede_keuze == "3":
    print(hoofdpoppetje, "schiet 7 bewakers neer en ontsnapt met andere gevangenen")
print("------------")
print("Eenmaal ontsnapt komt al snel het plan om naar Rusland te gaan, aangezien Rusland geen uitleveringsverdrag heeft met Nederland.")
print("---------------")
b = input("Eenmaal in Rusland aangekomen bevind je je in een bos. Kies welke kant je uit wil: L om naar links te gaan, R om naar rechts te gaan, V om voorwaarts te gaan: ")
if b == "L":
    print("Er komt een leger van skeletten op je af") 
    time.sleep(3)
    HP = HP - random.randint(0, 40)
    print("Je hebt nog", HP, 'HP over')
    print("---------------")
    time.sleep(3)
    dikke_papzak = input("Kies je ervoor om dieper het bos in te gaan (D) of terug naar het beginpunt te gaan? (S): ")
    if dikke_papzak == "D":
        print("Je bent dieper in het bos gegaan en je komt een oude man tegen")
        time.sleep(3)
        print("---------------")
        laurens_vetpens = input("Laat je de oude man met rust (R) of spreek je hem aan (S)?")
        print("-------------")
        if laurens_vetpens == "S":
            print("De oude man geeft je advies over hoe je het beste verder kunt gaan")
            time.sleep(3)
            print("--------------")
            print("De man zegt dat je het beste rechtdoor kan gaan, want je bent dichtbij een stad")
            time.sleep(3)
            print(hoofdpoppetje, "loopt al een tijdje rechtdoor totdat plotseling een leger van skeletten opduikt")
            time.sleep(3)
            vechton = input("Kies je er voor om te vechten? (V) of kies je ervoor om te vluchten? (VL)")
            if vechton == "V":
                print("Je koos er voor om te vechten, maar je hebt flinke damage gepakt")
                HP = HP - random.randint(40,55)
                print(HP)
                print("Je hebt de skeletten gedood en gaat richting het stadje om verder te gaan met je leven")
            if vechton == "VL":
                print("Je bent gevlucht en je hebt het stadje bereikt, waar je verder gaat met je leven")
                
        else: 
            print("De oude man verdwijnt plots")
            time.sleep(3)
            print("/n Er spawnen plots 30 zombies op de plek waar de oude man zojuist stond")
            JAN = input("Kies je ervoor om met ze te vechten (V) of om te vluchten (VL):    ")
            if JAN == "VL":
                print("De zombies zijn sneller dan", hoofdpoppetje)
                time.sleep(2)
                print(hoofdpoppetje, "gaat dood en word ook een zombie")
            if JAN == "V":
                print("De zombies zijn sterk, je pakt zieke damage")
                nieuwe_hp= HP - random.randint(50, 55)
                print(nieuwe_hp)
                time.sleep(3)
                print("Je bent verzwakt dus kies je er voor om keihard te sprinten na een huisje in de stad")
                time.sleep(3)
                print("De Nederlandse politie is toevallig dorpje en ze schieten je dood")
                



    


if b == "R":
    print("Je komt bij een vermoedelijk oude tempel aan, ga je naar binnen of keer je terug naar het eerste punt")
    HANS = input("Kies E voor de tempel binnen te gaan of kies voor P om naar het eerste punt te gaan")
    if HANS == "E":
        print(hoofdpoppetje, "gaat naar binnen en wordt verzwakt door de geur")
        HP = HP - random.randint(2, 5)
        time.sleep(3)
        Erik = input("Kies je er voor om toch door te gaan(D) of kies je er voor om terug te keren?(T)")
        if Erik == "D":
            print("Je gaat door de tempel heen en vindt een zeer zeldzame diamant, maar JE ACTIVEERT DE ZELFVERNIETINGSPROCEDURE")
            Lucas = input("Ga je keihard rennen (R) of ga je tactisch de ruimte verlaten(T)?")
            if Lucas == "R":
                print("Je gaat op een landmijn staan, dit is het einde voor jou!")
            if Lucas == "T":
                print("Je ontdekt op tijd de landmijn en ontsnapt succesvol")
                time.sleep(3)
                print("--------------")
                print(hoofdpoppetje, "gaat verder met het leven in Rusland")

 
        

if b == "V":
    print(hoofdpoppetje, "gaat rechtdoor")
    time.sleep(3)
    print("\n", hoofdpoppetje, 'komt een jong kind, een volwassene die erg op', hoofdpoppetje, "lijkt en een oude man, die iets in zijn handen heeft tegen")
    WAT = input("Spreek je ze aan(S) of loop je door(L)")
    if WAT == "S":
        print("\n De volwassene en het kind beginnen met praten.", hoofdpoppetje, "dit is allemaal uit de hand gelopen... ")
        time.sleep(5)
        print("\n Geef jezelf aan bij de politie")
        time.sleep(5)
        print(hoofdpoppetje, "\n geef jezelf aan")
        time.sleep(5)
        print("De volwassene en jongen verdwijnen in het niets.")
        time.sleep(5)
        print("De enige die overblijft is de oude man")
        time.sleep(5)
        print("Het 5s een tijd geleden hè", hoofdpoppetje)
        time.sleep(5)
        print("De oude man blijkt de vader te zijn!")
        time.sleep(4)
        print("Het spijt me voor wat die ene avond is gebeurd", hoofdpoppetje)
        Raymond = input("Vergeef je Vader? (J)a of (N)ee ")
        if Raymond == "J":
            print("Je hebt Vader vergeven en gaat jezelf aangeven bij de politie.")

        if Raymond == "N":
            print("Je hebt Vader niet vergeven en blijft in Rusland.")

    


