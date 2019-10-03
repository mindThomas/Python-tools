import numpy as np
from matplotlib import pyplot as plt
import cv2
from mss import mss
from PIL import Image

import keyboard

import win32con
import win32gui
import win32process
import win32api
from win32api import keybd_event

import subprocess
import time

Combs = {
    'A': [
        'SHIFT',
        'a'],
    'B': [
        'SHIFT',
        'b'],
    'C': [
        'SHIFT',
        'c'],
    'D': [
        'SHIFT',
        'd'],
    'E': [
        'SHIFT',
        'e'],
    'F': [
        'SHIFT',
        'f'],
    'G': [
        'SHIFT',
        'g'],
    'H': [
        'SHIFT',
        'h'],
    'I': [
        'SHIFT',
        'i'],
    'J': [
        'SHIFT',
        'j'],
    'K': [
        'SHIFT',
        'k'],
    'L': [
        'SHIFT',
        'l'],
    'M': [
        'SHIFT',
        'm'],
    'N': [
        'SHIFT',
        'n'],
    'O': [
        'SHIFT',
        'o'],
    'P': [
        'SHIFT',
        'p'],
    'R': [
        'SHIFT',
        'r'],
    'S': [
        'SHIFT',
        's'],
    'T': [
        'SHIFT',
        't'],
    'U': [
        'SHIFT',
        'u'],
    'W': [
        'SHIFT',
        'w'],
    'X': [
        'SHIFT',
        'x'],
    'Y': [
        'SHIFT',
        'y'],
    'Z': [
        'SHIFT',
        'z'],
    'V': [
        'SHIFT',
        'v'],
    'Q': [
        'SHIFT',
        'q'],
    '?': [
        'SHIFT',
        '/'],
    '>': [
        'SHIFT',
        '.'],
    '<': [
        'SHIFT',
        ','],
    '"': [
        'SHIFT',
        "'"],
    ':': [
        'SHIFT',
        ';'],
    '|': [
        'SHIFT',
        '\\'],
    '}': [
        'SHIFT',
        ']'],
    '{': [
        'SHIFT',
        '['],
    '+': [
        'SHIFT',
        '='],
    '_': [
        'SHIFT',
        '-'],
    '!': [
        'SHIFT',
        '1'],
    '@': [
        'SHIFT',
        '2'],
    '#': [
        'SHIFT',
        '3'],
    '$': [
        'SHIFT',
        '4'],
    '%': [
        'SHIFT',
        '5'],
    '^': [
        'SHIFT',
        '6'],
    '&': [
        'SHIFT',
        '7'],
    '*': [
        'SHIFT',
        '8'],
    '(': [
        'SHIFT',
        '9'],
    ')': [
        'SHIFT',
        '0'] }
Base = {
    '0': 48,
    '1': 49,
    '2': 50,
    '3': 51,
    '4': 52,
    '5': 53,
    '6': 54,
    '7': 55,
    '8': 56,
    '9': 57,
    'a': 65,
    'b': 66,
    'c': 67,
    'd': 68,
    'e': 69,
    'f': 70,
    'g': 71,
    'h': 72,
    'i': 73,
    'j': 74,
    'k': 75,
    'l': 76,
    'm': 77,
    'n': 78,
    'o': 79,
    'p': 80,
    'q': 81,
    'r': 82,
    's': 83,
    't': 84,
    'u': 85,
    'v': 86,
    'w': 87,
    'x': 88,
    'y': 89,
    'z': 90,
    '.': 190,
    '-': 189,
    ',': 188,
    '=': 187,
    '/': 191,
    ';': 186,
    '[': 219,
    ']': 221,
    '\\': 220,
    "'": 222,
    'ALT': 18,
    'TAB': 9,
    'CAPSLOCK': 20,
    'ENTER': 13,
    'BS': 8,
    'CTRL': 17,
    'ESC': 27,
    ' ': 32,
    'END': 35,
    'DOWN': 40,
    'LEFT': 37,
    'UP': 38,
    'RIGHT': 39,
    'SELECT': 41,
    'PRINTSCR': 44,
    'INS': 45,
    'DEL': 46,
    'LWIN': 91,
    'RWIN': 92,
    'LSHIFT': 160,
    'SHIFT': 161,
    'LCTRL': 162,
    'RCTRL': 163,
    'VOLUP': 175,
    'DOLDOWN': 174,
    'NUMLOCK': 144,
    'SCROLL': 145 }

def KeyUp(Key):
    keybd_event(Key, 0, 2, 0)


