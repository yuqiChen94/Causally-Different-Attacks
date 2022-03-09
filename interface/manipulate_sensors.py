def manipulate_LIT101(HMI,fake_lit101):
    # 1100.0, 800.0, 500.0, 250.0
    if fake_lit101>1100:
        HMI.LIT101.AHH=1
    if fake_lit101 > 800:
        HMI.LIT101.AH = 1
    if fake_lit101 < 500:
        HMI.LIT101.AL = 1
    if fake_lit101 < 250:
        HMI.LIT101.ALL = 1

def manipulate_LIT301(HMI,fake_lit301):
    if fake_lit301> 1200.0:
        HMI.LIT301.AHH=1
    if fake_lit301 > 1000:
        HMI.LIT301.AH = 1
    if fake_lit301 < 800:
        HMI.LIT301.AL = 1
    if fake_lit301 < 250:
        HMI.LIT301.ALL = 1


def manipulate_LIT401(HMI,fake_lit401):
    if fake_lit401>1200:
        HMI.LIT401.AHH=1
    if fake_lit401 > 1000:
        HMI.LIT401.AH = 1
    if fake_lit401 < 800:
        HMI.LIT401.AL = 1
    if fake_lit401 < 250:
        HMI.LIT401.ALL = 1