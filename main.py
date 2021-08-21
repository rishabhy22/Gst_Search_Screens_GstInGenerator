import firebase_admin
from firebase_admin import credentials,firestore
import random
import string
import datetime


creds = credentials.Certificate("E:\\programs\\PythonPrograms\\Experiments\\GstSearchScreens\\gst-search-50d04-firebase-adminsdk-8p6z5-9399b92e13.json")
f = open("E:\\programs\\PythonPrograms\\Experiments\\GstSearchScreens\\gstINs.txt", "a")
firebase_admin.initialize_app(credential=creds)

firestoreDB = firestore.client()

collectionRef= firestoreDB.collection(u'gstINs')


dates=[int(datetime.datetime(2017, 12, 2,10,24).timestamp()*1000),
        int(datetime.datetime(2013, 8, 11,23,59).timestamp()*1000),
       int(datetime.datetime(2015, 1, 30,16,11).timestamp()*1000),
        int(datetime.datetime(2020, 7, 21,22,13).timestamp()*1000),
        int(datetime.datetime(2016, 3, 24,16,20).timestamp()*1000),
        int(datetime.datetime(2017, 5, 13,1,16).timestamp()*1000)]

WORDS1 = ["Masters","Oil","Food","Water","Tech","Books"]
WORDS2 =    ["India","USA","Pakistan","Bangladesh","UAE","UK"]
WORDS3=["Limited","Private","Mearge","Organization","Corporation"]

pADD=[["K-37","B-46","L-98","D-6","P-100","J-4"],
    ["Mandoli","Vikas Nagar","Chowk","Chandni Chowk","Marine Drive","Azara"],
    ["Industrial Area","Rural Area","Urban"],
    ["Delhi","Lucknow","Mumbai","Dehradun","Hyderabad","Pune","Noida","Bengaluru"],
    ["119003","226022","344011","811231","161011","345920","827821","100291","826181"]]

aADD=["Floor","Top Floor","Middle"]

COB=[["Private","Public","Cooperative"],["Limited","Corporation","Organization","Company","Mearge"]]

tType=["Regular","Composition"]

for i in range(100):
    gstIn=''.join(random.choices(string.ascii_uppercase + string.digits,k=15))
    company=' '.join(random.choices(WORDS1)+random.choices(WORDS2)+random.choices(WORDS3))
    status= True if i%2 else False
    principalAddress=','.join(random.choice(add) for add in pADD)
    additionalAddress= random.choice(aADD)
    stateJuri='WARD '+ ''.join(random.choices(string.digits,k=2))
    centreJuri='RANGE - ' + ''.join(random.choices(string.digits,k=3))
    taxpayerType= random.choice(tType)
    cob=' '.join(random.choices(c)[0] for c in COB)
    dor=random.choice(dates)
    doc=random.choice(dates)
    if dor>doc:
        doc=None

    f.write(gstIn+'\n')
    collectionRef.document(gstIn).set({
        'gstIn':gstIn,
        'company':company,
        'principalAddress':principalAddress,
        'additionalAddress':additionalAddress,
        'stateJurisdiction':stateJuri,
        'centreJurisdiction':centreJuri,
        'taxpayerType':taxpayerType,
        'constitutionOfBusiness':cob,
        'dateOfReg':dor,
        'dateOfCanc':doc,
        'status':status
    })
    print(i,dor,doc)

f.close()