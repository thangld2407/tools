import numpy as np
import pandas as pd

DATA_PATH = 'data_samples/data.csv'


def read_file_csv():
    df = pd.read_csv(DATA_PATH)
    return df


def main():
    df = read_file_csv()
    arr = np.array(df)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i == 1):
                print(arr[i][j],)


main()
