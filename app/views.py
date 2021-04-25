from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib, base64
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
import requests
import pyrebase 

'''fireConfig={
    your firebase information here
    delete the string apostrophes if using firebase
}
fire=pyrebase.initialize_app(fireConfig)'''

data=pd.read_csv("cpdata.csv")
d1=list(data["temperature"][:30])
dicti={'rice': 0,'maize': 1,'chickpea': 2,'kidneybeans': 3,'pigeonpeas': 4,'mothbeans': 5,'mungbean': 6,'blackgram': 7,
 'lentil': 8,'pomegranate': 9,'banana': 10,'mango': 11,'grapes': 12,'watermelon': 13,'muskmelon': 14,'apple': 15,
 'orange': 16,'papaya': 17,'coconut': 18,'cotton': 19,'jute': 20,'coffee': 21}

months=['Sept19','Oct19', 'Nov19', 'Dec19','Jan20', 'Feb20', 'Mar20', 'Apr20','May20', 'Jun20',
 'Jul20','Aug20', 'Sept20','Oct20','Nov20','Dec20']

msp={'rice': {'MSP2019': 1815, 'Wholesep19': 1831, 'whooct19': 1829, 'incmsp': 80, 'incwho': 64,
  'price':[1550,1715,1735,1719,1677,1674,1653,1659,1655,1639,1651,1657,1662,1750,1688,1738]},
 'cotton': {'MSP2019': 5255, 'Wholesep19': 5378, 'whooct19': 5066, 'incmsp': 160, 'incwho': -365,
 'price':[4450,5029,5005,4333,4929,4303,4461,4031,4110,4149,4282,4530,4494,4890,4713,4710]},
 'maize': {'MSP2019': 1760, 'Wholesep19': 2065, 'whooct19': 2003, 'incmsp': 60, 'incwho': -68,
 'price':[1900,2842,2720,2718,2579,2599,2710,2594,2523,2448,2541,2604,2575,2897,2651,2619]},
 'mungbean': {'MSP2019': 7050, 'Wholesep19': 6253, 'whooct19': 6466, 'incmsp': 350, 'incwho': -1008,
 'price':[5400,5599,5442,5396,5099,5121,5035,4933,4919,4695,4678,4795,4755,5600,4906,5223]},
 'lentil': {'MSP2019': 4800, 'Wholesep19': 4834, 'whooct19': 4890, 'incmsp': 300, 'incwho': -1821,
 'price':[1550,1715,1735,1719,1677,1674,1653,1659,1655,1639,1651,1657,1662,1750,1688,1738]},
 'jute': {'MSP2019': 3950, 'Wholesep19': 4291, 'whooct19': 4313, 'incmsp': 300, 'incwho': -996,
 'price':[1550,1715,1735,1719,1677,1674,1653,1659,1655,1639,1651,1657,1662,1750,1688,1738]},
 'chickpea': {'MSP2019': 1815, 'Wholesep19': 1831, 'whooct19': 1829, 'incmsp': 80, 'incwho': 64,
  'price':[1550,1715,1735,1719,1677,1674,1653,1659,1655,1639,1651,1657,1662,1750,1688,1738]},
 'kidneybeans': {'MSP2019': 5255, 'Wholesep19': 5378, 'whooct19': 5066, 'incmsp': 160, 'incwho': -365,
 'price':[4450,5029,5005,4333,4929,4303,4461,4031,4110,4149,4282,4530,4494,4890,4713,4710]},
 'pigeonpeas': {'MSP2019': 1760, 'Wholesep19': 2065, 'whooct19': 2003, 'incmsp': 60, 'incwho': -68,
 'price':[1900,2842,2720,2718,2579,2599,2710,2594,2523,2448,2541,2604,2575,2897,2651,2619]},
 'mothbeans': {'MSP2019': 7050, 'Wholesep19': 6253, 'whooct19': 6466, 'incmsp': 350, 'incwho': -1008,
 'price':[5400,5599,5442,5396,5099,5121,5035,4933,4919,4695,4678,4795,4755,5600,4906,5223]},
 'blackgram': {'MSP2019': 4800, 'Wholesep19': 4834, 'whooct19': 4890, 'incmsp': 300, 'incwho': -1821,
 'price':[1550,1715,1735,1719,1677,1674,1653,1659,1655,1639,1651,1657,1662,1750,1688,1738]},
 'pomegranate': {'MSP2019': 3950, 'Wholesep19': 4291, 'whooct19': 4313, 'incmsp': 300, 'incwho': -996,
 'price':[1550,1715,1735,1719,1677,1674,1653,1659,1655,1639,1651,1657,1662,1750,1688,1738]},
 'banana': {'MSP2019': 1815, 'Wholesep19': 1831, 'whooct19': 1829, 'incmsp': 80, 'incwho': 64,
  'price':[1550,1715,1735,1719,1677,1674,1653,1659,1655,1639,1651,1657,1662,1750,1688,1738]},
 'mango': {'MSP2019': 5255, 'Wholesep19': 5378, 'whooct19': 5066, 'incmsp': 160, 'incwho': -365,
 'price':[4450,5029,5005,4333,4929,4303,4461,4031,4110,4149,4282,4530,4494,4890,4713,4710]},
 'grapes': {'MSP2019': 1760, 'Wholesep19': 2065, 'whooct19': 2003, 'incmsp': 60, 'incwho': -68,
 'price':[1900,2842,2720,2718,2579,2599,2710,2594,2523,2448,2541,2604,2575,2897,2651,2619]},
 'watermelon': {'MSP2019': 7050, 'Wholesep19': 6253, 'whooct19': 6466, 'incmsp': 350, 'incwho': -1008,
 'price':[5400,5599,5442,5396,5099,5121,5035,4933,4919,4695,4678,4795,4755,5600,4906,5223]},
 'muskmelon': {'MSP2019': 4800, 'Wholesep19': 4834, 'whooct19': 4890, 'incmsp': 300, 'incwho': -1821,
 'price':[1550,1715,1735,1719,1677,1674,1653,1659,1655,1639,1651,1657,1662,1750,1688,1738]},
 'apple': {'MSP2019': 3950, 'Wholesep19': 4291, 'whooct19': 4313, 'incmsp': 300, 'incwho': -996,
 'price':[1550,1715,1735,1719,1677,1674,1653,1659,1655,1639,1651,1657,1662,1750,1688,1738]},
 'orange': {'MSP2019': 1815, 'Wholesep19': 1831, 'whooct19': 1829, 'incmsp': 80, 'incwho': 64,
  'price':[1550,1715,1735,1719,1677,1674,1653,1659,1655,1639,1651,1657,1662,1750,1688,1738]},
 'papaya': {'MSP2019': 5255, 'Wholesep19': 5378, 'whooct19': 5066, 'incmsp': 160, 'incwho': -365,
 'price':[4450,5029,5005,4333,4929,4303,4461,4031,4110,4149,4282,4530,4494,4890,4713,4710]},
 'coconut': {'MSP2019': 1760, 'Wholesep19': 2065, 'whooct19': 2003, 'incmsp': 60, 'incwho': -68,
 'price':[1900,2842,2720,2718,2579,2599,2710,2594,2523,2448,2541,2604,2575,2897,2651,2619]},
 'coffee': {'MSP2019': 7050, 'Wholesep19': 6253, 'whooct19': 6466, 'incmsp': 350, 'incwho': -1008,
 'price':[5400,5599,5442,5396,5099,5121,5035,4933,4919,4695,4678,4795,4755,5600,4906,5223]}}

