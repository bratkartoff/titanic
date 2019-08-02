import paho.mqtt.client as paho
import pandas as pd
import time

#msg.payload = msg.payload.decode("utf-8")
cocain = "35,1064,25,18,7,43.4723,15.0752"

print("message received " , cocain)


values = (cocain).split(',')
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
print("DATA saved successful")