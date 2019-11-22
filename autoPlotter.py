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
    data.replace('', np.nan, inplace=True)
    data = data.dropna(axis = 0, how = 'any', thresh = None, subset = None,
                inplace = False)

    return data
#==============================================================================

#==============================================================================
def extractData():
    """
    Overview: Return a dataframe with columns/variables requested
    """
    columns = txt2.get().split(",") #names of relivent columns
    values = txt3.get().split("]")
    values = filter(lambda a: a != "[", x) #re,oving brackets from list
    col1 = data.groupby([columns[0]])
    col2 = data.groupby([columns[1]])
    col1 = [x for x in col1 if x in values[0]]
    col1 = [x for x in col2 if x in values[1]]
    return col1,col2
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
#===============================================================================
def makePlot():
    """
    Overview: Run the relivent plot routine when button pressed
    """
    fileRead()
    graphType = tkvar.get()
    if graphType == "Network":
        networkPlot()
    elif graphType == "Line":
        linePlot()
    elif graphType == "Scatter":
        scatterPlot()
    elif graphType == "Histogram":
        histoPlot()
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
