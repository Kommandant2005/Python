import pandas as pd
Days=["Monday","Tuesday","Wednesday","Thursday","Friday"]
days=pd.Series(Days)
var1=days.sort_values()
Classes=[6,0,3,0,8]
classes=pd.Series(Classes)
var3=classes**3
var2=classes.sort_values(ascending=False)
#dc={"Days":Days,"No. of Classes":Classes}
#df=pd.DataFrame(dc,index=[True,False,True,False,True])
#print(df.iloc[1:5,:3])
print(classes)
print(var2)
print(var3[var3>27])
print(var3[var3<27])
