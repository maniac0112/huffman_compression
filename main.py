class Node:
    def __init__(self,val=0):
        self.val=val
        self.frequency=None
        self.parent=None
        self.left=None
        self.right=None
        self.path=None

def compare(a,b):
    if a[1]>b[1]:
        return 1
    elif a[1]==b[1]:
        return 0
    else:
        return -1
        
def constructTree(s):
    D={} #initializing a dictionary
    #D stores (key,value) i.e (character,frequency)
    for i in s:
        if i in D:
            D[i]+=1
        else:
            D[i]=1
    #now we have a dictionary with all the (char,freq) in O(len(s)) time
    A=[] 
    for key in D:
        node=Node()
        node.val=key
        node.frequency=D[key]
        node.isLeaf=True
        D[key]=node
        A.append(node)
    while(len(A)>1):
        A=sorted(A,key=lambda x: x.frequency)
        first=A[0]
        second=A[1]
        combine=Node()
        combine.left=first
        combine.right=second
        combine.frequency=first.frequency+second.frequency
        first.parent=combine
        second.parent=combine
        A.remove(first)
        A.remove(second)
        A.append(combine)
    
    return (A[0],D)        

def compress(x):
    root,D=constructTree(x)
    for keys in D:
        s=""
        curr=D[keys]
        while(curr!=None):
            if curr.parent!=None:
                if curr.parent.left==curr:
                    s+=str(0)
                else:
                    s+=str(1)
            curr=curr.parent
        D[keys].path=s[::-1]
    #now D stores all letters and their codes!
    compressed=""
    for i in x:
        compressed=compressed+D[i].path
    return (compressed,D)

x,keys=compress("bcaadddccacacac")
print(x)
    
def extract(x,keys):
    extracted=""
    root=Node()
    for key in keys:
        curr=keys[key]
        while(curr.parent!=None):
            curr=curr.parent
            root=curr
        if curr.parent==None:
            break
    curr=root
    for i in x:
        if i==str(0):  
            curr=curr.left
        if i==str(1):
            curr=curr.right
        if (curr.path!=None):
            extracted+=curr.val
            curr=root
               
    return extracted

print(extract(x,keys))

        

