class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        new=[]
        for i in range (0,len(tokens)):
            if tokens[i] not in "+-*/":
                new.append(int(tokens[i]))
            else:
                b=new.pop()
                a=new.pop()

                if tokens[i]=="+":
                    res=a+b
                elif tokens[i]=="-":
                    res=a-b
                elif tokens[i]=="*":
                    res=a*b
                else:
                    res=int(a/b)
                new.append(res)
        return new.pop()


        