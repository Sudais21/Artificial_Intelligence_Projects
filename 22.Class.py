class Stack:
    def __init__(self):
     self.lst=[]
    # end of constructor

    def append(self,n):
        self.lst.append(n)
    # end of append

    def pop(self):
        return self.lst.pop()
    # end of pop

    # it will print all the lst values and will return in String
    def __repr__(self):
        return str(self.lst)
    # end of repr

    def isempty(self):
        return len(self.lst)==0
    # end of isempty

st=Stack()
st.append(10)
st.append(8)
st.append(12)
st.append(5)

print(st.isempty())
print(st) # it print object address
print(st.pop())
print(st.pop())





