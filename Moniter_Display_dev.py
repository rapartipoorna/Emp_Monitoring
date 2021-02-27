from screeninfo import get_monitors
import pandas as pd
import time
import schedule
monitors={}
def monitors_info():
    for m in get_monitors():
        if 'Monitor-Name' not in monitors:
            monitors['Monitor-Name']=[m.name]
        else:
            monitors['Monitor-Name'].append(m.name)
        if 'Display-Height' not in monitors:
            monitors['Display-Height']=[m.height]
        else:
            monitors['Display-Height'].append(m.height)
        if 'Display-Width' not in monitors:
            monitors['Display-Width']=[m.width]
        else:
            monitors['Display-Width'].append(m.width)  
    df=pd.DataFrame(monitors)
    df.to_csv('monitors-info.csv')
schedule.every(10).seconds.do(monitors_info)    
# schedule.every().hour.do(monitors_info)
while True:
    schedule.run_pending()
    time.sleep(1)
    # time.sleep(10)
    

    