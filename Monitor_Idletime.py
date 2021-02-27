import time,schedule
from idle_time import IdleMonitor
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
monitor = IdleMonitor.get_monitor()
cummulative_time=[]
Top_times=[]
now = datetime.now()

# converting seconds into hrs and into miniuts
def convert_to_preferred_format(sec):
   sec = sec % (24 * 3600)
   hour = sec // 3600
   sec %= 3600
   min = sec // 60
   sec %= 60
   print(str(hour)+'hr'+' '+str(min)+'m'+' '+str(sec)+'s')
#    print("seconds value in hours:",hour)
#    print("seconds value in minutes:",min)
#    return "%02d:%02d:%02d" % (hour, min, sec) 
   return sec
# current_time = now.strftime("%H:%M:%S")
# if current_time=='18:34:00':
#     print("working")
# print(current_time)
# print(datetime.strptime('18:47:00','%H:%M:%S').time())
def cumulative():
    print("this is cummulative")
    return sum(Top_times)  

while True:
    
    x=monitor.get_idle_time()
    if int(x)==0:
        try:
            max_time_value=max(cummulative_time)
            Top_times.append(max_time_value)
            cummulative_time.clear()
            later=datetime.now()
            diff=later-now
            Total_1=diff.days*24*60*60+diff.seconds
            Total=convert_to_preferred_format(diff.days*24*60*60+diff.seconds) # Total time from starting of application running.
            idle_time_1=sum(Top_times)
            idle_time=convert_to_preferred_format(sum(Top_times))  # Total Idle time 
            prod=convert_to_preferred_format(Total_1-idle_time_1)  # Total production time

            # creating data dictionary to give input to dataframe
            data = {'TOTAL_TIME(sec)':[Total], 'IDLE_TIME(sec)':[idle_time], 'PRODUCTION_TIME(sec)':[prod]}
            df=pd.DataFrame(data)
            df.to_csv('.\\times.csv') # creating csv file with data

            # plotting 
            fontdict={'size': 20, 'weight':'semibold',
              'family':'serif', 'style':'italic','color':'b'}
            row_data = df.iloc[0] # selecting first row from  dataframe data
            fig1=plt.figure(figsize=(10,6))
            plt.pie(row_data, labels =df.columns.values,autopct=lambda p: '{:.1f}%'.format(round(p)) 
                               if p > 0.5 else '',startangle=180, pctdistance=0.83)  # for pie chart
            plt.legend()
            plt.title("USER TIME CONSUMPTION",fontdict)
            plt.savefig('Timing_pie.png')
            fig=plt.figure(figsize=(10,6))
            plt.title("USER TIME CONSUMPTION",fontdict)
            plt.bar(df.columns.values,row_data,width=0.25) # for bar chart
            plt.xlabel('TIME-CATOGORY',color='b')
            plt.ylabel('TIME(seconds)',color='b')
            plt.savefig('Timing_bar.png')



            
        except:
            continue    
        

    else: 
        cummulative_time.append(x)
        print(x)
        time.sleep(2)   

# def jobs():
#     current_time = now.strftime("%H:%M:%S")
#     print(current_time)
#     if current_time==datetime.strptime('18:57:00','%H:%M:%S').time():
#         print("working")
#         print(sum(Top_times))
#     x=monitor.get_idle_time()
#     if int(x)==0:
#         try:
#             max_time_value=max(cummulative_time)
#             Top_times.append(max_time_value)
#             cummulative_time.clear()
#             # print(sum(Top_times))
#         except:
#             print("")    
        

#     else: 
#         cummulative_time.append(x)
#         print(x)
#         time.sleep(2)    
# schedule.every(1).seconds.do(jobs)
# while True:
#     schedule.run_pending()
#     time.sleep(1)


# while True:
#     x=monitor.get_idle_time()
#     if int(x)==0:
#         try:
#             max_time_value=max(cummulative_time)
#             Top_times.append(max_time_value)
#             cummulative_time.clear()
#             print(sum(Top_times))
#         except:
#             continue    
        

#     else: 
#         cummulative_time.append(x)
#         print(x)
#         time.sleep(2)   



          
    
# from ctypes import Structure, windll, c_uint, sizeof, byref
# import time
# import threading,schedule

# millis=0
# # def printit():
# #   threading.Timer(10.0, printit).start()
# #   print (get_idle_duration())
# timearray=[]
# class LASTINPUTINFO(Structure):
#     _fields_ = [
#         ('cbSize', c_uint),
#         ('dwTime', c_uint),
#     ]

# def get_idle_duration():
#     lastInputInfo = LASTINPUTINFO()
#     lastInputInfo.cbSize = sizeof(lastInputInfo)
#     windll.user32.GetLastInputInfo(byref(lastInputInfo))
#     millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
#     if millis=='0':

#     timearray.append(millis/1000.0)
#     return millis / 1000.0
    
# # schedule.Job.do(Cumulative_Time,'14:29')
# def Cumulative_Time():
#     j=0
#     for i in range(0,len(timearray)):
#         j=timearray[i]+j
#         print(str(j/60)+'Minuits')          

# for i in range(100000):
#     print(get_idle_duration())
#     # Cumulative_Time()
#     time.sleep(1)


