import csv 
list_of_ip = []
i=1


with open ('CSV/Machine_Adresse.csv','r')as MA:
        listing = list(csv.reader(MA))   
        
        for row in listing :
            #Si l'adresse 1 est vide on passe sinon on l'insert dans la list_of_ip
            if listing[1] == '':
                    continue
            else : list_of_ip.append((listing[i])[1]) 
                
            #Si l'adresse 2 est vide on passe sinon on l'insert dans la list_of_ip
            if listing[2] == '':        
                continue
            else : list_of_ip.append((listing[i])[2])
            i= i+1
            
print(list_of_ip)