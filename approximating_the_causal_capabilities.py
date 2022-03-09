from search.find_causal_capability import simulation_with_attack
from search.find_causal_capability import simulation_normal
from search.find_causal_capability import find_causal_capability
from attack_array.attack_array import interpret_capability_set
from statemachine.myFSM import convert_Y_set
history=[[[0, 2], [4, 2], [5, 2], [8, 1], [17, 1], [21, 2], [3, 2], [19, 2], [23, 2], [12, 2], [20, 2], [22, 1], [20, 1], [9, 2], [8, 2], [10, 2], [7, 2], [23, 1], [21, 1], [18, 2], [16, 2], [1, 1], [5, 1]], [[16, 1], [15, 2], [10, 1], [11, 1], [8, 1], [7, 2], [5, 2], [7, 1], [13, 1], [14, 1], [0, 1], [20, 1], [18, 1], [4, 2], [2, 1], [21, 2], [15, 1], [25, 1], [0, 2], [20, 2], [14, 2], [1, 2], [17, 1], [24, 2], [11, 2], [10, 2], [8, 2], [3, 1], [16, 2], [23, 1], [6, 1], [22, 1], [12, 2], [23, 2], [21, 1], [9, 1], [6, 2], [2, 2]]]
# history is an attack
print (interpret_capability_set(history[0]))
threshold=1000
sensor_index=0
# target sensor is LIT101, of which index is 0.
current_sensor=590
# current sensor value
time_interval=10
# time interval for simulator
# start from the initial state
print (simulation_with_attack(sensor_index,current_sensor,history,time_interval))
print (simulation_normal(sensor_index,current_sensor,history,time_interval))

Y_set=find_causal_capability(sensor_index,current_sensor,history,time_interval,threshold)
# print (find_causal_capability(sensor_index,current_sensor,history,time_interval,threshold))
print (convert_Y_set(Y_set))
