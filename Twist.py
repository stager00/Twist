from picrawler import Picrawler
from time import sleep
import readchar

crawler = Picrawler([10, 11, 12, 4, 5, 6, 1, 2, 3, 7, 8, 9])
speed = 90

manual = '''
Press keys on keyboard to control PiCrawler!
    w: Forward
    a: Turn left
    s: Backward
    d: Turn right
    i: Twist up
    k: Twist down
    j: Twist left
    l: Twist right
    esc: Quit
'''

def show_info():
    print("\033[H\033[J", end='')  # clear terminal window
    print(manual)

def twist(direction, speed):
    new_step = [[50, 50, -80], [50, 50, -80], [50, 50, -80], [50, 50, -80]]
    for i in range(4):
        for inc in range(30, 60, 5):
            if direction == 'up':
                rise = [50, 50, (-80 + inc * 0.5)]
                drop = [50, 50, (-80 - inc)]
            elif direction == 'down':
                rise = [50, 50, (-80 - inc)]
                drop = [50, 50, (-80 + inc * 0.5)]
            elif direction == 'left':
                rise = [50 + inc, 50, -80]
                drop = [50 - inc, 50, -80]
            elif direction == 'right':
                rise = [50 - inc, 50, -80]
                drop = [50 + inc, 50, -80]
            new_step[i] = rise
            new_step[(i + 2) % 4] = drop
            new_step[(i + 1) % 4] = rise
            new_step[(i - 1) % 4] = drop
            crawler.do_step(new_step, speed)

def main():
    show_info()
    while True:
        key = readchar.readkey()
        key = key.lower()
        if key in ('wasdijkl'):
            if 'w' == key:
                crawler.do_action('forward', 1, speed)
            elif 's' == key:
                crawler.do_action('backward', 1, speed)
            elif 'a' == key:
                crawler.do_action('turn left', 1, speed)
            elif 'd' == key:
                crawler.do_action('turn right', 1, speed)
            elif 'i' == key:
                twist('up', speed)
            elif 'k' == key:
                twist('down', speed)
            elif 'j' == key:
                twist('left', speed)
            elif 'l' == key:
                twist('right', speed)
            sleep(0.05)
            show_info()
        elif key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            print("\n  Quit")
            break
        sleep(0.02)

if __name__ == "__main__":
    main()
