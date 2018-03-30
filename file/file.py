file = open('/Users/wutianlong/PycharmProjects/python_demos/file/test_file.xml','w')

file.write('wutianlong')
file.write('\n')
file.write('yanruixue')
file.write('\n')

file.close()




file = open('test_file.xml','r')
for line in file.readlines():
    print (line)

file.close
