#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:11:16 2023

@author: nbadolo
"""


#import aspose.Cells as aw

import os
import  jpype     
import  asposecells     
#jpype.startJVM() 
from asposecells.api import Workbook
import glob # pour changer l'extension des fichiers
import pandas as pd 
import shutil # pour les copies de fichiers et de repertoires
#%%
# file_path1 = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/AC_Cet.txt'
# file_path2 = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/AC_Cet.ods'

## sample stars
path_sed1 = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/sample_stars/sed/'
path_sed2 = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/sample_stars/folder_sed/'
path_txt = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/sample_stars/folder_txt/'
path_csv = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/sample_stars/folder_csv/'

## large table
# path_sed1 = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/large_table_stars/sed/'
# path_sed2 = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/large_table_stars/folder_sed/'
# path_txt = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/large_table_stars/folder_txt/'
# path_csv = '/home/nbadolo/Bureau/Aymard/Donnees_sph/pyssed_log/large_table_stars/folder_csv/'

#%%
## copie des fichier avant leur modification
lst_sed = os.listdir(path_sed1)
print(lst_sed)
n_lst_sed1 = len(lst_sed)
print(n_lst_sed1)

for filename in os.listdir(path_sed2) : # netoye le repertoire avant la copie 
    os.remove(path_sed2 + "/" + filename)
print(os.listdir(path_sed2))

for fic in os.listdir(path_sed1):
    shutil.copy2(os.path.join(path_sed1, fic),path_sed2) #copie du repertoire 1 dans 2
    
print(os.listdir(path_sed2))

for filename in os.listdir(path_txt) : # netoye le repertoire avant la copie 
    os.remove(path_txt + "/" + filename)
print(os.listdir(path_txt))   

for fic in os.listdir(path_sed2):
    shutil.copy2(os.path.join(path_sed2, fic), path_txt) #copie du repertoire 1 dans 2#copie du repertoire sed2 dans txt
print(os.listdir(path_txt))

## conversion en format txt
lst_sed2 = glob.glob(os.path.join(path_txt, "*.sed")) 
n_lst_sed2 = len(lst_sed2) 
for i in range(n_lst_sed2) :  
    build_txt = os.path.splitext(lst_sed2[i])[0] + ".txt" # separation de sed et ajout de l'extension txt
    #build_txt.save(path_sed2)
    txt_file = os.rename(lst_sed2[i], build_txt)  # remplacement du fichier .sed par le fichier .txt
print(os.listdir(path_txt))

## conversion en format csv
lst_txt = glob.glob(os.path.join(path_txt, "*.txt"))
n_lst_txt = len(lst_txt)
# for i in range(n_lst_txt) and fic in os.listdir(path_txt):
#     star_name = os.path.splitext(lst_txt[i])[0]
#     print(star_name)
#     print(fic)
#     stop
#     file_txt = pd.read_csv(lst_txt[i], delimiter = ';') # ouverture du fichier txt avec csv
#     file_csv = file_txt.to_csv(path_csv + star_name+'.csv', index = None) # creation du fichier csv
#     stop


for fic in os.listdir(path_txt) :
    star_name = os.path.splitext(fic)[0]
    
    # stop
    file_txt = pd.read_csv(path_txt +fic, delimiter = ';') # ouverture du fichier txt avec csv
    file_csv = file_txt.to_csv(path_csv + star_name+'.csv', index = None) # creation du fichier csv
    print(file_txt)   
print(os.listdir(path_csv))
print(str(len(os.listdir(path_csv))) + ' tables sed ont été converties en tables csv')
#jpype.shutdownJVM()