def KeyDown(Key):
    keybd_event(Key, 0, 1, 0)


VK_CODE = {'backspace': 0x08,
           'tab': 0x09,
           'clear': 0x0C,
           'enter': 0x0D,
           'shift': 0x10,
           'ctrl': 0x11,
           'alt': 0x12,
           'pause': 0x13,
           'caps_lock': 0x14,
           'esc': 0x1B,
           'spacebar': 0x20,
           'page_up': 0x21,
           'page_down': 0x22,
           'end': 0x23,
           'home': 0x24,
           'left_arrow': 0x25,
           'up_arrow': 0x26,
           'right_arrow': 0x27,
           'down_arrow': 0x28,
           'select': 0x29,
           'print': 0x2A,
           'execute': 0x2B,
           'print_screen': 0x2C,
           'ins': 0x2D,
           'del': 0x2E,
           'help': 0x2F,
           '0': 0x30,
           '1': 0x31,
           '2': 0x32,
           '3': 0x33,
           '4': 0x34,
           '5': 0x35,
           '6': 0x36,
           '7': 0x37,
           '8': 0x38,
           '9': 0x39,
           'a': 0x41,
           'b': 0x42,
           'c': 0x43,
           'd': 0x44,
           'e': 0x45,
           'f': 0x46,
           'g': 0x47,
           'h': 0x48,
           'i': 0x49,
           'j': 0x4A,
           'k': 0x4B,
           'l': 0x4C,
           'm': 0x4D,
           'n': 0x4E,
           'o': 0x4F,
           'p': 0x50,
           'q': 0x51,
           'r': 0x52,
           's': 0x53,
           't': 0x54,
           'u': 0x55,
           'v': 0x56,
           'w': 0x57,
           'x': 0x58,
           'y': 0x59,
           'z': 0x5A,
           'numpad_0': 0x60,
           'numpad_1': 0x61,
           'numpad_2': 0x62,
           'numpad_3': 0x63,
           'numpad_4': 0x64,
           'numpad_5': 0x65,
           'numpad_6': 0x66,
           'numpad_7': 0x67,
           'numpad_8': 0x68,
           'numpad_9': 0x69,
           'multiply_key': 0x6A,
           'add_key': 0x6B,
           'separator_key': 0x6C,
           'subtract_key': 0x6D,
           'decimal_key': 0x6E,
           'divide_key': 0x6F,
           'F1': 0x70,
           'F2': 0x71,
           'F3': 0x72,
           'F4': 0x73,
           'F5': 0x74,
           'F6': 0x75,
           'F7': 0x76,
           'F8': 0x77,
           'F9': 0x78,
           'F10': 0x79,
           'F11': 0x7A,
           'F12': 0x7B,
           'F13': 0x7C,
           'F14': 0x7D,
           'F15': 0x7E,
           'F16': 0x7F,
           'F17': 0x80,
           'F18': 0x81,
           'F19': 0x82,
           'F20': 0x83,
           'F21': 0x84,
           'F22': 0x85,
           'F23': 0x86,
           'F24': 0x87,
           'num_lock': 0x90,
           'scroll_lock': 0x91,
           'left_shift': 0xA0,
           'right_shift ': 0xA1,
           'left_control': 0xA2,
           'right_control': 0xA3,
           'left_menu': 0xA4,
           'right_menu': 0xA5,
           'browser_back': 0xA6,
           'browser_forward': 0xA7,
           'browser_refresh': 0xA8,
           'browser_stop': 0xA9,
           'browser_search': 0xAA,
           'browser_favorites': 0xAB,
           'browser_start_and_home': 0xAC,
           'volume_mute': 0xAD,
           'volume_Down': 0xAE,
           'volume_up': 0xAF,
           'next_track': 0xB0,
           'previous_track': 0xB1,
           'stop_media': 0xB2,
           'play/pause_media': 0xB3,
           'start_mail': 0xB4,
           'select_media': 0xB5,
           'start_application_1': 0xB6,
           'start_application_2': 0xB7,
           'attn_key': 0xF6,
           'crsel_key': 0xF7,
           'exsel_key': 0xF8,
           'play_key': 0xFA,
           'zoom_key': 0xFB,
           'clear_key': 0xFE,
           '+': 0xBB,
           ',': 0xBC,
           '-': 0xBD,
           '.': 0xBE,
           '/': 0xBF,
           '`': 0xC0,
           ';': 0xBA,
           '[': 0xDB,
           '\\': 0xDC,
           ']': 0xDD,
           "'": 0xDE,
           '`': 0xC0}


