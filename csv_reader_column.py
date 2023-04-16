import pandas as pd


def csv_reader(filename, start, end):
    """This function reads a CSV file and extracts specific rows and columns of data based on the given start and end
    indices. The function takes three arguments: filename (string) which is the name of the CSV file, start (integer)
    which is the index of the starting row, and end (integer) which is the index of the ending row. The function
    returns three columns of data, each column is either x,y or z coordinates.  """
    print(start, end)
    csv_file = pd.read_csv(filename, header=0, delimiter=",")
    print(start, end)


    row_data = csv_file.iloc[start:end - 1].values
    column_data_x = csv_file.loc[start:end, "x (mm)"]

    column_data_y = csv_file.loc[start:end, "y (mm)"]
    column_data_z = csv_file.loc[start:end, "z (mm)"]
    print(column_data_x, column_data_y, column_data_z)
    return column_data_x, column_data_y, column_data_z


def csv_reader_quat(filename, start, end):
    """This function reads a CSV file and extracts specific rows and columns of data based on the given start and end
    indices. The function takes three arguments: filename (string) which is the name of the CSV file, start (integer)
    which is the index of the starting row, and end (integer) which is the index of the ending row.The function
    returns four columns of data, each column is either qx,qy,qz or qw quaternion coordinates. """
    print(start, end)
    csv_file = pd.read_csv(filename, header=0, delimiter=",")
    print(start, end)


    row_data = csv_file.iloc[start:end - 1].values
    column_data_qx = csv_file.loc[start:end, 'qx']

    column_data_qy = csv_file.loc[start:end, 'qy']
    column_data_qz = csv_file.loc[start:end, 'qz']
    column_data_qw = csv_file.loc[start:end, 'qw']

    return column_data_qx, column_data_qy, column_data_qz, column_data_qw

