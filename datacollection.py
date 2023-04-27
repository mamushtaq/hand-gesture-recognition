# This file contains code to collect the raw EMG data (converted to voltage) by reading the values being printed on serial monitor by arduino.
import serial  # Serial library is used to read values being printed on serial monitor by arduino
import pandas as pd  # Pandas library to sort the collected data into a dataframe

# An empty csv file. You can also directly create a new dataframe
df = pd.read_csv('My_data.csv')

# same baudrate as set in arduino with specifying arduino port.
ser = serial.Serial('COM5', 9600, timeout=.1)
if not ser.isOpen():
    ser.open()
for n in range(0, 30):
    array = []
    for x in range(300):
        s = ser.read(4)
        if x > 8:
            array.append(s.decode())
            print(array)
    df[n] = array
    array = []
df.transpose()
# Features are extracted from this raw data in matlab.
df.to_csv('filename.csv')
print(array)
ser.close()
