class DataPoint:
    def __init__(self,attributes):
        self.attributes= [1] + attributes
    def __str__(self):
        return str(self.attributes)

fileobj = open("yacht_hydrodynamics.data","r")
filedata = fileobj.readlines()
DataSet = [DataPoint([float(x) for x in line.split()]) for line in filedata if line.split()!=[]]

for point in DataSet:
    print(point)
