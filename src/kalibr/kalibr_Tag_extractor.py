import rosbag
import ast
from decimal import Decimal
#result: same with bag filepath, uwb_log.tum

error_limit = 10.0 #cm
bag = rosbag.Bag('continue_30fps_uwb.bag') #input bagfile name
uwb_log_raw = open("uwb_raw.txt", "w")



for topic, msg, t in bag.read_messages(topics=['/nlink_linktrack_tagframe0']):
      print >> uwb_log_raw, t
      print >> uwb_log_raw, msg
      # print(msg >> uwb_log_raw)
      # print("@@@@" >> uwb_log_raw)
uwb_log_raw = open("uwb_raw.txt", "r")
uwb_lines = list(uwb_log_raw)

uwb_log_raw_final_res = open("uwb_log.tum", "w")
last_time_stamp =  -1.0;
for i in range(0, len(uwb_lines), 14):
      print("---")
      error_xyz = uwb_lines[i + 7].strip('][').split(',') #conver to list
      error_xyz[0] = float(error_xyz[0][9:]) #error_posex meter
      error_xyz[1] = float(error_xyz[1][1:]) #error_posex meter

      pose_xyz = uwb_lines[i + 6].strip('][').split(',') #conver to list
      pose_xyz[0] = float(pose_xyz[0][9:]) #error_posex meter
      pose_xyz[1] = float(pose_xyz[1][1:]) #error_posex meter
      pose_xyz[2] = (pose_xyz[2][1:(len(pose_xyz[2])-3)])
      pose_xyz[2] = float(pose_xyz[2])

      quaternion_xyzw= uwb_lines[i + 11].strip('][').split(',') #conver to list
      quaternion_xyzw[0] = float(quaternion_xyzw[0][13:]) #error_posex meter
      quaternion_xyzw[1] = float(quaternion_xyzw[1][1:]) #error_posex meter
      quaternion_xyzw[2] = float(quaternion_xyzw[2][1:]) #error_posex meter
      quaternion_xyzw[3] = (quaternion_xyzw[3][1:(len(quaternion_xyzw[3])-3)])
      quaternion_xyzw[3] = float(quaternion_xyzw[3])

      if( (last_time_stamp < float(uwb_lines[i]) and (float(error_xyz[0])*100.0 < float(error_limit)) and (float(error_xyz[1])*100.0 < float(error_limit)))):
            last_time_stamp = float(uwb_lines[i])
            print("timestamp")
            uwb_lines[i] = (repr(uwb_lines[i]))
            uwb_log_raw_final_res.write(str(uwb_lines[i])[1:len(str(uwb_lines[i]))-3])
            uwb_log_raw_final_res.write(" ")
            print(uwb_lines[i])   
            print("pose_x")
            print(pose_xyz[0])
            uwb_log_raw_final_res.write(str(pose_xyz[0]))
            uwb_log_raw_final_res.write(" ")
            print("pose_y")
            uwb_log_raw_final_res.write(str(pose_xyz[1]))
            uwb_log_raw_final_res.write(" ")
            print(pose_xyz[1])
            print("pose_z")
            uwb_log_raw_final_res.write(str(0))
            uwb_log_raw_final_res.write(" ")
            print(pose_xyz[2])
            print("quaternion_xyzw[0]")
            uwb_log_raw_final_res.write(str(quaternion_xyzw[0]))
            uwb_log_raw_final_res.write(" ")
            print(quaternion_xyzw[0])
            print("quaternion_xyzw[1]")
            uwb_log_raw_final_res.write(str(quaternion_xyzw[1]))
            uwb_log_raw_final_res.write(" ")
            print(quaternion_xyzw[1])
            print("quaternion_xyzw[2]")
            uwb_log_raw_final_res.write(str(quaternion_xyzw[2]))
            uwb_log_raw_final_res.write(" ")
            print(quaternion_xyzw[2])
            print("quaternion_xyzw[3]")
            uwb_log_raw_final_res.write(str(quaternion_xyzw[3])+"\n")




# print(len(uwb_lines))
# print("0")
# print(uwb_lines[0])
# print("1")
# print(uwb_lines[1])
# print("2")
# print(uwb_lines[2])
# print("3")
# print(uwb_lines[3])
# print("4")
# print(uwb_lines[4])
# print("5")
# print(uwb_lines[5])
# print("6")
# print(uwb_lines[6])
# print("8")
# print(uwb_lines[8])
# print("9")
# print(uwb_lines[9])
# print("10")
# print(uwb_lines[10])
# print("11")
# print(uwb_lines[11])
# print("12")
# print(uwb_lines[12])