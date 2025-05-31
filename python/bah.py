
def nested_thingy():
    for i in range(5):
        for j in range(5):
            print(i+j, end="")
        print()

def pal(string):
    if len(string) <= 1:
        return True
    
    if string[0] == string[-1]:
        return pal(string[1:][:-1])
    else:
        return False
    
print(pal("tacocat"))

nested_thingy()