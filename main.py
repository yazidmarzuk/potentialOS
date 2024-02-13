from flask import Flask, render_template
from std_msgs.msg import String
import rospy

app = Flask(__name__)
data = "Waiting for data..."

def callback(msg):
    global data
    data = msg.data

rospy.init_node('ros_flask_app', anonymous=True)
rospy.Subscriber("/chatter", String, callback)

@app.route('/')
def index():
    return render_template('deleteme.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)