def home(request):
    #pred=getpre(26, 89, 6.5, 58)

    #push the values to database
    #db = fire.database()
    #val={"op":[34.0529,92.058,6.725,116.802]}
    #db.push(val)

    #pass the graph as image
    #plt.plot(d1,color='black')
    #plt.title("Temprature")
    #plt.xlabel("time")
    #plt.ylabel("temp val")
    #plt.show()  
    #fig1 = plt.gcf()
    #convert graph into dtring buffer and then we convert 64 bit code into image
    #buf = io.BytesIO()
    #fig1.savefig(buf,format='png')
    #buf.seek(0)
    #string1 = base64.b64encode(buf.read())
    #uri =  urllib.parse.quote(string1)

    x=[22.42776057	,93.91722423,	5.893490899,	102.7230739]
    #get values from firebase
    #x=db.child('-MVa-ggAobRLkTxsygMe/op').get().val()
    #y=db.child('1').get().val()
    #z=db.child('2').get().val()
    #a=db.child('3').get().val()
    #xx=[x,y,z,a]
    labelslist=['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean',
     'blackgram','lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon',
     'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
    lab,npk=getpre(x)
    cpredi=labelslist[int(lab)]
    pricess=msp[cpredi]['price']
    #print(pricess)
    return render(request,'home.html',{'result':labelslist[int(lab)],'N':npk[0][0], 
    'P':npk[0][1], 'K':npk[0][2], 'result1':x, 'cprices':pricess, 'temp':d1})


def weather(request):
    weacit=None
    if request.method == 'POST':
        city = request.POST['city']
  
        
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=271d1234d3f497eed5b1d80a07b3fcd1').read()
  
        # converting JSON data to a     dictionary
        list_of_data = json.loads(source)
        #print(list_of_data)
        # data for variable list_of_data
        weacit = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp'] -273) + 'C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
    else:
        weacit   ={}
    return render(request,'weather.html',weacit)

def crops(request):
    cropname={'c1':['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas'],
    'c2': ['mothbeans', 'mungbean','blackgram','lentil', 'pomegranate'],
    'c3':['banana', 'mango', 'grapes', 'watermelon','muskmelon'],
    'c4': ['apple', 'orange', 'papaya', 'coconut', 'cotton'],
    'c5':['jute','coffee']}
    #con={msp[cropname]}
    return render(request,'crop.html',cropname)

def croppro(request,x):
    #x=str(request.POST["num1"])
    #x='rice'
    #print(x)
    con=dict(msp[x])
    con['name']=x
    return render(request,'cropro.html',con)

def getpre(para):#temp,humidity,rainfall,ph):
    import pickle
    model = pickle.load(open("C:/Users/yagne/Desktop/anaconda/croppred/croplabel.pkl", "rb"))
    labpre = model.predict([para])

    model2=pickle.load(open("C:/Users/yagne/Desktop/anaconda/croppred/cropNPK.pkl", "rb"))

    para.append(int(labpre))
    npkpre=model2.predict([para])
    return labpre,npkpre


