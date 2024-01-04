"""
Your module description
"""
#import jsonFileHandler
#import sys
#sys.path.append("/home/ec2-user/environment/")

#from jsonFileHandler import readJsonFile 

import odc.jsonFileHandler as jsonFileHandler

data = jsonFileHandler.readJsonFile('files/insulin.json')
#data = readJsonFile('files/insulin.json')

if data != "" :
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
else:
    print("Error. Exiting program")