def solution(l):
    class_list = [Version(num) for num in l]
    class_list.sort()
    out_list = [c.toString() for c in class_list]
    return out_list

class Version:
    def __init__(self, number):
        split = number.split(".")
        self.major = split[0]
        self.minor = split[1] if len(split)>1 else ""
        self.revision = split[2] if len(split)>2 else ""

    def toString(self):
        m_dot = "." if self.minor !="" else ""
        r_dot = "." if self.revision != "" else ""
        return self.major+m_dot+self.minor+r_dot+self.revision

    def __lt__(self, other):
        return self.compare(other)==1

    def __gt__(self,other):
        return self.compare(other)==-1

    def __le__(self,other):
        return self.compare(other)>=0

    def __ge__(self,other):
        return self.compare(other)<=0

    def __eq__(self,other):
        return self.compare(other)==0

    def compare(self, other):
        major_check = check(self.major, other.major)
        if (major_check!=0):
            return major_check
        minor_check = check(self.minor, other.minor)
        if (minor_check!=0):
            return minor_check
        revision_check = check(self.revision, other.revision)
        return revision_check
        
def check(n1,n2):
    int_n1 = int(n1) if n1!="" else 0
    int_n2 = int(n2) if n2!="" else 0
    if (n1==n2):
        return 0
    elif (int_n1>int_n2):
        return -1
    elif (int_n1<int_n2):
        return 1
    elif (n1==""):
        return 1
    elif (n2==""):
        return -1

if __name__ == "__main__":
    list1 = ["1.11","2.0.0","1.2","2","0.1","1.2.1","1.1.1","2.0"]
    list2 = ["1.1.2","1.0","1.3.3","1.0.12","1.0.2"]
    print(solution(list1))
    print(solution(list2))
