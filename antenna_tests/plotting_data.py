#! /usr/bin/env python

import numpy as np, csv, matplotlib.pyplot as plt, sys

for file in sys.argv[1:]:
    f = open(file)
    csv_f = csv.reader(f)

    rowlist = []
    for row in csv_f:
        rowlist.append(row)
    
    test_type = str(rowlist[14][1])
    rowlist = rowlist[18:-1]
    
    x = np.array([r[0] for r in rowlist], dtype=np.float)
    y = np.array([r[1] for r in rowlist], dtype=np.float)
    
    print type(x), type(y)
    plt.plot(x/1e6, y, label=test_type+' '+file.replace('_', ' ').replace('.csv', ' ').replace('S22', '').replace('DB', '').replace('PH', '').replace('RL', 'resistive load').replace('SC', 'short cable'))
    if 'DB' in file:
        plt.xlabel('frequency (MHz)')
        plt.ylabel('log magnitude (dB)')
        plt.legend(loc='lower right')
    elif 'PH' in file:
        plt.xlabel('frequency (MHz)')
        plt.ylabel('phase (deg)')
        plt.legend(loc='lower right')

plt.show()
