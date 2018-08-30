import win32api as wapi
# import time

vk = {
    "1":            0x31,
    "2":            0x32,
    "3":            0x33,
    "4":            0x34,
    "5":            0x35,
    "6":            0x36,
    "7":            0x37,
    "8":            0x38,
    "9":            0x39,
    "0":            0x30,

    "NUMPAD1":    0x61,   
    "NUMPAD2":    0x62,    
    "NUMPAD3":    0x63,    
    "NUMPAD4":    0x64,    
    "NUMPAD5":    0x65,    
    "NUMPAD6":    0x66,    
    "NUMPAD7":    0x67,   
    "NUMPAD8":    0x68,    
    "NUMPAD9":    0x69,    
    "NUMPAD0":    0x60,    
    "DIVIDE":      0x6F,    
    "MULTIPLY":  0x6A,     
    "SUBSTRACT":    0x6D,      
    "ADD":        0x6B,    
    "DECIMAL":    0x6E,    
    "NUMPADENTER":  0x0D,      

    "A":        0x41,
    "B":            0x42,
    "C":            0x43,
    "D":            0x44,
    "E":            0x45,
    "F":            0x46,
    "G":            0x47,
    "H":            0x48,
    "I":            0x49,
    "J":            0x4A,
    "K":            0x4B,
    "L":            0x4C,
    "M":            0x4D,
    "N":            0x4E,
    "O":            0x4F,
    "P":            0x50,
    "Q":            0x51,
    "R":            0x52,
    "S":            0x53,
    "T":            0x54,
    "U":            0x55,
    "V":            0x56,
    "W":            0x57,
    "X":            0x58,
    "Y":            0x59,
    "Z":            0x5A,

    "F1":          0x70,
    "F2":          0x71,
    "F3":          0x72,
    "F4":          0x73,
    "F5":          0x74,
    "F6":          0x75,
    "F7":          0x76,
    "F8":          0x77,
    "F9":          0x78,
    "F10":        0x79,
    "F11":        0x7A,
    "F12":        0x7B,

    "UP":          0x26,
    "LEFT":      0x25,
    "RIGHT":        0x27,
    "DOWN":      0x28,

    "ESC":        0x1B,
    "SPACE":        0x20,      
    "RETURN":      0x0D,       
    "INSERT":      0x2D,       
    "DELETE":      0x2E,       
    "HOME":      0x24,
    "END":        0x23,
    "PRIOR":        0x21,      
    "NEXT":      0x22,     
    "BACK":      0x08,
    "TAB":        0x09,
    "LCONTROL":  0xA2,     
    "RCONTROL":  0xA3,     
    "LSHIFT":      0xA0,       
    "RSHIFT":      0xA1,       
    "LMENU":        0xA4,      
    "RMENU":        0xA5,      
    "LWIN":      0x5B,
    "RWIN":      0x5C,
    "APPS":      0x5D,
    "CAPITAL":    0x14,    
    "NUMLOCK":    0x90,    
    "SCROLL":      0x91,       

    "MINUS":        0xBD,      
    "LBRACKET":  0xDB,     
    "RBRACKET":  0xDD,     
    "SEMICOLON":    0xBA,      
    "APOSTROPHE":   0xDE,
    "GRAVE":        0xC0,
    "BACKSLASH":    0xDC,
    "COMMA":        0xBC,
    "PERIOD":      0xBE, 
    "SLASH":        0xBF,
}
kv = {v: k for k, v in vk.items()}


keyList = []
for char in vk:
    keyList.append(vk[char])
# print(keyList)
keystates= {}
def getKeys():
    keys = []
    for key in keyList:

        # print(type(key))
        keystate = wapi.GetAsyncKeyState(key)
        if keystate == -32768 or keystate == 1:
            keystate = 1
        else:
            keystate = 0
        keystates[kv[key]] = keystate

    return keystates
if __name__ == '__main__':
    while True:
        print(getKeys())