import pandas as pd

def calculate_heikin_ashi(df: pd.DataFrame) -> pd.DataFrame:
    ha_df = pd.DataFrame(index=df.index)
    ha_df['ha_close'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4
    
    ha_open = [df['open'].iloc[0]]
    for i in range(1, len(df)):
        prev_ha_open = ha_open[i-1]
        prev_ha_close = ha_df['ha_close'].iloc[i-1]
        curr_ha_open = (prev_ha_open + prev_ha_close) / 2
        ha_open.append(curr_ha_open)
        
    ha_df['ha_open'] = ha_open
    ha_df['ha_high'] = pd.concat([df['high'], ha_df['ha_open'], ha_df['ha_close']], axis=1).max(axis=1)
    ha_df['ha_low'] = pd.concat([df['low'], ha_df['ha_open'], ha_df['ha_close']], axis=1).min(axis=1)
    return ha_df