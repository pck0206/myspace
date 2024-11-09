def ReadFile(FileName):
    file = open(FileName,'r',encoding = 'utf-8')
    return file
def Merge(File1,File2):
    Line1 = [line for line in File1 if line != '\n']
    Line2 = [line for line in File2 if line != '\n']
    Line1.extend(Line2)
    Line1.sort()
    lst = []
    for i in Line1:
        lst.append(i[2:])
    return lst
def Write(lst,File):
    with open(File,'w',encoding = " utf-8") as f:
        for i in lst:
            f.write(i)

if __name__=="__main__":
    File1 = "decode1.txt"
    File2 = "decode2.txt"
    File3 = "decode_text.txt"
    a = ReadFile(File1)
    b = ReadFile(File2)
    Write(Merge(a,b),File3)