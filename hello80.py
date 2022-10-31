import pandas as pd

data = {"State":["Andhra Pradesh","Odisha","Madhya Pradesh","Gujarat"],
        "Toys":[4354,5654,6757,2344],
        "Books":[4634,3423,5645,2341],
        "Uniforms":[3242,4536,5643,2342],
        "Shoes":[1234,4537,2324,5646]
}


#print(myvar[["Books","Uniforms","Shoes"]])
myvar=pd.DataFrame(data)
#print(myvar.keys)
#print(myvar.values)
#print(myvar.T)
print(myvar.iloc[0:4,2:4])
 
