from tabulate import tabulate
import pandas as pd

#Table containing clinician's annotations of patient data.
table_data = {
    'Patient Reference': ['patient001novice', 'patient011novice', 'patient013novice', 'patient014novice',
                          'patient025novice', 'patient007expert', 'patient006expert',
                          'patient005expert',
                          'patient010expert', 'patient013expert', 'patient014expert',
                          'patient000expert', 'Test1expert', 'Test4expert', 'Test6expert', 'Test7expert', 'Test8expert',
                          'patient005novice', 'patient012novice', 'patient002novice'],
    'File Name End': ['2103', '1347', '3745', '2444', '3132', '5750', '2523', '5922', '3651', '4539', '3328',
                      '3942', '1958', '1134', '5242', '0710', '2516', '5055', '0135', '0351'],
    'Operator': ['Novice', 'Novice', 'Novice', 'Novice', 'Novice', 'Expert', 'Expert', 'Expert', 'Expert',
                 'Expert', 'Expert', 'Expert', 'Expert', 'Expert', 'Expert', 'Expert', 'Expert', 'Novice', 'Novice',
                 'Novice'],
    'AC Start': ['6482', '9978', '5585', '4497', '6800','1', '619', '1', '28533', '0', '2718', '10843', '1963',
                 'Failed', 'Failed', '1', '951', 'Failed', '1565', 'Failed'],
    'AC End': ['7430', '10594', '7909', '6287', '7522','1064', '1560', '1810', '29508', '187', '3983', '11590',
               '2496', 'Failed', 'Failed', '1583', '1188', 'Failed', '2475', 'Failed'],
    'BPD Start': ['1632', '13810', 'Failed', '11705', '1550', '5010', '14247', 'Failed', '18600', 'Failed',
                  '709', '4332', '327', '1140', '2085', 'Failed', '1737', '13240', '5417', 'Failed'],
    'BPD End': ['4882', '15128', 'Failed', '14975', '2625', '5572', '15082', 'Failed', '20147', 'Failed',
                '1204', '5430', '796', '1261', '2302', 'Failed', '2050', '16600', '7466', 'Failed'],
    'FL Start': ['8479', '11937', '3850', '8273', '10585', '1500', '8501', 'Failed', '17893', 'Failed', '5204',
                 'Failed', '3140', '3800', '1350', 'Failed', 'Failed', '4095', '13863', '1'],
    'FL End': ['9402', '13505', '4982', '9635', '11350', '1630', '8884', 'Failed', '18508', 'Failed', '5453',
               'Failed', '3268', '3951', '1493', 'Failed', 'Failed', '5383', '14342', '800']
}

print(tabulate(table_data, headers="keys", tablefmt="fancy_grid"))

df = pd.DataFrame(table_data)


def start_end(reference, column_start, column_end):
    """The start_end function takes a patient reference string, a starting column name,
    and an ending column name as input. It searches the df DataFrame for the row corresponding to the given patient reference.
    If the value in the starting column is not "Failed", it returns the integer values of the starting and ending columns for that row.
    If the value in the starting column is "Failed", it returns the string "Failed" for both the starting and ending columns."""
    print("ref:", reference)

    index = df[df["Patient Reference"] == reference].index.values
    print(type(index))
    print("Index:", index)
    start = df.iloc[index][column_start]
    for i in start:

        if i != "Failed":
            print("col start:", column_start)
            print("start:", start)
            end = df.iloc[index][column_end]
            print("col end:", column_end)
            print("end: ", end)
            return int(start), int(end)
        else:
            print("failed caught")
            return "Failed", "Failed"

