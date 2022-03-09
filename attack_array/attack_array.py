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





