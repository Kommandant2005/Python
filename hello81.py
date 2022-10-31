import pandas as pd

data = {"State":["Andhra Pradesh","Rajasthan","Madhya Pradesh","Gujarat"],
        "Statues":[4354,5654,6757,2344],
        "Jewellery":[4634,3423,5645,2341],
        "Makeup":[3242,4536,5643,2342],
        "Sandal":[1234,4537,2324,5646]
}

myvar = pd.DataFrame(data)

print(myvar.iloc[1:2,2:3])


