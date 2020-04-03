from socket import *
import sys
import os

print("-----------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------                   BETIM THAÇI                 -------------------------------------")
print("-----------------------------------            UNIVERSITETI I PRISHTINES          -------------------------------------")
print("-----------------------------------      INXHINIERI KOMPJUTERIKE DHE ELEKTRIKE    -------------------------------------")
print("-----------------------------------              RRJETAT KOMPJUTERIKE             -------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------------\n")
print("FIEK-UDP Klienti \n")

serverName = ""
serverPort = 0

soketiKlientit = socket(AF_INET,SOCK_DGRAM)

serverName = input("Sheno emrin e serverit: ")
serverPort = int(input("Sheno portin: "))

komandaInput = "empty"

print("Shenoni EXIT per te dalur nga lidhja")
print("Nese doni te thirrni metodat me poshte keni, manualin \n\n")
print("IPADDRESS  -> Sheno IPADDRESS dhe do te gjeni IP adresen tuaj")
print("PORT       -> Sheno PORT dhe do te gjeni numrin e portit tuaj")
print("COUNT      -> Sheno COUNT {tekst} dhe do te gjeni sa zanore dhe sa bashtingllore ka ne fjaline tuaj")
print("REVERSE    -> Sheno REVERSE {tekst} dhe do te ua ktheje tekstin")
print("PALINDROME -> Sheno PALINDROME {tekst} dhe do te gjeni nese fjalia juaj eshte palindrome ose jo")
print("TIME       -> Sheno TIME dhe do te shtypet koha aktuale ne server")
print("GAME       -> Sheno GAME dhe do te shtypen 5 numra te rendomte nga 0 deri ne 35")
print("GCF        -> Sheno GCF {numer} {numer} dhe do te ju ktheje faktorin me te madhe te perbashket e ketyre dy numrave")
print("CONVERT    -> Sheno CONVERT {CmToFeet / FeetToCm / KmToMiles / MileToKm} VLERA dhe do te shtypet vlera e konvertuar")
print("              nga nje njesi ne tjetren")
print("POW        -> Sheno POW {numer} {numer} dhe do te ju ktheje numrin e pare ne fuqi te numrit te dyte")
print("TABELA     -> Sheno TABELA {PRIVAT/INSTITUCION} {PRISHTNIA/ MITROVICA/ PEJA/ PRIZRENI/ FERIZAJI/ GJILANI/ GJAKOVA}")
print("              dhe do te gjenerohet nje tabel e makines \n")
    

try:
    print("------------------------------------------------------------------------------------------------------------------------")
    komandaInput = input("Zgjedhja juaj: ")

    if komandaInput == "":
        soketiKlientit.sendto(str("ERROR").encode(),(serverName,serverPort))
    elif komandaInput.upper()!="EXIT":
        soketiKlientit.sendto(str(komandaInput).encode(),(serverName,serverPort))

    data, address = soketiKlientit.recvfrom(128)
    print(str(data.decode()).strip())
except Exception as e:
        print(str(e))   
print("------------------------------------------------------------------------------------------------------------------------")
print("!!! Vetem nje kerkese mund te dergohet !!!")

soketiKlientit.close()
