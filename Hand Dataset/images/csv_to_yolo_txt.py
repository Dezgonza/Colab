import pandas as pd
import numpy as np

dftrain = pd.read_csv(r"C:\Users\Hogar\Documents\GitHub\Colab\Hand Dataset\images\train\train_labels.csv")
dftest = pd.read_csv(r"C:\Users\Hogar\Documents\GitHub\Colab\Hand Dataset\images\test\test_labels.csv")

x = np.asanyarray(dftrain)
y = np.asanyarray(dftest)

def convert_labels(xmin, ymin, xmax, ymax):
    """
    Definition: Parses label files to extract label and bounding box
        coordinates.  Converts (x1, y1, x1, y2) KITTI format to
        (x, y, width, height) normalized YOLO format.
    """
    size = [720,1280]
    dw = 1./size[1]
    dh = 1./size[0]
    x = (xmin + xmax)/2.0
    y = (ymin + ymax)/2.0
    w = xmax - xmin
    h = ymax - ymin
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

for j in y:
    b=str(j[0])[:-4]
    a = open(r'C:\Users\Hogar\Documents\GitHub\Colab\Hand Dataset\images\bbox/'+b+'.txt','a')
    i = convert_labels(j[-4],j[-3],j[-2],j[-1])
    a.write('0 '+str(i[0])+' '+str(i[1])+' '+str(i[2])+' '+str(i[3])+'\n')
    a.close()
