import pandas as pd
import numpy as np

sub_0283 = pd.read_csv('C:/PORTO/m29-PORTO-sub-0.282.csv')
sub_0284 = pd.read_csv('C:/PORTO/m32-stacked_1.csv')

m=33

w_sub_0283=0.5
w_sub_0284=0.5

final=sub_0283['id'].to_frame()
final['target']=sub_0283['target']*w_sub_0283+sub_0284['target']*w_sub_0284

final.to_csv('C:/PORTO/m{}-PORTO-ensemble.csv'.format(m), index=False) 
