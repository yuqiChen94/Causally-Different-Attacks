from interface.manipulate_actuators import all_cap_set
from statemachine.myFSM import State,StateMachine,Transition,random_generate_capability_history,excluding_attack_class1,composition
from search.predict_sensor import sensor_prediction
from statemachine.myFSM import convert_Y_set
from search.random_search import random_search
from search.find_causal_capability import find_causal_capability
from interface.manipulate_actuators import randomly_generate_actuator
from search.find_causal_capability import simulation_with_attack
from search.find_causal_capability import simulation_normal
iteration_num=10
interval=10
position=[0,1,2]
all_capability_set=all_cap_set.cap_set
attack_set=[]
state0=State('a',0,True)
transition0=Transition(0,state0,state0,"",all_capability_set)
state_list=[]
transition_list=[]

state_list.append(state0)
transition_list.append(transition0)

attack_strategy0=StateMachine(state_list,transition_list)
model_path="prediction_model/svm_model"
actuator=[1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 1, 2]
print (actuator)
sensor=590
target=1000
target_index=0
current_sensor=590
time_interval=10
# path = attack_strategy0.random_walk(2)
# history=random_generate_capability_history(path)
# print (history)
# print (sensor_prediction(history,model_path,sensor,actuator,interval,position))
num_ind=100
length=2

history=random_search(num_ind,length,attack_strategy0,model_path,sensor,actuator,interval,position,target)
# history=[[[1,1]]]
# print (history)
# print (simulation_normal(target_index, current_sensor, history, time_interval))
# print (simulation_with_attack(target_index, current_sensor, history, time_interval))
attack=find_causal_capability(target_index,current_sensor,history,time_interval,target)
if attack!=None:
    print(attack)
    attack_set.append(attack)
Y_set=convert_Y_set(attack)
print (Y_set)
new_state_machine = excluding_attack_class1(Y_set, all_capability_set)
new_state_machine.update_targets()
new_attack_strategy=composition(attack_strategy0,new_state_machine)

print (new_attack_strategy.get_all_feasible_transition_list())
for i in range(0,iteration_num):
    history=random_search(num_ind,length,new_attack_strategy,model_path,sensor,actuator,interval,position,target)
    attack=find_causal_capability(target_index,current_sensor,history,time_interval,target)
    if attack != None:
        print(attack)
        attack_set.append(attack)
    Y_set=convert_Y_set(attack)
    new_state_machine = excluding_attack_class1(Y_set, all_capability_set)
    new_state_machine.update_targets()
    new_attack_strategy = composition(attack_strategy0, new_state_machine)
#
#
# print (new_attack_strategy.get_all_feasible_transition_list())
# # #

print (attack_set)