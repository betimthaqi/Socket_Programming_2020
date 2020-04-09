from socket import *
import random
import datetime
import sys
import threading
import math

print("-----------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------                   BETIM THAÇI                 -------------------------------------")
print("-----------------------------------            UNIVERSITETI I PRISHTINES          -------------------------------------")
print("-----------------------------------      INXHINIERI KOMPJUTERIKE DHE ELEKTRIKE    -------------------------------------")
print("-----------------------------------              RRJETAT KOMPJUTERIKE             -------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------------\n")
print("FIEK-UDP Serveri \n")

serverPort = 13000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print('Serveri startoi ne hostin lokal me IP adrese: ' + str(gethostbyname(gethostname())) + " ne portin: " + str(serverPort))
print('Serveri eshte gati te pranoje kerkesen')

#metoda IPADDRESS
def IPADDRESS(address):
    return str(address[0])

# metoda PORT
def PORT(address):
    return str(address[1])

# metoda COUNT
def COUNT(fjalia):
    zan = 0;
    basht = 0;
    ZANORET = ['A','E','Ë','I','O','U','Y','a','e','ë','i','o','u','y']
    BASHT = ['Q', 'R', 'T', 'P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','q','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    for i in str(fjalia):
        if i in ZANORET:
            zan += 1
        elif i in BASHT:
            basht+= 1
    return "Zanore " + str(zan) + " Bashtingllore " + str(basht)
   

# metoda REVERSE
def REVERSE(fjalia):
    fjalia1 = fjalia[::-1].strip()
    return fjalia1

# metoda PALINDROME
def PALINDROME(fjalia):    
    string1 = fjalia.replace(" ","")
    if(string1[::1] == string1[::-1]):
        return str("palindrome")
    else:
        return str("jopalindrome")
    
# metoda TIME
def TIME():
    koha = datetime.datetime.now()
    rezultati = "Data:      Ora: \n" + koha.strftime("%d.%m.%Y %I:%M:%S %p")
    return str(rezultati)

# metoad GAME
def GAME():
    numrat = []
    for x in range(5):
        numrat.append(random.randint(1,35))
    numrat.sort()
    numratstring = str(numrat)
    return numratstring

# metoda GCF
def GCF(nr1, nr2):
    try:
         x = int(nr1)
         y = int(nr2)
    except:
        return "Error"
    gcd = math.gcd(x,y)     
    return str(gcd)

# metoda CONVERT
def CONVERT(opsioni,vleraHyrese):
    try:
        vlera = float(vleraHyrese)
    except:
        return "Error"
    if opsioni=="CmToFeet":
        rezultati = (vlera/30.40)
    elif opsioni=="FeetToCm":
        rezultati = (vlera*30.40)
    elif opsioni=="KmToMiles":
        rezultati = (vlera/1.60)
    elif opsioni=="MileToKm":
        rezultati = (vlera*1.60)
    else:
        return "Error"
    rezultati = "{:.2f}".format(rezultati)
    return str(rezultati)

# metoda POW
def POW(nr1, nr2):
    try:
         x = int(nr1)
         y = int(nr2)
    except:
        return "Error"
    powr = pow(x,y)     
    return str(powr)

# metoda TABELA
def TABELA(opsioni,vlera):
    if vlera=="PRISHTINA":
        qyteti = "01"
    elif vlera=="MITROVICA":
        qyteti = "02"
    elif vlera=="PEJA":
        qyteti = "03"
    elif vlera=="PRIZRENI":
        qyteti = "04"
    elif vlera=="FERIZAJI":
        qyteti = "05"
    elif vlera=="GJILANI":
        qyteti = "06"
    elif vlera=="GJAKOVA":
        qyteti = "07"
    else:
        return "Error"
    randomnumber = random.randint(100,999)
    alfabeti = 'QERTYUIOPASDFGHJKLZXCVBNM'
    shkronjat = ''.join(random.sample(alfabeti,2))
    if opsioni=="PRIVAT":
        return str(qyteti + " - " + str(randomnumber) + " - " + shkronjat)
    elif opsioni=="INSTITUCION":
        return str(qyteti + "Z" + " - " + str(randomnumber) + " - " + shkronjat)
    else:
        return "Error"

# metoda DERGESAKLIENT
def DERGESAKLIENT(IPKlientit,portiKlientit,mesazhi):
    try:
        print("----------------------------------------------------MESAZH-------------------------------------------------------------")
        print("Te dhenat e derguara tek klienti "+str(IPKlientit)+" me numer te portit " + str(portiKlientit) + " jane:\n\"" + mesazhi + "\"")
    except Exception as e:
        print(str(e))


error = False

kerkesa = (bytes)("empty".encode())
try:
     while str(kerkesa.decode())!="":
         kerkesa, addr = serverSocket.recvfrom(128)
         kerkesaStr = str(kerkesa.decode()).strip()
         kerkesaArray = kerkesaStr.split(' ')
         fjalapar = kerkesaArray[0]
         kerkesaArray[0] = kerkesaArray[0].upper()

         # metoda IPADDRESS
         if kerkesaArray[0]=="IPADDRESS":
             if(len(kerkesaArray)>1):
                 error=True
             else:
                 DERGESAKLIENT(addr[0],addr[1],"IP adresa juaj eshte: "+IPADDRESS(addr))
                 serverSocket.sendto(("IP adresa juaj eshte: "+IPADDRESS(addr)).encode(),addr)
         # metoda PORT
         elif kerkesaArray[0]=="PORT":
             if(len(kerkesaArray)>1):
                 error=True
             else:
                 DERGESAKLIENT(addr[0],addr[1],"Numri i portit tuaj eshte: "+PORT(addr))
                 serverSocket.sendto(("Numri i portit tuaj eshte: "+PORT(addr)).encode(),addr)
         # metoda COUNT
         elif kerkesaArray[0]=="COUNT":
             fjaliaShenuar = kerkesaStr.replace(fjalapar,"",1)
             rezultati = "Ne fjaline tuaj \"" + fjaliaShenuar.strip() + "\" ka: " + COUNT(fjaliaShenuar.strip())
             DERGESAKLIENT(addr[0],addr[1],rezultati)
             serverSocket.sendto(rezultati.encode(),addr)
         # metoda REVERSE
         elif kerkesaArray[0]=="REVERSE":
             fjaliaShenuar = kerkesaStr.replace(fjalapar,"",1)
             rezultati = "Fjalia juaj e shenuar eshte: " + REVERSE(fjaliaShenuar)
             DERGESAKLIENT(addr[0],addr[1],rezultati)
             serverSocket.sendto(rezultati.encode(),addr)
         # metoda PALINDROME
         elif kerkesaArray[0]=="PALINDROME":
             fjaliaShenuar = kerkesaStr.replace(fjalapar,"",1)
             rezultati = "Fjalia juaj e shenuar \"" + fjaliaShenuar.strip() + "\" eshte " + PALINDROME(fjaliaShenuar) 
             DERGESAKLIENT(addr[0],addr[1],rezultati)
             serverSocket.sendto(rezultati.encode(),addr)
         # metoda TIME
         elif kerkesaArray[0]=="TIME":
             if(len(kerkesaArray)>1):
                 error=True
             else:
                 DERGESAKLIENT(addr[0],addr[1],TIME())
                 serverSocket.sendto(TIME().encode(),addr)
         # metoda GAME
         elif kerkesaArray[0]=="GAME":
             if(len(kerkesaArray)>1):
                 error=True
             else:
                 DERGESAKLIENT(addr[0],addr[1],"Rezultatet nga loja: "+GAME())
                 serverSocket.sendto(("Rezultatet nga loja: "+GAME()).encode(),addr)
         # metoda CONVERT
         elif kerkesaArray[0]=="CONVERT":
             for i in range(len(kerkesaArray)):
                 if "" in kerkesaArray:
                     kerkesaArray.remove("")
             if len(kerkesaArray)>3 or len(kerkesaArray)<3:
                 error=True
             else:
                 if str(CONVERT(str(kerkesaArray[1]),kerkesaArray[2]))=="Error":
                     error = True                 
                 else:
                     arrayPerShtypje = str(kerkesaArray[1]).lower().split("to")
                     rezultati = kerkesaArray[2] + " " + str(arrayPerShtypje[0]) + " jane te barabarte me " + CONVERT(str(kerkesaArray[1]),kerkesaArray[2]) + " " + str(arrayPerShtypje[1])
                     DERGESAKLIENT(addr[0],addr[1],str(rezultati))
                     serverSocket.sendto(str(rezultati).encode(),addr)
         # metoda TABELA
         elif kerkesaArray[0]=="TABELA":
             for i in range(len(kerkesaArray)):
                 if "" in kerkesaArray:
                     kerkesaArray.remove("")
             if len(kerkesaArray)>3 or len(kerkesaArray)<3:
                 error=True
             else:
                 if str(TABELA(str(kerkesaArray[1]),kerkesaArray[2]))=="Error":
                     error = True                 
                 else:
                     rezultati = "Tabela e gjeneruar sipas kerkesave tuaja eshte: " + TABELA(str(kerkesaArray[1]),str(kerkesaArray[2]))
                     DERGESAKLIENT(addr[0],addr[1],str(rezultati))
                     serverSocket.sendto(str(rezultati).encode(),addr)
         # metoda GCF
         elif kerkesaArray[0]=="GCF":
             for i in range(len(kerkesaArray)):
                 if "" in kerkesaArray:
                     kerkesaArray.remove("")
             if len(kerkesaArray)>3 or len(kerkesaArray)<3:
                 error=True
             else:
                 if GCF(kerkesaArray[1],kerkesaArray[2])=="Error":
                     error = True                 
                 else:
                     rezultati = "Faktori me i madhe i perbashket i numrit " + kerkesaArray[1] + " dhe numrit " + kerkesaArray[2] + " eshte numri " + GCF(kerkesaArray[1],kerkesaArray[2])
                     DERGESAKLIENT(addr[0],addr[1],rezultati)
                     serverSocket.sendto(rezultati.encode(),addr)
         # metoda POW
         elif kerkesaArray[0]=="POW":
             for i in range(len(kerkesaArray)):
                 if "" in kerkesaArray:
                     kerkesaArray.remove("")
             if len(kerkesaArray)>3 or len(kerkesaArray)<3:
                 error=True
             else:
                if POW(kerkesaArray[1],kerkesaArray[2])=="Error":
                     error = True                 
                else:
                     rezultati = "Numri " + kerkesaArray[1] + " i ngritur ne fuqi " + kerkesaArray[2] + " eshte i barabarte me " + POW(kerkesaArray[1],kerkesaArray[2])
                     DERGESAKLIENT(addr[0],addr[1],rezultati)
                     serverSocket.sendto(rezultati.encode(),addr)

         # asnjona prej metodave me larte
         else:
             serverSocket.sendto("Kerkesa juaj eshte invalide, ju lutem provoni perseri!".encode(),addr)

         # error = true
         if error==True:
             serverSocket.sendto("Kerkesa juaj eshte invalide, ju lutem rregulloni gabimin!".encode(),addr)
             error = False

except Exception as e:
        print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR")
        print(str(e))
