import os
from collections import OrderedDict

def readFiles():
    key_values_txt={}
    for file in os.listdir(os.getcwd()):
        if file[-4:]==".txt" and file!="result.txt":
            with open(os.path.join(os.getcwd(),file)) as txt:
                space_result=txt.readlines()
                key_values_txt[len(space_result)]=space_result
                key_values_txt[len(space_result)]+=[str(file)]
    return key_values_txt


def createResult(dictValues):
    with open(os.path.join(os.getcwd(),"result.txt"),"w") as file:
        new_dict=OrderedDict(sorted(dictValues.items(), key=lambda t: t[0]))
        for key,values in new_dict.items():
            file.write(values[-1]+"\n")
            file.write(str(key)+"\n")
            for i in values:
                if i[-4:]==".txt":
                    continue
                else:
                    file.write(i)

createResult(readFiles())