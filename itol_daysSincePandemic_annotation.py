#!/myMiniconda3/envs/py3.8.3/bin/python
import pandas as pd
import plotly.express as px
import numpy as np
import random
import os
os.chdir("C:/Users/tyson/OneDrive/Desktop/Hackensack/AddPangolin")
df=pd.read_table("metadata_2020-07-29_13-52.tsv")
hackensackDF=pd.read_table("HackensackMetaData.csv", delimiter=",")
legendLabels = ['102-108',
                '109-115',
                '116-122',
                '123-129']
colors = ['#f7f7f7',
          '#cccccc',
          '#969696',
          '#525252']

f = open("itol_daysSincePandemic_annotation.txt","w")
f.write("DATASET_COLORSTRIP")
f.write('\n')
f.write("SEPARATOR SPACE")
f.write('\n')
f.write("DATASET_LABEL clade_annotation")
f.write('\n')
f.write("COLOR #ff0000")
f.write('\n')
f.write("STRIP_WIDTH 25")
f.write('\n')
f.write("MARGIN 0")
f.write('\n')
f.write("BORDER_WIDTH 1")
f.write('\n')
f.write("BORDER_COLOR #000")
f.write('\n')
f.write("SHOW_INTERNAL 0")
f.write('\n')
f.write("LEGEND_TITLE DAYS-SINCE-PANDEMIC-STARTED")
f.write('\n')
f.write("LEGEND_SHAPES ")
for color in colors:
    f.write("1")
    f.write(" ")
f.write('\n')
f.write("LEGEND_COLORS ")
for color in colors:
    f.write(color)
    f.write(" ")
f.write('\n')
f.write("LEGEND_LABELS ")
for dayRange in legendLabels:
    f.write(dayRange)
    f.write(" ")
f.write('\n')
f.write("DATA")
f.write('\n')

f.write('\n')
a_file=open("combinedHackensackThatHaveMetadata.fasta")
for line in a_file:
    stripped_line = line.strip()
    if (">" in stripped_line):
        #print(stripped_line)
        if ("NJ-BioR" in stripped_line):
            myID=stripped_line.replace('>','')
            stripped_line=stripped_line.replace('>','')
            thisDF = hackensackDF[hackensackDF['ID']==myID]
            if (len(thisDF)>0):
                days = int(thisDF.iloc[0, 10])
                if (102<=days<=108):
                    f.write(stripped_line)
                    f.write(" ")
                    f.write(colors[0])
                    f.write(" ")
                    f.write("COL")
                    f.write(colors[0])
                    f.write('\n')
                    f.write('\n')
                if (109<=days<=115):
                    f.write(stripped_line)
                    f.write(" ")
                    f.write(colors[1])
                    f.write(" ")
                    f.write("COL")
                    f.write(colors[1])
                    f.write('\n')
                    f.write('\n')
                if (116<=days<=122):
                    f.write(stripped_line)
                    f.write(" ")
                    f.write(colors[2])
                    f.write(" ")
                    f.write("COL")
                    f.write(colors[2])
                    f.write('\n')
                    f.write('\n')
                if (122<=days<=128):
                    f.write(stripped_line)
                    f.write(" ")
                    f.write(colors[3])
                    f.write(" ")
                    f.write("COL")
                    f.write(colors[3])
                    f.write('\n')
                    f.write('\n')
            else:
                f.write(stripped_line)
                f.write(" ")
                f.write("#ffffff")
                f.write(" ")
                f.write("COL")
                f.write("#ffffff")
                f.write('\n')
                f.write('\n')