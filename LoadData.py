import pandas as pd

def load_data(filename):
    with open(filename) as f:
        matrix_type = f.readline().strip()
        if matrix_type == 'DY':
            df = pd.read_csv(f, skiprows=3, sep=";", index_col=0, header=None)
            # pop the labels (last column)
            cdata = df.pop(df.shape[1])
            return df, cdata
        if matrix_type == 'DN':
            df = pd.read_csv(f, skiprows=3, sep=";", index_col=0, header=None)
            return df, None

def load_proj(filename):
    df, cdata = load_data(filename)
    df.columns = ['x', 'y']
    return df, cdata

