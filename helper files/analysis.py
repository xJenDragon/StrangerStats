import pandas as pd


def monster_summary(df, agg_funcs=["mean", "median", "var", "sum"]):
    """
    Summarize monster sightings by monster type.
    Parameters:
        df (pd.DataFrame): Monster sightings dataframe
        agg_funcs (list): List of aggregations to apply
    """
    return df.groupby("Monster")["Count"].agg(agg_funcs)


def area_summary(df, top_n=5, sort_by="sum"):
    """
    Summarize monster sightings by area.
    Parameters:
        df (pd.DataFrame): Monster sightings dataframe
        top_n (int): Show only the top N areas
        sort_by (str): Aggregation to sort by ('sum' or 'mean')
    """
    grouped = df.groupby("Area")["Count"].agg(["sum", "mean"])
    return grouped.sort_values(by=sort_by, ascending=False).head(top_n)
