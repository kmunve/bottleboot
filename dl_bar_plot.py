# -*- coding: utf-8 -*-
__author__ = 'kmu'

import matplotlib
matplotlib.use('Agg')
import numpy as np
import pylab as plt

def bar_plot(dates, values, title="", filename="danger_level", media_path=r"/home/karsten/mysite/media/"):

    distr = np.bincount(values)

    DL_labels = ['0 - no rating', '1 - low', '2 - moderate', '3 - considerable', '4 - high', '5 - very high']
    DL_colors = ['0.5', '#ccff66', '#ffff00', '#ff9900', '#ff0000', 'k']

    fsize = (16, 10)
    fig = plt.figure(figsize=fsize)

    colors = []
    for n in values:
        if n == 1:
            colors.append(DL_colors[1])
        elif n == 2:
            colors.append(DL_colors[2])
        elif n == 3:
            colors.append(DL_colors[3])
        elif n == 4:
            colors.append(DL_colors[4])
        elif n == 5:
            colors.append(DL_colors[5])
        else:
            colors.append(DL_colors[0])

    ax = plt.axes([.15, .05, .8, .9])
    ax.bar(dates, values, color=colors)

    plt.yticks(range(len(DL_labels)), DL_labels)#, size='small')
    plt.xlabel('Date')
    plt.ylabel('Danger level')
    plt.title(title)


    # this is an inset axes over the main axes
    afrac = 0.2
    bfrac = (float(fsize[0])/float(fsize[1])) * afrac
    apos = 0.95-afrac
    bpos = 0.95-bfrac
    a = plt.axes([apos, bpos, afrac, bfrac])

    a.pie(distr, colors=DL_colors, autopct='%1.0f%%', shadow=False)
    plt.setp(a, xticks=[], yticks=[])

    plt.savefig(media_path+filename+"_thumb.png", dpi=90)
    plt.savefig(media_path+filename+".png", dpi=300)
    plt.savefig(media_path+filename+".pdf", dpi=600)
    plt.close(fig)
