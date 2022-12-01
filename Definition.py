import csv

#tdebut "recherche de liens"
def find_Interface(path, looking_for):
    with open(path, 'r') as file:
        if (path.__contains__("CSV/Machine_Interface")):
            reader = csv.DictReader(file)
            result = []
            for line in reader:
                test1 = line["Interface1"]
                test2 = line["Interface2"]
                if (test1.__contains__(looking_for)):
                    result.append(test1)
                if (test2.__contains__(looking_for)):
                    result.append(test2)
            print(result)
            return result
        else:
            print("here should be an error")
#fin "recherche de liens"

#créer un dictionnaire pour le nom des machines
def dict_MachineName(path):
    with open(path , 'r') as file:
        if (path.__contains__("CSV/Machine_Name")):
            result = {}
            reader = csv.DictReader(file)
            for line in reader:
                result[line["Id_Machine"]]=line["Machine_Name"]
            print(result)
            return result
        else:
            print("here should be an error n2")
            
find_Interface("CSV/Machine_Interface.csv",'/0')