def press(*args):
    '''
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        time.sleep(.05)
        win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)


def pressAndHold(*args):
    '''
    press and hold. Do NOT release.
    accepts as many arguments as you want.
    e.g. pressAndHold('left_arrow', 'a','b').
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        time.sleep(.05)


def pressHoldRelease(*args):
    '''
    press and hold passed in strings. Once held, release
    accepts as many arguments as you want.
    e.g. pressAndHold('left_arrow', 'a','b').

    this is useful for issuing shortcut command or shift commands.
    e.g. pressHoldRelease('ctrl', 'alt', 'del'), pressHoldRelease('shift','a')
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        time.sleep(.05)

    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(.1)


def release(*args):
    '''
    release depressed keys
    accepts as many arguments as you want.
    e.g. release('left_arrow', 'a','b').
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, win32con.KEYEVENTF_KEYUP, 0)




def GetNESwindow():
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            #_, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if "NES" in win32gui.GetWindowText(hwnd):
                hwnds.append(hwnd)
                print("Found window")
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds[0]


hwnd = GetNESwindow()
print(hwnd)

win = win32gui.GetWindowRect(hwnd)
win32gui.MoveWindow(hwnd, win[0], win[1], 500, 500, True)
#win32gui.SetForegroundWindow(hwnd)
#win32api.PostMessage( hwnd,win32con.WM_KEYDOWN, 39, 0)

#for hwnd in get_hwnds_for_pid(notepad.pid):
#    print(hwnd, "=>", win32gui.GetWindowText(hwnd))
#    print(win32gui.GetWindowRect(hwnd))

sct = mss()

dataLog = np.empty((0,7), int)

