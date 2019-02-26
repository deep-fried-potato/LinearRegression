import random

class DataPoint:
    def __init__(self,attributes):
        self.attributes= [1] + attributes[:-1]
        self.value = attributes[-1]
        def __str__(self):
            return str(self.attributes) + " : " +str(self.value)

def dotprod(K, L):
    if len(K) != len(L):
        return 0
    return sum(i[0] * i[1] for i in zip(K, L))

def addlists(list1,list2):
    return [x1+x2 for (x1,x2) in zip(list1,list2)]

def subtract(List1,List2):
    return [x1 - x2 for (x1, x2) in zip(List1, List2)]

def scalarprod(scalar,vector):
    return [scalar*element for element in vector]

def MSE_cost(DataSet,weights):
    result=0
    for point in DataSet:
        result += (dotprod(point.attributes,weights)-point.value)**2
    return result/(2*len(DataSet))


def gradient(DataSet,weights):
    result = [0]*len(DataSet[0].attributes)
    for point in DataSet:
        result=addlists(result,scalarprod((dotprod(point.attributes,weights) - point.value),point.attributes))
    return scalarprod(1/len(DataSet),result)





fileobj = open("yacht_hydrodynamics.data","r")
filedata = fileobj.readlines()
DataSet = [DataPoint([float(x) for x in line.split()]) for line in filedata if line.split()!=[]]
random.shuffle(DataSet)

TrainSize=200
eta=0.03
TrainingSet = DataSet[:TrainSize]
TestSet= DataSet[TrainSize:]

weights = [0]*len(DataSet[0].attributes)

epoch=0
while MSE_cost(TrainingSet,weights)>10:
    weights = subtract(weights,scalarprod(eta,gradient(TrainingSet,weights)))
    if epoch%100==0:
        print("Iteration: ",epoch," MSE Error: ",MSE_cost(TrainingSet,weights),"Weights :",weights,end="\r" )
    epoch+=1
