#!/usr/bin/env python
import rospy
from radar.msg import radar_message
import serial
import time
import numpy as np
import math

def radar_data_passing():
 # create serial object with corresponding COM Port and open it 
 com_obj=serial.Serial('/dev/ttyUSB0')
 com_obj.baudrate=115200
 com_obj.parity=serial.PARITY_EVEN
 com_obj.stopbits=serial.STOPBITS_ONE
 com_obj.bytesize=serial.EIGHTBITS

 # connect to sensor and set baudrate 
 payloadlength = (4).to_bytes(4, byteorder='little')
 value = (3).to_bytes(4, byteorder='little')
 header = bytes("INIT", 'utf-8')
 cmd_init = header+payloadlength+value
 com_obj.write(cmd_init)
 # get response
 response_init = com_obj.read(9)
 if response_init[8] != 0:
  print('Error during initialisation for K-LD7')
 # delay 75ms
 time.sleep(0.075)
 # change to higher baudrate
 com_obj.baudrate = 2E6

 # change max speed to 25km/h
 value = (1).to_bytes(4, byteorder='little')
 header = bytes("RSPI", 'utf-8')
 cmd_frame = header+payloadlength+value
 com_obj.write(cmd_frame)

 # get response
 response_init = com_obj.read(9)
 if response_init[8] != 0:
  print('Error: Command not acknowledged')
    
 # change max range to 10m
 value = (1).to_bytes(4, byteorder='little')
 header = bytes("RRAI", 'utf-8')
 cmd_frame = header+payloadlength+value
 com_obj.write(cmd_frame)

 # get response
 response_init = com_obj.read(9)
 if response_init[8] != 0:
  print('Error: Command not acknowledged')
	
 # Pulish node set
 rospy.init_node('start_node', anonymous=False)
 pub = rospy.Publisher('radar_data', radar_message, queue_size=10)
 rate = rospy.Rate(1)
 vel = radar_message()
 while not rospy.is_shutdown():
  for ctr in range(100):
   # request next frame data
   PDAT = (4).to_bytes(4, byteorder='little')
   header = bytes("GNFD", 'utf-8')
   cmd_frame = header+payloadlength+PDAT
   com_obj.write(cmd_frame)
   # get acknowledge
   resp_frame = com_obj.read(9)
   if resp_frame[8] != 0:
    print('Error: Command not acknowledged')

   # get header 
   resp_frame = com_obj.read(4)

   # get payload len
   resp_len = com_obj.read(4)

   # initialize arrays
   distances_x = np.zeros(100)
   distances_y = np.zeros(100)
   speeds = np.zeros(100)
   distances = np.zeros(100)
   i = 0
   length = resp_len[0]

   # get data, until payloadlen is zero
   while length > 0:
    PDAT_Distance = np.frombuffer(com_obj.read(2), dtype=np.uint16)
    PDAT_Speed = np.frombuffer(com_obj.read(2), dtype=np.int16)/100
    PDAT_Angle = math.radians(np.frombuffer(com_obj.read(2), dtype=np.int16)/100)
    PDAT_Magnitude = np.frombuffer(com_obj.read(2), dtype=np.uint16)
					
    distances_x[i] = -(PDAT_Distance * math.sin(PDAT_Angle))
    distances_y[i] = PDAT_Distance * math.cos(PDAT_Angle)
    distances[i] = PDAT_Distance
    speeds[i] = PDAT_Speed
    i = i + 1
    # subtract stored datalen from payloadlen
    length = length - 8
   vel.start_time = rospy.Time.now()
   vel.data = speeds
   vel.num = max(speeds)
   # pub.publish(vel)
   rospy.loginfo("------")
   rospy.loginfo("Start Time(sec): %d", vel.start_time.secs)
   rospy.loginfo("Max speed: %f", vel.num)
   pub.publish(vel)    
   # reset arrays
   distances_x = np.zeros(100)
   distances_y = np.zeros(100)
   speeds = np.zeros(100)
   distances = np.zeros(100)
   i = 1   

if __name__ == '__main__':
 try:radar_data_passing()
 except rospy.ROSInterruptException:
  pass
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
