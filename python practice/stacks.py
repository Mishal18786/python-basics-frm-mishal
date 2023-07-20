class stack():
    
    def __init__(self):
        self.list_stack = []
        
    def is_empty(self):
        if not self.list_stack:
            return True
        else:
            return False
        
    def push(self,item):
        self.list_stack.append(item)
    
    def pop(self):
        return self.list_stack.pop()
    
    def peek(self):
        if self.list_stack == []:
            return None
        else:
            return self.list_stack[-1]
            
    def __repr__(self):
        return  repr(self.list_stack)
    
# st = stack()
# new = st.is_empty()
# print(new)

# st.push(50)
# st.push(60)
# print(st)

# p = st.peek()
# print(p)
# a = st.pop()
# print(a)

'''challenge   {[()]} '''

def brack(s):
    stack = []
    
    bb = {'(':')' , '[':']' , '{':'}' }
    
    for char in s:
        
        if char is bb.keys():
            stack.append(char)
        else:
            if len(stack) == 0 or bb[stack.pop()] != char:
                return False
            
    return len(stack) == 0
     
string = '[[({})]]'
          
print(brack(string))

string2 = '(([)][]'

print(brack(string2))

            
            
            
            
            
            