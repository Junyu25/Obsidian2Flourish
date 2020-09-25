import os
import re
import sys
import pandas as pd

Dir = sys.argv[1]

regex = r"(\[\[.*?\]\])"
Links = pd.DataFrame()

for subdirs, dirs, files in os.walk(Dir):
    for file in files:
        if file.endswith(".md"):
            #print(os.path.join(subdirs, file))
            filePath = os.path.join(subdirs, file)
            infile = open(filePath, 'r') 
            for line in infile:
                #print(line.strip())
                match = re.search(regex, line.strip())
                if match != None: 
                    node = match.group().replace("[[", "").replace("]]", "")
                    Links = Links.append({"Source":str(file.replace(".md", "")), "Target":str(node), "Value":"1"}, ignore_index=True)
                    print(node)
            # Closing files 
            infile.close() 

Links.to_csv("Links.csv", index=False)
Sum = pd.concat([Links["Source"], Links["Target"]], ignore_index=True, sort=False)
Points = Sum.value_counts()
Points.to_csv("Points.csv")