import matplotlib.pyplot as plt


def boxplot(path_len_list_nov, path_len_list_exp):
    """This function creates a boxplot for three different planes (AC, BPD, and FL) from two sets of data ( novice
    and expert). It cleans the data by removing any items that have the value "Failed", "Error", or 0.0. It then
    creates nested lists for each measure, with the novice and expert data separated. Depending on the motion metric
    re-label "y_label" accordingly.It creates a subplot with three box-plots, one for each measure,
    with the novice and expert data side-by-side. """

    AC_list_nov, AC_list_exp = path_len_list_nov[::3], path_len_list_exp[::3]
    BPD_list_nov, BPD_list_exp = path_len_list_nov[1::3], path_len_list_exp[1::3]
    FL_list_nov, FL_list_exp = path_len_list_nov[2::3], path_len_list_exp[2::3]

    # remove "Failed" and "Error" from the lists
    clean_AC_nov = [i for i in AC_list_nov if i != "Failed" and i != "Error" and i != 0.0]
    clean_BPD_nov = [i for i in BPD_list_nov if i != "Failed" and i != "Error" and i != 0.0]
    clean_FL_nov = [i for i in FL_list_nov if i != "Failed" and i != "Error" and i != 0.0]

    clean_AC_exp = [i for i in AC_list_exp if i != "Failed" and i != "Error" and i != 0.0]
    clean_BPD_exp = [i for i in BPD_list_exp if i != "Failed" and i != "Error" and i != 0.0]
    clean_FL_exp = [i for i in FL_list_exp if i != "Failed" and i != "Error" and i != 0.0]

    # print cleaned lists
    print("PATH LENGTH AC NOV CLEANED:", clean_AC_nov)
    print("PATH LENGTH BPD NOV CLEANED:", clean_BPD_nov)
    print("PATH LENGTH FL NOV CLEANED:", clean_FL_nov)

    print("PATH LENGTH AC EXPERT CLEANED:", clean_AC_exp)
    print("PATH LENGTH BPD EXPERT CLEANED:", clean_BPD_exp)
    print("PATH LENGTH FL EXPERT CLEANED:", clean_FL_exp)


    nested_list_ac = [clean_AC_nov, clean_AC_exp]
    nested_list_bpd = [clean_BPD_nov, clean_BPD_exp]
    nested_list_fl = [clean_FL_nov, clean_FL_exp]

    # create subplots
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

    # set labels
    x_labels = ['Novice', 'Expert']
    y_label = 'Translational Path Length (rad)'

    # create boxplots
    bp_ac = axs[0].boxplot(nested_list_ac, positions=range(len(nested_list_ac)), labels=x_labels)
    bp_bpd = axs[1].boxplot(nested_list_bpd, positions=range(len(nested_list_bpd)), labels=x_labels)
    bp_fl = axs[2].boxplot(nested_list_fl, positions=range(len(nested_list_fl)), labels=x_labels)

    # set axis labels
    axs[0].set_ylabel(y_label)
    axs[1].set_ylabel(y_label)
    axs[2].set_ylabel(y_label)

    axs[0].set_xlabel("Operator")
    axs[1].set_xlabel("Operator")
    axs[2].set_xlabel("Operator")

    # set titles
    axs[0].set_title('AC')
    axs[1].set_title('BPD')
    axs[2].set_title('FL')

    plt.subplots_adjust(wspace=0.5)
    plt.show()
