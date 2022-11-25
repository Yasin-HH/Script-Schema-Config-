#Utilisation de diagrams on utilise Graphviz pour rendre le diagramme.
#Puis on installe diagrams


#Cette ligne importera les morceaux de diagramme nécessaires pour créer les éléments de diagramme génériques. 
from diagrams import Cluster, Edge, Diagram
#Ajoutez les lignes suivantes pour importer les icônes Droplet, DbaasPrimary et Logstash : 
from diagrams.aws.management import OpsworksDeployments #Image Switch
from diagrams.aws.network import VPCRouter  #Image Routeur
from diagrams.onprem.client import Client   #Image Machine


import csv  #Import du mode csv
from io import StringIO





List_of_Interface = [];
List_of_Name = [];
List_of_Name2 = []
List_of_type = []

#Dictionnaire du Machine_Interface
with open ('CSV/Machine_Interface.csv','r')as MI:
    Interface = csv.DictReader(MI)

    for row in Interface :
        #Dictionnaire du CSV interfaces
        List_of_Interface.append(row)

    
#Dictionnaire du Machine_Name
with open ('CSV/Machine_Name.csv','r')as MI:
    Name = csv.DictReader(MI)

    for row in Name :
        #Dictionnaire du CSV Name
        List_of_Name.append(row)
        #Liste de tout les Noms des machines
        List_of_Name2.append(row['Machine_Name'])


#Recupere la liste sans doublon des types
with open ('CSV/Machine_Types.csv','r')as MT:
    Type = csv.reader(MT)
    Type.__next__()  #Enlever l'en tếte
    for row in Type :
        x = []
        y = []
        if row[1] in List_of_type:
            continue
        else :
            List_of_type.append(row[1])
        
print (List_of_type)













print(List_of_Interface)
print(List_of_Name)
print(List_of_Name2)





# Le showpeut l'ouvrir lors de la création, mais il a été défini sur False puisqu'on travaille sur un hôte Linux. 
# Le fichier généré sera nommé quelle que soit la chaîne assignée à filename. 
# La directionest la direction dans laquelle vous voulez que le diagramme soit imprimé. 
# Les valeurs prises en charge pour directionsommes TB(Haut -> Bas) et LR(Gauche -> Droite). 
with Diagram("Schema du reseau", show=False, filename="my-diagram", direction="BT"):

        i =1
        for i, row in List_of_type:
            if row == 'Routeur':
                R = VPCRouter("R{i}")
            elif row == 'Switch':
                S = OpsworksDeployments("S{i}")
            else : 
                M = Client("M")

#On crée une image du réseau
#-----------------------Partie Node----------------------------
        
        List_of_Name2[0] = R
        R2 = R 
        S1 = S
        M1 = M
        S2 = S
        M2 = M
  
        #Pour chaque Machine dans un Reseau on le place dedans


        #En fonction de son Type on lui attribue une Image
        #Partie Image
        #Utilisation du CSV --Machine_Type
        
        
        #Partie Nom 
        #Utilisation du CSV Machine_Name

        List_of_Name2[0] - S2

#--------------------Partie Edge (Lien)------------------------
#Utilisation du CSV Machine_Interface



        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#Fonctionnalité Avancée
#Ajout d'une ligne
'''def add_row(path):
    #éventuellement check si fichier existant et si non en créer un avec les fieldnames attendus en fonction du path fournit
    with open (path, 'a') as file:
        obj = csv.writer(file, dialect='excel')
        
        #test le chemin fournit pour vérifier de quel type est le fichier que l'on souhaite modifier
        try:
            
            if (path.contains("machine_name")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                machine_name = input("Please enter the machine_name you wish to add")
                obj.writerow([ID_machine, machine_name])
                
            elif (path.contains("Routing_table")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                network_address = input("Please enter the network_address you wish to add")
                mask = input("Please enter the mask you wish to add")
                interfaces = input("Please enter the interfaces you wish to add")
                obj.writerow([ID_machine, network_address, mask, interfaces])
                
            elif (path.contains("machine_address")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                address1 = input("Please enter the first address you wish to add")
                address2 = input("Please enter the second adress you wish to add")
                mask = input("Please enter the mask you wish to add")
                obj.writerow([ID_machine, address1, address2, mask])
                
            elif (path.contains("machine_interface")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                interface1 = input("Please enter the first interface you wish to add")
                interface2 = input("Please enter the second interface you wish to add")
                obj.writerow([ID_machine, interface1, interface2])
                
            elif (path.contains("machine_type")):
                ID_machine = input("Please enter the ID_machine you wish to add")
                machine_type = input("Please enter the type of the machine you wish to add")
                obj.writerow([ID_machine, machine_type])
        except:
            print("Error: the specified file is incorrectly named, verify it contains one of those: machine_name ; routing_table ; machine_address ; machine_interface ; machine_type")
    file.close()
'''



'''
import re #Utilisation des expressions régulières



#Recuperation des adresse de reseau en /24 -> 255.255.255.0
ip_24 = re.compile('[0-9]*.[^0-9]')


#Liste des adresses de reseau
list_of_res =[];

#Liste des Adresse IP
list_of_ip = [];


#FONCTION AVANCEE
#Recuperation de tout les reseaux Pour la création des clusteurs 
#Utilisation du CSV Machine_Adresse
with open ('CSV/Machine_Adresse.csv','r')as MA:
    listing = csv.reader(MA)
    listing.__next__()  #Enlever l'en tếte
    for row in listing :
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
    #l'expression reguliere separt en 3 bloc reseau don on doit les associers pour former la partie reseau
    x = ip_24.findall(list_of_ip[i])
    
    #fusion des elements d'une meme liste 
    y = ''.join(x)
    i=i+1
    #Ajout des ip reseau dans la list res alias "reseau"
    #avec le fait que le reseau soit unique
    if y in list_of_res:
        continue
    else : list_of_res.append(y)

print(list_of_res)

'''










#Fonctionnalité Avancée
#Suppression d'une ligne
'''def del_row(path, to_del):
    with open (path, 'w') as file:
        obj = csv.reader(file, dialect='excel')
        to_keep = "bloup"
        content = StringIO.write(to_keep)
        StringIO.close(content)
'''
#Rechercher un element d'un fichier csv
#def research(path, looking_for):
 #   with open (path, 'r') as file:
  #      obj = csv.reader(file, dialect='excel')
   #     next(obj) #sautez entête
    #    for row in obj
        
#def del_row(path, looking_for):
 #   with open(path, 'r') as file:
  #      obj = csv.reader(file)
   #     next(obj) #sautez entête
    #    to_keep = {(row[0], row[2]) for row in obj}

#    f = fileinput.input('fileA', inplace=True) # sys.stdout is redirected to the file
 #   print next(f), # write header as first line

#    w = csv.writer(sys.stdout)
 #   for row in csv.reader(f):
  #      if (row[0], row[2]) in to_keep: # write it if it's in B
   #         w.writerow(row)
            
#suppression ligne (copie du fichier minus la suppression)