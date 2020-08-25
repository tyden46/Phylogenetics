#!/myMiniconda3/envs/py3.8.3/bin/python
import pandas as pd
import plotly.express as px
import numpy as np
import random
import os
os.chdir("C:/Users/tyson/OneDrive/Desktop/Hackensack/AddPangolin")
df=pd.read_table("metadata_2020-07-29_13-52.tsv")
hackensackDF=pd.read_table("HackensackMetaData.csv",delimiter=",")
legendLabels = ['20-30',
                '30-40',
                '40-50',
                '50-60',
                'Unknown']
colors = ['#ffffb2',
          '#fecc5c',
          '#fd8d3c',
          '#e31a1c',
          "#ffffff"]

f = open("itol_bmi_annotation.txt","w")
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
f.write("LEGEND_TITLE BMI")
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
for bmi in legendLabels:
    f.write(bmi)
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
            if len(thisDF)>0 and str(thisDF.iloc[0, 7])=="Unknown":
                f.write(stripped_line)
                f.write(" ")
                f.write("#ffffff")
                f.write(" ")
                f.write("COL")
                f.write("#ffffff")
                f.write('\n')
                f.write('\n')
            elif (len(thisDF)>0):
                bmi = float(thisDF.iloc[0, 7])
                if (20<=bmi<30):
                    f.write(stripped_line)
                    f.write(" ")
                    f.write(colors[0])
                    f.write(" ")
                    f.write("COL")
                    f.write(colors[0])
                    f.write('\n')
                    f.write('\n')
                if (30<=bmi<40):
                    f.write(stripped_line)
                    f.write(" ")
                    f.write(colors[1])
                    f.write(" ")
                    f.write("COL")
                    f.write(colors[1])
                    f.write('\n')
                    f.write('\n')
                if (40<=bmi<50):
                    f.write(stripped_line)
                    f.write(" ")
                    f.write(colors[2])
                    f.write(" ")
                    f.write("COL")
                    f.write(colors[2])
                    f.write('\n')
                    f.write('\n')
                if (50<=bmi<60):
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