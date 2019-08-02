
#receive
import paho.mqtt.client as paho
import pandas as pd
import time




#def store_message():
    

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg): #todo test
    '''
    msg.payload = msg.payload.decode("utf-8")

    print("message received " , msg.payload)
    print("message topic=",msg.topic)

    values = (msg.payload).split(',')
    s = pd.Series(values, index = ["humi", "pres", "temp"])
    s["date"] = time.time()

    newdata = pd.DataFrame({"air_humi": s["humi"], "air_pres": s["pres"], "air_temp": s["temp"], "date": s["date"]}, index=[0])
    newdata.set_index("date", inplace=True)




    try:
        data = pd.read_csv("data.csv")
        data.set_index("date", inplace=True)
        data = pd.concat([data,newdata], sort = False)
 
    except Exception:
        data = newdata

    data.to_csv("data.csv")
    '''
    msg.payload = msg.payload.decode("utf-8")

    print("message received " , msg.payload)
    print("message topic=",msg.topic)

    values = (msg.payload).split(',')
    s = pd.Series(values, index = ["humi", "pres", "temp", "watertemp", "ph-wert", "gpsb", "gpsl"])
    s["date"] = time.time()

    newdata = pd.DataFrame({"air_humi": s["humi"], "air_pres": s["pres"], "air_temp": s["temp"], "date": s["date"], "water_temp": s["watertemp"], "water_pH": s["ph-wert"], "gps_b":s["gpsb"], "gps_l":s["gpsl"]}, index=[0])
    newdata.set_index("date", inplace=True)




    try:
        data = pd.read_csv("data.csv")
        data.set_index("date", inplace=True)
        data = pd.concat([data,newdata], sort = False)
 
    except Exception:
        data = newdata

    data.to_csv("data.csv")
    


client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message


client.connect("broker.hivemq.com", 1883)

client.subscribe("SpeedBoat/Sensors", qos=1)

client.loop_forever()

#while 1:
