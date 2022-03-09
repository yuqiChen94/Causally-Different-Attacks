from search.predict_sensor import sensor_prediction
from statemachine.myFSM import random_generate_capability_history
from plc import plc1,plc2,plc3,plc4,plc5,plc6
import sys,os
sys.path.insert(0,os.getcwd())
from SCADA import H
from IO import *
from plant.plant import plant
from interface import manipulate_actuators



def find_max(list1):
    max_fintness_value=max(list1)
    max_fintness_index=list1.index(max_fintness_value)
    return max_fintness_index,max_fintness_value



def find_min(list1):
    min_fintness_value=min(list1)
    min_fintness_index=list1.index(min_fintness_value)
    return min_fintness_index,min_fintness_value



def random_search(num_ind,length,attack_strategy,model_path,sensor,actuator,interval,position,target):
    best=2000
    for i in range(0,num_ind):
        path = attack_strategy.random_walk(length)
        history = random_generate_capability_history(path)
        new_sensor=sensor_prediction(history,model_path,sensor,actuator,interval,position)
        fitness=abs(target-new_sensor)
        if fitness<best:
            best=fitness
            best_history=history


    return best_history



