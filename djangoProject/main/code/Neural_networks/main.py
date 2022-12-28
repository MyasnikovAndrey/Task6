import pandas as pd

from n_network import training


def print_hi(name):
    tempAr = ['Java', 'PY', 'Web', 'Unity', 'IT', 'administrator', 'crypto', 'Gaming', 'Frontend', 'DevOps', 'QA', 'mobile', 'DEX', 'Design', 'Math', 'Fullstack', 'JS', 'InfSec', 'SQL', 'Service', 'C++', 'NodeJS', 'NoCode', 'Pascal', 'OS', 'Data', '1C', 'Software', 'C#', 'AWS', 'ML', 'Golang', 'PHP', 'Backend', 'VR']
    #print(tempAr)
    Frontend = [tempAr[2], tempAr[8], tempAr[13], tempAr[15], tempAr[16]]
    Backend = [tempAr[0], tempAr[1], tempAr[15], tempAr[18], tempAr[20], tempAr[21], tempAr[28], tempAr[31], tempAr[32], tempAr[33]]
    easy = [tempAr[1], tempAr[2], tempAr[22], tempAr[23]]
    sql = [tempAr[18]]
    qa = [tempAr[10]]
    DataS = [tempAr[1], tempAr[14], tempAr[25]]
    SysAdmin = [tempAr[5],tempAr[9],tempAr[17]]
    print(Frontend)
    print(Backend)
    print(easy)
    print(len(tempAr))

    training()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
