
def replacer(string, *args):
    c = ''
    for element in args:
        c+= string.replace(element,'')
        return c
a= "CREATE\\cf4  \\cf2 USER\\cf4  \\cf5 'limon_qa_user'\\cf4 @\\cf5 '*'\\cf4  IDENTIFIED \\cf2 BY\\cf4  \\cf5 'ienath0A aichee7P Nuca6sai'\\cf4 ;"
# print replacer(a, '\\cf4', '\\cf2', '\\cf5', '\cf2', '\cf5', '@\cf5')

def sqleditor(f):
    with open(f) as file:
        data = file.read()
        for el in data:
            replacer(el, '\\cf4', '\\cf2', '\\cf5', '\cf2', '\cf5', '@\cf5')
        return data
print sqleditor('/Users/mbilichenko/Documents/Untitled6.rtf')