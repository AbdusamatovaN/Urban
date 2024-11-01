import requests
import pandas as pd
import numpy as np

r = requests.get('https://api.github.com/events')
print(r.status_code)
print(r.text)

s = pd.Series([1, 3, 5, np.nan, 6, 8])
data = pd.DataFrame(s)
print(s)

a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a.shape)

