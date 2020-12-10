from color import convert as c
from color import plot as p
import util as u
import numpy as np
import make_RGB as m


sw=9
#0 : plot colormap depend on H and L
#1 : plot Intensity depend on H and L
#2 : plot colormap depend on H and Intensity
#3 : plot Intensity depend on H and Intensity
#4 : plot Intensity depend on H and L (RGB is converted to Intensity)
#5 : plot colormap depend on H (L is 0.5, S is 1)
#6 : plot Intensity depend on H (L is 0.5, S is 1)
#7 :
#8 :
#9 : confirm colorcode

H=0
dH=1
dL=0.1
dI=0.1

if sw==0:#plot colormap depend on H and L
    RGBL=list()
    while H < 360:
        RGBL.append(m.make_RGB_along_L(H, dL))
        H+=dH

    p.show_colormap(RGBL,0)
elif sw==1: #plot Intensity depend on H and L
    while H < 360:
        if H==0:
            LI=m.make_RGB_L_vs_I(H, dL)
        else:
            LI=np.hstack((LI,m.make_RGB_L_vs_I(H, dL)[:,1][:,np.newaxis]))
        H+=dH

    print(LI.shape)
    u.plot_LI(LI)
elif sw==2: #plot colormap depend on H and Intensity
    RGBH=list()
    while H < 360:
        RGBIL=m.make_RGBI_along_L(H,dL)
        RGBH.append(m.make_RGB_along_I(RGBIL, dI))
        H+=dH

    p.show_colormap(RGBH,0)
elif sw==3:#plot Intensity depend on H and Intensity
    while H < 360:
        II = np.ndarray([0, 2])
        RGBIL=m.make_RGBI_along_L(H,dL)
        RGBH=m.make_RGB_along_I(RGBIL, dI)
        I=0
        for RGB in RGBH:
            II = np.vstack((II, np.array([[I, c.RGB_to_intensity(RGB)]])))
            I+=dI
        if H==0:
            IIH=II
        else:
            IIH=np.hstack((IIH,II[:,1][:,np.newaxis]))
        H+=dH

    print(IIH.shape)
    u.plot_LI(IIH)
elif sw==4: #plot Intensity depend on H and L (RGB is converted to Intensity)
    while H < 360:
        II = np.ndarray([0, 2])
        RGBIL=m.make_RGBI_along_L(H,dL)
        RGBH=m.make_RGB_along_I(RGBIL, dI)
        I=0
        for RGB in RGBH:
            II = np.vstack((II, np.array([[I, RGB[3]]])))
            I+=dI
        if H==0:
            IIH=II
        else:
            IIH=np.hstack((IIH,II[:,1][:,np.newaxis]))
        H+=dH

    print(IIH.shape)
    u.plot_LI(IIH)
elif sw==5:#plot colormap depend on H (L is 0.5, S is 1)
    RGBH=list()
    while H <= 360:
        RGBH.append(c.HLS_to_RGB(H, 0.5, 1))
        H+=dH

    p.show_colormap(RGBH,1)
elif sw==6: #plot Intensity depend on H (L is 0.5, S is 1)
    HI=np.ndarray([0, 2])
    while H <=360:
        HI=np.vstack((HI, np.array([[H, c.RGB_to_intensity(c.HLS_to_RGB(H, 0.5, 1))]])))
        H+=dH

    print(HI.shape)
    u.plot_HI(HI)
elif sw==7:
    RGB=c.HLS_to_RGB(10,0.5,1)
    RGB=map(lambda x:x*255, RGB)
    print(c.RGB_to_colorcode(RGB))
elif sw==8:
    dH=30
    H = 0

    while H<360:
        p.make_image(H)
        H+=dH
elif sw==9:
    C1=c.HLS_to_RGB(210, 0.5, 1)
    p.make_image(210,0.5,1)
    C2=c.HLS_to_RGB(300, 0.5, 1)
    p.make_image(300,0.5,1)
    I1=c.RGB_to_intensity(C1)
    I2=c.RGB_to_intensity(C2)
    white=c.RGB_to_intensity([1,1,1])
    print(C1,C2,I1,I2,(I1+I2)/2,white)
    RGBL=m.make_RGB_from_HI(210, (I1+I2)/2)
    print(RGBL)
    RGBL=m.make_RGB_from_HI(300, (I1+I2)/2)
    print(RGBL)
elif sw==10:
    RGB=c.HLS_to_RGB(10,0.5,1)
    RGB=map(lambda x:x*255, RGB)
    print(c.RGB_to_colorcode(RGB))