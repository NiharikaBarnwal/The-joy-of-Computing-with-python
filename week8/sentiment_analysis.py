# nltk not working
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file='NPTEL/week8/data_file.xslsx'
xl=pd.ExcelFile(file) #Read from Excel
dfs=xl.parse(xl.sheet_names[0]) #Parsing Excel sheet to dataframe
dfs=list(dfs['Timeline']) #Removes the blank rows from the data frame
print(dfs)
sid=SentimentIntensityAnalyzer()
str1 = "UTC+05:30"
for data in dfs:
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])