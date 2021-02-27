from __future__ import print_function
from Xlib import X, display
from Xlib.ext import randr

import win32api
import ctypes
# print(len(win32api.EnumDisplayMonitors()))
monitors=win32api.EnumDisplayMonitors()
print(win32api.EnumDisplayMonitors())
# print(win32api.GetUserName())
d=win32api.EnumDisplayDevices()
print(d.DeviceName)
print(d.DeviceString)
# print(d.StateFlags)
print(d.DeviceID)
# print(d.DeviceKey)
# print(d.Size)

# from Xlib import display
# from Xlib.ext import randr

# def find_mode(id, modes):
#    for mode in modes:
#        if id == mode.id:
#            return "{}x{}".format(mode.width, mode.height)

# def get_display_info():
#     d = display.Display(':0')
#     screen_count = d.screen_count()
#     default_screen = d.get_default_screen()
#     result = []
#     screen = 0
#     info = d.screen(screen)
#     window = info.root

#     res = randr.get_screen_resources(window)
#     for output in res.outputs:
#         params = d.xrandr_get_output_info(output, res.config_timestamp)
#         if not params.crtc:
#            continue
#         crtc = d.xrandr_get_crtc_info(params.crtc, res.config_timestamp)
#         modes = set()
#         for mode in params.modes:
#             modes.add(find_mode(mode, res.modes))
#         result.append({
#             'name': params.name,
#             'resolution': "{}x{}".format(crtc.width, crtc.height),
#             'available_resolutions': list(modes)
#         })

#     return result

# print(get_display_info())