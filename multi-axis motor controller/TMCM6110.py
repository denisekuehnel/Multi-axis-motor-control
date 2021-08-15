RotateRight = 1 # ROR
RotateLeft = 2 # ROL
MotorStop = 3 # MST
MoveToPosition = 4  # MVP
SetAxisParameter = 5 # SAP
GetAxisParameter = 6 # GAP
StoreAxisParameter = 7 #STAP
RestoreAxisParameter = 8 # RSAP
ReferenceSearch = 13 # RFS
WaitForAnEventToOccur = 24 # WAIT

class MoveToPositionType():
    ''' 0 absolute \n
    1 relative \n
    2 coordinate \n'''
    absolute = 0
    relative = 1
    coordinate = 2

class ReferenceSearchType():
    '''START - start reference search \n 
    STOP - abort reference search \n
    STATUS - get status, value <0> (reference search active) or <other values> (no reference search active)'''

    START = 0
    STOP = 1 
    STATUS = 2

class WaitForAnEventToOccurType():
    '''Ticks - timer ticks, value <no. of ticks> \n
    POS - target position reached, value <no. of ticks for timeout> \n
    REFSW - reference switch, value <no. of ticks for timeout> \n
    LIMSW - limit switch, value <no.of ticks for timeout> \n
    RFS - reference search completed, value <no.of ticks for timeout> '''
    Ticks = 0 
    POS = 1
    REFSW = 2
    LIMSW = 3
    RFS = 4

class AxisParameterType():
    '''All axis parameters can be used wit SetAxisParameter and GetAxisParameter.\n
    See Documentation for further information about values. \n 
    https://cdn-reichelt.de/documents/datenblatt/C300/HB_TMCM6110_FM.pdf
    '''
    TargetPosition = 0
    ActualPosition = 1
    TargetSpeed = 2
    ActualSpeed = 3
    MaximumPositioningSpeed = 4
    MaximumAcceleration = 5
    AbsoluteMaximumCurrentScale = 6
    StandbyCurrent = 7
    TargetPositionReached = 8
    ReferenceSwitchStatus = 9
    RightLimitSwitchStatus = 10
    LeftLimitSwitchStatus = 11
    RightLimitSwitchDisable = 12
    LeftLimitSwitchDisable = 13
    MinimumSpeed = 130
    ActualAcceleration = 135
    RampMode = 138
    MicrostepResolution = 140
    ReferenceSwitchTolerance = 141
    SoftStopFlag = 149
    RampDivisor = 153
    #All numbers except 154 – 167
    SmartEnergyCurrentMinumum = 168
    SmartEnergyCurrentDownStep = 169
    SmartEnergyHysteresis = 170
    SmartEnergyCurrentStepUp = 171
    SmartEnergyHysteresisStart = 172
    StallGuard2FilterEnable = 173
    StallGuard2Threshold = 174
    # ab 168- 174 wieder
    # nicht 175-179
    SmartEnergyActualCurrent = 180
    StopOnStall = 181
    SmartEnergyThresholdSpeed = 182
    SmartEnergySlowRunCurrent = 183
    # 180-183
    ReferenceSearchMode = 193 # RSM # address, commandNr, type, motor, value, val val val 
    ReferencingSearchSpeed = 194 
    ReferencingSwitchSpeed = 195
    DistanceEndSwitches = 196

    # nein 184, ja 193 – Ende

class ReferenceSearchModeValue():
    '''1 search left stop switch only \n
    2 search right stop switch, then search left stop switch \n
    3 search right stop switch, then search left stop switch from both sides \n
    4 search left stop switch from both sides \n
    5 search home switch in negative direction, reverse the direction when 
    left stop switch reached \n
    6 search home switch in positive direction, reverse the direction when
    right stop switch reached \n
    7 search home switch in positive direction, ignore end switches \n
    8 search home switch in negative direction, ignore end switches \n'''
    SearchLeftStopSwitch = 1
    SearchRightStopSwitch = 2
    SearchRightStopSwitchBothSides = 3
    SearchLeftStopSwitchBothSides = 4
    SearchHomeSwitchNegativeDirection = 5
    SearchHomeSwitchPositiveDirection = 6
    SearchHomeSwitchPositiveDirection2 = 7
    SearchHomeSwitchNegativeDirection2 = 8
    search_modes = {'SearchLeftStopSwitch' : SearchLeftStopSwitch, 
                        'SearchRightStopSwitch' : SearchRightStopSwitch,
                        'SearchRightStopSwitchBothSides' : SearchRightStopSwitchBothSides,
                        'SearchLeftStopSwitchBothSides' : SearchLeftStopSwitchBothSides,
                        'SearchHomeSwitchNegativeDirection' : SearchHomeSwitchNegativeDirection,
                        'SearchHomeSwitchPositiveDirection' : SearchHomeSwitchPositiveDirection,
                        'SearchHomeSwitchPositiveDirection2' : SearchHomeSwitchPositiveDirection2,
                        'SearchHomeSwitchNegativeDirection2' : SearchHomeSwitchNegativeDirection2}


# SAP (All numbers except 154 – 167, ab 168- 174 wieder, nicht 175-179, 180-183, nein 184, ja 193 – Ende) bei denen mit Einheiten sinnvoll, wenn z.B. ranges schon abfangen + Einheiten)
# GAP ( - „ – (gilt für beides))
# STAP (ganz gut, in gui evtl. definieren welches stage modell welche par hat)
# RSAP ( -„ - )
# RFS 
