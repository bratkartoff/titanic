
#receive
import paho.mqtt.client as paho
import pandas as pd
import time




#def store_message():
    

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    values = (msg.payload).split(',')
    s = pd.Series(values, index = ["humi", "pres", "temp"])
    s["date"] = time.time()

    newdata = pd.DataFrame({"humi": s["humi"], "pres": s["pres"], "temp": s["temp"], "date": s["date"]}, index=[0])
    newdata.set_index("date", inplace=True)




    try:
        data = pd.read_csv("data.csv")
        data.set_index("date", inplace=True)
        data = pd.concat([data,newdata], sort = False)
 
    except Exception as e:
        data = newdata

    data.to_csv("data.csv")

    


client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message


client.connect("broker.hivemq.com", 1883)

client.subscribe("SpeedBoat/Sensors", qos=1)

client.loop_forever()

#while 1: