import pandas as pd


def get_normed_data(data: pd.DataFrame) -> pd.DataFrame:
    norm = (data ** 2).sum(axis=1).apply("sqrt")
    normed_df = data.divide(norm, axis=0)
    sim_df = normed_df.dot(normed_df.T)
    return sim_df
