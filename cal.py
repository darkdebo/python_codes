
from functools import reduce
class simplecalculator:
    def __init__(self, *args):
        self.args=args

    def add(self):
        return sum(self.args)

    def mul(self):
        m=1
        for i in self.args:
            m*=i
        return m 
    def div(self):
        return reduce(lambda a,b:a/b,self.args)

    def sub(self):
        return reduce(lambda a,b:a-b,self.args)


s=simplecalculator(1,2)

print('addition',s.add(),'multiplication',s.mul(),'division',s.div(),'sub',s.sub())

                        