#####################
# sender
#####################

import socket
import time
import os


this_dir, this_filename = os.path.split(__file__)
myfile = os.path.join(this_dir, 'temp.txt') 


def send_file(filename, host, port):
    # Open the file to be sent
    with open(myfile, "rb") as f:
        data = f.read()

    # Create a socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Send the file data
    start_time = time.time()
    s.sendall(data)
    end_time = time.time()

    # Calculate the transfer speed
    file_size = len(data)
    transfer_time = end_time - start_time
    transfer_speed = file_size / transfer_time / (1024 * 1024)  # Convert to MB/s

    print(f"File sent in {transfer_time:.2f} seconds at {transfer_speed:.2f} MB/s")

    # Close the socket connection
    s.close()

if __name__ == "__main__":
    filename = "temp.txt"
    host = "192.168.2.127"
    port = 12345  # Choose a free port

    send_file(filename, host, port)
