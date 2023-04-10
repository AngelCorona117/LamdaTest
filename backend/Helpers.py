# SOME LIBRARIES WHERE DUPLICATED HERE FOR READABILITY PURPOUSES, however fell free to delete them.
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

COLOR = ["#788ed6"]

# !!! FUNCTIONS FOR PLOTS.PY !!!


def get_total_logs(title):  # where title is a string
    """Returns a dictionary with the total logs of the server"""

    Logs = requests.get("http://127.0.0.1:8000/totallogs")
    Logs = Logs.json()
    DictOfLogs = {title: Logs}
    return DictOfLogs


def get_dict_of_mime_types():
    """Returns a dictionary with the total logs of the server stacked by mime-type"""

    MimesDict = requests.get("http://127.0.0.1:8000/dictofmimetype").json()

    return MimesDict


# where something is a dictionary(and the keys are the x axis and the values are the y axis)
def get_x_and_y_axis(something, average=1):
    """Returns a tuple with the x and y axis of a plot"""

    X = []
    Y = []
    for key, value in something.items():
        X.append(key)
        Y.append(value/average)
    return X, Y


def create_plot(axis, rotation=0):
    """Creates a plot with the given axis"""

    if len(axis[0]) == 1:

        # make the x axis take just some width of the plot
        x = [1]
        y = axis[1]
        plt.bar(x, y, width=0.5, align='center', color="#788ed6", zorder=2)
        plt.grid(True, color="#000000", axis="y", alpha=0.5, zorder=1)

        # Remove x-axis tick labels and change it to text
        plt.xlim(0, 2)
        plt.xticks([], [])
        plt.text(x=1, y=1, s=axis[0][0], ha='center', va='top')

        # Add y-values to the top of the bars
        for i, v in enumerate(y):
            plt.text(x=1, y=v+0.2,
                     s="{:.2f}".format(round(v, 2)), ha='center', va='bottom')
            return

    # im using this to avoid the overlapping of the xsticks text strings when rotating to 90 degreea
    xlabels_new = [str(label).replace('/', '/\n').replace(".", ".\n")
                   for label in axis[0]]
    positions = range(len(axis[1]))

    # display axis
    plt.bar(positions, axis[1], width=0.4,
            align='center', color=COLOR, zorder=2)
    plt.grid(True, color="#000000", axis="y", alpha=0.5, zorder=1)
    plt.xticks(positions, xlabels_new, rotation=rotation,
               fontsize=13, ha='center')


def create_plot_With_time(axis, COLOR, rotation=0, key=""):
    """Creates a plot with the given axis where x axis is a timestamp and y is the amount of logs"""

    # im using this to avoid the overlapping of the xsticks text strings when rotating to 90 degrees
    xlabels_new = [str(label).replace('T', 'T\n') for label in axis[0]]

    # display axis
    positions = range(len(axis[1]))
    plt.plot(positions, axis[1], color=COLOR, label=key, zorder=3)
    plt.fill_between(positions, axis[1], color=COLOR, alpha=0.2, zorder=2)
    plt.grid(True, color="#000000", axis="y", alpha=0.5, zorder=1)
    plt.xticks(positions, xlabels_new, rotation=rotation,
               fontsize=10, ha='center')


# where every argument is a string
def create_image_plot(title, filename, padding=20, xlabel="", ylabel=""):
    """Creates a plot and saves it as a png file"""

    plt.title(title, fontsize=18, color="#1C1A1A", pad=padding)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(f"static/plots/{filename}.png",
                dpi=150, bbox_inches='tight', pad_inches=0.1)
    fig = plt.gcf()
    plt.close(fig)


def get_x_values_of_every_plot(X_axis):
    """Formats the text of the Xaxis"""

    for i, v in enumerate(X_axis):
        plt.text(i, v, "{:.2f}".format(round(v, 2)),
                 ha='center', va='bottom', fontsize=13)


def add_legend_to_plot():
    """Adds a legend to the plot"""

    Legend = plt.legend(fontsize=8, frameon=True,
                        handlelength=3, handleheight=2, loc="upper center", ncol=5, fancybox=True,
                        bbox_to_anchor=(0.5, 1.15), borderpad=0, facecolor='white')

    Legend.get_frame().set_edgecolor('white')

# !!! FUNCTIONS FOR CREATEAPI.PY !!!


def get_dict_of_somenthing(dict, item):
    """Returns a dictionary of the given elements"""

    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1
    return dict


def get_dict_of_timestamp_counts(dataset):
    """creates a pandas dataframe from the dataset and then converts it to a dictionary"""

    df = pd.DataFrame(dataset)
    df = df.rename(columns={df.columns[0]: 'timestamp'})
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('datetime', inplace=True)

    # group the timestamps into blocks of 10 minutes
    Counts = df.resample('15T').count()
    Counts = Counts.rename(columns={'timestamp': 'count'})

    # convet the dataframe to a dictionary
    Counts = Counts.to_dict()['count']
    return Counts


def get_existance_of_item_in_dict_keys(item, dict, timestamp):
    if not item in dict.keys():
        ListOfTimestamps = [timestamp]
        dict[item] = ListOfTimestamps
    else:
        dict[item].append(timestamp)
    return dict


def get_pandas_datatime_format_from_dict(dict):
    """Returns a pandas dataframe from a given dictionary"""
    SortedByGruopsOfTimestamps = {}
    for key, value in dict.items():

        Counts = get_dict_of_timestamp_counts(value)
        SortedByGruopsOfTimestamps[key] = Counts

    return SortedByGruopsOfTimestamps
