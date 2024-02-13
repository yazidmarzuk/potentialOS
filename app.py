from flask import Flask, render_template, request, jsonify, redirect, url_for
import rospy
from std_msgs.msg import Float32
from threading import Thread, Event
import signal, sys
from pythonScripts.systemStats import json_data 

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
    return render_template("index.html")

@app.route('/extensions')
def extensions():
    return render_template("extensions.html")

@app.route('/thruster-ui')
def thrusterUI():
    return render_template("thruster-ui.html")


@app.route('/sonarviewer')
def sonarViewer():
    return render_template("sonarviewer.html")


@app.route('/terminal')
def terminal():
    return render_template("terminal.html")


@app.route('/robot_vitals')
def robotVitals():
    return render_template("robot_vitals.html")

# on the terminal type: curl http://127.0.0.1:5000/ 
@app.route('/api-call', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
          return json_data 
  
@app.route('/home/<int:num>', methods = ['GET']) 
def disp(num):   
    return jsonify({'data': num**2}) 

@app.route('/system-info')
def systemInfo():
    return render_template("system-info.html",data=get_msg())

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

