from real_plc import plc1,plc2,plc3,plc4,plc5,plc6
import sys,os
sys.path.insert(0,os.getcwd())
from SCADA import H
from IO import *
from plant.plant import plant
from interface import get_data
import numpy as np
x=[]
y=[]
path_x="training_data/x_lit101.npy"
path_y="training_data/y_lit101.npy"
time_interval=1
log_path=''
maxstep = 2*10
# Initiating Plant
Plant = plant(log_path, time_interval,maxstep)
Plant.result[0][0]=590
# Defining I/O
IO_DI_WIFI = DI_WIFI()
IO_P1 = P1()
IO_P2 = P2()
IO_P3 = P3()
IO_P4 = P4()
IO_P5 = P5()
IO_P6 = P6()
# print ("Initializing SCADA HMI")
HMI = H()
# print ("Initializing PLCs\n")
PLC1 = plc1.plc1(HMI)
PLC2 = plc2.plc2(HMI)
PLC3 = plc3.plc3(HMI)
PLC4 = plc4.plc4(HMI)
PLC5 = plc5.plc5(HMI)
PLC6 = plc6.plc6(HMI)

# print ("Now starting Simulation")

# Main Loop Body
for time in range(0,maxstep):
    LIT101_vector = []
    LIT301_vector = []
    LIT401_vector = []
    Sec_P = not bool(time%(1/time_interval))
    Min_P = not bool(time%(60/time_interval))
    Plant.Actuator(IO_P1,IO_P2,IO_P3,IO_P4,IO_P5,IO_P6)
    Plant.Plant(IO_P1,IO_P2,IO_P3,IO_P4,IO_P5,IO_P6,time,HMI)
    # if True:
    #     manipulate_LIT101(HMI,1000)
    #     manipulate_LIT301(HMI, 1000)
    #     manipulate_LIT401(HMI, 1000)
# #PLC working
    PLC1.Pre_Main_Raw_Water(IO_P1,HMI)
    PLC2.Pre_Main_UF_Feed_Dosing(IO_P2,HMI)
    PLC3.Pre_Main_UF_Feed(IO_P3,HMI,Sec_P,Min_P)
    PLC4.Pre_Main_RO_Feed_Dosing(IO_P4,HMI,)
    PLC5.Pre_Main_High_Pressure_RO(IO_P5,HMI,Sec_P,Min_P)
    PLC6.Pre_Main_Product(IO_P6,HMI)
    # LIT101_vector.append(Plant.result[time][0])
    # LIT101_vector.extend(get_data.get_all_actuators(HMI))
    # print (LIT101_vector)
#     x.append(LIT101_vector)
# for i in range(0,maxstep):
#     y.append(Plant.result[i][0])
#
#
#
# x=np.array(x)
# y=np.array(y)
#
# x.dump(path_x)
# y.dump(path_y)
# print (x)
# print (y)