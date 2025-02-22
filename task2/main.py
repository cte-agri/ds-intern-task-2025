import math
import time

import numpy as np
import pandas as pd


def main(input_row):
    lines = input_row.strip().splitlines()
    inputs = [list(map(int, line.split())) for line in lines]

    price = 1000 #ここの処理を変える

    return price


if __name__ == '__main__':
    df = pd.read_csv(f"./sample_100.csv")
    start_time = time.time()

    result = []
    for row in range(len(df)):
        input_row = df.loc[row, "input"]
        result_tmp = main(input_row)
        result.append(result_tmp)
    df["result"] = result

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"elapsed time: {elapsed_time}")

    mae = np.mean(np.abs(df["output"]-df["result"]))
    print(f"MAE: {mae}")
    
    score = math.log(mae * elapsed_time)
    print(f"SCORE: {score}")