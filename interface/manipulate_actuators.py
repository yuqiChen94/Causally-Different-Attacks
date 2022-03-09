from random import randint

class all_cap_set:
    cap_set=[]
    for i in range(0,26):
        p=[i,1]
        cap_set.append(p)
        p=[i,2]
        cap_set.append(p)


def get_tag_name(x):
    return {
        0: "MV101",
        1: "P101",
        2: "P102",
        3: "MV201",
        4: "P201",
        5:  "P202",
        6:  "P203",
        7:  "P204",
        8:  "P205",
        9:  "P206",
        10:  "MV301",
        11:  "MV302",
        12:  "MV303",
        13:  "MV304",
        14:  "P301",
        15:  "P302",
        16:  "P401",
        17:  "P402",
        18:  "P403",
        19:  "P404",
        20:  "UV401",
        21:  "P501",
        22:  "P502",
        23:  "P601",
        24:  "P602",
        25:  "P603",
    }.get(x, "error")

def get_tag_index(x):
    return {
        "MV101": 0,
        "P101": 1,
        "P102": 2,
        "MV201": 3,
        "P201": 4,
        "P202": 5,
        "P203": 6,
        "P204": 7,
        "P205": 8,
        "P206": 9,
        "MV301": 10,
        "MV302": 11,
        "MV303": 12,
        "MV304": 13,
        "P301": 14,
        "P302": 15,
        "P401": 16,
        "P402": 17,
        "P403": 18,
        "P404": 19,
        "UV401": 20,
        "P501": 21,
        "P502": 22,
        "P601": 23,
        "P602": 24,
        "P603": 25,
    }.get(x, "error")

def get_behavior(x):
    return {
        0: "off",
        1: "off",
        2: "on"}.get(x, "error")


def interpret_capability_set(capability_set):
    cap_set=[]
    for cap in capability_set:
        cap_set.append([get_tag_name(cap[0]),get_behavior(cap[1])])

    return cap_set
# def map_capability_set(capability_set):
#     pass

def manipulate_HMI(HMI,attack_array):
    for attack_set in attack_array:
        if attack_set[0]==0:
            HMI.MV101.Status = attack_set[1]
        if attack_set[0] == 1:
            HMI.P101.Status = attack_set[1]
        if attack_set[0] == 2:
            HMI.P102.Status = attack_set[1]
        if attack_set[0] == 3:
            HMI.MV201.Status = attack_set[1]
        if attack_set[0] == 4:
            HMI.P201.Status = attack_set[1]
        if attack_set[0] == 5:
            HMI.P202.Status = attack_set[1]
        if attack_set[0] == 6:
            HMI.P203.Status = attack_set[1]
        if attack_set[0] == 7:
            HMI.P204.Status = attack_set[1]
        if attack_set[0] == 8:
            HMI.P205.Status = attack_set[1]
        if attack_set[0] == 9:
            HMI.P206.Status = attack_set[1]
        if attack_set[0] == 10:
            HMI.MV301.Status = attack_set[1]
        if attack_set[0] == 11:
            HMI.MV302.Status = attack_set[1]
        if attack_set[0] == 12:
            HMI.MV303.Status = attack_set[1]
        if attack_set[0] == 13:
            HMI.MV304.Status = attack_set[1]
        if attack_set[0] == 14:
            HMI.P301.Status = attack_set[1]
        if attack_set[0] == 15:
            HMI.P302.Status = attack_set[1]
        if attack_set[0] == 16:
            HMI.P401.Status = attack_set[1]
        if attack_set[0] == 17:
            HMI.P402.Status = attack_set[1]
        if attack_set[0] == 18:
            HMI.P403.Status = attack_set[1]
        if attack_set[0] == 19:
            HMI.P404.Status = attack_set[1]
        if attack_set[0] == 20:
            HMI.UV401.Status = attack_set[1]
        if attack_set[0] == 21:
            HMI.P501.Status = attack_set[1]
        if attack_set[0] == 22:
            HMI.P502.Status = attack_set[1]
        if attack_set[0] == 23:
            HMI.P601.Status = attack_set[1]
        if attack_set[0] == 24:
            HMI.P602.Status = attack_set[1]
        if attack_set[0] == 25:
            HMI.P603.Status = attack_set[1]

def manipulate_IO(P1,P2,P3,P4,P5,P6,attack_array):
    for attack_set in attack_array:
        if attack_set[0]==0:
            if (attack_set[1]-1):
                P1.MV101.DI_ZSO = 1
                P1.MV101.DI_ZSC = 0
            else:
                P1.MV101.DI_ZSC = 1
                P1.MV101.DI_ZSO = 0
        if attack_set[0] == 1:
            P1.P101.DI_Run = attack_set[1]-1
        if attack_set[0] == 2:
            P1.P102.DI_Run = attack_set[1]-1
        if attack_set[0] == 3:
            if (attack_set[1]-1):
                P2.MV201.DI_ZSO = 1
                P2.MV201.DI_ZSC = 0
            else:
                P2.MV201.DI_ZSC = 1
                P2.MV201.DI_ZSO = 0

        if attack_set[0] == 10:
            if (attack_set[1]-1):
                P3.MV301.DI_ZSO = 1
                P3.MV301.DI_ZSC = 0
            else:
                P3.MV301.DI_ZSC = 1
                P3.MV301.DI_ZSO = 0
        if attack_set[0] == 11:
            if (attack_set[1]-1):
                P3.MV302.DI_ZSO = 1
                P3.MV302.DI_ZSC = 0
            else:
                P3.MV302.DI_ZSC = 1
                P3.MV302.DI_ZSO = 0
        if attack_set[0] == 12:
            if (attack_set[1]-1):
                P3.MV303.DI_ZSO = 1
                P3.MV303.DI_ZSC = 0
            else:
                P3.MV303.DI_ZSC = 1
                P3.MV303.DI_ZSO = 0
        if attack_set[0] == 13:
            if (attack_set[1]-1):
                P3.MV304.DI_ZSO = 1
                P3.MV304.DI_ZSC = 0
            else:
                P3.MV304.DI_ZSC = 1
                P3.MV304.DI_ZSO = 0

        if attack_set[0] == 14:
            P3.P301.DI_Run = attack_set[1]-1
        if attack_set[0] == 15:
            P3.P302.DI_Run = attack_set[1]-1
        if attack_set[0] == 16:
            P4.P401.DI_Run = attack_set[1]-1
        if attack_set[0] == 17:
            P4.P402.DI_Run = attack_set[1]-1


        if attack_set[0] == 21:
            P5.P501.DI_Run = attack_set[1]-1
        if attack_set[0] == 22:
            P5.P502.DI_Run = attack_set[1]-1
        if attack_set[0] == 23:
            P6.P601.DI_Run = attack_set[1]-1
        if attack_set[0] == 24:
            P6.P602.DI_Run = attack_set[1]-1

def randomly_generate_actuator():
    actuator=[]
    for i in range(0,26):
        actuator.append(randint(1,2))


    return actuator