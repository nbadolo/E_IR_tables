#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:35:07 2023

@author: nbadolo
"""



import xlrd
import pandas as pd
from xlrd import*
from openpyxl import load_workbook
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# Comparaison des valeurs de E_IR et L*/L_IR de mes calculs et ceux de Iain.
# IL s'agit de représenter ldans une curbes les valeurs de Iain en fonction des
#  des miennes
# =============================================================================

"""
# Definitions bloc:
    file_path_l: chemin gros tableau
    file_path_s: chemin du petit tableau
    file_path_r: chemin des étoiles resolues
"""

file_path_c = '/home/nbadolo/Bureau/Aymard/These/for_biblio_papers/compar_log_par.ods'

df_c = pd.read_excel(file_path_c)

#%%
fig = plt.figure('Comparison of E_IR and L*/LIR  values: Mine vs McD')
fig.set_size_inches(18.5, 10, forward = True)
plt.subplot(1,2,1)
plt.plot(df_c["E_IR_Mine"], df_c["E_IR_McD"], 'b^')
plt.legend(["E_IR"])
plt.xlabel('Mine', size=10)
plt.ylabel('McDonald 2012', size=10)

plt.subplot(1,2,2)
plt.plot(df_c["L*/LIR_Mine"], df_c["L*/LIR_McD"], 'ro')
plt.legend(["L*/LIR"])
plt.xlabel('Mine', size=10)
plt.ylabel('McDonald 2012', size=10)


#plt.title( label = "Excess infrared in relation to key parameters" ,fontsize = 12 ,color = "k" )

plt.savefig('/home/nbadolo/Bureau/Aymard/These/for_biblio_papers/plots/log_paper_plots/' + 'comparEIR.pdf', 
                dpi=100, bbox_inches ='tight')


plt.savefig('/home/nbadolo/Bureau/Aymard/These/for_biblio_papers/plots/log_paper_plots/' + 'comparEIR.png', 
                dpi=100, bbox_inches ='tight')
plt.tight_layout()
plt.show()