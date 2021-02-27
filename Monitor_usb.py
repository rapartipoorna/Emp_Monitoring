import win32com.client
import os 
import win32file
import wmi
import datetime
import pandas as pd
import matplotlib.pyplot as plt
# def get_devices():  # searching logical_disk and return SerialNumber, Name of Logical Disk
#     wmi = win32com.client.GetObject("winmgmts:")
#     return {item.VolumeSerialNumber: (item.Name, item.VolumeName) for item in wmi.InstancesOf("Win32_LogicalDisk")}
# while 1:

#     print(get_devices())

USB_INFO={}
raw_wql = "SELECT * FROM __InstanceCreationEvent WITHIN 2 WHERE TargetInstance ISA \'Win32_USBHub\'"
c = wmi.WMI ()
watcher = c.watch_for(raw_wql=raw_wql)
while 1:
  usb = watcher()
  t=datetime.datetime.now()
  print(datetime.datetime.now())
  if 'DETECTION-TIME' not in USB_INFO:
      USB_INFO['DETECTION-TIME'] = [str(t)]
  else:
      USB_INFO['DETECTION-TIME'].append(str(t))
  if 'USB-ID'  not in USB_INFO:
      USB_INFO['USB-ID'] = [usb.DeviceID]
  else:
      USB_INFO['USB-ID'].append(usb.DeviceID) 
  if 'MACHINE-NAME' not in USB_INFO:
      USB_INFO['MACHINE-NAME'] = [usb.SystemName]
  else:
      USB_INFO['MACHINE-NAME'].append(usb.SystemName)

  df=pd.DataFrame(USB_INFO)
  df.to_csv('usb-detection.csv')
  
#   print(df)                
#   USB_INFO['DETECTION-TIME'].append(str(t))
#   USB_INFO['USB-ID']=usb.DeviceID
#   USB_INFO['MACHINE-NAME']=usb.SystemName
  



# def locate_usb():
#     drive_list = []
#     drivebits = win32file.GetLogicalDrives()
#     for d in range(1, 26):
#         mask = 1 << d
#         if drivebits & mask:
#             # here if the drive is at least there
#             drname = '%c:\\' % chr(ord('A') + d)
#             t = win32file.GetDriveType(drname)
#             if t == win32file.DRIVE_REMOVABLE:
#                 drive_list.append(drname)
#     return drive_list

# print(locate_usb())

# def get_usb_volume_name():  # pragma: no cover
#     str_computer = "."
#     logical_disk_device_ids = []
#     volumes = []
#     try:
#         obj_wmi_service = win32com.client.Dispatch("WbemScripting.SWbemLocator")
#         obj_swbem_services = obj_wmi_service.ConnectServer(str_computer, "root\cimv2")

#     # 1. Win32_DiskDrive
#         col_items = obj_swbem_services.ExecQuery("SELECT * FROM Win32_DiskDrive WHERE InterfaceType = \"USB\"")
#         for item in col_items:
#             disk_drive_device_ids = item.DeviceID.replace('\\', '').replace('.', '')

#     # 2. Win32_DiskDriveToDiskPartition
#         col_items = obj_swbem_services.ExecQuery("SELECT * from Win32_DiskDriveToDiskPartition")
#         disk_partition_device_ids = []
#         for obj_item in col_items:
#             for disk_drive_device_id in disk_drive_device_ids:
#                 if disk_drive_device_id in str(obj_item.Antecedent):
#                     disk_partition_device_ids.append(obj_item.Dependent.split('=')[1].replace('"', ''))
#                     break

#     # 3. Win32_LogicalDiskToPartition
#         col_items = obj_swbem_services.ExecQuery("SELECT * from Win32_LogicalDiskToPartition")
#         for objItem in col_items:
#             for disk_partition_device_id in disk_partition_device_ids:

#                 if disk_partition_device_id in str(objItem.Antecedent):
#                     logical_disk_device_ids.append(objItem.Dependent.split('=')[1].replace('"', ''))
#                     break

#     # 4. Win32_LogicalDisk
#         col_items = []
#         for logical_disk_device_id in logical_disk_device_ids:
#             col_items.append(obj_swbem_services.ExecQuery("SELECT * from Win32_LogicalDisk WHERE DeviceID=\"" +
#                                                       logical_disk_device_id + "\""))

#         for col_item in col_items:
#             volumes.append(col_item[0].VolumeName)
#     except IndexError:
#         pass
#     volumes_result = []
#     logical_disk_device_ids_result = []
#     for i in range(len(volumes)):
#         if volumes[i] != "":
#             volumes_result.append(volumes[i])
#             logical_disk_device_ids_result.append(logical_disk_device_ids[i])

#     return logical_disk_device_ids_result, volumes_result

# # def get_usb_device():
# #     try:
# #         usb_list = []
    
# #         wmi = win32com.client.GetObject("winmgmts:")
# #         for usb in wmi.InstancesOf("Win32_USBHub"):
# #             print(usb.DeviceID)
# #             print(usb.description)
# #             # print(usb_list)
# #             usb_list.append(usb.description)

# #         print(usb_list)
# #         return usb_list
# #     except Exception as error:
# #         print('error', error)


# # get_usb_device()
# print(get_usb_volume_name())