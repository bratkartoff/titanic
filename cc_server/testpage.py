import io
import random
import pandas as pd
import numpy as np
from flask import Response, Flask, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
#import importlib



app = Flask(__name__)

@app.route('/plots/air_humi.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(),  mimetype='image/png')

def create_figure():
    data = pd.read_csv("data.csv")
    data = data.tail(100) #letzte 100 daten
    data["date"] = data["date"].astype('datetime64[s]')
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    #xs = range()
    xs = data["date"]
    ys = data["humi"]
    print(ys)
    axis.plot(xs, ys)
    return fig

@app.route('/TimeCourse')
def show():
    return render_template(
        "TimeCourse.html",
        air_temp='/plots/air_humi.png',
        air_pres='/plots/air_humi.png',
        air_humi='/plots/air_humi.png',
        water_temp='/plots/air_humi.png',
        water_hp='/plots/air_humi.png'
    )


@app.route('/diagramtest')
def diagram_test():
    img_link = "/plot.png"
    return render_template(
        'hello.html',
        img_link=img_link
    )





@app.route('/aktualisierungstest')
def akt():
    #return '<img src="plot.png" id="myImage" />'
    return render_template('reload.html')

if __name__ == '__main__':
    app.run(debug=True)