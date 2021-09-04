#region Ascii control code set
from telnetlib3.telopt import REJECTED


BELL                = chr(0x07) 
NEW_PAGE            = chr(0x0C)
DEVICE_CONTROL_3    = chr(0x13)
CLEAR_EOL           = chr(0x18)
SS2                 = chr(0x19)
ESCAPE              = chr(0x1B)
UNIT_SEPARATOR      = chr(0x1F)
#endregion


#region Atribute
NORMAL_SIZE         = chr(0x4C)
NORMAL_VIDEO        = chr(0x5C)
#endregion


#region Cursor direction
CURSOR_LEFT         = chr(0x08)
CURSOR_RIGHT        = chr(0x09)
CURSOR_DOWN         = chr(0x0A)
CURSOR_UP           = chr(0x0B)
#endregion


#region Minitel keys
ENVOI               = chr(0x41)
RETOUR              = chr(0x42)
REPETITION          = chr(0x43)
GUIDE               = chr(0x44)
ANNULATION          = chr(0x45)
SOMMAIRE            = chr(0x46)
CORRECTION          = chr(0x47)
SUITE               = chr(0x48)
CONNEXION           = chr(0x49)
#endregion


COLOR = {
    'BLACK'     : 0,
    'RED'       : 1,
    'GREEN'     : 2,
    'YELLOW'    : 3,
    'BLUE'      : 4,
    'MAGENTA'   : 5,
    'CYAN'      : 6,
    'WHITE'     : 7
}

SIZE = {
    'NORMAL'        : 0,
    'DOUBLE_HEIGHT' : 1,
    'DOUBLE_WIDTH'  : 2,
    'DOUBLE'        : 3,
}

BLINK = {
    'ON'    : chr(0x48),
    'OFF'   : chr(0x49)
}

UNDERLINE = {
    'OFF'   : chr(0x59),
    'ON'    : chr(0x5A)
}

INVERT = {
    'OFF'   : chr(0x5C),
    'ON'    : chr(0x5D)
}

CURSOR = {
    'ON'    : chr(0x11),
    'OFF'   : chr(0x14) 
}