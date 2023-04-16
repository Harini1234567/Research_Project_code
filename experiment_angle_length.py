import csv
import matplotlib.pyplot as plt
import numpy as np
"""This code defines several functions to process sensor data from CSV files. The main function process_all_files 
takes a list of filenames as input, reads the CSV data from each file, extracts the sensor data, and calculates the 
total rotational path length for each sensor based on the quaternions. The total rotational path lengths for each sensor are then 
returned as two separate lists. The other functions in the code are called within process_all_files and perform 
specific tasks such as converting quaternions to rotation matrices and calculating the rotation angle between two 
matrices. The code is also plotting a graph that compares the "rotational path lengths" of the two sensors for each file."""

def quat_to_rotation_matrix(o1,x1, y1, z1):
    """
        This function takes in four arguments: o1, x1, y1, and z1.
        It returns a 3x3 rotation matrix based on the input quaternion values.
        """
    rot_matrix1 = np.zeros((3,3))

    rot_matrix1[0,0] = 1 - 2*y1*y1 - 2*z1*z1
    rot_matrix1[0,1] = 2*x1*y1 - 2*o1*z1
    rot_matrix1[0,2] = 2*x1*z1 + 2*o1*y1
    rot_matrix1[1,0] = 2*x1*y1 + 2*o1*z1
    rot_matrix1[1,1] = 1 - 2*x1*x1 - 2*z1*z1
    rot_matrix1[1,2] = 2*y1*z1 - 2*o1*x1
    rot_matrix1[2,0] = 2*x1*z1 - 2*o1*y1
    rot_matrix1[2,1] = 2*y1*z1 + 2*o1*x1
    rot_matrix1[2,2] = 1 - 2*x1*x1 - 2*y1*y1
    #caps the values in the matrix between -1 to 1
    np.clip(rot_matrix1, -1, 1, out=rot_matrix1)
    return rot_matrix1



def get_rot_angle(rot_matrix):
    """
        This function takes in a 3x3 rotation matrix and calculates the rotation angle.
        It returns the rotation angle in radians.
        """

    trace = rot_matrix[0, 0] + rot_matrix[1, 1] + rot_matrix[2, 2]
    theta =np.arccos(np.clip((trace - 1)/ 2,-1,1))
    return theta


def calculate_total_angle_length(sensor_data):
    """
        This function takes in a list of quaternions (sensor_data).
        It calculates the total angle length by creating a list of rotation matrices based on the quaternions,
        calculating the angle between each matrix, and summing all the angles.
        It returns the total angle length in radians.
        """
    rot_matrices = []
    for quat in sensor_data:
        rot_matrices.append(quat_to_rotation_matrix(*quat))


    rot_angles = []
    for i in range(len(rot_matrices) - 1):
        rel_rot = np.matmul(rot_matrices[i + 1], np.linalg.inv(rot_matrices[i]))
        np.linalg.inv(rot_matrices[i])

        angle = get_rot_angle(rel_rot)
        rot_angles.append(angle)

    # sum of all rotation angles
    total_angle = (sum(rot_angles))
    return total_angle








def process_csv_file(filename):
    """
        This function takes in a filename and reads the data from the file.
        It extracts the sensor data from the file and calculates the total angle length for each sensor.
        It returns the total angle lengths for sensor 1 and sensor 2.
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
                o1,x1, y1, z1 = map(float, row[5:9])
                sensor1_data.append((o1,x1, y1, z1))
            if state2 == "OK":
                o1,x2, y2, z2 = map(float, row[18:22])
                sensor2_data.append((o1,x2, y2, z2))
        sensor1_total_angle_length = calculate_total_angle_length(sensor1_data)
        sensor2_total_angle_length = calculate_total_angle_length(sensor2_data)
        return sensor1_total_angle_length, sensor2_total_angle_length

def process_all_files(filenames):
    """
            Processes all files in the input list using the `process_csv_file` function, and returns the total angle
            lengths for each of two sensors for each file in the form of two lists."""
    sensor1_angle_lengths = []
    sensor2_angle_lengths = []
    for filename in filenames:
        sensor1_total_angle_length, sensor2_total_angle_length = process_csv_file(filename)
        sensor1_angle_lengths.append(sensor1_total_angle_length)
        sensor2_angle_lengths.append(sensor2_total_angle_length)
    return sensor1_angle_lengths, sensor2_angle_lengths


filenames = ['/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/USTracking 2/experiment1-sweep-fan.csv',
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


#his code is plotting a graph that compares the "rotational path lengths" of two sensors, sensor1 and sensor2, for a set of files specified in the variable filenames.
sensor1_angle_lengths, sensor2_angle_lengths = process_all_files(filenames)
diff = [abs(b - a) for a, b in zip(sensor1_angle_lengths, sensor2_angle_lengths)]
print(diff)
print(sum(diff))



fig, ax = plt.subplots()
colors = ['red', 'blue', 'green', 'teal', 'orange', 'black', 'purple', 'pink', 'brown', 'navy', 'grey', 'cyan']
lines = []
for i in range(len(filenames)):
    ax.scatter(1, sensor1_angle_lengths[i], color=colors[i], label=f'Sensor 1 - {filename_edit[i]}', linestyle="dashed")
    ax.scatter(2, sensor2_angle_lengths[i], color=colors[i], label=f'Sensor 2 - {filename_edit[i]}', linestyle="dashed")
    line, = ax.plot([1, 2], [sensor1_angle_lengths[i], sensor2_angle_lengths[i]], color=colors[i], linestyle="dashed")
    lines.append(line)

# create a separate legend figure and axis
fig_legend, ax_legend = plt.subplots()
ax_legend.legend(lines, [f"{filename_edit[i]}" for i in range(len(filenames))], loc='center')


ax.set_xlim(0, 3)
ax.set_xticks([1, 2])
ax.set_xticklabels(['Sensor 1', 'Sensor 2'])
ax.set_ylabel('Rotational Path Length (rad)')
ax.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1, fontsize='small')
plt.show()
fig_legend.show()



