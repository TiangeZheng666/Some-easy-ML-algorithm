# this part I will make a decision tree (DT)
#the main idea is the dictionary and entropy
#well, I can not find an appropriate dataset
#So if you have some,that's so kind of you 
#if you can send it to me.

from math import log
# Shannon Entropy: l(x) = log(p(x))




class DT:
    def __init__(self) -> None:
        
        #make a dataset by the book by Peter Harrington
        self.dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
        self.labels = ['no surfacing','flippers']
        self.dic = {'no surfacing' : 0,'flippers':0}
        self.tree = {}
    #get Shannon entropy
    def get_entropy(self):
        index = 0
        for i in self.dic.keys():
            t_ = 0.0
            f_ = 0.0
            for item in self.dataSet:
                if item[index] == 1:
                    t_+=1
                else:
                    f_+=1
            entropy = 0.0
            entropy -= log(t_/len(self.dataSet),2)
            entropy -= log(f_/len(self.dataSet),2)
            self.dic[i] = entropy
            index += 1

    #get the most important info and pop it
    def get_max_entropy(self):
        max = ""
        max_entropy = 0.0
        index = 0
        i = 0
        for key in self.dic.keys():
            if max_entropy<self.dic[key]:
                max_entropy = self.dic[key]
                index = i
                max = key
            i+=1
        self.dic.pop(max)
        return (max,index)
    def get_data(self):
        return self.dataSet

#make a tree in a recursion
def add_tree(Dt,name,index,dic,data):
    if Dt.dic:
        dic[name] = {1:{},0:{}}
        newname,newindex=Dt.get_max_entropy()
        newdata1 = []
        newdata0 = []
        for line in data:
            if line[index] ==1:
                newdata1.append(line)
            else:
                newdata0.append(line)
        dic[name][1] = add_tree(Dt,newname,newindex,dic[name][1],newdata1)
        dic[name][0] = add_tree(Dt,newname,newindex,dic[name][0],newdata0)
    else:
        dic[name] = {1:[],0:[]}
        for line in data:
            if line[index] == 1:
                dic[name][1].append(line[len(line)-1])
            else:
                dic[name][0].append(line[len(line)-1])        
    return dic
if __name__=='__main__':

    a = DT()
    a.get_entropy()
    max,index=a.get_max_entropy()
    dic = {}
    dic = add_tree(a,max,index=index,dic=dic,data=a.get_data())

#we can judge according to the dic, of course,
#we can make the yes to a number or a probability
#but I didn't do in this way
    print(dic)