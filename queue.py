class arrayQueue():
    def __init__(ashu):
        ashu.queen=[]
        
    def enqueue(ashu,ganesh):
        return ashu.queen.append(ganesh)
    
    def deque(ashu):
        if not ashu.queen:
            return 'Queue is empty'
        ele=ashu.queen[0]
        ashu.queen=ashu.queen[1:]
        return ele
    
    def isEmpty(ashu):
        return not ashu.queen==[]
    
q1=arrayQueue()
q1.enqueue(18)
q1.enqueue(28)
print(q1.deque())
#print(q1.deque())
#print(q1.deque())
print(q1.isEmpty())
print(q1.queen)