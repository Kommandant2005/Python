import pandas as pd
import numpy as np

d = {'Name':["a","b","c","d","e","f","g","h","i","j","k","l"],
     'Age':[1,2,3,4,5,6,7,8,9,10,11,12],
     'Rating':[2.85,9.2,5.7,2.1,3.4,3.5,5.2,4.8,5.1,6.33,7.8,2.0]
}

df= pd.DataFrame(d,index=[True,False,True,False,True,False,True,False,True,False,True,False])

print(df)
#print(df.head(10))
#print(df.tail(10))
