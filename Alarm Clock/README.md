## Alarm Clock

### About Project

The Alarm Clock is a Python program that allows users to set an alarm for a specific time. Once the set time matches the current time, the alarm will sound, alerting the user.

### Problem Statement

The project aims to solve the problem of waking up or being reminded of important events by providing a customizable alarm clock. By taking user input for the desired alarm time, the code continuously checks the current time and triggers an alarm when the set time matches the current time.

### Algorithm

The algorithm used in the Alarm Clock is as follows:

1. Take input from the user for the desired alarm time in the format: `HH:MM:SS AM/PM`.
2. Extract the individual features of the alarm time, including hours, minutes, seconds, and period of the day.
3. Continuously check the current time using a while loop.
4. Extract the features of the current time, including hours, minutes, seconds, and period of the day.
5. Compare the features of the alarm time and the current time.
6. If the features match, sound the alarm.
7. Repeat steps 4-6 until the alarm is triggered.

### Python Skills Learned

During the development of this project, the following Python skills were utilized:

- `Working with datetime objects:` extracting time features and comparing time values.
- `List indexing:` extracting individual features from the alarm time input.
- `Loops:` continuously checking the current time until the alarm is triggered.
- `Conditional statements:` comparing time features to determine if the alarm should be triggered.
- `External libraries:` importing and using external libraries like `datetime` and `playsound`.

### Installation

To run the Alarm Clock program, you need to install the required libraries. Use the following command to install the necessary libraries:

```python
    pip install playsound
```


### Usage

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to start the Alarm Clock:
```python
    python alarm_clock.py
```

4. Enter the desired alarm time in the format: `HH:MM:SS AM/PM`.
5. The program will continuously check the current time.
6. When the set alarm time matches the current time, the program will sound the alarm and display a message.
7. Press `Ctrl+C` to stop the alarm.


