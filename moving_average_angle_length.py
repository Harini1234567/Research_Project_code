import table_data
import get_reference as gr
import ac_bpd_fl as ac
import box_plot_path_len as bx
import _3d_matrix as _3d
import numpy as np
import pandas as pd

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
                    """This main script does the same as the "final_code_angle_length" main script except the 
                    following code calculates the moving average of the rotational path lengths by only using every 
                    third value and summing. Thus, the graphs plot moving average rotational path length. """
                moving_averages = []
                for i in range(len(rot_angles) - (3 - 1)):
                    moving_averages.append(sum(rot_angles[i:i + 3]) / 3)
                if len(rot_angles[i + 3:]) == 3:
                    moving_averages.append(sum(rot_angles[i + 3:]) / 3)
                total_angle = sum(moving_averages)

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
                """This main script does the same as the "final_code_angle_length" main script except the following 
                code calculates the moving average of the rotational path lengths by only using every third value and 
                summing. Thus, the graphs plot moving average rotational path length. """
                moving_averages = []
                for i in range(len(rot_angles) - (3 - 1)):
                    moving_averages.append(sum(rot_angles[i:i + 3]) / 3)
                if len(rot_angles[i + 3:]) == 3:
                    moving_averages.append(sum(rot_angles[i + 3:]) / 3)
                total_angle = sum(moving_averages)

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

bx.boxplot(angle_len_list_nov, angle_len_list_exp)
