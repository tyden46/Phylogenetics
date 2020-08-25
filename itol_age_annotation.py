#!/myMiniconda3/envs/py3.8.3/bin/python
import pandas as pd
import plotly.express as px
import numpy as np
import random
import os
os.chdir("C:/Users/tyson/OneDrive/Desktop/Hackensack/AddPangolin")
df=pd.read_table("metadata_2020-07-29_13-52.tsv")
hackensackDF=pd.read_table("HackensackMetaData.csv",delimiter=",")
legendLabels = ['30-39',
                '40-49',
                '50-59',
                '60-69',
                '70-79',
                '80-89']
colors = ['#2166AC',
          '#67A9CF',
          '#D1E5F0',
          '#FDDBC7',
          '#EF8A62',
          '#B2182B']
f = open("itol_age_annotation.txt","w")
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
f.write("LEGEND_TITLE Clade")
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
for ageRange in legendLabels:
    f.write(ageRange)
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
                age = int(thisDF.iloc[0, 1])
                if (30 <= age <= 39 and len(thisDF) > 0):
                    f.write(stripped_line)
                    f.write(" ")
                    f.write(colors[0])
                    f.write(" ")
                    f.write("COL")
                    f.write(colors[0])
                    f.write('\n')
                    f.write('\n')
                if (40 <= age <= 49 and len(thisDF) > 0):
                    f.write(stripped_line)
                    f.write(" ")
                    f.write(colors[1])
                    f.write(" ")
                    f.write("COL")
                    f.write(colors[1])
                    f.write('\n')
                    f.write('\n')
                if (50 <= age <= 59 and len(thisDF) > 0):
                    f.write(stripped_line)
                    f.write(" ")
                    f.write(colors[2])
                    f.write(" ")
                    f.write("COL")
                    f.write(colors[2])
                    f.write('\n')
                    f.write('\n')
                if (60 <= age <= 69 and len(thisDF) > 0):
                    f.write(stripped_line)
                    f.write(" ")
                    f.write(colors[3])
                    f.write(" ")
                    f.write("COL")
                    f.write(colors[3])
                    f.write('\n')
                    f.write('\n')
                if (70 <= age <= 79 and len(thisDF) > 0):
                    f.write(stripped_line)
                    f.write(" ")
                    f.write(colors[4])
                    f.write(" ")
                    f.write("COL")
                    f.write(colors[4])
                    f.write('\n')
                    f.write('\n')
                if (80 <= age <= 89 and len(thisDF) > 0):
                    f.write(stripped_line)
                    f.write(" ")
                    f.write(colors[5])
                    f.write(" ")
                    f.write("COL")
                    f.write(colors[5])
                    f.write('\n')
                    f.write('\n')
            else:
                age=0
                f.write(stripped_line)
                f.write(" ")
                f.write("#ffffff")
                f.write(" ")
                f.write("COL")
                f.write("#ffffff")
                f.write('\n')
                f.write('\n')