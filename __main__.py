#如果外部 python文件 引用，需要将此文件名__main__修改下,否则和系统冲突

def getvalue(a):
    return a+ 1;

if __name__ == '__main__':
    b=10;
    print (getvalue(b))
    print('程序自身在运行')
else:
    print('我来自另一模块引用')
