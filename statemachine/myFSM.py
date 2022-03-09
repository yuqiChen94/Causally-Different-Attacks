from random import randint
import random
from typing import NamedTuple
import ast


def clean_list(a,b):
    tmp=[element for element in a if element not in b]
    return tmp

def delete_element(a,b):
    tmp = [element for element in a if element !=b]
    return tmp
def list_intersection(a,b):
    tmp = [val for val in a if val in b]
    return tmp

def list_union(a,b):
    temp=[]
    lst1=a+b
    [temp.append(i) for i in lst1 if not i in temp]
    return temp

def proper_subset_without_empty(s):
    x = len(s)
    t=[]
    for i in range(1,((1 << x)-1)):
        t.append([s[j] for j in range(x) if (i & (1 << j))])
    return t

def subset_without_empty(s):
    x = len(s)
    t=[]
    for i in range(1,1 << x):
        t.append([s[j] for j in range(x) if (i & (1 << j))])
    return t



class State(NamedTuple):
    name: str
    index: int
    initial: bool
    def __repr__(self):
        return 'State(%s)' % (self.name+','+str(self.index)+','+str(self.initial))

class Transition(NamedTuple):
    index: int
    source: State
    target: State
    cap_conditions: list
    capability_set: list


    def __repr__(self):
        return 'Transition(%s)' % (str(self.index)+','+str(self.source)+','+str(self.target)+','+str(self.cap_conditions)+','+str(self.capability_set))

    def get_capability_set(self):
        return self.capability_set




class StateMachine:
    def __init__(self,state_list,transition_list):
        self.state_list=state_list
        self.transition_list=transition_list
        # self.state_len=len(state_list)
        # self.transition_len=len(transition_list)

        intial_set=[]
        for states in self.state_list:
            if states.initial==True:
                intial_set.append(states.index)
        self.intial_set=intial_set

        self.transition_index_for_all_states=[]
        self.target_for_all_states=[]

    def get_feasible_transition_list(self,current_state):
        feasible_transition_list=[]
        for transition in self.transition_list:
            if transition.source==current_state:
                feasible_transition_list.append(transition.index)
        return feasible_transition_list



    def get_all_feasible_transition_list(self):
        self.transition_index_for_all_states=[]
        for state in self.state_list:
            self.transition_index_for_all_states.append(self.get_feasible_transition_list(state))

    def update_targets(self):
        self.get_all_feasible_transition_list()
        for feasible_transition_list in self.transition_index_for_all_states:
            target=[]
            for i in feasible_transition_list:
                target.append(self.transition_list[i].target.index)
            self.target_for_all_states.append(target)



# get the transition index for all the states
#length>=1
    def random_walk(self,length):
        path=[]
        ini_len=len(self.intial_set)
        first=randint(0,ini_len-1)
        current_state=self.state_list[first]
        i=0
        # print (current_state)
        while i<length:
            feasible_transition_list=self.get_feasible_transition_list(current_state)
            # print (feasible_transition_list)
            trainsion_index=feasible_transition_list[randint(0,len(feasible_transition_list)-1)]
            transition=self.transition_list[trainsion_index]
            # print ('Fire Transition%s' % transition.index)
            path.append(transition)
            current_state=transition.target
            i=i+1

        return path


def random_generate_capability_history(path):
    capability_history=[]
    for transition in path:
        n=randint(1,len(transition.capability_set))
        slice = random.sample(transition.capability_set, n)
        capability_history.append(slice)
    # print (capability_history)
    return capability_history

def construct_capability_set(history):
    distinct_capability_set=[]
    for cap_set in history:
        for cap in cap_set:
            if cap not in distinct_capability_set:
                distinct_capability_set.append(cap)
    return distinct_capability_set

def remove_duplication(history):
    new_history=[]
    i=0
    for cap_set in history:
        cap_set.sort()
        if i==0:
            new_history.append(cap_set)
            i=i+1
        else:
            if cap_set!=new_history[i-1]:
                new_history.append(cap_set)
                i=i+1

    return new_history



