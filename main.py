import keyboard

import window


for slot_ch in list('1234567890uiopklm') + ['comma', 'dot', 'slash', 'semicolon']:
    keyboard.add_hotkey(
        'ctrl+alt+shift+' + slot_ch,
        window.put_to,
        args=(slot_ch,)
    )
    keyboard.add_hotkey(
        'ctrl+alt+' + slot_ch,
        window.switch_to,
        args=(slot_ch,)
    )

keyboard.add_hotkey('ctrl+alt+j', window.alt_tab)

print 'Started'
keyboard.wait()
