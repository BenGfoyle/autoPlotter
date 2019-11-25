"""
Author: Ben Guilfoyle - bengfoyle.github.io
Overview: This script will create a GUI through the use of tkinter, with the aim
of being able to perform some simple plotting and data analysis on a given file.
"""

from tkinter import * #gui elements
import numpy as np #mathematical functions
import matplotlib.pyplot as plt #make plots
import pandas as pd #csv handler
from itertools import groupby
import networkx as nx

#==============================================================================
def fileRead():
    """
    Overview: Read in a csv/json file of data and returns a pandas dataframe
    """

    #define lists and and file name, ISO-8859-1 for Irish characters
    file = txt1.get()
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
    # data.replace('', np.nan, inplace=True)
    # data = data.dropna(axis = 0, how = 'any', thresh = None, subset = None,
    #             inplace = False)

    return data
#==============================================================================

#==============================================================================
def extractData(data):
    """
    Overview: Return a dataframe with columns/variables requested
    """
    columns = txt2.get().split(",") #names of relivent columns
    #removing brackets from list
    values = txt3.get().split("]")
    values = list(filter(lambda a: a != "[", values))
    col1 = data[columns[0]]
    col2 = data[columns[1]]
    #col1 and col2 only have requested values
    # col1 = [x for x in col1 if x in values[0]]
    # col2 = [x for x in col2 if x in values[1]]
    return list(col1),list(col2)
#==============================================================================

#==============================================================================
def networkPlot(x,y):
    """
    Overview: Return a network plot based on a given list
    """
    G = nx.Graph()
    combined = list(zip(x,y))

    combined = set(combined)

    c1Filter, c2Filter = list(set(zip(*combined)))

    #constuct graph of filtered nodes
    filter = c1Filter + c2Filter
    G = nx.Graph()
    N = len(filter)
    labels = filter
    G.add_nodes_from(c1Filter)
    G.add_nodes_from(c2Filter)
    G.add_edges_from(combined)
    nx.draw(G, with_labels = True)
    plt.show()
    return
#==============================================================================

#==============================================================================
def linePlot(x,y):
    """
    Overview: Return a line plot based on a given list
    """
    plt.plot(x,y)
    plt.show()
    return
#==============================================================================

#==============================================================================
def scatterPlot(x,y):
    """
    Overview: Return a scatter plot based on a given list
    """
    plt.scatter(x,y)
    plt.show()
    return
#==============================================================================

#==============================================================================
def histoPlot(x):
    """
    Overview: Return a histogram based on a given list
    """
    plt.hist(x)
    plt.show()
    return
#==============================================================================


#===============================================================================
"""
GUI Elements
"""
#===============================================================================
def makePlot():
    """
    Overview: Run the relivent plot routine when button pressed
    """
    data = fileRead()
    x,y = extractData(data)
    graphType = tkvar.get()
    if graphType == "Network":
        networkPlot(x,y)
    elif graphType == "Line":
        linePlot(x,y)
    elif graphType == "Scatter":
        scatterPlot(x,y)
    elif graphType == "Histogram":
        histoPlot(x)
#===============================================================================

window = Tk()
window.title("Clericus Visualisation")
window.geometry('500x200')

#Insert text with user input text field.

lbl1 = Label(window, text="CSV/JSON Filename:")
lbl1.grid(column=0, row=0)

txt1 = Entry(window, width = 25)
txt1.grid(column = 1, row = 0)

lbl2 = Label(window, text="Columns to View(a,b):")
lbl2.grid(column=0, row=1)

txt2 = Entry(window, width = 25)
txt2.grid(column = 1, row = 1)

lbl3 = Label(window, text="Values to View(in first column):")
lbl3.grid(column=0, row=2)

txt3 = Entry(window, width = 25)
txt3.grid(column = 1, row = 2)

#dropdown menu fo graph types
graphs = {"Network","Line","Scatter","Histogram"}
tkvar = StringVar(window)
tkvar.set("Network")

popupMenu = OptionMenu(window, tkvar, *graphs)
Label(window, text="Choose a graph type").grid(column = 0, row = 3)
popupMenu.grid(column = 1, row =3)

btn3 = Button(window, text="Submit", command = makePlot)
btn3.grid(column=2, row=3)

#loop until closed
window.mainloop()

#===============================================================================
