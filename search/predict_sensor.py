import os
import numpy as np
import joblib


def fitness_function(sensor_value, HH, LoLo):
    if sensor_value >= HH:
        return float("inf")
    else:
        if sensor_value <= LoLo:
            return float("inf")
        else:
            return 1 / (1 - abs(sensor_value - (HH + LoLo) / 2) / (
                    HH / 2 - LoLo / 2))




def predict_svm_with_sensor(model_path,current_sensor_value,current_actuator_array):
    clf = joblib.load(model_path)
    X=[]
    X.append(current_sensor_value)
    X.extend(current_actuator_array)
    X = np.array(X).reshape(1, -1)
    return clf.predict(X)


def predict_svm(model_path,current_actuator_array,position):
    clf = joblib.load(model_path)
    X=[]
    for i in position:
        X.append(current_actuator_array[i])
    X = np.array(X).reshape(1, -1)
    return clf.predict(X)


# def predict_svm_lit101(model_path,current_actuator_array):
#     clf = joblib.load(model_path)
#     X= current_actuator_array[0:3]
#     X = np.array(X).reshape(1, -1)
#     return clf.predict(X)


#
# def sensor_prediction_lit101(history,model_path,current_sensor_value,current_actuator_array,interval):
#     for cap_set in history:
#         sorted_cap_set=sorted(cap_set)
#         sorted_cap_set.append([-1,-1])
#         attack_array=[]
#         # print (sorted_cap_set)
#         i=0
#         while i<(len(sorted_cap_set)-1):
#             if sorted_cap_set[i][0]!=sorted_cap_set[i+1][0]:
#                 attack_array.append(sorted_cap_set[i])
#                 i=i+1
#             else:
#                 i=i+2
#         # print (current_actuator_array)
#         # print ("attack array:%s" % attack_array)
#         for cap in attack_array:
#             # new_actuator=current_actuator_array[:]
#             current_actuator_array[cap[0]]=cap[1]
#         # print (current_sensor_value)
#         # print(current_actuator_array)
#         change=predict_svm_lit101(model_path,current_actuator_array)
#         # print (change)
#         current_sensor_value=current_sensor_value+change*interval
#         # print (current_sensor_value)
#
#     return current_sensor_value



def sensor_prediction(history,model_path,current_sensor_value,current_actuator_array,interval,position):
    for cap_set in history:
        sorted_cap_set=sorted(cap_set)
        sorted_cap_set.append([-1,-1])
        attack_array=[]
        # print (sorted_cap_set)
        i=0
        while i<(len(sorted_cap_set)-1):
            if sorted_cap_set[i][0]!=sorted_cap_set[i+1][0]:
                attack_array.append(sorted_cap_set[i])
                i=i+1
            else:
                i=i+2
        # print (current_actuator_array)
        # print ("attack array:%s" % attack_array)
        for cap in attack_array:
            # new_actuator=current_actuator_array[:]
            current_actuator_array[cap[0]]=cap[1]
        # print (current_sensor_value)
        # print(current_actuator_array)
        change=predict_svm(model_path,current_actuator_array,position)
        # print (change)
        current_sensor_value=current_sensor_value+change*interval
        # print (current_sensor_value)

    return current_sensor_value

