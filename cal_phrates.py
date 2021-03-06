"""Utility functions used by the notebooks
"""

import json
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pd.options.display.max_columns = 48
pd.options.display.max_rows = 48


def cal_phrate_alex(d, stream, phrates=None, recompute=False):
    """Compute peak photon rate in bursts for all streams (1-spot ALEX version)
    """
    if phrates is None:
        phrates = {}
    phrates_fname = Path('results/%s_phrate_%s.csv' % (mlabel_alex, stream))
    phrates_fnameB = Path('results/%s_phrate_%sB.csv' % (mlabel_alex, stream))
    if phrates_fname.is_file() and not recompute:
        with open(phrates_fname) as f:
            phrates[str(stream)] = json.load(f)
        phr = pd.read_csv(phrates_fnameB, index_col=0)
        phr.columns = [int(c) for c in phr.columns]
        phr.columns.name = 'spot'
        phrates[str(stream)+'B'] = phr
    else:
        try:
            d.calc_max_rate(m=10, ph_sel=stream, compact=True)
        except ValueError:
            d.calc_max_rate(m=10, ph_sel=stream, compact=False)
        phrates[str(stream)+'B'] = make_df_bursts_alex(d.max_rate)
        phrates[str(stream)] = {
                        'num_bursts': int(d.num_bursts),
                        'num_nans': int(np.isnan(d.max_rate[0]).sum())}
        phrates[str(stream)]['num_valid'] = int(d.num_bursts - phrates[str(stream)]['num_nans'])
        phrates[str(stream)]['valid_fraction'] = float(100 * phrates[str(stream)]['num_valid'] / d.num_bursts)

        phrates_fname.parent.mkdir(parents=True, exist_ok=True)
        with open(phrates_fname, 'wt') as f:
            json.dump(phrates[str(stream)], f)
        phrates[str(stream)+'B'].to_csv(phrates_fnameB)

    print('   Valid fraction (mean of all ch): %.1f %%' %
          np.mean(phrates[str(stream)]['valid_fraction']))
    return phrates


def make_df_bursts_alex(list_of_columns):
    """Create dataframe for burst data for 1-spot ALEX"""
    ncols = len(list_of_columns)
    nrows = max(len(x) for x in list_of_columns)
    columns = np.arange(ncols)
    df = pd.DataFrame(columns=columns, index=np.arange(nrows), dtype=float)
    df.columns.name = 'spot'
    for col, col_data in zip(columns, list_of_columns):
        df.iloc[:len(col_data), col] = col_data
    return df


def make_df_bursts(list_of_columns):
    """Create 48-column dataframe for 48-spot PAX data"""
    ncols = 48
    assert len(list_of_columns) == ncols
    nrows = max(len(x) for x in list_of_columns)
    columns = np.arange(ncols)
    df = pd.DataFrame(columns=columns, index=np.arange(nrows), dtype=float)
    df.columns.name = 'spot'
    for col, col_data in zip(columns, list_of_columns):
        df.iloc[:len(col_data), col] = col_data
    return df


def make_df_spots(list_of_tuples=None):
    """Create 48-rows dataframe for 48-spot PAX data"""
    nrows = 48
    df = pd.DataFrame(index=np.arange(nrows))
    if list_of_tuples is None:
        list_of_tuples = []
    for col, col_data in list_of_tuples:
        df[col] = col_data
    return df

def cal_phrate(d, stream, bsearch_params, phrates=None, recompute=False):
    Path('results').mkdir(exist_ok=True)
    if phrates is None:
        phrates = {}
    phrates_fname = Path(f'results/{d.name}_{bsearch_params}_phrate_{stream}.csv')
    phrates_fnameB = Path(f'results/{d.name}_{bsearch_params}_phrate_{stream}B.csv')
    if phrates_fname.is_file() and not recompute:
        phrates[str(stream)] = pd.read_csv(phrates_fname, index_col=0)
        phrates[str(stream)].index.name = 'spot'
        phr = pd.read_csv(phrates_fnameB, index_col=0)
        phr.columns = [int(c) for c in phr.columns]
        phr.columns.name = 'spot'
        phrates[str(stream)+'B'] = phr
    else:
        try:
            d.calc_max_rate(m=10, ph_sel=stream, compact=True)
        except ValueError:
            d.calc_max_rate(m=10, ph_sel=stream, compact=False)
        phrates[str(stream)+'B'] = make_df_bursts(d.max_rate)
        phrates[str(stream)] = (make_df_spots()
                        .assign(**{'num_bursts': d.num_bursts})
                        .assign(**{'num_nans': [np.isnan(x).sum() for x in d.max_rate]})
                        .assign(**{'num_valid': lambda x: x.num_bursts - x.num_nans})
                        .assign(**{'valid_fraction': lambda x: 100 * x.num_valid / x.num_bursts})
                      )
        phrates[str(stream)].to_csv(phrates_fname)
        phrates[str(stream)+'B'].to_csv(phrates_fnameB)

    print(f'   Valid fraction (mean of all ch): {phrates[str(stream)].valid_fraction.mean():.1f}')
    return phrates
