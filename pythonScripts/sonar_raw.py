import socket
import codecs

# IP address and port of the device
IP_ADDRESS = "192.168.2.100"
PORT = 51200

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = (IP_ADDRESS, PORT)
sock.connect(server_address)

try:
    while True:
        # Receive data from the server
        data = sock.recv(1024)
        if not data:
            break

        # Parse the received data
        start_of_packet = data[:2].decode('utf-8')


        payload_length = int.from_bytes(data[2:4], byteorder='little')
        packet_id = int.from_bytes(data[4:6], byteorder='little')
        payload = data[8:8+payload_length].decode('utf-8')
        checksum = int.from_bytes(data[8+payload_length:8+payload_length+2], byteorder='little')


        print(data)
        print("Start of Packet:", start_of_packet)
        print("Payload Length:", payload_length)
        print("Packet ID:", packet_id)
        print("Payload:", payload)
        print("Checksum:", checksum)

finally:
    # Close the socket
    sock.close()