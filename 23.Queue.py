class Queue:
    def __init__(self):
     self.lst=[]
    # end of constructor

    def append(self,n):
        self.lst.append(n)
    # end of append

    def pop(self):
        if len(self.lst)>0:
            return self.lst.pop(0)
    # end of pop

    # it will print all the lst values and will return in String
    def __repr__(self):
        return str(self.lst)
    # end of repr

    def isempty(self):
        return len(self.lst)==0
    # end of isempty

st=Queue()
st.append(10)
st.append(8)
st.append(12)
st.append(5)

print(st.isempty())
print(st) # it print object address
print(st.pop())
print(st.pop())