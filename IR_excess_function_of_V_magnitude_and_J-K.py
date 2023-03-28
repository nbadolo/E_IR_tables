#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:19:26 2023

@author: nbadolo
"""


#import xlrd
import pandas as pd
from xlrd import*
from openpyxl import load_workbook
#jpype.startJVM() 
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import glob # pour changer l'extension des fichiers
from astropy.table import Table 





"""
This code plot the excess infrared as fonction of magnitude in V band and J-K band 
"""
# =============================================================================
# Nous representons ici, pour le grand tableau log, l'échantillon et les objets  
# resolus les execes infra rouge  en fonction de la magnitude en V et de la J-K
# des étoiles  
# =============================================================================

"""
# Definitions bloc:
    file_path_l: chemin gros tableau
    file_path_s: chemin du petit tableau
    file_path_r: chemin des étoiles resolues
"""

#sub_folder = 'resolved_stars'
sub_folder2 = 'sample_stars'
sub_folder3 = 'large_table_stars'
lst_folder =[sub_folder2 ,sub_folder3]
for folder in lst_folder :
    
    path_txt = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/'+ folder +'/txt_files/'
    path_csv = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/'+ folder +'/csv_files/'
    
    ## conversion du format txt  en format csv
    lst_txt = glob.glob(os.path.join(path_txt, "*.txt"))
    n_lst_txt = len(lst_txt)
    
    for fic in os.listdir(path_txt) :
        table_name = os.path.splitext(fic)[0]
        
        # stop
        file_txt = pd.read_csv(path_txt +fic)# delimiter = ';') # ouverture du fichier txt avec csv
        file_csv = file_txt.to_csv(path_csv + table_name+'.csv', index = None) # creation du fichier csv
        #print(file_txt)   
    #print(os.listdir(path_csv))

#%%
#file_path_r = '/home/nbadolo/Bureau/Aymard/These/for_biblio_papers/used_tables/resol_log.ods'
file_path_s = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/'+ lst_folder[0] +'/csv_files/' + lst_folder[0] +'_E_IR_L_LIR.csv'
file_path_l = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/'+ lst_folder[1] +'/csv_files/' + lst_folder[1] +'_E_IR_L_LIR.csv'


#df_r = Table.read(file_path_r, format="csv", delimiter="\t")
df_s = Table.read(file_path_s, format="csv") #, delimiter=";")
df_l = Table.read(file_path_l, format="csv")#, delimiter="\t")

##df_r = pd.read_csv(file_path_r)
# df_s = pd.read_csv(file_path_s)
# df_l = pd.read_csv(file_path_l)

#print(df_s.iloc[0])
#stop
v_mag_s = df_s['V_mag']
e_ir_s = df_s['E_IR']
m_j_k_s = df_s['M_J_K']
mean_s = np.mean(m_j_k_s)

v_mag_l = df_l['V_mag']
e_ir_l = df_l['E_IR']
m_j_k_l = df_l['M_J_K']
mean_l = np.mean(m_j_k_l)


print(np.max(e_ir_s))
## Premiere façon de representer:  x = V; y = E_IR; color = J-K
plt.figure(figsize=(11, 10))
plt.rcParams['font.size'] = '20' #change font size globally
plt.scatter(v_mag_s, e_ir_s, s = mean_s*150, c = m_j_k_s, cmap = 'inferno')
plt.scatter(v_mag_l, e_ir_l, s = mean_l*40, c = m_j_k_l, cmap = 'inferno')
plt.legend(["Study sample", "McDonald et al. 2012, 2017"], prop={'size': 20})
#plt.scatter(diff_pm, std_plus/mean, s=stat_plus*2.5, c=stat_plus, cmap = 'hsv_r')
cbar = plt.colorbar() #, ticks=range(0, len(mean), 3))
cbar.set_label('J-K mag', fontsize = 22, weight = 'bold')
plt.xlabel("Magnitude in V band", fontsize = 22, weight = 'bold')
#plt.xticks(fontsize = 20, weight = 'bold')
plt.ylabel("E_IR", fontsize = 22, weight = 'bold')
# #plt.ylabel("$\dfrac{\sigma}{mean}$", fontsize = 22, weight = 'bold')
# plt.yticks(fontsize = 20, weight = 'bold')
# plt.savefig('{}/std_vs_diff_vs_nb_FEROS.png'.format(sav_im, dpi=300, bbox_inches='tight'))
#plt.savefig('{}/stdmean_vs_diff_vs_nb1_FEROS.png'.format(sav_im, dpi=300, bbox_inches='tight'))
plt.savefig('/home/nbadolo/Bureau/Aymard/These/for_biblio_papers/plots/log_paper_plots/' + 'E_IR_f_V_J_K_magn.pdf', 
                dpi=100, bbox_inches ='tight')

plt.savefig('/home/nbadolo/Bureau/Aymard/These/for_biblio_papers/plots/log_paper_plots/' + 'E_IR_f_V_J_K_magn.png', 
                dpi=100, bbox_inches ='tight')
plt.show()
plt.close()
#%%
## deuxieme façon de representer:  x = V; y = E_IR; size = J-K N.B: no colorbar here
plt.figure(figsize=(11, 10))
plt.rcParams['font.size'] = '20' #change font size globally
plt.scatter(v_mag_s, e_ir_s, s = m_j_k_s*150, color='b')
plt.scatter(v_mag_l, e_ir_l, s = m_j_k_l*150, color ='gray')
plt.legend(["Study sample", "McDonald et al. 2012, 2017"], prop={'size': 20})
#plt.scatter(diff_pm, std_plus/mean, s=stat_plus*2.5, c=stat_plus, cmap = 'hsv_r')
#cbar = plt.colorbar() #, ticks=range(0, len(mean), 3))
#cbar.set_label('J-K mag', fontsize = 22, weight = 'bold')
plt.xlabel("Magnitude in V band", fontsize = 22, weight = 'bold')
#plt.xticks(fontsize = 20, weight = 'bold')
plt.ylabel("E_IR", fontsize = 22, weight = 'bold')
# #plt.ylabel("$\dfrac{\sigma}{mean}$", fontsize = 22, weight = 'bold')
# plt.yticks(fontsize = 20, weight = 'bold')
# plt.savefig('{}/std_vs_diff_vs_nb_FEROS.png'.format(sav_im, dpi=300, bbox_inches='tight'))
#plt.savefig('{}/stdmean_vs_diff_vs_nb1_FEROS.png'.format(sav_im, dpi=300, bbox_inches='tight'))
plt.savefig('/home/nbadolo/Bureau/Aymard/These/for_biblio_papers/plots/log_paper_plots/' + 'E_IR_f_V_J_K_magn2.pdf', 
                dpi=100, bbox_inches ='tight')

plt.savefig('/home/nbadolo/Bureau/Aymard/These/for_biblio_papers/plots/log_paper_plots/' + 'E_IR_f_V_J_K_magn2.png', 
                dpi=100, bbox_inches ='tight')
plt.show()
plt.close()