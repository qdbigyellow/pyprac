import numpy as np
import pandas as pd

if __name__ == "__main__":
    ts1 = pd.Series(np.random.randn(10), index = pd.date_range('1/1/2019', periods=10))
    ts2 = pd.Series(np.random.randn(10), index = pd.date_range('1/2/2019', periods=10))
    print(ts1)