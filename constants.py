print("오픈소스 팀원 5")
print("팀장 이준한")
print("조원 최수헌")
print("조원 강우림")
print("조원 이선호")
print("조원 손영우")
print("조원 김민구")
print("")
print("[조작법] 위쪽:W 왼쪽:A 오른쪽:D 아래쪽:S")
print("")
level =int(input("난이도를 설정하세요(쉬움=1,보통=2,어려움=3) : "))

if level == 1 :
    SIZE = 3
    size = 1
    GRID_LEN = 6
    
elif level == 2 :
    SIZE = 5
    size = 2
    GRID_LEN = 5
    
elif level == 3 :
    SIZE = 5
    size = 2
    GRID_LEN = 4

else :
    SIZE = 7
    size = 3
    GRID_LEN = 3
    
GRID_PADDING = 1

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"

BACKGROUND_COLOR_DICT = {2: "#F5FFFA", 4: "#F0F8FF", 8: "#F5F5F5",
                         16: "#FFF0F5", 32: "#FFFAF0", 64: "#F5FFFA",
                         128: "#F8F8FF", 256: "#F0FFF0", 512: "#FFF5EE",
                         1024: "#FFFFF0", 2048: "#F0FFFF",

                         4096: "#ff007f", 8192: "#000000", 16384: "#f2b179",
                         32768: "#f59563", 65536: "#f67c5f", 131072: "#f65e3b" }

CELL_COLOR_DICT = {2: "#7A6F95", 4: "#776e65", 8: "#7A6F95", 16: "#776e65",
                   32: "#7A6F95", 64: "#776e65", 128: "#7A6F95",
                   256: "#776e65", 512: "#7A6F95", 1024: "#776e65",
                   2048: "#7A6F95",

                   4096: "#776e65", 8192: "#7A6F95", 16384: "#776e65",
                   32768: "#7A6F95", 65536: "#776e65", 131072: "7A6F95" }

FONT = ("Sylfaen", 40, "bold")


KEY_UP_ALT = "\'\\uf700\'"
KEY_DOWN_ALT = "\'\\uf701\'"
KEY_LEFT_ALT = "\'\\uf702\'"
KEY_RIGHT_ALT = "\'\\uf703\'"

KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"
KEY_BACK = "'b'"

KEY_J = "'j'"
KEY_K = "'k'"
KEY_L = "'l'"
KEY_H = "'h'"


