from matplotlib import pyplot as plt
import csv
import make_RGB as m

def show_colormap(colorlist):
    nh=len(colorlist) #num Hue
    nl=len(colorlist[0]) #num Lightness
    fig = plt.figure()

    i=1
    for cl in colorlist:
        for c in cl:
            plt.subplot(nh, nl, i, facecolor=c)
            plt.tick_params(labelbottom=False,
                           labelleft=False,
                           labelright=False,
                           labeltop=False,
                           bottom=False,
                           left=False,
                           right=False,
                           top=False)
            i+=1

    plt.show()

def plot_LI(LI):

    fig = plt.figure()

    p=1
    for i in range(6):
        plt.subplot(3, 2, i+1)
        plt.grid()
        for j in range(6):
            plt.plot(LI[:,0], LI[:,p], '-o', label='theta='+str(10*(p-1)), linewidth=0.5, markersize=6)
            plt.legend()
            p+=1
        i+=1

    plt.show()

def plot_HI(HI):

    fig = plt.figure()

    plt.tick_params(labelbottom=False,
                    labelleft=False,
                    labelright=False,
                    labeltop=False,
                    bottom=False,
                    left=False,
                    right=False,
                    top=False)

    yrange=[float(i / 10.0) for i in range(0, 11, 1)]
    print(yrange)

    ax1 = fig.add_subplot(111, xticks=range(0,390,30), yticks=yrange)

    ax1.plot(HI[:, 0], HI[:, 1], '-', linewidth=5)
    plt.xlim(0, 360)
    plt.ylim(0, 1)

    plt.grid()

    plt.show()

def save_list(l,path):

    with open(path, "w") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(l)

def show_colormap2(colorlist):
    nl=len(colorlist) #num Hue
    fig = plt.figure()
    plt.subplots_adjust(wspace=0)

    i=1
    for cl in colorlist:
        plt.subplot(1, nl, i, facecolor=cl)
        plt.tick_params(labelbottom=False,
                       labelleft=False,
                       labelright=False,
                       labeltop=False,
                       bottom=False,
                       left=False,
                       right=False,
                       top=False)
        i+=1

    plt.show()

def make_RGB_for_R():

    sw = 0  # 0:dL 1:dI
    H = 0
    dH = 30
    dL = 0.01
    dI = 0.01

    if sw == 0:
        while H < 360:
            RGBL = m.make_RGB_along_L2(H, dL)
            save_list(RGBL, "HL" + str(int(H)) + ".csv")
            H += dH
    elif sw == 1:
        while H < 360:
            RGBIL = m.make_RGBI_along_L(H, dL)
            RGBI = m.make_RGB_along_I(RGBIL, dI)
            save_list(RGBI, "HI" + str(int(H)) + ".csv")
            H += dH
