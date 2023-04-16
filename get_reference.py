# one variable which is filename as a list
def get_reference():
    """This function returns two dictionaries: reference_path_dict_novice and reference_path_dict_expert. These
    dictionaries contain paths to various CSV files that are used for analysis.When using this code the file paths
    for both should be changed according to where the files are stored in your directory. """

    reference_path_dict_novice = {
        'patient001novice': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/BrianData/Clinical Data for Comparison/Patient1Novice/Patient001-Novice-20200117112103.csv",
        'patient011novice': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/Missing_files/Patient011-c2-Novice-20200207111347.csv",
        'patient013novice': '/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/Missing_files/Patient013-TC-Novice-20200210153745.csv',
        'patient014novice': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/Missing_files/Patient014-ET-Novice-20200211112444.csv",
        'patient025novice': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/Missing_files/Patient025-Operator000-Novice-20200317-153132.csv",
        'patient005novice': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/BrianData 3/Clinical Data for Comparison/Patient5Novice/Patient005Operator1-Novice-20200120115055.csv",
        'patient002novice': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/BrianData 3/Clinical Data for Comparison/Patient2Novice/Patient002 Operator1-Novice-20200117120351.csv",
        'patient012novice': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/Patient012-de-Novice-20200207120135.csv"
    }

    reference_path_dict_expert = {
        'patient007expert': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/BrianData/Clinical Data for Comparison/Patient7Expert/Patient007Operator1-Expert-20200121115750.csv",
        'patient006expert': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/BrianData/Clinical Data for Comparison/Patient6Expert/Patient006Operator1-Expert-20200121112523.csv",
        'patient005expert': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/BrianData/Clinical Data for Comparison/Patient5Expert/Patient005Operator2-Expert-20200120115922.csv",
        'patient010expert': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/Missing_files/patient010-cd-Expert-20200206153651.csv",
        'patient013expert': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/Missing_files/Patient013-cd-Expert-20200210154539.csv",
        'patient014expert': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/Missing_files/Patient014-MD-Expert-20200211113328.csv",

        'Test1expert': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/testUSTrackingData (2)/original data/Test1-20191217111958.csv",
        'Test4expert': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/testUSTrackingData (2)/original data/Test4-20191217121134.csv",
        'Test6expert': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/testUSTrackingData (2)/original data/Test6-20191217145242.csv",
        'Test7expert': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/testUSTrackingData (2)/original data/Test7-20191217150710.csv",
        'Test8expert': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/testUSTrackingData (2)/original data/Test8-20191217162516.csv",
        'patient000expert': "/Users/slurpp/Library/Containers/com.microsoft.Excel/Data/Downloads/Missing_files/Patient000-Operator020-Expert-20200311-153942.csv", }

    return reference_path_dict_novice, reference_path_dict_expert
