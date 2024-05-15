import pandas as pd
import os
import matplotlib.pyplot as plt
import category_encoders as ce
import numpy as np



def IPOsuccess(row):
    
    if int(row["Target stock price after completion\nUSD"]) < int(row["Target stock price 1 week after completion\nUSD"]) and \
       int(row["Target stock price 1 week after completion\nUSD"]) < int(row["Target stock price 1 month after completion\nUSD"]):
        
        return 1
    
    elif int(row["Target stock price after completion\nUSD"]) > int(row["Target stock price 1 week after completion\nUSD"]) and \
       int(row["Target stock price 1 week after completion\nUSD"]) > int(row["Target stock price 1 month after completion\nUSD"]):
        return -1
    
    return 0



df = pd.read_excel("IPOdataset.xlsx")

## Remove columns -> "Pre-deal market capitalisation",
##                   "Deal equity value","Target businees description","Target stock price after completion\nUSD.1"

df = df.drop(columns=["Pre-deal target market capitalisation (Last available year)\nth USD", \
                      "Deal equity value\nth USD", "Target business description(s)", \
                      "Target stock price after completion\nUSD.1", "Completed date"])

# Replace "n.a." value with NaN
df_withoutNull = df.replace("n.a.", np.nan, inplace=False)

# Remove NaN values
df_withoutNull.dropna(inplace=True)

# Add target label ("Success") based on stock prices
df_withoutNull["Success of IPO"] = df_withoutNull.apply(IPOsuccess,axis=1)

# Encode categorical variables
encoder = ce.BinaryEncoder(cols=['Target country code',"Target major sector"])
df_encoded = encoder.fit_transform(df_withoutNull)

# Drop columns: Target stock price after 1 month and 1 week
df_encoded.drop(columns=["Target stock price 1 month after completion\nUSD","Target stock price 1 week after completion\nUSD"],inplace=True)




