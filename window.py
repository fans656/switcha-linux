import os
import subprocess

import keyboard


slots = {}


def switch_to(slot_name):
    wid = slots.get(slot_name)
    if wid:
        cmd = "wmctrl -ia {}".format(wid)
        os.system(cmd)
        print('Switch to {}'.format(wid))
    else:
        print('No window at slot {}'.format(slot_name.upper()))


def put_to(slot_name):
    slots[slot_name] = wid = int(get_active_window_id().decode(), 16)
    print('Put {} to slot {}'.format(wid, slot_name.upper()))


def alt_tab():
    keyboard.press_and_release('alt+tab')
    print('emulate alt+tab')


def get_active_window_id():
    return subprocess.check_output(
        "xprop -root | grep _NET_ACTIVE_WINDOW | head -1 | awk '{print $5}'",
        shell=True).strip()
