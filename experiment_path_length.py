import csv
import math
import matplotlib.pyplot as plt

"""This main code  is calculating the total path length of two sensors, i.e., sensor1 and sensor2, for a set of files 
specified in the variable filenames. The process_csv_file function reads the data from the files and extracts the 
sensor data. It then calculates the total path length for each sensor and returns the total path lengths for sensor1 
and sensor2. The process_all_files function processes all files in the input list using the process_csv_file 
function, and returns the total path lengths for each of two sensors for each file in the form of two lists.The 
euclidean_distance function calculates the Euclidean distance between two points in three-dimensional space, 
and the calculate_total_path_length function calculates the total path length from a sequence of points.. The code 
is also plotting a graph that compares the "translational path lengths" of the two sensors for each file.  """

def euclidean_distance(x1, y1, z1, x2, y2, z2):
    """Calculates the Euclidean distance between two points in three-dimensional space."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def calculate_total_path_length(sensor_data):
    """Calculates and returns total path length from an input sequence of points."""
    total_path_length = 0
    for i in range(1, len(sensor_data)):
        x1, y1, z1 = sensor_data[i - 1]
        x2, y2, z2 = sensor_data[i]
        total_path_length += euclidean_distance(x1, y1, z1, x2, y2, z2)
    return total_path_length


def process_csv_file(filename):
    """
            This function takes in a filename and reads the data from the file.
            It extracts the sensor data from the file and calculates the total path length for each sensor.
            It returns the total path lengths for sensor 1 and sensor 2.
            """
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)  # skip the header row
        sensor1_data = []
        sensor2_data = []
        for row in reader:
            state1 = row[4]
            state2 = row[17]
            if state1 == "OK":
                x1, y1, z1 = map(float, row[9:12])
                sensor1_data.append((x1, y1, z1))
            if state2 == "OK":
                x2, y2, z2 = map(float, row[22:25])
                sensor2_data.append((x2, y2, z2))
        sensor1_total_path_length = calculate_total_path_length(sensor1_data)
        sensor2_total_path_length = calculate_total_path_length(sensor2_data)
        return sensor1_total_path_length, sensor2_total_path_length


def process_all_files(filenames):
    """
        Processes all files in the input list using the `process_csv_file` function, and returns the total path
        lengths for each of two sensors for each file in the form of two lists."""

    sensor1_path_lengths = []
    sensor2_path_lengths = []
    for filename in filenames:
        sensor1_total_path_length, sensor2_total_path_length = process_csv_file(filename)
        sensor1_path_lengths.append(sensor1_total_path_length)
        sensor2_path_lengths.append(sensor2_total_path_length)
    return sensor1_path_lengths, sensor2_path_lengths


filenames = [
    '/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/USTracking 2/experiment1-sweep-fan.csv',
    '/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/USTracking 2/experiment2-sweep.csv',
    '/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/USTracking 2/experiment3-sweep.csv',
    '/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/USTracking 2/experiment4-fan.csv',
    '/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/USTracking 2/experiment5-fan.csv',
    '/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/USTracking 2/experiment6-rotate.csv',
    '/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/USTracking 2/experiment7-rotate.csv',
    '/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/USTracking 2/experiment8-swipe-fan.csv',
    '/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/USTracking 2/experiment9-swipe-rotate.csv',
    '/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/USTracking 2/experiment10-swipe-rotate.csv',
    '/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/USTracking 2/experiment11-all.csv',
    '/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/USTracking 2/experiment12-all.csv']
filename_edit = ['experiment1-sweep-fan',
                 'experiment2-sweep',
                 'experiment3-sweep',
                 'experiment4-fan',
                 'experiment5-fan',
                 'experiment6-rotate',
                 'experiment7-rotate',
                 'experiment8-swipe-fan',
                 'experiment9-swipe-rotate',
                 'experiment10-swipe-rotate',
                 'experiment11-all',
                 'experiment12-all']

#his code is plotting a graph that compares the "translational path lengths" of two sensors, sensor1 and sensor2, for a set of files specified in the variable filenames.
sensor1_path_lengths, sensor2_path_lengths = process_all_files(filenames)
fig, ax = plt.subplots()
colors = ['red', 'blue', 'green', 'teal', 'orange', 'black', 'purple', 'pink', 'brown', 'navy', 'grey', 'cyan']
lines = []
for i in range(len(filenames)):
    ax.scatter(1, sensor1_path_lengths[i], color=colors[i], label=f'Sensor 1 - {filename_edit[i]}', linestyle="dashed")
    ax.scatter(2, sensor2_path_lengths[i], color=colors[i], label=f'Sensor 2 - {filename_edit[i]}', linestyle="dashed")
    line, = ax.plot([1, 2], [sensor1_path_lengths[i], sensor2_path_lengths[i]], color=colors[i], linestyle="dashed")
    lines.append(line)

# create a separate legend figure and axis
fig_legend, ax_legend = plt.subplots()
ax_legend.legend(lines, [f"{filename_edit[i]}" for i in range(len(filenames))], loc='center')


ax.set_xlim(0, 3)
ax.set_xticks([1, 2])
ax.set_xticklabels(['Sensor 1', 'Sensor 2'])
ax.set_ylabel(' Translational Path Length (mm)')
ax.legend(loc='center right', bbox_to_anchor=(-0.15, 0.5))


plt.show()
fig_legend.show()





