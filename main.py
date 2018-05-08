import os
import subprocess

from flask import *


app = Flask(__name__)


"""
map <slot-name> to <window-id>

<slot-name> is 'U', 'I', 'O', 'P', 'J', 'K', 'L' etc
<window-id> is the first column of 'wmctrl -l', see 'man wmctrl'
"""
slots = {}


@app.route('/<path:path>')
def index(path):
    parts = path.split('-')
    operation = parts[0]
    slot_name = parts[-1]
    if operation == 'switch':
        switch_to(slot_name)
    elif operation == 'put':
        put_to(slot_name)
    return ''


def switch_to(slot_name):
    wid = slots.get(slot_name)
    if wid:
        cmd = "wmctrl -ia {}".format(wid)
        os.system(cmd)
        print 'Switch to {}'.format(wid)
    else:
        print 'No window at slot {}'.format(slot_name.upper())


def put_to(slot_name):
    slots[slot_name] = wid = get_active_window_id()
    print 'Put {} to slot {}'.format(wid, slot_name.upper())


def get_active_window_id():
    return subprocess.check_output(
        "xprop -root | grep _NET_ACTIVE_WINDOW | head -1 | awk '{print $5}'",
        shell=True).strip()


if __name__ == '__main__':
    app.run(port=6560)
