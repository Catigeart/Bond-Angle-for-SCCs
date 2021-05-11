import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import constants as C
import pdb
#sns.set_style("whitegrid")

all_df = pd.read_csv(C.PROC_DATA_PATH + 'all_df.csv', index_col=0)
plt.figure(figsize=(10,3))                                                               
sns.distplot(all_df['scalar_coupling_constant'])
plt.title('Displot of scalar coupling constant')
plt.savefig('./Distplot.png', dpi=600, bbox_inches='tight')
plt.savefig('./Distplot.tif', dpi=600, bbox_inches='tight')