def excluding_attack_class1(Y_set,all_capability_set):
    new_state_list = []
    state_0 = State('q0', 0, True)
    new_state_list.append(state_0)
    capability_set0=clean_list(all_capability_set,Y_set)
    cap_list=[]
    tran_list=[]
    transition_0=Transition(0,state_0,state_0,"",capability_set0)
    tran_list.append(transition_0)

    tran_ind=1
    state_ind = 1
    for cap in Y_set:
        state_name="q{%s}"% cap
        state_i=State(state_name,state_ind,False)
        state_ind=state_ind+1
        new_state_list.append(state_i)
        new_cap=delete_element(all_capability_set,cap)
        # print (cap)
        cap_list.append(new_cap)


    for i in range(0,len(cap_list)):
        transition1 = Transition(tran_ind, state_0 , new_state_list[i+1], "", cap_list[i])
        tran_ind=tran_ind+1
        transition2 = Transition(tran_ind, new_state_list[i+1],new_state_list[i+1], "", cap_list[i])
        tran_ind = tran_ind + 1
        tran_list.append(transition1)
        tran_list.append(transition2)
        # print (transition1,transition2)

    return  StateMachine(new_state_list,tran_list)


def convert_Y_set(history):
    Y_set=[]
    for cap_set in history:
        for cap in cap_set:
            if cap not in Y_set:
                Y_set.append(cap)


    return Y_set

def composition(statemachine1,statemachine2):

    statemachine1.update_targets()
    statemachine2.update_targets()
    state_list1=statemachine1.state_list
    state_list2 = statemachine2.state_list
    new_state_list=[]
    new_tran_list=[]
    state_ind=0
    tran_ind=0
    for state1 in state_list1:
        for state2 in state_list2:
            new_state_name="[%s]" % (str(state1.index)+" ,"+str(state2.index))
            if (state1.initial and state2.initial) ==True:
                new_initial=True
            else:
                new_initial=False
            new_state=State(new_state_name,state_ind,new_initial)
            new_state_list.append(new_state)
            state_ind = state_ind + 1

    # print (new_state_list)
    # print (statemachine1.transition_list)
# construct new states
    for new_source in new_state_list:
        source_index = ast.literal_eval(new_source.name)
        # print (source_index)
        for new_target in new_state_list:
            target_index = ast.literal_eval(new_target.name)
            # print(source_index,target_index)
            if target_index[0] in statemachine1.target_for_all_states[source_index[0]] and target_index[1] in statemachine2.target_for_all_states[source_index[1]]:
                for i in statemachine1.transition_index_for_all_states[source_index[0]]:
                    if statemachine1.transition_list[i].target.index==target_index[0]:
                        new_transition1=statemachine1.transition_list[i]
                for i in statemachine2.transition_index_for_all_states[source_index[1]]:
                    if statemachine2.transition_list[i].target.index==target_index[1]:
                        new_transition2=statemachine2.transition_list[i]
                new_cap=list_intersection(new_transition1.capability_set,new_transition2.capability_set)
                new_transition=Transition(tran_ind,new_source,new_target,"",new_cap)
                new_tran_list.append(new_transition)
                tran_ind=tran_ind+1

    return StateMachine(new_state_list,new_tran_list)







# capability_set1=[[0,1],[0,2],[1,1],[1,2]]
# capability_set2=[[0,2],[0,3],[1,1],[1,2]]
# capability_set3=[[1,1],[1,2]]
# capability_set4=[[1,1]]
# state1=State('a',0,True)
# state2=State('b',1,False)
# state3=State('c',2,False)
# transition1=Transition(0,state1,state2,"",capability_set1)
# transition2=Transition(1,state2,state2,"",capability_set2)
# transition3=Transition(2,state2,state3,"",capability_set3)
# transition4=Transition(3,state3,state1,"",capability_set1)
# state_list=[]
# transition_list=[]
# state_list.append(state1)
# state_list.append(state2)
# state_list.append(state3)
# transition_list.append(transition1)
# transition_list.append(transition2)
# transition_list.append(transition3)
# transition_list.append(transition4)
# attack_strategy1=StateMachine(state_list,transition_list)
# attack_strategy2=StateMachine(state_list,transition_list)
# # # attack_strategy1.get_all_feasible_transition_list()
# print (attack_strategy1.transition_index_for_all_states)
# print (composition(attack_strategy1,attack_strategy2).transition_list)

# path=attack_strategy1.random_walk(3)
# history=random_generate_capability_history(path)
# print (history)
# Y_set=[[[0, 2], [1, 2], [2, 2]]]
#
# print (attack_strategy1.intial_set)
# print (state_list)
# print (transition_list)
# # excluding_attack_class2(history)
# history=random_generate_capability_history(path)
# print (excluding_attack_class1(Y_set,all_capability_set).state_list)
# print (excluding_attack_class1(Y_set,all_capability_set).transition_list)
#
# test_history=[[[1,1],[0,2]],[[0,2],[1,1]],[[1, 1], [1, 2], [0, 2]], [[0,2]],[[0,2]],[[1, 2], [1, 1]], [[0, 2], [0, 1], [1, 2]]]
# excluding_attack_class3(test_history)