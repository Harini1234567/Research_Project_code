import table_data
import get_reference as gr
import ac_bpd_fl as ac
import box_plot_path_len as bx
import _3d_matrix as _3d
import numpy as np
import pandas as pd

"""This main script uses modules above and functions to read in data from CSV files, calculate the rotational path 
length of the data, and create box plots of the rotational path length for novice and expert groups. 

The script first calls gr.get_reference() to get file names and paths for reference files for novice and expert 
groups. It then calls ac.get_ac_bpd_fl() to get the start and end columns for each of the measurements of interest ( 
ultrasound planes). t gets the ac_bpd_fl dictionary. It loops through the filename dictionary for novice patients and 
calculates the rotation angles for each quaternion from the file using _3d_matrix.quaternion_to_rotation_matrix() and 
_3d_matrix.get_rotation_angle(). The total angle is then appended to angle_len_list_nov. The same process is repeated 
for the expert patients and the total angles are appended to angle_len_list_exp. If there is an 
error during the process, the error message is printed and "Error" is appended to the appropriate list. 

Finally, the script calls bx.boxplot() to create a box plot of the path length for novice and expert groups. The 
script prints out the path length lists before and after cleaning.


 
 
 """
filename_dict_nov, filename_dict_exp = gr.get_reference()
ac_dict = ac.get_ac_bpd_fl()

angle_len_list_nov = []

for key, value in filename_dict_nov.items():
    reference = key
    file_path = value


    for i in ac_dict:
        column_start = i
        column_end = ac_dict[i]


        start, end = table_data.start_end(reference, column_start, column_end)

        if (start != "Failed") or (end != 'Failed'):


            try:
                df = pd.read_csv(file_path)
                quaternion_list = df.loc[start:end, ['qx', 'qy', 'qz', 'qw']].values.tolist()
                rot_matrices = []
                for quat in quaternion_list:
                    rot_matrices.append(_3d.quaternion_to_rotation_matrix(*quat))

                # list to store rotation angles
                rot_angles = []
                for i in range(len(rot_matrices) - 1):
                    rel_rot = np.matmul(rot_matrices[i + 1], np.linalg.inv(rot_matrices[i]))
                    np.linalg.inv(rot_matrices[i])

                    angle = _3d.get_rotation_angle(rel_rot)


                    rot_angles.append(angle)

                # sum of all rotation angles
                print("SEPARATE ANGLES:", rot_angles)
                total_angle = (sum(rot_angles))
                print("Total Angle: ", total_angle)

                angle_len_list_nov.append(total_angle)

                print(column_start, "KEY:", key)




            except IndexError:

                print("index error")
                angle_len_list_nov.append("Error")
                continue
            except Exception as e:
                print(e)
                angle_len_list_nov.append("Error")

                continue


        else:
            print("failed measurement")
            angle_len_list_nov.append("Failed")

print("list NOVICE", angle_len_list_nov)

angle_len_list_exp = []

for key, value in filename_dict_exp.items():
    reference = key
    file_path = value

    for i in ac_dict:
        column_start = i
        column_end = ac_dict[i]

        start, end = table_data.start_end(reference, column_start, column_end)
        print("start", start, "end", end)

        if (start != "Failed") or (end != 'Failed'):

            try:
                df = pd.read_csv(file_path)
                quaternion_list = df.loc[start:end, ['qx', 'qy', 'qz', 'qw']].values.tolist()
                rot_matrices = []
                for quat in quaternion_list:
                    rot_matrices.append(_3d.quaternion_to_rotation_matrix(*quat))

                # list to store rotation angles
                rot_angles = []
                for i in range(len(rot_matrices) - 1):
                    rel_rot = np.matmul(rot_matrices[i + 1], np.linalg.inv(rot_matrices[i]))
                    np.linalg.inv(rot_matrices[i])

                    angle = _3d.get_rotation_angle(rel_rot)

                    rot_angles.append(angle)

                print("SEPARATE ANGLES:", rot_angles)
                total_angle = (sum(rot_angles))
                print("Total Angle: ", total_angle)

                angle_len_list_exp.append(total_angle)

                print(column_start, "KEY:", key)


            except IndexError:

                print("index error")
                angle_len_list_exp.append("Error")
                continue
            except Exception as e:
                print(e)
                angle_len_list_exp.append("Error")

                continue

        else:
            print("failed measurement")
            angle_len_list_exp.append("Failed")
print("list NOVICE", angle_len_list_nov)
print("list EXPERT", angle_len_list_exp)

print("ANGLE LENGTH NOVICE BEFORE CLEANING:", angle_len_list_nov)
print("ANGLE LENGTH EXPERT BEFORE CLEANING:", angle_len_list_exp)

bx.boxplot(angle_len_list_nov, angle_len_list_exp)
