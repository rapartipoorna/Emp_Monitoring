import schedule
import time

def job(t):
    print ("I'm working...", t)
    return

schedule.every().day.at("15:05").do(job,'It is 15:05')


while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute