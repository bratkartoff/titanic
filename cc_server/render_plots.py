import io
import random
import pandas as pd
import numpy as np
from flask import Response, Flask, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import matplotlib as mpl

app = Flask(__name__)

plt.style.use('seaborn')


@app.route('/plots/air_humi.png')
def plot_png_0():
    fig = create_figure_0()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(),  mimetype='image/png')

def create_figure_0():
    data = pd.read_csv("data.csv")
    data = data.tail(100) #letzte 100 daten
    data["date"] = data["date"].astype('datetime64[s]')
    #fig = Figure()
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1)
    #xs = range()
    
    xs = data["date"]
    ys = data["air_humi"]
    #print(ys)
    plt.xlabel('Time')
    plt.ylabel('rel. Humidity in %')
    axis.plot(xs, ys)
    return fig

@app.route('/plots/air_pres.png')
def plot_png_1():
        fig = create_figure_1()
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(),  mimetype='image/png')

def create_figure_1():
    data = pd.read_csv("data.csv")
    data = data.tail(100) #letzte 100 daten
    data["date"] = data["date"].astype('datetime64[s]')
    #fig = Figure()
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1)
    #xs = range()
    
    xs = data["date"]
    ys = data["air_pres"]
    #print(ys)
    plt.xlabel('Time')
    plt.ylabel('Pressure [HPa]')
    axis.plot(xs, ys)
    return fig



@app.route('/plots/air_temp.png')
def plot_png_2():
    fig = create_figure_2()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(),  mimetype='image/png')

def create_figure_2():
    data = pd.read_csv("data.csv")
    data = data.tail(100) #letzte 100 daten
    data["date"] = data["date"].astype('datetime64[s]')
    #fig = Figure()
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1)
    #xs = range()
    
    xs = data["date"]
    ys = data["air_temp"]
    #print(ys)
    plt.xlabel('Time')
    plt.ylabel('Air Temperature in C')
    axis.plot(xs, ys)
    return fig


'''
@app.route('/plots/air_humi.png')
def plot_png_3():
    fig = create_figure_3()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(),  mimetype='image/png')

def create_figure_3():
    data = pd.read_csv("data.csv")
    data = data.tail(100) #letzte 100 daten
    data["date"] = data["date"].astype('datetime64[s]')
    #fig = Figure()
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1)
    #xs = range()
    
    xs = data["date"]
    ys = data["humi"]
    #print(ys)
    plt.xlabel('Time')
    plt.ylabel('rel. Humidity in %')
    axis.plot(xs, ys)
    return fig



@app.route('/plots/air_humi.png')
def plot_png_4():
    fig = create_figure_4()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(),  mimetype='image/png')

def create_figure_4():
    data = pd.read_csv("data.csv")
    data = data.tail(100) #letzte 100 daten
    data["date"] = data["date"].astype('datetime64[s]')
    #fig = Figure()
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1)
    #xs = range()
    
    xs = data["date"]
    ys = data["humi"]
    #print(ys)
    plt.xlabel('Time')
    plt.ylabel('rel. Humidity in %')
    axis.plot(xs, ys)
    return fig



  '''



@app.route('/aktualisierungstest') #todo rm
def akt():
    #return '<img src="plot.png" id="myImage" />'
    return render_template('reload_frame.html', picture_path = "plots/air_pres.png")



if __name__ == '__main__':
    app.run(debug=True)
