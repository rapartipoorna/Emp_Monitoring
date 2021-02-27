from win32gui import GetForegroundWindow
import psutil
import time
import win32process
import pandas as pd
import matplotlib.pyplot as plt

process_time={}
timestamp = {}
while True:
    try:
        current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
        
    except:
        continue    
    timestamp[current_app] = int(time.time())
    time.sleep(1)
    if current_app not in process_time.keys():
        process_time[current_app] = 0
    process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
    df = pd.DataFrame(list(process_time.items()),columns=['APP-NAME','DURATION']) 
    df.to_csv('Application_track.csv')

    # plotting 
    fontdict={'size': 20, 'weight':'semibold',
        'family':'serif', 'style':'italic','color':'b'}
    fig1=plt.figure(figsize=(10,6))
    plt.pie(df['DURATION'], labels =df['APP-NAME'],autopct=lambda p: '{:.1f}%'.format(round(p)) 
                        if p > 0.5 else '',startangle=180, pctdistance=0.83)  # for pie chart
    plt.legend()
    plt.title("APPLICATIONS USAGE",fontdict)
    plt.savefig('Apps-usage_pie.png')
    plt.close()
    fig2=plt.figure(figsize=(10,6))
    plt.title("APPLICATIONS USAGE",fontdict)
    plt.bar(df['APP-NAME'],df['DURATION'],width=0.25) # for bar chart
    plt.xlabel('APP-NAME',color='b')
    plt.ylabel('DURATION(seconds)',color='b')
    plt.savefig('Apps-usage_bar.png')
    plt.close()
