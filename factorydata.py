import csv 
import random 
import datetime

#Setting up the range of the values for power consumption and temperature 

power_range =(6, 10)
temp_range = (35, 50)
vibration_range = (0.1, 0.7)
pressure_range = (40, 65)
position_range =(0.001, 0.010)
speed_range = (4500, 7500)
tool_wear_range = (0, 0.2)


# Define the start and end time of the machine running
start_time = datetime.time(hour=9, minute=0, second=0)
end_time = datetime.time(hour=14, minute=0, second=0)


#Defining number of data points 
# 5*60 to sample 5 hours of data, sampled every minute 
num_data_points = 5*60

data = [] # List stores the data

#Generating the data 

for i in range(num_data_points):
    # Generate a random value for power consumption and temperature within the specified range
    power = round(random.uniform(*power_range),2)
    temp = round(random.uniform(*temp_range),2)
    vib = round(random.uniform(*vibration_range),2)
    pres = round(random.uniform(*pressure_range),2)
    pos = round(random.uniform(*position_range),2)
    speed = round(random.uniform(*speed_range),2)
    tools = round(random.uniform(*tool_wear_range),2)

    # Generate a random time between the start and end time of the machine running
    time_diff_seconds = (end_time.hour - start_time.hour) * 3600 + (end_time.minute - start_time.minute) * 60
    time_diff_minutes = time_diff_seconds / 60
    time_offset_minutes = i % time_diff_minutes
    timestamp_time = (datetime.datetime.combine(datetime.date.today(), start_time) + datetime.timedelta(minutes=time_offset_minutes)).time()

    # Get the current date and combine it with the generated time to get the timestamp
    timestamp_date = datetime.datetime.now().date()
    timestamp = datetime.datetime.combine(timestamp_date, timestamp_time).isoformat()

    #Add the data to the list
    data.append([timestamp, power, temp, vib, pres, pos, speed, tools])

with open('millingmachinedata1.csv', 'w', newline='') as file4:
    writer = csv.writer(file4)
    writer.writerow(['Timestamp', 'Power Consumption (kW)', 'Temperature', 'Vibration (mm/S RMS)', 'Pressure (bar)', 'Position (mm)', 'Speed (RPM)', 'Tool Wear (mm)'])
    for row in data:
        writer.writerow(row)
