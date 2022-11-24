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
        
            R1 = VPCRouter("R1")
            R2 = VPCRouter("R2")    
            S1 = OpsworksDeployments("S1")
            M1 = Client("M1")
            S2 = OpsworksDeployments("S2")
            M2 = Client("M2")
        
    
    
    #créer des dépendances entre les différents éléments du diagramme
    # - un lien 
    # << ou >> une flèche
    
    
    M1 - S1 
    S1 - R1
    M2 - S2 
    S2 - R2
    R2 - R1
    

