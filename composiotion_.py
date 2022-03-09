from interface.manipulate_actuators import all_cap_set
from statemachine.myFSM import State,StateMachine,Transition,random_generate_capability_history,excluding_attack_class1,composition
from search.predict_sensor import sensor_prediction
from statemachine.myFSM import convert_Y_set
from search.random_search import random_search
from search.find_causal_capability import find_causal_capability

all_capability_set=all_cap_set.cap_set

Y_set=[[0, 2],[1,1]]

state0=State('a',0,True)
transition0=Transition(0,state0,state0,"",all_capability_set)
state_list=[]
transition_list=[]

state_list.append(state0)
transition_list.append(transition0)

attack_strategy0=StateMachine(state_list,transition_list)
new_m=excluding_attack_class1(Y_set,all_capability_set)


# print (new_m.state_list)
# print (new_m.transition_list)

attack_strategy=composition(attack_strategy0,new_m)
print (attack_strategy.get_all_feasible_transition_list())