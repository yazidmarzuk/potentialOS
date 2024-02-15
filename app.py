from flask import Flask, render_template, request, jsonify, redirect, url_for
import rospy
from std_msgs.msg import Float32
from threading import Thread, Event
import signal, sys
from pythonScripts.systemStats import system_stats
from pythonScripts.processes import get_processes 
from pythonScripts.layout_selector import selector 

import psutil
import json
from datetime import datetime

import random

msg = 0.0
event = Event()

def callback(data):
    global msg 
    msg = data


Thread(target=lambda: rospy.init_node('ros_web_tester', disable_signals=True, anonymous=True)).start()
rospy.Subscriber("/chatter",Float32, callback)

# Create WSGI App
app=Flask(__name__)

def get_msg():
    while True:
        global msg
        return msg.data

@app.route('/')
def index():
    highlight = selector()
    highlight["Index"] = "nav-link"
    return render_template("index.html", PotentialOS_Nav=highlight )

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




if __name__=="__main__":
    #liveServer Functionality
    # rospy.init_node("web-ros-test")
    # rospy.Subscriber("/chatter", Float32, updateValues) 
    app.run(debug=True) 
    # app.run(host='0.0.0.0',port=4444,debug=True) 

