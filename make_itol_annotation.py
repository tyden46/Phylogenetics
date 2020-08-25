#!/myMiniconda3/envs/py3.8.3/bin/python
import pandas as pd
import plotly.express as px
import numpy as np
import random
total=["#F1B8C2",
       "#EFBAB6",
       "#E9BDAB",
       "#E2C1A2",
       "#D8C49C",
       "#CCC899",
       "#BFCC9B",
       "#B2CFA0",
       "#A4D2A9",
       "#98D3B3",
       "#8FD4BF",
       "#8AD4CB",
       "#8CD2D6",
       "#94D0DF",
       "#A0CDE7",
       "#AFC8EC",
       "#BFC4EE",
       "#CEBFED",
       "#DBBCE9",
       "#E5B9E2",
       "#ECB7D9",
       "#F0B7CE"]
random.seed(1)
random.shuffle(total)
df=pd.read_table("metadata_2020-07-29_13-52.tsv")
f = open("hackensack_color_strip.txt","w")
f.write("DATASET_COLORSTRIP")
f.write('\n')
f.write("SEPARATOR SPACE")
f.write('\n')
f.write("DATASET_LABEL color_strip2")
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
f.write("DATA")
f.write('\n')

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
            f.write(" ")
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
                f.write('\n')
            f.write('\n')