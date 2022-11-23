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
    

#Liste des Adresse IP
list_of_ip = [];

# Le showpeut l'ouvrir lors de la création, mais il a été défini sur False puisqu'on travaille sur un hôte Linux. 
# Le fichier généré sera nommé quelle que soit la chaîne assignée à filename. 
# La directionest la direction dans laquelle vous voulez que le diagramme soit imprimé. 
# Les valeurs prises en charge pour directionsommes TB(Haut -> Bas) et LR(Gauche -> Droite). 
with Diagram("Schema du reseau", show=False, filename="Schema de configuration Reseau", direction="BT"):


#Fonctionnalité du Noyau
#Avec des fichiers CSV déjà configurer
#On crée une image du réseau


#-----------------------Partie Node----------------------------
#Recuperation de tout les reseaux Pour la création des clusteurs 
#Utilisation du CSV Machine_Adresse
    with open ('CSV/Machine_Adresse.csv','r')as MA:
        listing = csv.reader(MA)
        listing.__next__()
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
            
print(list_of_ip)   

#Avec la liste des ip des machines recupérer seulement l'ip du reseau
        
            
        #Pour chaque Machine dans un Reseau on le place dedans


        #En fonction de son Type on lui attribue une Image
        #Partie Image
        #Utilisation du CSV --Machine_Type
        
        
        #Partie Nom 
        #Utilisation du CSV Machine_Name



#--------------------Partie Edge (Lien)------------------------
#Utilisation du CSV Machine_Interface










#Fonctionnalité Avancée
#Ajout d'une ligne
def add_row(path):
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


#Fonctionnalité Avancée
#Suppression d'une ligne
def del_row(path, to_del):
    with open (path, 'w') as file:
        obj = csv.reader(file, dialect='excel')
        to_keep = "bloup"
        content = StringIO.write(to_keep)
        StringIO.close(content)




#Hugo c'est quoi ?
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