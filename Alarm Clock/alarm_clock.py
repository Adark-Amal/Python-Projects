from datetime import datetime
from playsound import playsound


# NB: This code is the revised version of the alarm_clock_old.py script. This is more concise and efficient
 
def alarm_clock():
    """
    Function to set and trigger an alarm clock based on user input
    
    Parameters:
        None
    
    Returns:
        None: only sound is played
    """
    
    # Prompt the user to enter the desired alarm time
    alarm_time = input("Enter the time of the alarm to be set (HH:MM:SS AM/PM): ")

    # Convert the alarm time to a datetime object
    alarm_datetime = datetime.strptime(alarm_time, "%I:%M:%S %p")

    print("Alarm is set for:", alarm_datetime.strftime("%I:%M:%S %p"))

    # Run an infinite loop to continuously check the current time
    while True:
        # Get the current time
        current_time = datetime.now().strftime("%I:%M:%S %p")

        # Check if the current time matches the alarm time
        if current_time == alarm_time:
            print("Alarm triggered!")
            playsound('alarm.mp3')  # Play the alarm sound
            break


# Run the alarm clock function
alarm_clock()
