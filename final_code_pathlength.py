import table_data
import csv_reader_column as rd
import plot_function as plot
import path_length as path
import get_reference as gr
import ac_bpd_fl as ac
import box_plot_path_len as bx

"""This main script uses modules above and functions to read in data from CSV files, calculate the translational path length of the 
data, and create box plots of the translational path length for novice and expert groups. The "plot_function" is not 
used in the main script but can be used to visualise the 3d trajectory of operators. 

The script first calls gr.get_reference() to get file names and paths for reference files for novice and expert 
groups. It then calls ac.get_ac_bpd_fl() to get the start and end columns for each of the measurements of interest (
ultrasound planes). 

The script then loops through the files and columns, reading in data from the CSV files using rd.csv_reader() and 
calculating the path length using path.diff_consecutive_nums(). It adds the path length to a list, path_len_list_nov 
for novice files and path_len_list_exp for expert files. If there is an error with the file, the script catches the 
exception and adds the string "Error" to the path length list instead. To use this code to calculate the moving 
average translational path length use path.moving_average function instead. 

Finally, the script calls bx.boxplot() to create a box plot of the path length for novice and expert groups. The 
script prints out the path length lists before and after cleaning. """
filename_dict_nov, filename_dict_exp = gr.get_reference()
ac_dict = ac.get_ac_bpd_fl()

path_len_list_nov = []

for key, value in filename_dict_nov.items():
    reference = key
    file_path = value

    for i in ac_dict:
        column_start = i
        column_end = ac_dict[i]

        start, end = table_data.start_end(reference, column_start, column_end)

        if (start != "Failed") or (end != 'Failed'):

            try:
                x, y, z = rd.csv_reader(file_path, start, end)
                # plot.create_3d_scatter(x, y, z)
                path_length = path.diff_consecutive_nums(x, y, z)

                path_len_list_nov.append(path_length)

                print(column_start, "KEY:", key)



            except IndexError:

                print("index error")

                path_len_list_nov.append("Error")

                continue
            except Exception as e:
                print(e)

                path_len_list_nov.append("Error")

                continue


        else:
            print("failed measurement")

            path_len_list_nov.append("Failed")

print("list NOVICE", path_len_list_nov)

path_len_list_exp = []
for key, value in filename_dict_exp.items():
    reference = key
    file_path = value

    for i in ac_dict:
        column_start = i
        column_end = ac_dict[i]

        start, end = table_data.start_end(reference, column_start, column_end)

        if (start != "Failed") or (end != 'Failed'):

            try:
                x, y, z = rd.csv_reader(file_path, start, end)
                # plot.create_3d_scatter(x, y, z)
                path_length = path.diff_consecutive_nums(x, y, z)

                path_len_list_exp.append(path_length)

                print(column_start, "KEY:", key)



            except IndexError:

                print("index error")

                path_len_list_exp.append("Error")

                continue
            except Exception as e:
                print(e)

                path_len_list_exp.append("Error")

                continue


        else:
            print("failed measurement")

            path_len_list_exp.append("Failed")

print("PATH LENGTH NOVICE BEFORE CLEANING:", path_len_list_nov)
print("PATH LENGTH EXPERT BEFORE CLEANING:", path_len_list_exp)

bx.boxplot(path_len_list_nov, path_len_list_exp)
