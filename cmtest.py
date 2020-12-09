import convert as c

test=0

if test==0:
    RGB=c.HLS_to_RGB(10,0.5,1)
    RGB=map(lambda x:x*255, RGB)
    print(c.RGB_to_colorcode(RGB))