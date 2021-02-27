import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize

file_paths=[] # list for saving filepaths information
file_names=[] # list for saving filenames information
times=[]  # list for saving timestamps 
events=[] # list for saving event type

# main function to run my_event_handler
if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

# This function will create dataframe 
# This function will create bar plot
# This function will be called in  below event handler functions
def plotting(File_path,event_type,Time,File_name=None):
    if File_name is None:
        File_name=File_path.split('\\')[-1]
    File_path=File_path
    File_name=File_name
    Time=Time
    event_type=event_type
    file_paths.append(File_path)
    file_names.append(File_name)
    times.append(Time)
    events.append(event_type)
    data={'FILE_PATH':file_paths,'FILE_NAME':file_names,'EVENT_TIME':times,'EVENT_TYPE':events}
    df = pd.DataFrame(data)

    # save the datframe data into csv file
    df.to_csv('.\\Monitored_files.csv')

    # counting files  by grouping the 'EVENT_TYPE' column 
    # and saving into the result dataframe
    result=df.groupby('EVENT_TYPE')['FILE_NAME'].count().reset_index(name='Files_Count')

    # count the no.of times a file is modified  by condition - where 'EVENT_TYPE' is Modified
    df_modified=df[df['EVENT_TYPE'] == 'Modified'].groupby('FILE_NAME')['FILE_NAME'].count().reset_index(name='Count')
    

    """ ploting """

    data = [2, 3, 5, 6, 8, 12, 7, 5]
    my_cmap = cm.get_cmap('jet')
    my_norm = Normalize(vmin=0, vmax=8)
    plt.style.use('seaborn')
    labelparams = {'size': 20, 'weight':'semibold',
              'family':'serif', 'style':'italic'}
    fig=plt.figure(figsize=(10,6))
    plt.bar(result['EVENT_TYPE'], result['Files_Count'], width=0.1, color=my_cmap(my_norm(data)))
    plt.xticks(result['EVENT_TYPE'], rotation='horizontal')
    plt.xlabel("EVENT-TYPE",  labelparams,color='darkblue')
    plt.ylabel('Files-Count', labelparams,color='darkblue')
    plt.title("FILES - OPERATION - STATISTICS", labelparams,color='darkred')
    plt.savefig('img\\01_img.png')


    plt.bar(df_modified['FILE_NAME'], df_modified['Count'], width=0.1, color=my_cmap(my_norm(data)))
    plt.xticks(df_modified['FILE_NAME'], rotation='horizontal')
    plt.xlabel("FILE-NAME",  labelparams,color='darkblue')
    plt.ylabel('FREAQUENCY', labelparams,color='darkblue')
    plt.title("MOST MODIFIED FILES", labelparams,color='darkred')
    plt.savefig('img\\02_img.png')
    return result


 # This is create event
def on_created(event):
    print(f"hey, {event.src_path} has been created!")
    Time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(plotting(event.src_path,'Create',Time))
    
  # This is Delete event
def on_deleted(event):
    print(f" hey buddy , Someone deleted {event.src_path}!")
    Time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(plotting(event.src_path,'Delete',Time))
    
   # This is Modified event
def on_modified(event):
    print(f"hey buddy, {event.src_path} has been modified")
    Time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(plotting(event.src_path,'Modified',Time))

    # This is Moved event
def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
    Time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(plotting(event.dest_path,'Moved',Time))
 
# Asigning the methods to respected event handlers
my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved 

path = "D:\Local_Files_analysis\Files_analysis\img"   # The directory path where all files will be monitored

go_recursively = True
my_observer = Observer()  # initializing observer
my_observer.schedule(my_event_handler, path, recursive=go_recursively)  # scheduling observer
    

my_observer.start() # starting observer

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join() 
              