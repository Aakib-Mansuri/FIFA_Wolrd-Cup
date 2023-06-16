import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['FIFAWorldCup']
collection = db['Players']
excelFile = open('PlayersDat.txt','r')

document = {
    '_id': 1,
    'FifaId': 1,
    'Name': 'AAkib',
    'DOB': '2002-05-01',
    'Height': 6.7,
    'Weight': 55,
    'Performance':{
        'OverallRating': 99,
        'Balance': 65,
        'Stamina': 70,
        'Strength': 55
    }
}

                
for line in excelFile:
    lineArray = line.split('\t')
    i = 0
    for key in document.keys():
        if type(document[key]) == type({}):
            for miniKey in document[key].keys():
                if lineArray[i] != 'NULL':
                    document[key][miniKey] = int(lineArray[i])  
                else:
                    document[key][miniKey] = lineArray[i]
                i += 1
                
        else:
            if key in ('Name','DOB'): 
                document[key] = lineArray[i]
            else:
                document[key] = int(lineArray[i])
            i+=1
        
    collection.insert_one(document)