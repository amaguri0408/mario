import time
import argparse

# 定数
G = 0.5

parser = argparse.ArgumentParser(description="")

# parser.add_argument('', default="", type=int, help="")
# parser.add_argument('', action="store_true", help="")
parser.add_argument('-m', '--mario', action="store_true", help="")
parser.add_argument('-l', '--luigi', action="store_true", help="")
parser.add_argument('-j', '--jump', action="store_true", help="")

args = parser.parse_args()
state = {k: v for k, v in args._get_kwargs()}


pose = [
    [
        "_____rrrrr______",
        "____rrrrrrrrrr__",
        "____kkkyyky_____",
        "___kykyyykyyy___",
        "___kykkyyykyyy__",
        "___kkyyyykkkk___",
        "_____yyyyyyy____",
        "____bbrbbb______",
        "___bbbrbbrbbb___",
        "__bbbbrrrrbbbb__",
        "__yybryrryrbyy__",
        "__yyyrrrrrryyy__",
        "__yyrrrrrrrryy__",
        "____rrr__rrr____",
        "___bbb____bbb___",
        "__bbbb____bbbb__",
    ],
]

jump = [
    [
        "_____________yyy",
        "______rrrrr__yyy",
        "_____rrrrrrrrryy",
        "_____kkkyyky_bbb",
        "____kykyyykyybbb",
        "____kykkyyykyyyb",
        "____kkyyyykkkkb_",
        "______yyyyyyyb__",
        "__bbbbbrbbbrb___",
        "_bbbbbbbrbbbr__b",
        "yybbbbbbrrrrr__b",
        "yyy_rrbrryrryrbb",
        "_y_brrrrrrrrrrbb",
        "__bbbrrrrrrrrrbb",
        "_bbbrrrrrrr_____",
        "_b__rrrr________",
    ],
]

walk = [
    [
        "_____rrrrr______",
        "____rrrrrrrrr___",
        "____kkkyyky_____",
        "___kykyyykyyy___",
        "___kykkyyykyyy__",
        "___kkyyyykkkk___",
        "_____yyyyyyy____",
        "__bbbbrrbb______",
        "yybbbbrrrbbbyyy_",
        "yyy_bbryrrrbbyy_",
        "yy__rrrrrrr__b__",
        "___rrrrrrrrrbb__",
        "__rrrrrrrrrrbb__",
        "_bbrrr___rrrbb__",
        "_bbb____________",
        "__bbb___________",
    ],
    [
        "_____rrrrr______",
        "____rrrrrrrrr___",
        "____kkkyyky_____",
        "___kykyyykyyy___",
        "___kykkyyykyyy__",
        "___kkyyyykkkk___",
        "_____yyyyyyy____",
        "____bbrbbb______",
        "___bbbbrrbb_____",
        "___bbbrryrry____",
        "___bbbbrrrrr____",
        "___rbbyyyrrr____",
        "____rbyyrrr_____",
        "_____rrrbbb_____",
        "_____bbbbbbb____",
        "_____bbbb_______",
    ],
    [
        "________________",
        "_____rrrrr______",
        "____rrrrrrrrr___",
        "____kkkyyky_____",
        "___kykyyykyyy___",
        "___kykkyyykyyy__",
        "___kkyyyykkkk___",
        "_____yyyyyyy____",
        "____bbbbrb_y____",
        "___ybbbbbbyyy___",
        "__yyrbbbbbyy____",
        "__bbrrrrrrr_____",
        "__brrrrrrrr_____",
        "_bbrrr_rrr______",
        "_b____bbb_______",
        "______bbbb______",
    ],
]

color_dict = {"k": 0xeb, "r": 1, "g": 2, "y": 3, "b": 4, "w": 7}
color_dict_luigi = {"k": 0xeb, "r": color_dict["w"], "y": 3, "b": color_dict["g"]}
def print_color(color="", text="■ "):
    if not color:
        print("  ", end="")
        # print(text, end="")
    else:
        print(f"\033[38;5;{color}m", end="")
        print(text, end="")
        print("\033[m", end="")

def func_walk(mario=True, luigi=False):
    for line in pose[0]:
        if mario or not luigi:
            for pixel in line:
                if pixel == "_":
                    print_color()
                else:
                    print_color(color_dict[pixel])
            for _ in range(1):
                print_color()
        if luigi:
            for pixel in line:
                if pixel == "_":
                    print_color()
                else:
                    print_color(color_dict_luigi[pixel])
        print()
    try:
        time.sleep(0.5)
        # time.sleep(1)
    except KeyboardInterrupt:
        print()
        exit()

    idx = 0
    while True:
        print("\033[16A", end="")
        for line in walk[idx]:
            if mario or not luigi:
                for pixel in line:
                    if pixel == "_":
                        print_color()
                    else:
                        print_color(color_dict[pixel])
                for _ in range(1):
                    print_color()
            if luigi:
                for pixel in line:
                    if pixel == "_":
                        print_color()
                    else:
                        print_color(color_dict_luigi[pixel])
            print()
        idx = (idx + 1) % len(walk)
        try:
            time.sleep(0.08)
            # time.sleep(1)
        except KeyboardInterrupt:
            print()
            exit()


G = 0.2
def func_jump(mario=True, luigi=False):
    state = 0
    stand_time = 1
    stand_start_time = time.time()
    std_speed = -2
    speed = std_speed
    H = int(speed ** 2 // (2 * G) + 1 + 16)
    std_mario_y = H - 16 - 1
    mario_y = std_mario_y
    print("\n" * H)
    while True:
        print(f"\033[{H}A", end="")
        print(f"{' ' * 40}\n" * H)
        print(f"\033[{H}A", end="")
        print("\n" * (int(mario_y) - 1))
        if state == 0:
            for line in pose[0]:
                if mario or not luigi:
                    for pixel in line:
                        if pixel == "_":
                            print_color()
                        else:
                            print_color(color_dict[pixel])
                    for _ in range(1):
                        print_color()
                if luigi:
                    for pixel in line:
                        if pixel == "_":
                            print_color()
                        else:
                            print_color(color_dict_luigi[pixel])
                print()
            if time.time() - stand_start_time >= stand_time:
                state = 1
        elif state == 1:
            for line in jump[0]:
                if mario or not luigi:
                    for pixel in line:
                        if pixel == "_":
                            print_color()
                        else:
                            print_color(color_dict[pixel])
                    for _ in range(1):
                        print_color()
                if luigi:
                    for pixel in line:
                        if pixel == "_":
                            print_color()
                        else:
                            print_color(color_dict_luigi[pixel])
                print()
            mario_y += speed
            speed += G
            if mario_y >= std_mario_y:
                mario_y = std_mario_y
                state = 0
                speed = std_speed
                stand_start_time = time.time()
        
        try:
            time.sleep(0.01)
        except KeyboardInterrupt:
            print()
            exit()

if args.jump:
    func_jump(mario=args.mario, luigi=args.luigi)
else:
    func_walk(mario=args.mario, luigi=args.luigi)