while 1:
    win = win32gui.GetWindowRect(hwnd)
    mon = {'top': win[1], 'left': win[0], 'width': win[2] - win[0], 'height': win[3] - win[1]}
    #win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 39, 0)
    im = sct.grab(mon)
    img = Image.frombytes('RGB', im.size, im.rgb, decoder_name='raw')
    image = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    region = image[80:440, 20:480]  # print(image.shape)

    thresh = cv2.inRange(region, (50,50,100), (255, 255, 255))
    out = cv2.bitwise_and(region, region, mask=thresh)
    region2 = out[180:out.shape[0], 0:out.shape[1]]  # print(image.shape)

    cv2.imshow('Image', region2)

    region3 = cv2.cvtColor(region2, cv2.COLOR_BGR2GRAY);
    #region = cv2.GaussianBlur(region, (5, 5), 0)
    blurred = cv2.blur(region3, (5, 5))
    edges = cv2.Canny(blurred, 150, 260, apertureSize = 3)

    bottomLine = region3[region3.shape[0]-5:region3.shape[0], 0:region3.shape[1]]
    ret, botline = cv2.threshold(bottomLine, 150, 255, cv2.THRESH_BINARY)
    trackBorderBottom = []
    for y in range(0, botline.shape[0]):
        for x in range(2, botline.shape[1]-1):
            if ((botline[y,x-2] == 0) and (botline[y,x-1] == 255) and (botline[y,x] == 255) and (botline[y,x+1] == 0)):
                if (not x in trackBorderBottom):
                    trackBorderBottom.append(x)

    trackBorderBottom = np.array(trackBorderBottom)
    print('Bottom', trackBorderBottom)
    left = trackBorderBottom[trackBorderBottom < (botline.shape[1]/2)]
    right = trackBorderBottom[trackBorderBottom > (botline.shape[1]/2)]

    if (left.shape[0] > 0):
        leftTrackBorderBottom = min(left)
    else:
        leftTrackBorderBottom = 0

    if (right.shape[0] > 0):
        rightTrackBorderBottom = max(right)
    else:
        rightTrackBorderBottom = botline.shape[1]

    trackCenterBottom = (leftTrackBorderBottom + rightTrackBorderBottom) / 2
    print('Bottom center:', trackCenterBottom)

    topLine = region3[0:5, 0:region3.shape[1]]
    ret, topline = cv2.threshold(topLine, 150, 255, cv2.THRESH_BINARY)
    trackBorderTop = []
    z = 0
    for y in range(0, topline.shape[0]):
        for x in range(1, topline.shape[1]-1):
            if ((topline[y,x-2] == 0) and ((topline[y,x-1] == 255) or (topline[y,x] == 255)) and (topline[y,x+1] == 0)):
                z = z + 1
                if (not x in trackBorderTop):
                    trackBorderTop.append(x)

    trackBorderTop = np.array(trackBorderTop)
    print('Top', trackBorderTop)

    if (trackBorderTop.shape[0] > 0):
        leftTrackBorderTop = min(trackBorderTop)
        rightTrackBorderTop = max(trackBorderTop)
    else:
        leftTrackBorder = 0
        rightTrackBorderTop = botline.shape[1]

    trackCenterTop = (leftTrackBorderTop + rightTrackBorderTop) / 2
    print('Top center:', trackCenterTop)

    cv2.imshow('Top line', topline)

    data = np.array([keyboard.is_pressed('x'),  keyboard.is_pressed('left'), keyboard.is_pressed('right'), leftTrackBorderTop, rightTrackBorderTop, leftTrackBorderBottom, rightTrackBorderBottom])
    dataLog = np.row_stack((dataLog, data))

    cv2.imshow('Edges', edges)
    cv2.imwrite('edges.png', edges)

    # # np.poly1d([a b c])
    # cv2.imshow('Image', blurred)
    # cv2.imshow('Edges', edges)
    #
    # dots = cv2.findNonZero(edges)
    # dots2 = dots.reshape(dots.shape[0], 2)
    #
    # dotsLeft = dots2[(dots2[:, 0] < trackCenter - 80) & (dots2[:, 1] > 10)]
    # dotsRight = dots2[(dots2[:, 0] > trackCenter + 80) & (dots2[:, 1] > 10)]
    #
    # # Just verify that it has been written correctly and that the x-y coordinates are correct
    # newImg = np.zeros(edges.shape, np.uint8)
    # newImg[dotsLeft[:, 1], dotsLeft[:, 0]] = 150
    # newImg[dotsRight[:, 1], dotsRight[:, 0]] = 150
    # cv2.imshow('Converted', newImg)
    #
    # right_curve = np.poly1d(np.polyfit(dotsLeft[:, 1], dotsLeft[:, 0], 2))
    # left_curve = np.poly1d(np.polyfit(dotsRight[:, 1], dotsRight[:, 0], 2))
    #
    # rightCurveY = np.linspace(0, (edges.shape[0] - 1), (edges.shape[0])).astype(int)
    # rightCurveX = right_curve(rightCurveY).astype(int)
    # rightCurveX[rightCurveX < 0] = 0
    # rightCurveX[rightCurveX >= edges.shape[1]] = edges.shape[1] - 1
    #
    # leftCurveY = np.linspace(0, (edges.shape[0] - 1), (edges.shape[0])).astype(int)
    # leftCurveX = left_curve(leftCurveY).astype(int)
    # leftCurveX[leftCurveX < 0] = 0
    # leftCurveX[leftCurveX >= edges.shape[1]] = edges.shape[1] - 1
    #
    # calcRightDots = np.column_stack((rightCurveX, rightCurveY))
    # calcLeftDots = np.column_stack((leftCurveX, leftCurveY))
    #
    # visPoly = np.zeros([edges.shape[0], edges.shape[1], 3], np.uint8)
    # visPoly = visPoly + cv2.cvtColor(cv2.multiply(edges, 0.3), cv2.COLOR_GRAY2BGR)
    # visPoly[calcRightDots[:, 1], calcRightDots[:, 0], 1] = 255
    # visPoly[calcLeftDots[:, 1], calcLeftDots[:, 0], 2] = 255
    # cv2.imshow('Polynomial line fit', visPoly)

    #minLineLength = 100
    #maxLineGap = 100
    #lines = cv2.HoughLines(edges,1,np.pi/180,150)
    #for rho, theta in lines[0]:
        #a = np.cos(theta)
        #b = np.sin(theta)
        #x0 = a * rho
        #y0 = b * rho
        #x1 = int(x0 + 1000 * (-b))
        #y1 = int(y0 + 1000 * (a))
        #x2 = int(x0 - 1000 * (-b))
        #y2 = int(y0 - 1000 * (a))

    #    cv2.line(region, (x1, y1), (x2, y2), (0, 255, 255), 2)
    #lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    #for x1, y1, x2, y2 in lines[0]:
    #    cv2.line(region, (x1, y1), (x2, y2), (0, 255, 0), 2)

    #cv2.waitKey(25)
    #break

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

    #print(keyboard.is_pressed('right'))

print(dataLog)
#dataLogA = np.asarray(dataLog)
np.savetxt("foo.csv", dataLog, delimiter=",", fmt='%d', newline='\r\n')
#dataLog.tofile('foo.csv',sep=',',format='%d')