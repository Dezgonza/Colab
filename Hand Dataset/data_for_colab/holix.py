file =  open('train.txt', 'r')
file1 =  open('train1.txt', 'w')
k = '/content/darknet/data_for_colab/data/'
for i in file:
    file1.write(k + i[i.index('/')+1:])
