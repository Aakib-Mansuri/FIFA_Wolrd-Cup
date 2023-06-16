import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['FIFAWorldCup']
collection = db['Matches']
excelFile = open('MatchesDat.txt','r')

document = {
    '_id': 1,
    'MatchId': 1,
    'Country': 'India',
    'League': 'DSC',
    'Season': '2015/16',
    'Date': '12-1-12',
    'HomeTeam':{
        'Name': 'ABCM(BDT)',
        'Players':[
            {'FifaId': 1, 'Name': 'Aakib'},
            {'FifaId': 2, 'Name': 'Aakib'},
            {'FifaId': 3, 'Name': 'Aakib'},
            {'FifaId': 4, 'Name': 'Aakib'},
            {'FifaId': 5, 'Name': 'Aakib'},
            {'FifaId': 6, 'Name': 'Aakib'},
            {'FifaId': 7, 'Name': 'Aakib'},
            {'FifaId': 8, 'Name': 'Aakib'},
            {'FifaId': 9, 'Name': 'Aakib'},
            {'FifaId': 10, 'Name': 'Aakib'},
            {'FifaId': 11, 'Name': 'Aakib'}
        ]
    },
    
    'AwayTeam':{
        'Name': 'SAKM(DT)',
        'Players':[
            {'FifaId': 1, 'Name': 'Aakib'},
            {'FifaId': 2, 'Name': 'Aakib'},
            {'FifaId': 3, 'Name': 'Aakib'},
            {'FifaId': 4, 'Name': 'Aakib'},
            {'FifaId': 5, 'Name': 'Aakib'},
            {'FifaId': 6, 'Name': 'Aakib'},
            {'FifaId': 7, 'Name': 'Aakib'},
            {'FifaId': 8, 'Name': 'Aakib'},
            {'FifaId': 9, 'Name': 'Aakib'},
            {'FifaId': 10, 'Name': 'Aakib'},
            {'FifaId': 11, 'Name': 'Aakib'}
        ]
    },

    'Goals':{'HomeTeam': 1, 'AwayTeam': 1}
}

id = 1                
for line in excelFile:
    i = 0
    lineArray = line.split('\t')
    for key in document.keys():
        if key == '_id':
            document[key] = id
            id += 1

        elif type(document[key]) == type({}):
            for miniKey in document[key].keys():
                if type(document[key][miniKey]) == type([]):
                    for player in range(0,len(document[key][miniKey])):
                        if lineArray[i] != 'NULL':
                            document[key][miniKey][player]['FifaId'] = int(lineArray[i])  
                        else:
                            document[key][miniKey][player]['FifaId'] = lineArray[i]
                        i += 1
                        document[key][miniKey][player]['Name'] = lineArray[i]
                        i += 1
                else:
                    if miniKey in ('HomeTeam','AwayTeam'):
                        document[key][miniKey] = int(lineArray[i])
                    else:
                        document[key][miniKey] = lineArray[i]
                    i += 1
        else:
            if key == 'MatchId': 
                document[key] = int(lineArray[i])
            else:
                document[key] = lineArray[i]
            i+=1
        
    collection.insert_one(document)