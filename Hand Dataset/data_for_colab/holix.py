file =  open('test.txt', 'r')
file1 =  open('test1.txt', 'w')
k = '/content/Colab/HandDataset/data_for_colab/data'
for i in file:
    file1.write(k + i[i.index('data/')+4:])
