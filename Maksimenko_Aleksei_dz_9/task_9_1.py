from time import sleep
from sty import fg
from sty import Style, RgbFg
from termcolor import colored

fg.orange = Style(RgbFg(255, 150, 50))


class TrafficLight:
    __color = [fg.red + 'Red' + fg.rs, fg.orange + 'Amber' + fg.rs, colored('Green', 'green')]

    def on_running(self):
        i = 0
        while i < 3:
            print(f'switching the Light \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(10)
            i += 1


example = TrafficLight()
example.on_running()
