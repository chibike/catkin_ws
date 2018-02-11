#!/usr/bin/env python

import curses

def main(stdscr):
    stdscr.nodelay(1)
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c != -1:
            # print numeric value
            stdscr.addstr(str(c) + ' ')
            stdscr.refresh()
            # return cursor to start position
            stdscr.move(0, 0)

if __name__ == '__main__':
    curses.wrapper(main)

##from pynput.keyboard import Key, Listener
##
##def on_press(key):
##    print '{0} pressed'.format(key)
##
##def on_release(key):
##    print '{0} release'.format(key)
##    if key == Key.esc:
##        return False
##
### Collect events until released
##with Listener(on_press=on_press, on_release=on_release) as listener:
##    listener.join()
