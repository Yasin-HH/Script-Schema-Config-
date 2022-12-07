
import re #Utilisation des expressions régulières
from diagrams import Cluster, Edge, Diagram
from diagrams.aws.network import VPCRouter  #Image Routeur
from diagrams.onprem.client import Client   #Image Machine
from diagrams.aws.management import OpsworksDeployments #Image Switch
import csv 
from io import StringIO

#------------------------OUVERTURE DES csv----------------------
    
def interfacecsv(): 
    List_of_Interface = []
    #Dictionnaire du Machine_Interface
    with open ('csv/Machine_Interface.csv','r')as MI:
        for row in csv.DictReader(MI):
            List_of_Interface.append(row)
    return List_of_Interface
        
def namecsv():        
    List_of_Name = []
    #Dictionnaire du Machine_Name
    with open ('csv/Machine_Name.csv','r')as MI:
        for row in csv.DictReader(MI):
            List_of_Name.append(row)
    return List_of_Name

def typecsv():
    List_of_type = []
    #Dictionnaire du types
    with open ('csv/Machine_Type.csv','r')as MT:
        for row in csv.DictReader(MT):
            List_of_type.append(row)
    return List_of_type

def adressecsv():
    List_of_addresse = []
    #Dictionnaire du types
    with open ('csv/Machine_Address.csv','r')as MA:
        for row in csv.DictReader(MA):
            List_of_addresse.append(row)
        return List_of_addresse


#--------------AJOUT DE TOUT LES DONNES DANS UN DICTIONNAIRE--------

def list_complet():
    List_of_Interface = interfacecsv()
    List_of_Name = namecsv()
    List_of_type = typecsv()
    List_of_addresse = adressecsv()
    #Ajout de l'interface
    List_of_complet = List_of_Interface.copy()
    
    #ajout du name
    for row in List_of_complet:
        for row1 in List_of_Name:
            if row['Id_machine'] == row1['Id_machine']:
                row['Name'] = row1['Machine_name']
            else:
                continue
    
    #ajout du type
    for row in List_of_complet:
        for row1 in List_of_type:
            if row['Id_machine'] == row1['Id_machine']:
                row['Type'] = row1['Machine_Type']
            else:
                continue

    #ajout des addresses et masque
    for row in List_of_complet:
        for row1 in List_of_addresse:
            if row['Id_machine'] == row1['Id_machine']:
                row['adresse1'] = row1['Adress1']
                row['adresse2'] = row1['Adress2']
                row['Masque'] = row1['Masque']
            else:
                continue
            
    return List_of_complet



#-------------------------RECUPERATION DES INTERFACES DES MACHINES---------------------------
#tdebut "recherche de liens"
def find_Interface(path, looking_for):
    
    with open(path, 'r') as file:
        if (path.__contains__("csv/Machine_Interface")):
            reader = csv.DictReader(file)
            result = []
            for line in reader:
                test1 = line["Interface1"]
                test2 = line["Interface2"]
                if (test1.__contains__(looking_for)):
                    result.append(test1)
                if (test2.__contains__(looking_for)):
                    result.append(test2)
            
            return result
        else:
            print("here should be an error")
            
#fin "recherche de liens"
def find_Interface2(path, looking_for):
    with open(path, 'r') as file:
        if (path.__contains__("csv/Machine_Interface")):
            reader = csv.DictReader(file)
            result = []
            for line in reader:
                test2 = line["Interface2"]
                if (test2.__contains__(looking_for)):
                    result.append(test2)
            return result
        else:
            print("here should be an error")
#fin "recherche de liens"

#-----------------------RECUPERATION DES RESEAU UNIQUE
def resunique():

    ip_24 = re.compile('[0-9]*.[^0-9]')      #Recuperation des adresse de reseau en /24 -> 255.255.255.0
    list_of_res =[]         #Liste des adresses de reseau
    list_of_ip = []         #Liste des Adresse IP

    
    #Recuperation de tout les reseaux Pour la création des clusteurs 
    #Utilisation du CSV Machine_Adresse
    with open ('csv/Machine_Address.csv','r')as MA:
        for row in csv.reader(MA):        
    #Si l'adresse 1 est vide on passe sinon on l'insert dans la list_of_ip
            if row[1] == '':
                continue
            else : 
                list_of_ip.append((row[1])) 
                    
            #Si l'adresse 2 est vide on passe sinon on l'insert dans la list_of_ip
            if row[2] == '':        
                continue
            else : 
                list_of_ip.append((row[2]))

    #recuperation de tout les ip des machine
    print(list_of_ip)


    x = [];
    y = [];
    i=0

    #utilisation de l'expressions reguliere pour avoir seulement la partie reseau de l'ip
    while i < len(list_of_ip):
        #l'expression reguliere separt en 3 bloc reseau, on doit les associers pour former la partie reseau
        x = ip_24.findall(list_of_ip[i])
        
        #fusion des elements d'une meme liste 
        y = ''.join(x)
        i=i+1
        #Ajout des ip reseau dans la list res alias "reseau"
        #avec le fait que le reseau soit unique
        if y in list_of_res:
            continue
        else : list_of_res.append(y)
    return list_of_res

#-------------------------GENERATION DE L'IMAGE BASIC------------------------
def gen_img():
    
    
    List_of_complet = list_complet()
    interutil = [] #lier au find_Interface
    interutil1 = [] #lier au find_Interface
     
 
    with Diagram("Schema du reseau", show=False, filename="Image/Image_basic1", direction="BT"):

#-----------------------Partie Node----------------------------
        #A chaque Type on lui attribue une image specifice  
        for row in List_of_complet:
            if row['Type'] == 'Routeur':
                row['Image'] = VPCRouter(str(row['Name']))
            elif row['Type'] == 'Switch':
                row['Image'] = OpsworksDeployments(str(row['Name']))
            elif row ['Type'] == 'Machine':
                row['Image'] = Client(str(row['Name']))
            else :
                print('Error Type')
                
#--------------------Partie Edge (Lien)------------------------ 


        #CLUSTER

        
        
        
        for row in List_of_complet:          
            interutil.append(row['Interface1'])
            search = row['Interface1']
            search = search[3:]
            result = find_Interface("csv/Machine_Interface.csv",search)
            result.remove(str(row['Interface1']))
            for elem in result:
                if elem in interutil:
                    continue
                else :
                    for row1 in List_of_complet:
                        if elem == row1['Interface1']:
                            row['Image'] - row1['Image']
                        elif elem == row1['Interface2']:
                            row['Image'] - row1['Image']
            result = []
            #print("Inrerutils")
            
        interutil = []
        for row in List_of_complet:
            if row['Interface2'] == "":
                continue
            else:
                interutil.append(row['Interface2'])
                search = row['Interface2']
                search = search[3:]
                result = find_Interface2("csv/Machine_Interface.csv",search)
                result.remove(str(row['Interface2']))
                for elem in result:
                    if elem in interutil:
                        continue
                    else :
                        
                        for row1 in List_of_complet:
                            if elem == row1['Interface2']:
                                row['Image'] - row1['Image']
                result = []            
                
            
                

list_complet()
gen_img()
test = resunique()
print(test)
