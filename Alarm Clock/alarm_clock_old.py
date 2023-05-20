from datetime import datetime   
from playsound import playsound
    
    
def alarm():
    """
    Function to set and trigger an alarm clock based on user input
    
    Parameters:
        None
    
    Returns:
        None: only sound is played
    """

    # take input from user in the defined format
    alarm_time = input("Enter the time of alarm to be set:HH:MM:SS AM/PM\n")
    
    # select features of stated time by user 
    alarm_hour=alarm_time[0:2]
    alarm_minute=alarm_time[3:5]
    alarm_seconds=alarm_time[6:8]
    alarm_period = alarm_time[9:11].upper()
    
    print("Setting up alarm..")
    
    # loop that checks a condition and sounds alarm when its true
    while True:

        # assign current time
        now = datetime.now()

        # select features of current time
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_seconds = now.strftime("%S")
        current_period = now.strftime("%p")

        # compare both user defined features and current time features
        if (alarm_period==current_period) & (alarm_hour==current_hour) & (alarm_minute==current_minute) & (alarm_seconds==current_seconds):
            print("David Wake Up!")
            playsound('alarm.mp3')
            break