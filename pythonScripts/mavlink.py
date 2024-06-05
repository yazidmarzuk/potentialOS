import requests
import schedule
import time
import math

#Script to receive via MAVLink (GCS side)
from pymavlink import mavutil

#If through WiFi
mavlink_connection = mavutil.mavlink_connection(device='udpin:192.168.1.163:14551', baudrate=57600)

#Else through a radio antenna,
# mavlink_connection = mavutil.mavserial(device='/dev/ttyUSB0', baud=57600)

while 1:
    mavlink_connection.wait_heartbeat()
    print("[INFO] Heartbeat Received")
    msg = mavlink_connection.recv_msg()
    print(msg)


def make_api_request():
    global data, vision_position_delta
    url = 'http://100.89.76.72:6040/'

    # url = 'http://100.89.76.72:6040/mavlink/vehicles/255/components/0/messages/VISION_POSITION_DELTA'
    response = requests.get(url)
    if response.status_code == 200:
        # Extract the position delta
    # position_delta = vision_position_delta['position_delta']


        data = response.json()
        print(data)
        vision_position_delta = data['components']['0']['messages']['VISION_POSITION_DELTA']['message']
        print(vision_position_delta)

        # Process the data as needed
        # print(data)
        position_delta_x = data['message']['position_delta'][0]
        position_delta_y = data['message']['position_delta'][1]
        position_delta_z = data['message']['position_delta'][2]
        time_delta = data['message']['time_delta_usec']

        vx = math.sqrt((position_delta_x)**2 + (position_delta_y)**2)/time_delta
        print("Velocity x")
        print(vx)

        v_all = math.sqrt((position_delta_x)**2 + (position_delta_y)**2 + (position_delta_z)**2)/time_delta
        print("Velocity Overall")
        print(v_all)
        
    else:
        print('Failed to fetch data')

# Schedule the API request to run every 5 minutes
# schedule.every(0.1).seconds.do(make_api_request)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)