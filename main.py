import numpy as np
import pandas as pd
from tabulate import tabulate

play=pd.read_csv('Console Generation data.csv')

play=play.rename(columns={' Original Price ':'Original Price',' 2022 Price (Adjusted for inflation) ':'2022 Price (Adjusted for inflation)',' Total Systems Sold ':'Total Systems Sold'})

#time periode nettoyage
play["Time period"]=play["Time period"].str.lower().str.strip()
play["Time period"]=play["Time period"].str.replace("present","2026")
play["Time period"]=play["Time period"].str.replace("?present","-2026")
play["Time period"]=play["Time period"].str.replace("?","-")

#Primary consoles
play["Primary consoles"]=play["Primary consoles"].str.lower().str.strip()

#Year of release
play["Year of release"]=play["Year of release"].astype(int)

#Game media
play["Game media"]=play["Game media"].str.lower().str.strip()

#Original Price
play["Original Price"]=play["Original Price"].str.lower().str.strip()
play["Original Price"]=play["Original Price"].str.extract('\$(.+)',1)
play["Original Price"]=play["Original Price"].astype(float)

#2022 Price (Adjusted for inflation)
play["2022 Price (Adjusted for inflation)"]=play["2022 Price (Adjusted for inflation)"].str.lower().str.strip()
play["2022 Price (Adjusted for inflation)"]=play["2022 Price (Adjusted for inflation)"].str.extract('\$(.+)',1)
play["2022 Price (Adjusted for inflation)"]=play["2022 Price (Adjusted for inflation)"].str.replace(',','')
play["2022 Price (Adjusted for inflation)"]=play["2022 Price (Adjusted for inflation)"].astype(float)




#Total Systems Sold
play["Total Systems Sold"]=play["Total Systems Sold"].str.replace(',','')
play["Total Systems Sold"]=play["Total Systems Sold"].astype(float)


play=play.drop(columns=["Generation"])

xb=play[play["Primary consoles"].str.contains("xb")]
nin=play[play["Primary consoles"].str.contains("nin")]
play=play[play["Primary consoles"].str.contains("play")]

play.to_csv("C:/Users/fresnel/Desktop/csv traite/Playstation.csv",index=False)
xb.to_csv("C:/Users/fresnel/Desktop/csv traite/Xbox.csv",index=False)
nin.to_csv("C:/Users/fresnel/Desktop/csv traite/Nintendo.csv",index=False)

print(tabulate(nin,tablefmt="psql",headers="keys",showindex=False))
print(tabulate(play,tablefmt="psql",headers="keys",showindex=False))
print(tabulate(xb,tablefmt="psql",headers="keys",showindex=False))

