from search.predict_sensor import sensor_prediction
from statemachine.myFSM import random_generate_capability_history
from plc import plc1,plc2,plc3,plc4,plc5,plc6
import sys,os
sys.path.insert(0,os.getcwd())
from SCADA import H
from IO import *
from plant.plant import plant
from interface import manipulate_actuators

# 0: "MV101",
# 1: "P101",
# 2: "P102",
# 3: "MV201",
# 4: "P201",
# 5: "P202",
# 6: "P203",
# 7: "P204",
# 8: "P205",
# 9: "P206",
# 10: "MV301",
# 11: "MV302",
# 12: "MV303",
# 13: "MV304",
# 14: "P301",
# 15: "P302",
# 16: "P401",
# 17: "P402",
# 18: "P403",
# 19: "P404",
# 20: "UV401",
# 21: "P501",
# 22: "P502",
# 23: "P601",
# 24: "P602",
# 25: "P603",

def simulation_normal(target_index,current_sensor,history,time_interval):
    walk_length = len(history)
    start_time=400
    init = [505,890,900,200,200]
    init[target_index]=current_sensor
    maxstep = walk_length * time_interval+start_time
    # Initiating Plant
    Plant = plant(init, 1, maxstep)
    # Defining I/O
    IO_P1 = P1()
    IO_P2 = P2()
    IO_P3 = P3()
    IO_P4 = P4()
    IO_P5 = P5()
    IO_P6 = P6()
    HMI = H()
    # if current_actuator!="":
    #     HMI.MV101.Status = current_actuator[0]
    #     HMI.P101.Status = current_actuator[1]
    #     HMI.P102.Status = current_actuator[2]
    #     HMI.MV201.Status = current_actuator[3]
    #     HMI.P201.Status = current_actuator[4]
    #     HMI.P202.Status = current_actuator[5]
    #     HMI.P203.Status = current_actuator[6]
    #     HMI.P204.Status = current_actuator[7]
    #     HMI.P205.Status = current_actuator[8]
    #     HMI.P206.Status = current_actuator[9]
    #     HMI.MV301.Status = current_actuator[10]
    #     HMI.MV302.Status = current_actuator[11]
    #     HMI.MV303.Status = current_actuator[12]
    #     HMI.MV304.Status = current_actuator[13]

    PLC1 = plc1.plc1(HMI)
    PLC2 = plc2.plc2(HMI)
    PLC3 = plc3.plc3(HMI)
    PLC4 = plc4.plc4(HMI)
    PLC5 = plc5.plc5(HMI)
    PLC6 = plc6.plc6(HMI)
    # Main Loop Body
    for time in range(0, maxstep):
        Sec_P = True
        Min_P = not bool(time % (60))

        Plant.Actuator(IO_P1, IO_P2, IO_P3, IO_P4, IO_P5, IO_P6)
        # manipulate_actuators.manipulate_IO(IO_P1, IO_P2, IO_P3, IO_P4, IO_P5, IO_P6, attack_array)
        Plant.Plant(IO_P1, IO_P2, IO_P3, IO_P4, IO_P5, IO_P6, time, HMI)

        # #PLC working
        PLC1.Pre_Main_Raw_Water(IO_P1, HMI)
        PLC2.Pre_Main_UF_Feed_Dosing(IO_P2, HMI)
        PLC3.Pre_Main_UF_Feed(IO_P3, HMI, Sec_P, Min_P)
        PLC4.Pre_Main_RO_Feed_Dosing(IO_P4, HMI, )
        PLC5.Pre_Main_High_Pressure_RO(IO_P5, HMI, Sec_P, Min_P)
        PLC6.Pre_Main_Product(IO_P6, HMI)

    return Plant.result[maxstep][target_index]


