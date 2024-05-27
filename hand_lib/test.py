# pip install pyserial
# ls /dev/ttyUSB0
# sudo chmod 666 /dev/USB0

import serial
import binascii

hand_id=1
port="/dev/ttyUSB0"
baud=115200 # 115200bps

serial = serial.Serial()
serial.port = port
serial.baudrate = baud
serial.timeout = 100
serial.open()

packet = bytearray()
packet.append(0xEB)
packet.append(0x90)
packet.append(hand_id)
packet.append(0x04)
packet.append(0x11)
packet.append(0xFE)
packet.append(0x05)
packet.append(0x0C)

check_num = 0
# length = int("04", 16)+5
length = int(packet[3])+5
print(length)
for i in range(2, length-1):
    check_num =check_num+packet[i]
check_num = check_num & 0xff
packet.append(check_num)
# command = binascii.unhexlify(f"EB90{hand_id}0411FE050C")+check_num
serial.write(packet)

response = serial.read(64)
print(binascii.hexlify(response))
# response = serial.readline()
# print(response)