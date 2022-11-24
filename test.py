
from diagrams import Cluster, Edge, Diagram
from diagrams.aws.management import OpsworksDeployments
from diagrams.aws.network import VPCRouter
from diagrams.onprem.client import Client


with Diagram("Schema du reseau", filename="my-diagramtest", direction="BT"):
    with Cluster ("Reseau"):
        
            R1 = VPCRouter("R1")
            R2 = VPCRouter("R2")    
            S1 = OpsworksDeployments("S1")
            M1 = Client("M1")
            S2 = OpsworksDeployments("S2")
            M2 = Client("M2")
    
    
    M1 - S1 
    S1 - R1
    M2 - S2 
    S2 - R2
    R2 - R1
    