def simulation_with_attack(target_index,current_sensor,history,time_interval):

    walk_length = len(history)
    start_time=400
    init = [505,890,900,200,200]
    init[target_index]=current_sensor
    maxstep = walk_length * time_interval+start_time
    Plant = plant(init, 1, maxstep)
    IO_P1 = P1()
    IO_P2 = P2()
    IO_P3 = P3()
    IO_P4 = P4()
    IO_P5 = P5()
    IO_P6 = P6()
    HMI = H()
    PLC1 = plc1.plc1(HMI)
    PLC2 = plc2.plc2(HMI)
    PLC3 = plc3.plc3(HMI)
    PLC4 = plc4.plc4(HMI)
    PLC5 = plc5.plc5(HMI)
    PLC6 = plc6.plc6(HMI)
    for time in range(0, start_time):
        Sec_P = True
        Min_P = not bool(time % (60))

        Plant.Actuator(IO_P1, IO_P2, IO_P3, IO_P4, IO_P5, IO_P6)
        # manipulate_actuators.manipulate_IO(IO_P1, IO_P2, IO_P3, IO_P4, IO_P5, IO_P6, attack_array)
        Plant.Plant(IO_P1, IO_P2, IO_P3, IO_P4, IO_P5, IO_P6, time, HMI)

        # #PLC working
        PLC1.Pre_Main_Raw_Water(IO_P1, HMI)
        PLC2.Pre_Main_UF_Feed_Dosing(IO_P2, HMI)
        PLC3.Pre_Main_UF_Feed(IO_P3, HMI, Sec_P, Min_P)
        PLC4.Pre_Main_RO_Feed_Dosing(IO_P4, HMI, )
        PLC5.Pre_Main_High_Pressure_RO(IO_P5, HMI, Sec_P, Min_P)
        PLC6.Pre_Main_Product(IO_P6, HMI)


    # print (Plant.result[star_time][target_index])
    for t in range (0,walk_length):
        for time in range(t*time_interval+start_time, (t+1)*time_interval+start_time):
            Sec_P = True
            Min_P = not bool(time % (60))

            Plant.Actuator(IO_P1, IO_P2, IO_P3, IO_P4, IO_P5, IO_P6)
            manipulate_actuators.manipulate_IO(IO_P1, IO_P2, IO_P3, IO_P4, IO_P5, IO_P6, history[t])
            Plant.Plant(IO_P1, IO_P2, IO_P3, IO_P4, IO_P5, IO_P6, time, HMI)

        # #PLC working
            PLC1.Pre_Main_Raw_Water(IO_P1, HMI)
            PLC2.Pre_Main_UF_Feed_Dosing(IO_P2, HMI)
            PLC3.Pre_Main_UF_Feed(IO_P3, HMI, Sec_P, Min_P)
            PLC4.Pre_Main_RO_Feed_Dosing(IO_P4, HMI, )
            PLC5.Pre_Main_High_Pressure_RO(IO_P5, HMI, Sec_P, Min_P)
            PLC6.Pre_Main_Product(IO_P6, HMI)
            # print (time)
            # print (Plant.result[time+600][target_index])
    return Plant.result[maxstep][target_index]

def find_causal_capability(target_index,current_sensor,history,time_interval,threshold):
    walk_length=len(history)
    cal_set=[]
    print ("length %s" % walk_length)
    for t in range (0,walk_length):
        cal=[]
        history_t=[history[t]]
        normal_output=simulation_normal(target_index, current_sensor,history_t, time_interval)
        abnormal_output=simulation_with_attack(target_index, current_sensor,history_t, time_interval)
        if normal_output==abnormal_output:
            current_sensor=normal_output
            print (current_sensor)

        else:
            for cap in history[t]:
                history_c=[[cap]]
                new_abnormal_output = simulation_with_attack(target_index, current_sensor, history_c, time_interval)
                if new_abnormal_output!=normal_output:
                    if abs(threshold-new_abnormal_output)<abs(threshold-normal_output):
                        cal.append(cap)
            cal_set.append(cal)


    return cal_set




