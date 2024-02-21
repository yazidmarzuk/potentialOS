from flask import Flask, render_template, request, jsonify, redirect, url_for
import rospy
from std_msgs.msg import Float32
from threading import Thread, Event
import signal, sys
from pythonScripts.systemStats import system_stats
from pythonScripts.processes import get_processes 
from pythonScripts.layout_selector import selector 
from pythonScripts.network_test import run_speedtest
from pythonScripts.sensorData import SensorDataSend

from sensor_msgs.msg import FluidPressure


import psutil
import json
from datetime import datetime

import random

msg = 0.0
SensorData = SensorDataSend()

event = Event()

def pressure_callback(data):
  global SensorData  
  depth_val = round((data.fluid_pressure-101.5)*0.1023,2)
  SensorData = SensorDataSend()
  SensorData["DepthSensor"] = depth_val
  SensorData["Pressure"] = data.fluid_pressure
  print(SensorData["Pressure"])



Thread(target=lambda: rospy.init_node('ros_web_tester', disable_signals=True, anonymous=True)).start()
rospy.Subscriber("/potrov2/pressure",FluidPressure, pressure_callback)

# Create WSGI App
app=Flask(__name__)

def get_msg():
    while True:
        global msg
        return msg.data

@app.route('/')
def index():
    global SensorData
    highlight = selector()
    highlight["Index"] = "nav-link"
    return render_template("index.html", PotentialOS_Nav=highlight, SensorData=SensorData )

@app.route('/potpit')
def potpit():
    highlight = selector()
    highlight["PotPit"] = "nav-link"
    # return render_template("potpit.html", PotentialOS_Nav=highlight)
    return render_template("potpit.html", PotentialOS_Nav=highlight)

@app.route('/extensions')
def extensions():
    highlight = selector()
    highlight["Extensions"] = "nav-link"
    return render_template("extensions.html", PotentialOS_Nav=highlight)

@app.route('/thruster-ui')
def thrusterUI():
    highlight = selector()
    highlight["ThrusterData"] = "nav-link"
    return render_template("thruster-ui.html", PotentialOS_Nav=highlight)


@app.route('/sonarviewer')
def sonarViewer():
    highlight = selector()
    highlight["SonarViewer"] = "nav-link"
    return render_template("sonarviewer.html", PotentialOS_Nav=highlight)


@app.route('/terminal')
def terminal():
    highlight = selector()
    highlight["Terminal"] = "nav-link"
    return render_template("terminal.html", PotentialOS_Nav=highlight)


@app.route('/robot_vitals')
def robotVitals():
    highlight = selector()
    highlight["RobotStats"] = "nav-link"
    return render_template("robot_vitals.html", PotentialOS_Nav=highlight)



# on the terminal type: curl http://127.0.0.1:5000/api-curl
@app.route('/api-call', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
          return system_stats()
  
@app.route('/processes')
def process():
    return get_processes()

@app.route('/process-ui')
def sysprocess():
    highlight = selector()
    return render_template('processes.html')


@app.route('/system-info')
def systemInfo():
    highlight = selector()
    highlight["SystemInfo"] = "nav-link"
    return render_template("system-info.html", PotentialOS_Nav=highlight)

def signal_handler(signal, msg):
    rospy.signal_shutdown("end")
    sys.exit(0)

signal.signal(signal.SIGINT,signal_handler)

@app.route('/speedtest',methods = ['GET', 'POST'])
def speedtest():
    if(request.method == 'GET'): 
        print("request recieved")
        return run_speedtest()

@app.route('/sensor-data',methods = ['GET', 'POST'])
def sensorData():
    if(request.method == 'GET'): 
        print("sensor data request recieved")
        return SensorData




if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True) 

