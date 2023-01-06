from random import choice

# introducere quizz catre participanti
print("\n")
print("Salut, acesta este un quizz! ")
print("\n")
print("Vrei sa participi?")
print("\n")
print ("Raspunde cu DA sau NU!")
print("\n")

# se verifica daca jucatorul este pregatit de joc sau nu
while True:
    # raspunsul jucatorului
    raspuns= str(input("Raspunsul tau este: ").lower())
    print("\n")
    if raspuns == "da":
        print("Esti pregatit?")
        break
    elif raspuns == "nu":
        print("Ok te asteptam cand esti pregatit!")  
        exit()  
    else:
        print("Cred ca ai scris altceva, te rog raspunde cu 'DA' sau 'NU'.\n")
   

# se adreseaza prima intrebare

print("Prima intrebare din quizz este:\n ")


# lista de intrebari din quizz
lista_intrebari = [
    "Are blatul pufos ,are gustul frumos are sosul piperat si salamul cam muscat. ",
    "Frunze n-are, Nu-i nici floare , În paduri si pe ogor, Prin gradini si-n deal la vie sta mereu într-un picior. Ce este? ",
    "Ce cade-n apa si nu face stropi? ",
    "Am cămăşi nenumărate, plângi de le dezbraci pe toate! "
]
lista_intrebari.sort()

# se creaza o lista noua de match fata de lista de intrebari pentru a valida daca am doar ghicitori unice
# daca intrebarea aleasa random din lista de intrebari este in lista_de_trecere ==> pass (adica nu imi afisa intrebarea), daca nu ia celelalte conditii la rand
lista_de_trecere = []

# aceasta variabila stocheaza raspunsurile corecte
stocare_raspunsuri_corecte = []
# aceasta variabila cuantifica raspunsurile corecte
numarare_raspunsuri_corecte = 0

# aceasta variabila stocheaza raspunsurile gresite
stocare_raspunsuri_gresite = []
# aceasta variabila cuantifica raspunsurile gresite
numarare_raspunsuri_gresite = 0

# bucla de intrebari pana la epuizarea listei
while True:
    intrebare_random = choice(lista_intrebari)
    if intrebare_random in lista_de_trecere:
        pass
    else:
        print(intrebare_random)
        print("\n") 
        print("Stii ce este?")
        print("\n")
        raspuns_gamer = str(input("Raspunsul tau este: "))
        if intrebare_random == "Are blatul pufos ,are gustul frumos are sosul piperat si salamul cam muscat. " and raspuns_gamer == "pizza":
            numarare_raspunsuri_corecte += 1
            stocare_raspunsuri_corecte.append(raspuns_gamer)
            print(f"Bravo ai " + str(numarare_raspunsuri_corecte) + " punct!")
            lista_de_trecere.append(intrebare_random)
            lista_de_trecere.sort()
            if lista_de_trecere == lista_intrebari:
                print("Jocul s-a terminat! Multumim ca ai participat!")
                print(f"Jucatorule ai avut "+ str(numarare_raspunsuri_corecte) +" raspunsuri corecte si "+ str(numarare_raspunsuri_gresite) + " raspunsuri gresite. Trainne your mind! Good Look!!! \n")
                exit() 
            print("Crezi ca sti sa raspunzi la urmatoarea intrebare?\n")           
        elif intrebare_random == "Frunze n-are, Nu-i nici floare , În paduri si pe ogor, Prin gradini si-n deal la vie sta mereu într-un picior. Ce este? " and raspuns_gamer == "ciuperca":
            numarare_raspunsuri_corecte += 1
            stocare_raspunsuri_corecte.append(raspuns_gamer)
            print(f"Bravo ai " + str(numarare_raspunsuri_corecte) + " puncte!")
            lista_de_trecere.append(intrebare_random)
            lista_de_trecere.sort()
            if lista_de_trecere == lista_intrebari:
                print("Jocul s-a terminat! Multumim ca ai participat!")
                print(f"Jucatorule ai avut "+ str(numarare_raspunsuri_corecte) +" raspunsuri corecte si "+ str(numarare_raspunsuri_gresite) + " raspunsuri gresite. Trainne your mind! Good Look!!! \n")
                exit()  
            print("Crezi ca sti sa raspunzi la urmatoarea intrebare?\n")      
        elif intrebare_random == "Ce cade-n apa si nu face stropi? " and raspuns_gamer == "frunza":
            numarare_raspunsuri_corecte += 1
            stocare_raspunsuri_corecte.append(raspuns_gamer)
            print(f"Bravo ai " + str(numarare_raspunsuri_corecte) + " puncte!")
            lista_de_trecere.append(intrebare_random)
            lista_de_trecere.sort()
            if lista_de_trecere == lista_intrebari:
                print("Jocul s-a terminat! Multumim ca ai participat!")
                print(f"Jucatorule ai avut "+ str(numarare_raspunsuri_corecte) +" raspunsuri corecte si "+ str(numarare_raspunsuri_gresite) + " raspunsuri gresite. Trainne your mind! Good Look!!! \n")
                exit()
            print("Crezi ca sti sa raspunzi la urmatoarea intrebare?\n")           
        elif intrebare_random == "Am cămăşi nenumărate, plângi de le dezbraci pe toate! " and raspuns_gamer == "ceapa":
            numarare_raspunsuri_corecte += 1
            stocare_raspunsuri_corecte.append(raspuns_gamer)
            print(f"Bravo ai " + str(numarare_raspunsuri_corecte) + " puncte!")
            lista_de_trecere.append(intrebare_random)
            lista_de_trecere.sort()
            if lista_de_trecere == lista_intrebari:
                print("Jocul s-a terminat! Multumim ca ai participat!")
                print(f"Jucatorule ai avut "+ str(numarare_raspunsuri_corecte) +" raspunsuri corecte si "+ str(numarare_raspunsuri_gresite) + " raspunsuri gresite. Trainne your mind! Good Look!!! \n")
                exit()
            print("Crezi ca sti sa raspunzi la urmatoarea intrebare?\n")
            continue    
        else:
            if raspuns_gamer != "pizza" or raspuns_gamer != "ciuperca" or raspuns_gamer != "frunza" or raspuns_gamer != "ceapa":
                stocare_raspunsuri_gresite.append(raspuns_gamer)
                numarare_raspunsuri_gresite += 1
                print("\n")
                print("Gresit! Nu este acesta raspunsul corect!")
                lista_de_trecere.append(intrebare_random)
                lista_de_trecere.sort()
                if lista_de_trecere == lista_intrebari:
                    print("Jocul s-a terminat! Multumim ca ai participat")
                    print(f"Jucatorule ai avut "+ str(numarare_raspunsuri_corecte) +" raspunsuri corecte si "+ str(numarare_raspunsuri_gresite) + " raspunsuri gresite. Trainne your mind! Good Look!!! \n")
                    exit()
                print("Urmatoarea intrebare este: ")
                print("\n")























































