import pandas as pd

data = {"fruit":pd.Series(["apple","banana","mango","grapes","strawberry"]),
        "vegetable":pd.Series(["tomato","cucumber","ladyfinger","eggplant","greenonion"])
}

df = pd.DataFrame(data)

print(df)
