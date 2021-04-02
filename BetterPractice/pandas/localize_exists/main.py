# %%
import time
import random
import datetime
import numpy as np
import pandas as pd

# %%
n = int(3e3)
today = datetime.date.today()
delta = datetime.timedelta(days=1)

for k in [int(1e4), int(1e5), int(1e6), int(3e6)]:
    print(
        f'--------------- Experiment [{k}] starts ------------------------------')
    days = ['{}'.format(today + i * delta) for i in range(n)]

    # Generate df2
    df2 = pd.DataFrame()
    df2['date'] = days
    df2

    # Generate df1
    df1 = pd.DataFrame()
    df1['date'] = random.choices(days[:-10], k=k)
    df1

    # Recommended solution.
    # It won't run at n of 1e6, since it will cost too much time.
    if k < 1e6:
        t0 = time.time()
        o1 = df2[~np.in1d(df2['date'], df1['date'])]['date']
        print(f'Recommended solution [{k}] costs', time.time() - t0, 'seconds')
        o1

    # Set solution
    t0 = time.time()
    set1 = set(df1['date'])
    o2 = df2['date'][df2['date'].map(lambda x: x not in set1)]
    print(f'Set solution [{k}] costs', time.time() - t0, 'seconds')
    o2

    # Compare the results of the two solutions
    if k < 1e6:
        print((o1 == o2).unique())

# %%
set(df2['date']).difference(set(df1['date']))
# %%
