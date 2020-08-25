#!/myMiniconda3/envs/py3.8.3/bin/python
import pandas as pd
import plotly.express as px
import numpy as np
import random
ListOfClades=["A.1.1",
              "A.1.3",
              "A.4",
              "A.6",
              "A.2",
              "A.5",
              "A.3",
              "A.1",
              "A",
              "B.1.34",
              "B.1.69",
              "B.1.71",
              "B.1.19",
              "B.1.23",
              "B.1.22",
              "B.1.37",
              "B.1.13",
              "B.1.36",
              "B.1.66",
              "B.1.40",
              "B.1.12",
              "B.1.30",
              "B.1.31",
              "B.1.39",
              "B.1.34",
              "B.1.26",
              "B.1.41",
              "B.1.38",
              "B.1.29",
              "B.1.43",
              "B.1.33",
              "B.1.35",
              "B.1.72",
              "B.1.32",
              "B.1.67",
              "B.1.70",
              "B.1.1",
              "B.1.5",
              "B.1.3",
              "B.1.8",
              "B.2.6",
              "B.2.2",
              "B.2.7",
              "B.2.4",
              "B.2.5",
              "B.2.1",
              "B.1.6",
              "B.14",
              "B.13",
              "B.16",
              "B.15",
              "B.1"
              "B.3",
              "B.9",
              "B.5",
              "B.6",
              "B.4",
              "B.7",
              "B.2",
              "B"]
print(len(ListOfClades))

total=["#F1B8C2","#F0B8BE","#EFB9B9","#EEBAB5","#ECBBB0","#EABCAC","#E8BEA9","#E5BFA5","#E2C0A2","#DFC29F",
       "#DBC39D","#D7C59B","#D3C69A","#CEC899","#CAC999","#C5CB9A","#C0CC9B","#BBCD9C","#B6CE9E","#B1CFA1",
       "#ABD0A4","#A6D1A7","#A1D2AB","#9DD3AE","#98D3B3","#94D4B7","#91D4BB","#8ED4C0","#8CD4C4","#8AD4C8",
       "#8AD4CD","#8AD3D1","#8CD3D5","#8ED2D9","#91D1DC","#94D0E0","#98CFE3","#9DCDE5","#A3CCE8","#A8CAEA",
       "#AEC9EB","#B4C7ED","#BAC5ED","#C0C4EE","#C5C2EE","#CBC0ED","#D0BFEC","#D5BDEB","#DABCE9","#DEBBE7",
       "#E2BAE5","#E5B9E2","#E8B8DF","#EBB7DB","#EDB7D7","#EFB7D3","#F0B6CF","#F1B7CB","#F1B7C7"]
random.seed(1)
random.shuffle(total)
df=pd.read_table("metadata_2020-07-29_13-52.tsv")
f = open("hackensack_color_strip_all_clades.txt","w")
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
for color in total:
    f.write("1")
    f.write(" ")
f.write('\n')
f.write("LEGEND_COLORS ")
for color in total:
    f.write(color)
    f.write(" ")
f.write('\n')
f.write("LEGEND_LABELS ")
for clade in ListOfClades:
    f.write(clade)
    f.write(" ")
f.write('\n')
f.write("DATA")
f.write('\n')

