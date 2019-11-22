"""
Author: Ben Guilfoyle - bengfoyle.github.io
Overview: This script will create a GUI through the use of tkinter, with the aim
of being able to perform some simple plotting and data analysis on a given file.
"""

from tkinter import * #gui elements
import numpy as np #mathematical functions
import matplotlib.pyplot as plt #make plots
import pandas as pd #csv handler
import networkx as nx

#==============================================================================
def fileRead(file):
    """
    Overview: Read in a csv/json file of data and returns a pandas dataframe
    """

    #define lists and and file name, ISO-8859-1 for Irish characters
    name, ext = file.split(".")
    data = pd.DataFrame()
    if ext == "csv":
        data = pd.read_csv(file, encoding='ISO-8859-1')
    elif ext == "json":
        data = pd.read_json(file, encoding='ISO-8859-1')
        data = data.transpose()
    else:
        print("Error: Unsupported File Type ", ext)

    #replace blanks with nan and drop anyt nan values
    data.replace('', np.nan, inplace=True)
    data = data.dropna(axis = 0, how = 'any', thresh = None, subset = None,
                inplace = False)

    return data
#==============================================================================

#==============================================================================
def extractData(data):
    """
    Overview: Return a dataframe with columns/variables requested
    """
    reliventData = []
    return reliventData
#==============================================================================

#==============================================================================
def networkPlot():
    """
    Overview: Return a network plot based on a given list
    """
    G = nx.Graph()
    G.add_edge(1,2)
    G.add_edge(1,3)
    nx.draw(G, with_labels=True)
    plt.show()
    return
#==============================================================================

#==============================================================================
def linePlot():
    """
    Overview: Return a line plot based on a given list
    """
    x = [1,2,3]
    y = [3,2,1]
    plt.plot(x,y)
    plt.show()
    return
#==============================================================================

#==============================================================================
def scatterPlot():
    """
    Overview: Return a scatter plot based on a given list
    """
    x = [1,2,3]
    y = [3,2,1]
    plt.scatter(x,y)
    plt.show()
    return
#==============================================================================

#==============================================================================
def histoPlot():
    """
    Overview: Return a histogram based on a given list
    """
    x = [1,1,1,2,2,3]
    plt.hist(x)
    plt.show()
    return
#==============================================================================


#===============================================================================
"""
GUI Elements
"""

window = Tk()
window.title("Clericus Visualisation")
window.geometry('500x200')

#Insert text with user input text field.

lbl1 = Label(window, text="CSV/JSON Filename:")
lbl1.grid(column=0, row=0)

txt1 = Entry(window, width = 25)
txt1.grid(column = 1, row = 0)

lbl2 = Label(window, text="Columns to View:")
lbl2.grid(column=0, row=1)

txt2 = Entry(window, width = 25)
txt2.grid(column = 1, row = 1)

lbl3 = Label(window, text="Values to View:")
lbl3.grid(column=0, row=2)

txt3 = Entry(window, width = 25)
txt3.grid(column = 1, row = 2)

#button that runs function on click
btn1 = Button(window, text="Network Graph", command = networkPlot)
btn1.grid(column=0, row=4)

btn2 = Button(window, text="Scatter Plot", command = scatterPlot)
btn2.grid(column=0, row=5)

btn3 = Button(window, text="Line Plot", command = linePlot)
btn3.grid(column=1, row=4)

btn3 = Button(window, text="Histogram", command = histoPlot)
btn3.grid(column=1, row=5)

#loop until closed
window.mainloop()

#===============================================================================
