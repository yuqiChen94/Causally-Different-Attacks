

import joblib
import random
import pickle
import numpy as np
import os
class population:
    pop=[]
    actuator_set=[]
    fitness=[]

    def __init__(self,*arg):
        if len(arg)==6:
            self.number_of_actuators=arg[0]
            self.initial_sensor=arg[1]
            self.number_of_individual=arg[2]
            print (self.number_of_individual)
            self.Upperbound=arg[3]
            self.Lowerbound=arg[4]
            self.model_path=arg[5]
        else:
            print ("error")
        self.pop = []
        self.actuator_set = []
        self.fitness=[]



    def actuatorEncoding(self):
        actuatorset = []
        for i in range(self.number_of_individual):
            temp = []
            for j in range(0,self.number_of_actuators):
                temp.append(random.randint(1, 2))
            actuatorset.append(temp)
            self.actuator_set=actuatorset[0:]
        return actuatorset[0:]


    def generateInd(self):
        self.pop=[]
        for i in range(len(self.actuator_set)):
            t = []
            t.append(self.initial_sensor)
            for j in range(self.number_of_actuators):
                t.append(self.actuator_set[i][j])
            self.pop.append(t)

        return self.pop

    def predict_svm(self):
        new_sensor = []
        svr_model = joblib.load(self.model_path)
        for i in range(0, len(self.actuator_set)):
            t = []
            t = self.pop[i][1:]
            t.insert(0, self.pop[i][0][0])
            x = np.array(t)
            y = svr_model.predict(x.reshape(1, -1))
            new_sensor.append(float(y[0]))
        return new_sensor




    def fitness_fn(self):
        self.fitness=[]
        v=0

        new_sensor_value = self.predict_svm()

        print (new_sensor_value)

        for i in range(len(new_sensor_value)):
            v = self.fitness_function(new_sensor_value[i],self.Upperbound,self.Lowerbound)
            self.fitness.append(v)


        return self.fitness

    def fitness_function(self, sensor_value,HH,LoLo):
        if sensor_value >= HH:
            return float("inf")
        else:
            if sensor_value <= LoLo:
                return float("inf")
            else:
                return 1 / (1 - abs(sensor_value - (HH + LoLo) / 2) / (
                        HH / 2 - LoLo / 2))




