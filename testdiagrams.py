#Utilisation de diagrams on utilise Graphviz pour rendre le diagramme.
#Puis on installe diagrams


#Cette ligne importera les morceaux de diagramme nécessaires pour créer les éléments de diagramme génériques. 
from diagrams import Cluster, Edge, Diagram

#Ajoutez les lignes suivantes pour importer les icônes Droplet, DbaasPrimary et Logstash : 

#Image Switch
from diagrams.aws.management import OpsworksDeployments
#Image Routeur
from diagrams.aws.network import VPCRouter
#Image Machine
from diagrams.onprem.client import Client

#Import du mode csv
import csv

#La showpeut l'ouvrir lors de la création, mais il a été défini sur Falsepuisque vous travaillez sur un hôte Linux. 
# Le fichier généré sera nommé quelle que soit la chaîne assignée à filename. 
# La directionest la direction dans laquelle vous voulez que le diagramme soit imprimé. 
# Les valeurs prises en charge pour directionsommes TB(Haut -> Bas) et LR(Gauche -> Droite). 
# Sélection du directionpeut faciliter la lecture du schéma. Pour ce diagramme, vous utiliserez LR.
with Diagram("Schema du reseau", filename="my-diagram", direction="BT"):
    with Cluster ("Reseau"):
        
        with Cluster("192.168.3"):
            
            Routeur1 = VPCRouter("Routeur1")
            Routeur2 = VPCRouter("Routeur2")
            
        with Cluster("192.168.1"):
            Routeur1
            switch1 = OpsworksDeployments("Switch1")
            Machine1 = Client("Machine1")
            
        with Cluster("192.168.2"):
            Routeur2
            switch2 = OpsworksDeployments("Switch2")
            Machine2 = Client("Machine2")
        
    
    
    #créer des dépendances entre les différents éléments du diagramme
    # - un lien 
    # << ou >> une flèche
    Machine1 - switch1 - Routeur1 
    Machine2 - switch2 - Routeur2  
    Routeur2 - Routeur1
    

