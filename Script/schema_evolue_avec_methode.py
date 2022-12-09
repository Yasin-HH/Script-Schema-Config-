#--------------IMPORT DES LIBRAIRIES ET BIBLIOTHEQUE------------
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
#------------------------------

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
                row['Type'] = row1['Machine_type']
            else:
                continue

    #ajout des addresses et masque
    for row in List_of_complet:
        for row1 in List_of_addresse:
            if row['Id_machine'] == row1['Id_machine']:
                row['adresse1'] = row1['Address1']
                row['adresse2'] = row1['Address2']
                row['Masque'] = row1['Masque']
            else:
                continue
            
    return List_of_complet
#--------------------------


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
def reseau_unique():
    global ip_08
    ip_08 = re.compile('^\d{1,3}\.')
    global ip_16
    ip_16 = re.compile('^\d{1,3}\.\d{1,3}\.')
    global ip_24v2
    ip_24v1 = re.compile('[0-9]*.[^0-9]')
    ip_24v2 = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.')
    List_of_addresse = adressecsv()

    list_reseau = []

    for row in List_of_addresse:
        #print('Ligne en action',row)
        x = []
        y = []
        
        if row['Masque']=='255.255.255.0':
            if row['Address1'] == '':
                continue
            else :
                x = re.findall(ip_24v2,row['Address1'])
                #print('x',x)
            if row['Address2'] == '':
                continue
            else:
                y = re.findall(ip_24v2,row['Address2'])
                #print('y',y)
                
        elif row['Masque']=='255.255.0.0': 
            if row['Address1'] == '':
                continue
            else :
                x = re.findall(ip_16,row['Address1'])
            if row['Address2'] == '':
                continue
            else:
                y = re.findall(ip_16,row['Address2'])
                
        elif row['Masque']=='255.0.0.0': 
            if row['Address1'] == '':
                continue
            else :
                x = re.findall(ip_08,row['Address1'])
            if row['Address2'] == '':
                continue
            else:
                y = re.findall(ip_08,row['Address2'])
                
        elif row['Masque']=='':
            continue
        
        else:
            print('Masque inexistant / pas ajouter au script')
            
        #print('avant',list_reseau)
        
        for elem in x:
            if x[0] in list_reseau:
                continue
            
            else:
                list_reseau.append(x[0])
                #print('ajout de x',list_reseau)
            
        #print('entre',list_reseau)
        for elem in y:
            if y[0] in list_reseau:
                continue
            else:
                list_reseau.append(y[0])
                #print('ajout de y',list_reseau)
         
        #print('apres',list_reseau)
            
    return list_reseau
            

#-------------------------GENERATION DE L'IMAGE AVEC CLUSTER PARTIE LOGIQUE----------                 
def gen_imgcluster():
    
    List_of_res = reseau_unique()
    List_of_complet = list_complet()
      
    interutil = [] #lier au find_Interface
    interutil1 = [] #lier au find_Interface
    
    with Diagram("Schema du reseau",show=False, filename="Image/Evolue_Avec_Cluster", direction="BT"):
        
    #---------------------------PARTIE NODE-----------------------------
        for row in List_of_complet:
            if row['Type'] == 'Switch':
                row['Image'] = OpsworksDeployments(str(row['Name']))
            else :
                continue
        
        for elem in List_of_res:
            #print('Reseau en cours',elem)
            with Cluster(elem):
                for row in List_of_complet:
                    #print('Ligne en action', row)

                    x =[] #Stock temporairement les reseau des adress1 avec l'expression reguliere
                    testad1 = [] #Liste qui va servire de test vis a vis de la liste reseau

                    if row['Masque'] == '255.255.255.0':
                        x = re.findall(ip_24v2,row['adresse1'])    
                        testad1.append(x[0])
                        #print('Adresse1 en cour de test',testad1)
                        if testad1[0] == elem:
                        #On passe à l'inisialisation
                            if row['Type'] == 'Routeur':
                                row['Image'] = VPCRouter(str(row['Name']))
                            elif row ['Type'] == 'Machine':
                                row['Image'] = Client(str(row['Name']))
                            else :
                                print('Error Type')
                        else:
                            continue      
                        
                    elif row['Masque'] == '255.255.0.0':
                        x = re.findall(ip_16,row['adresse1'])
                        testad1.append(x[0])
                        
                        if testad1[0] == elem:
                        #On passe à l'inisialisation
                            if row['Type'] == 'Routeur':
                                row['Image'] = VPCRouter(str(row['Name']))
                            elif row ['Type'] == 'Machine':
                                row['Image'] = Client(str(row['Name']))
                            else :
                                print('Error Type')
                        else:
                            continue   
                         
                    elif row['Masque'] == '255.0.0.0':
                        x = re.findall(ip_08,row['adresse1'])
                        testad1.append(x[0])
                        
                        if testad1[0] == elem:
                        #On passe à l'inisialisation
                            if row['Type'] == 'Routeur':
                                row['Image'] = VPCRouter(str(row['Name']))
                            elif row ['Type'] == 'Machine':
                                row['Image'] = Client(str(row['Name']))
                            else :
                                print('Error Type')
                        else:
                            continue 
                    elif row['Masque'] == '': 
                        continue
                    else:
                        print('Error Masque', row['Masque'], 'De la machine ID : ',row['Id_machine'])
                        
                    
                    #print('ligne de fin',row)
                    
#--------------------------------PARTIE EDGE---------------------------

        for row in List_of_complet:          
            #print(row)
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
   
   
gen_imgcluster()

