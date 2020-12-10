from color import convert as c
import numpy as np

def make_RGB_along_L(H, dL):
    RGBL=list()
    L=0
    for i in range(int(1/dL)+1):
        RGB=c.HLS_to_RGB(H,L,1)
        RGB=map(lambda x:x*255, RGB)
        RGBL.append(c.RGB_to_colorcode(RGB))
        L+=dL

    return RGBL

def make_RGB_along_L2(H, dL):
    RGBL=list()
    L=0
    for i in range(int(1/dL)+1):
        RGB=c.HLS_to_RGB(H,L,1)
        RGBL.append(RGB)
        L+=dL

    return RGBL

def make_RGB_L_vs_I(H, dL):
    LI=np.ndarray([0,2])
    L=0
    for i in range(int(1/dL)+1):
        RGB=c.HLS_to_RGB(H,L,1)
        LI=np.vstack((LI, np.array([[L,c.RGB_to_intensity(RGB)]])))
        L+=dL

    return LI

def make_RGBI_along_L(H, dL):
    RGBIL=list()
    L=0
    for i in range(int(1/dL)+1):
        RGBIL.append(c.HLS_to_RGBIL(H,L,1))
        L+=dL

    return RGBIL

def make_RGB_along_I(RGBIL, dI):
    RGB=list()
    #RGB.append([0,0,0,0])
    RGB.append([0,0,0])
    I=dI
    j=0
    for i in range(1,int(1/dI)):
        get=1
        while get:
            if RGBIL[j][3]<= I < RGBIL[j+1][3]:
                RGBj = RGBIL[j]
                RGBjp = RGBIL[j+1]
                rate = ( I - RGBj[3] ) / ( RGBjp[3] - RGBj[3] )
                R= rate * ( RGBjp[0] - RGBj[0] ) + RGBj[0]
                G= rate * ( RGBjp[1] - RGBj[1] ) + RGBj[1]
                B= rate * ( RGBjp[2] - RGBj[2] ) + RGBj[2]
                L= rate * ( RGBjp[4] - RGBj[4] ) + RGBj[4]
                #RGB.append([R, G, B,L])
                RGB.append([R, G, B])
                get=0
            else: j+=1
        I+=dI
    #RGB.append([1,1,1,1])
    RGB.append([1,1,1])

    return RGB

def make_RGB_from_HI(H,I):
    RGBIL = make_RGBI_along_L(H, 0.0001)


    RGB=list()
    j=0
    get=1
    while get:
        if RGBIL[j][3]<= I < RGBIL[j+1][3]:
            RGBj = RGBIL[j]
            RGBjp = RGBIL[j+1]
            rate = ( I - RGBj[3] ) / ( RGBjp[3] - RGBj[3] )
            R= rate * ( RGBjp[0] - RGBj[0] ) + RGBj[0]
            G= rate * ( RGBjp[1] - RGBj[1] ) + RGBj[1]
            B= rate * ( RGBjp[2] - RGBj[2] ) + RGBj[2]
            L= rate * ( RGBjp[4] - RGBj[4] ) + RGBj[4]
            RGB.append([R, G, B,L])
            get=0
        else: j+=1

    return RGB