f.write('\n')
#LEGEND_COLORS,#3C91E6,#9fd356,#fa824c,#C879FF
#LEGEND_LABELS,MERS,Bat_Coronavirus,COVID19,Coronavirus_related_SARS
proportion=4000/len(df['pangolin_lineage'])
numPerClade=df['pangolin_lineage'].value_counts(normalize=True)
#160232 #efff22 COL#efff22
a_file=open("mafft_alignmentSubset_400.fa")
for line in a_file:
    stripped_line = line.strip()
    if (">" in stripped_line):
        #print(stripped_line)
        if ("NJ-BioR" in stripped_line):
            stripped_line=stripped_line.replace('>','')
            f.write(stripped_line)
            f.write(" ")
            f.write("#ffffff")
            f.write(" ")
            f.write("COL")
            f.write("#ffffff")
            f.write('\n')
        else:
            if ("North America" in stripped_line):
                stripped_line=stripped_line.replace("North America","NorthAmerica")
            date=stripped_line.split("|")[2]
            print(date)
            if(len(date.split("-"))<3):
                print(date)
                newDate=date+"-00"
                print(newDate)
                stripped_line=stripped_line.replace(date,newDate)
            id=stripped_line.split("|")[1]
            thisDF = df[df['gisaid_epi_isl'] == id]
            f.write("'")
            f.write("hCoV-19/")
            f.write(thisDF.iloc[0,0])
            f.write("|")
            f.write(thisDF.iloc[0,2])
            f.write("|")
            f.write(date)
            f.write("|")
            region=thisDF.iloc[0,5]
            if ("North America" in thisDF.iloc[0,5]):
                region=region.replace("North America","NorthAmerica")
            if ("South America" in thisDF.iloc[0,5]):
                region=region.replace("South America","SouthAmerica")
            f.write(region)
            f.write("'")
            f.write(" ")
            counter = 0
            for q in ListOfClades:
                if q in str(thisDF.iloc[0,17]):
                    f.write(total[counter])
                    f.write(" COL")
                    f.write(total[counter])
                    f.write('\n')
                counter=counter+1
            """
            if "A.1" in str(thisDF.iloc[0,17]) :
                f.write(total[0])
                f.write(" COL")
                f.write(total[0])
                f.write('\n')
            elif "A.2" in str(thisDF.iloc[0,17]) :
                f.write(total[1])
                f.write(" COL")
                f.write(total[1])
                f.write('\n')
            elif "A.3" in str(thisDF.iloc[0,17]) :
                f.write(total[2])
                f.write(" COL")
                f.write(total[2])
                f.write('\n')
            elif "A.4" in str(thisDF.iloc[0,17]) :
                f.write(total[3])
                f.write(" COL")
                f.write(total[3])
                f.write('\n')
            elif "A.5" in str(thisDF.iloc[0,17]) :
                f.write(total[4])
                f.write(" COL")
                f.write(total[4])
                f.write('\n')
            elif "A.6" in str(thisDF.iloc[0,17]) :
                f.write(total[5])
                f.write(" COL")
                f.write(total[5])
                f.write('\n')
            elif "B.2" in str(thisDF.iloc[0,17]) :
                f.write(total[6])
                f.write(" COL")
                f.write(total[6])
                f.write('\n')
            elif "B.3" in str(thisDF.iloc[0,17]) :
                f.write(total[7])
                f.write(" COL")
                f.write(total[7])
                f.write('\n')
            elif "B.4" in str(thisDF.iloc[0,17]) :
                f.write(total[8])
                f.write(" COL")
                f.write(total[8])
                f.write('\n')
            elif "B.5" in str(thisDF.iloc[0,17]) :
                f.write(total[9])
                f.write(" COL")
                f.write(total[9])
                f.write('\n')
            elif "B.6" in str(thisDF.iloc[0,17]) :
                f.write(total[10])
                f.write(" COL")
                f.write(total[10])
                f.write('\n')
            elif "B.7" in str(thisDF.iloc[0,17]) :
                f.write(total[11])
                f.write(" COL")
                f.write(total[11])
                f.write('\n')
            elif "B.9" in str(thisDF.iloc[0,17]) :
                f.write(total[12])
                f.write(" COL")
                f.write(total[12])
                f.write('\n')
            elif "B.10" in str(thisDF.iloc[0,17]) :
                f.write(total[13])
                f.write(" COL")
                f.write(total[13])
                f.write('\n')
            elif "B.13" in str(thisDF.iloc[0,17]) :
                f.write(total[14])
                f.write(" COL")
                f.write(total[14])
                f.write('\n')
            elif "B.14" in str(thisDF.iloc[0,17]) :
                f.write(total[15])
                f.write(" COL")
                f.write(total[15])
                f.write('\n')
            elif "B.15" in str(thisDF.iloc[0,17]) :
                f.write(total[16])
                f.write(" COL")
                f.write(total[16])
                f.write('\n')
            elif "B.16" in str(thisDF.iloc[0,17]) :
                f.write(total[17])
                f.write(" COL")
                f.write(total[17])
                f.write('\n')
            elif "B.1" in str(thisDF.iloc[0,17]) :
                f.write(total[18])
                f.write(" COL")
                f.write(total[18])
                f.write('\n')
            elif "B" in str(thisDF.iloc[0,17]) :
                f.write(total[20])
                f.write(" COL")
                f.write(total[20])
                f.write('\n')
            elif "A" in str(thisDF.iloc[0,17]) :
                f.write(total[21])
                f.write(" COL")
                f.write(total[21])
                f.write('\n')"""
            f.write('\n')
print(total)