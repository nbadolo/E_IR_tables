#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 08:36:42 2023

@author: fbado
"""

###plot2
plt.figure(figsize=(11, 10))
plt.rcParams['font.size'] = '20' #change font size globally
plt.scatter(diff_pm, std_plus, s=stat_plus*2.5, c=stat_plus, cmap = 'hsv')
#plt.scatter(diff_pm, std_plus/mean, s=stat_plus*2.5, c=stat_plus, cmap = 'hsv_r')
cbar = plt.colorbar(extend='max', ticks=range(0, len(mean), 3))
cbar.set_label('Number of stars', fontsize = 22, weight = 'bold')
plt.xlabel("$max_{Vbroad} - min_{Vbroad}$ (km/s)", fontsize = 22, weight = 'bold')
plt.xticks(fontsize = 20, weight = 'bold')
plt.ylabel("$\sigma$ (km/s)", fontsize = 22, weight = 'bold')
#plt.ylabel("$\dfrac{\sigma}{mean}$", fontsize = 22, weight = 'bold')
plt.yticks(fontsize = 20, weight = 'bold')
plt.savefig('{}/std_vs_diff_vs_nb_FEROS.png'.format(sav_im, dpi=300, bbox_inches='tight'))
#plt.savefig('{}/stdmean_vs_diff_vs_nb1_FEROS.png'.format(sav_im, dpi=300, bbox_inches='tight'))
plt.show()
plt.close()