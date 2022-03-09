from plc import plc1,plc2,plc3,plc4,plc5,plc6
import sys,os
sys.path.insert(0,os.getcwd())
from SCADA import H
from IO import *
from plant.plant import plant
from interface import manipulate_actuators
history=[[[20, 1]], [[21, 1], [15, 1], [2, 1], [21, 2], [8, 1], [6, 1], [9, 2], [16, 1], [14, 1], [1, 1], [14, 2], [19, 2],
                     [4, 2], [12, 1], [5, 1], [13, 2], [5, 2], [16, 2], [1, 2], [11, 2], [3, 2], [10, 1], [13, 1], [24, 2], [25, 2], [0, 2]]]



print(history)
data_set=[]
time_interval=1
log_path=''
maxstep = 60*60
# Initiating Plant
Plant = plant(log_path, time_interval,maxstep)
# Defining I/O
IO_DI_WIFI = DI_WIFI()
IO_P1 = P1()
IO_P2 = P2()
IO_P3 = P3()
IO_P4 = P4()
IO_P5 = P5()
IO_P6 = P6()
print ("Initializing SCADA HMI")
HMI = H()
print ("Initializing PLCs\n")
PLC1 = plc1.plc1(HMI)
PLC2 = plc2.plc2(HMI)
PLC3 = plc3.plc3(HMI)
PLC4 = plc4.plc4(HMI)
PLC5 = plc5.plc5(HMI)
PLC6 = plc6.plc6(HMI)
print ("Now starting Simulation")
attack_array=[[1,2]]
# Main Loop Body
for time in range(0,10):
    Sec_P = True
    Min_P = not bool(time%(60))

    Plant.Actuator(IO_P1,IO_P2,IO_P3,IO_P4,IO_P5,IO_P6)
    manipulate_actuators.manipulate_IO(IO_P1, IO_P2, IO_P3, IO_P4, IO_P5, IO_P6, history[0])
    Plant.Plant(IO_P1,IO_P2,IO_P3,IO_P4,IO_P5,IO_P6,time,HMI)

# #PLC working
    PLC1.Pre_Main_Raw_Water(IO_P1,HMI)
    PLC2.Pre_Main_UF_Feed_Dosing(IO_P2,HMI)
    PLC3.Pre_Main_UF_Feed(IO_P3,HMI,Sec_P,Min_P)
    PLC4.Pre_Main_RO_Feed_Dosing(IO_P4,HMI,)
    PLC5.Pre_Main_High_Pressure_RO(IO_P5,HMI,Sec_P,Min_P)
    PLC6.Pre_Main_Product(IO_P6,HMI)

    print (time)


for time in range(10,20):
    Sec_P = True
    Min_P = not bool(time%(60))

    Plant.Actuator(IO_P1,IO_P2,IO_P3,IO_P4,IO_P5,IO_P6)
    manipulate_actuators.manipulate_IO(IO_P1, IO_P2, IO_P3, IO_P4, IO_P5, IO_P6, history[1])
    Plant.Plant(IO_P1,IO_P2,IO_P3,IO_P4,IO_P5,IO_P6,time,HMI)

# #PLC working
    PLC1.Pre_Main_Raw_Water(IO_P1,HMI)
    PLC2.Pre_Main_UF_Feed_Dosing(IO_P2,HMI)
    PLC3.Pre_Main_UF_Feed(IO_P3,HMI,Sec_P,Min_P)
    PLC4.Pre_Main_RO_Feed_Dosing(IO_P4,HMI,)
    PLC5.Pre_Main_High_Pressure_RO(IO_P5,HMI,Sec_P,Min_P)
    PLC6.Pre_Main_Product(IO_P6,HMI)


    print (time)