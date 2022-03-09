from pycomm.ab_comm.clx import Driver as ClxDriver

# PLC IP addresses
PLC_IPS = {
    'plc1': '192.168.1.10',
    'tag_plc1': ['HMI_LIT101.Pv','HMI_FIT101.Pv'],
    'plc2': '192.168.1.20',
    'tag_plc2': ['HMI_FIT201.Pv'],
    'plc3': '192.168.1.30',
    'tag_plc3': ['HMI_LIT301.Pv','HMI_FIT301.Pv','HMI_DPIT301.Pv'],
    'plc4': '192.168.1.40',
    'tag_plc4': ['HMI_LIT401.Pv','HMI_FIT401.Pv'],
    'plc5': '192.168.1.50',
    'plc6': '192.168.1.60',
    'tag_plc6': ['HMI_FIT601.Pv'],
    'plc1r': '192.168.1.11',
    'plc2r': '192.168.1.21',
    'plc3r': '192.168.1.31',
    'plc4r': '192.168.1.41',
    'plc5r': '192.168.1.51',
    'plc6r': '192.168.1.61',
}
# Read PLC Values for the configured tags
def test_plc_read_val(plc_ip, tag_name):
    plc = ClxDriver()
    if plc.open(plc_ip):
        tagg = plc.read_tag(tag_name)
        plc.close()
        return (tagg)
    else:
        print("Unable to open", plc_ip)


def get_sensor_value():
    s=[]
    s.append( test_plc_read_val(PLC_IPS['plc1'], 'HMI_FIT101.Pv'))
    s.append( test_plc_read_val(PLC_IPS['plc1'], 'HMI_LIT101.Pv'))
    s.append( test_plc_read_val(PLC_IPS['plc2'], 'HMI_FIT201.Pv'))
    s.append( test_plc_read_val(PLC_IPS['plc3'], 'HMI_LIT301.Pv'))
    s.append( test_plc_read_val(PLC_IPS['plc3'], 'HMI_FIT301.Pv'))
    s.append( test_plc_read_val(PLC_IPS['plc3'], 'HMI_DPIT301.Pv'))
    s.append( test_plc_read_val(PLC_IPS['plc4'], 'HMI_LIT401.Pv'))
    s.append( test_plc_read_val(PLC_IPS['plc4'], 'HMI_FIT401.Pv'))
    s.append( test_plc_read_val(PLC_IPS['plc6'], 'HMI_FIT501.Pv'))
    s.append( test_plc_read_val(PLC_IPS['plc6'], 'HMI_FIT601.Pv'))
    return s

def test_plc_write(plc_ip, tag_name, value, tag_type):
    """Write a plc tag and print a BOOL status code.

    :plc_ip: TODO
    :tag_name: TODO
    :value: TODO
    :tag_type: TODO

    """
    plc = ClxDriver()
    if plc.open(plc_ip):
        print(plc.write_tag(tag_name, value, tag_type))
        plc.close()
    else:
        print("Unable to open", plc_ip)

def per(n, a):
    for i in range(1 << n):
        s = bin(i)[2:]
        s = '0' * (n - len(s)) + s
        a.append(map(int, list(s)))
    return a

def map_tag_name(x):
    return {
        0: "HMI_MV101",
        1: "HMI_P101",
        2: "HMI_P102",
        3: "HMI_MV201",
        4: "HMI_P201",
        5:  "HMI_P202",
        6:  "HMI_P203",
        7:  "HMI_P204",
        8:  "HMI_P205",
        9:  "HMI_P206",
        10:  "HMI_MV301",
        11:  "HMI_MV302",
        12:  "HMI_MV303",
        13:  "HMI_MV304",
        14:  "HMI_P301",
        15:  "HMI_P302",
        16:  "HMI_P401",
        17:  "HMI_P402",
        18:  "HMI_P403",
        19:  "HMI_P404",
        20:  "HMI_UV401",
        21:  "HMI_P501",
        22:  "HMI_P502",
        23:  "HMI_P601",
        24:  "HMI_P602",
        25:  "HMI_P603",


    }.get(x, "error")

def map_plc(x):
    return {
        0: 'plc1',
        1: 'plc1',
        2: 'plc1',
        3: 'plc2',
        4: 'plc2',
        5: 'plc2',
        6: 'plc2',
        7: 'plc2',
        8: 'plc2',
        9: 'plc2',
        10: 'plc3',
        11: 'plc3',
        12: 'plc3',
        13: 'plc3',
        14: 'plc3',
        15: 'plc3',
        16: 'plc4',
        17: 'plc4',
        18: 'plc4',
        19: 'plc4',
        20: 'plc4',
        21: 'plc5',
        22: 'plc5',
        23: 'plc6',
        24: 'plc6',
        25: 'plc6',

    }.get(x, "error")

def configure_function(actuator_array,position):
    for i in position:
        cmd=actuator_array[i]
        plc=map_plc(i)
        auto_str = map_tag_name(i) + ".Auto"
        cmd_str = map_tag_name(i) + ".Cmd"
        test_plc_write(PLC_IPS[plc], auto_str, 0, 'BOOL')
        test_plc_write(PLC_IPS[plc], cmd_str, cmd, 'INT')

