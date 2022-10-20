import pandas as pd

data ={'Name': ['Jai','Princi','Gaurav','Anuj'],
                'Height': [5.1,6.2,5.6,6.0],
                'Qualification': ['Msc','MA','MBA','DNB']}

address = {'Delhi':'Jai','Bangalore':'Princi',
           'Patna':'Gaurav','Chennai':'Anuj'}
myvar = pd.DataFrame(data)


myvar['Address'] = address


print(myvar)
    
