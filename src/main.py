import pandas as pd
import numpy as np


def main():
    interactiondata = pd.read_csv('data/interactiondata.csv')
    userdata = pd.read_csv('data/userdata.csv')

    df = pd.merge(interactiondata, userdata, on='userid')
    df.head()


if __name__ == '__main__':
    main()