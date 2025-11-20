import numpy as np
import pandas as pd

feat_ranges = pd.DataFrame({
    'smoke_emiss': [0.25, 4],
    'smoke_diam': [90, 299],
    'sig_w': [0.4, 1.2],
    'dry_dep_acc': [0.1, 10],
    'sea_spray': [0.25, 4],
    'a_ent_1_rp': [0.02, 0.5],
    'bparam': [-0.15, -0.13],
    'kappa_oc': [0.2, 0.65],
    'dms': [0.33, 3],
    'anth_so2': [0.6, 1.5],
    'autoconv_exp_nd': [-3, -1],
    'bc_ri': [0.4, 1]
})
feat_ranges.index = ['Minimum', 'Maximum']
param_ranges_df = feat_ranges.T

log_scale_params = [
        'smoke_emiss',
        'dry_dep_acc',
        'sea_spray',
        'dms',
        'anth_so2'
    ]

def sig_w_norm_to_raw(norm_val):
    x = norm_val
    x1 = 0.004765
    y1 = 0.405241
    x2 = 0.724138
    y2 = 1.196552
    m = (y2 - y1) / (x2 - x1)

    # y - y1 = m * (x - x1)
    y = m * (x - x1) + y1
    raw_val = y
    return raw_val

def sig_w_raw_to_norm(raw_val):
    x = raw_val
    y1 = 0.004765
    x1 = 0.405241
    y2 = 0.724138
    x2 = 1.196552
    m = (y2 - y1) / (x2 - x1)

    # y - y1 = m * (x - x1)
    y = m * (x - x1) + y1
    norm_val = y
    return norm_val

def conv_raw_to_norm(raw_scale_val,param_name):

    log_scale_params = [
        'smoke_emiss',
        'dry_dep_acc',
        'sea_spray',
        'dms',
        'anth_so2'
    ]

    raw_min = param_ranges_df.loc[param_name, 'Minimum']
    raw_max = param_ranges_df.loc[param_name, 'Maximum']
    
    if param_name == 'sig_w':
        norm_val = sig_w_raw_to_norm(raw_scale_val)
        return norm_val

    if param_name in log_scale_params:
        norm_scale_val = (np.log10(raw_scale_val) - np.log10(raw_min)) / (np.log10(raw_max) - np.log10(raw_min))
    else:
        norm_scale_val = (raw_scale_val - raw_min) / (raw_max - raw_min)

    return norm_scale_val

def conv_norm_to_raw(norm_scale_val,param_name):

    log_scale_params = [
        'smoke_emiss',
        'dry_dep_acc',
        'sea_spray',
        'dms',
        'anth_so2'
    ]

    raw_min = param_ranges_df.loc[param_name, 'Minimum']
    raw_max = param_ranges_df.loc[param_name, 'Maximum']

    if param_name == 'sig_w':
        raw_val = sig_w_norm_to_raw(norm_scale_val)
        return raw_val
    
    if param_name in log_scale_params:
        raw_scale_val = 10**(norm_scale_val*(np.log10(raw_max) - np.log10(raw_min)) + np.log10(raw_min))
    else:
        raw_scale_val = norm_scale_val*(raw_max - raw_min) + raw_min

    return raw_scale_val