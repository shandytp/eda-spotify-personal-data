import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def decode_JSON(data_path, encode='utf-8'):
    return json.load(open(data_path, encoding=encode))

def filterByArtist(df_name, artist_name):
    return df_name[df_name['artist'] == artist_name]

def track_count(df_name):
    return df_name.groupby(['artist', 'album']).count()