import requests
import pandas as pd
import matplotlib.pyplot as plt
from Helpers import get_total_logs, get_dict_of_mime_types, get_x_and_y_axis, create_plot, create_image_plot, get_x_values_of_every_plot, create_plot_With_time, add_legend_to_plot

USERLENGHT = requests.get("http://127.0.0.1:8000/length").json()
COLOR = ["#788ed6"]
PALLETTE = ["#CF458D", "red", "#000000", "#87CEEB",
            "#374187", "#2B2D42", "#FDE6B0", "#78B58D", "#788ed6", "red"]

# remove top and right borders
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False

# format the figure of plot
plt.rcParams['figure.figsize'] = [12, 3]

# REMEMBER TO ACTIVATE THE API BEFORE RUNNING THIS FILE
# (wait for the server say "Application startup complete")

def step_1():       # Step 1: Total Count of Logs
    """Creates an image plot with the total count of logs"""

    DictOfLogs = get_total_logs("logs")
    Axis = get_x_and_y_axis(DictOfLogs)
    create_plot(Axis)
    create_image_plot('Total count of logs',
                      '2.1.Step1Plot(total)')


def step_1_over_time():         # Step 1: Total Count of Logs
    """Creates an image plot with the total count of logs over time"""

    DictOfLogsOverTime = requests.get(
        "http://127.0.0.1:8000/totallogsovertime").json()
    Axis = get_x_and_y_axis(DictOfLogsOverTime)
    create_plot_With_time(Axis, "#788ed6", 90)
    create_image_plot('Total count of logs over time',
                      '2.21.Step1OverTimePlot(total)')


def step_2():       # Step 2: Logs count stacked by log type( mime-type)
    """Creates an image plot with the total count of logs stacked by mime-type"""

    MimesDict = get_dict_of_mime_types()
    Axis = get_x_and_y_axis(MimesDict)
    create_plot(Axis, 90)
    get_x_values_of_every_plot(Axis[1])
    create_image_plot('Logs count stacked by log type',
                      '1.0Step2Plot(total)')


def step_2_over_time():
    """Creates an image plot with the total count of logs stacked by mime-type over time"""
    i = 0
    FinalAxis=[]
    DictOfMimeTypeOverTime = requests.get(
        "http://127.0.0.1:8000/mimetypeovertime").json()
    for key, value in DictOfMimeTypeOverTime.items():

        # for every dict create a subplot
        Axis = get_x_and_y_axis(value)
        color = PALLETTE[i]
        create_plot_With_time(Axis, color, 90, key)
        if i==0:
            FinalAxis = Axis      
        i += 1
    add_legend_to_plot()
    create_plot_With_time(FinalAxis, color, 90, key)
    create_image_plot('Logs count stacked by log type over time',
                      '1.2Step2OverTimePlot(total)',30)


def step_2_averange_log():      # Step 2: Averange Logs per user stacked by log type( mime-type)
    """Creates an image plot with the averange count of logs per user stacked by mime-type"""

    MimesDict = get_dict_of_mime_types()
    Axis = get_x_and_y_axis(MimesDict, USERLENGHT)
    create_plot(Axis, 90)
    get_x_values_of_every_plot(Axis[1])
    create_image_plot('Averange logs per user stacked by log type',
                      '1.1Step2AverangeLogPlot(averange)')


def step_2_averange_log_over_time():
    """Creates an image plot with the total count of logs stacked by mime-type over time"""
    i = 0
    FinalAxis=[]
    DictOfMimeTypeOverTime = requests.get(
        "http://127.0.0.1:8000/mimetypeovertime").json()
    for key, value in DictOfMimeTypeOverTime.items():

        # for every dict create a subplot
        Axis = get_x_and_y_axis(value, USERLENGHT)
        color = PALLETTE[i]
        create_plot_With_time(Axis, color, 90, key)
        if i==0:
            FinalAxis = Axis  
        i += 1

    add_legend_to_plot()
    create_plot_With_time(FinalAxis, color, 90, key)
    create_image_plot('Averange Logs count stacked by log type over time',
                      '1.3Step2OverTimePlot(averange)',30)


def step_3():       # Step3: Logs count stacked by log level (Status Codes)
    """Creates an image plot with the total count of logs stacked by log level"""

    DictOfLevels = get_total_logs("INFO")
    Axis = get_x_and_y_axis(DictOfLevels)
    create_plot(Axis)
    create_image_plot('Count of logs stacked by log level',
                      '3.0Step3Plot(total)')


def step_3_averange_level():         # Step3: Averange Logs per user stacked by log level (Status Codes)
    """Creates an image plot with the averange count of logs per user stacked by log level"""

    DictOfLevels = get_total_logs("INFO")
    Axis = get_x_and_y_axis(DictOfLevels, USERLENGHT)
    create_plot(Axis)
    create_image_plot('Averange logs per user stacked by log level',
                      '3.1Step3AverangeLevelPlot(averange)')


def step_3_status_codes():      # Step 3: get all status codes
    """Creates an image plot with the total count of logs stacked by status code"""

    DictOfStatusCode = requests.get(
        "http://127.0.0.1:8000/dictofstatuscode").json()
    Axis = get_x_and_y_axis(DictOfStatusCode)
    create_plot(Axis)
    get_x_values_of_every_plot(Axis[1])
    create_image_plot('Logs count by status code',
                      '3.2Step3StatusCodesPlot(total)')


def step_3_status_code_over_time():     # Step 3: get all status codes with time
    DictOfStatusCode = requests.get(
        "http://127.0.0.1:8000/statuscodeovertime").json()
    i = 0
    # create a plot for every status code
    for key, value in DictOfStatusCode.items():
        Axis = get_x_and_y_axis(value)
        create_plot_With_time(Axis, "#788ed6", 90)
        create_image_plot(f'Logs count by status code: {key}',
                          f'3.4{i}Step3Statuscode{key}(total)')
        i += 1


def step_3_averange_status_codes():       # Step 3: get averange status codes per user
    """Creates an image plot with the averange count of logs per user stacked by status code"""

    DictOfStatusCode = requests.get(
        "http://127.0.0.1:8000/dictofstatuscode").json()
    Axis = get_x_and_y_axis(DictOfStatusCode, USERLENGHT)
    create_plot(Axis)
    get_x_values_of_every_plot(Axis[1])
    create_image_plot('Averange logs per user by status code',
                      '3.3Step3AverangeStatusCodesPlot(averange)')


def step_3_averange_status_code_over_time():     # Step 3: get averange status codes per user with time
    DictOfStatusCode = requests.get(
        "http://127.0.0.1:8000/statuscodeovertime").json()
    i = 0
    # create a plot for every status code
    for key, value in DictOfStatusCode.items():
        Axis = get_x_and_y_axis(value, USERLENGHT)
        create_plot_With_time(Axis, "#788ed6", 90)
        create_image_plot(f'Averange logs per user by status code: {key}',
                          f'3.5{i}Step3Statuscode{key}(averange)')
        i += 1


if __name__ == "__main__":
    step_1()
    step_1_over_time()
    step_2()
    step_2_averange_log()
    step_2_over_time()
    step_2_averange_log_over_time()
    step_3()
    step_3_averange_level()
    step_3_status_codes()
    step_3_status_code_over_time()
    step_3_averange_status_codes()
    step_3_averange_status_code_over_time()


