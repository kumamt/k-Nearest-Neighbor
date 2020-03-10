
# coding: utf-8

# In[22]:


#Computational Intelligence II prerequisite
#k-Nearest Neighbour Algorithm implementation in Python
#python Version 3

#Amit Kumar MA16W1-M
#Wasif Siddiqui MA16W1-M
import csv #imports the data set and displays it with Comma Seperated Values
with open(r'C:\Users\AMIT\Desktop\Project\TrainingSamplesLabeled.csv') as csvfile:
    lines =csv.reader(csvfile)
    for row in lines:
        print(', '.join(row))
    


# In[23]:


#This function is to load the data set and splits it into Training set and Test set.
import csv
import random
def loadDataSet(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1): #len(dataset) calculates the the total number of data, this loops runs till the range of(lengths-1).
	        for y in range(6): # as we have 7 dimentional data so we run the loop for range=6
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split: #till we reach the percentage of spilt it appends the value of dataSet into trainingSet array.
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x]) #as soon 80% data is in trainigSet, it adds the dataSet in Testdata array.


# In[24]:


#This Function finds the Euclidean distance between two data points.
import math
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance+= pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)


# In[25]:


#This function finds the Neighbours of testInstance after sorting them by using distance as the factor.
import operator
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist= euclideanDistance(testInstance, trainingSet[x], length) #calclates the distance
		distances.append((trainingSet[x], dist)) #appends the distance
	distances.sort(key=operator.itemgetter(1))#sorts the distance into ascending order
	neighbors= [] #declaration of neighbour array
	for x in range(k):
		neighbors.append(distances[x][0])#for all neighbour which are in range of k=17, the neighbour array is updates with those data points.
	return neighbors


# In[26]:


import operator
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]


# In[27]:


#calculates the accuracy of this kNN model.
def getAccuracy(testSet, predictions):
	correct= 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0


# In[28]:


def main():
    #preparing data
    trainingSet=[] #array of training set data
    testSet=[] #array of test set data 
    split=0.80 #split percentage as defined is 80%
    loadDataSet(r'C:\Users\AMIT\Desktop\Project\TrainingSamplesLabeled.csv', split, trainingSet, testSet) #calling the loadDataSet which seperates trainingSet and testSet into their respective variables.
    print('Train '+repr(len(trainingSet))) #prints the random 80% of Training set data 
    print('Test '+repr(len(testSet)))#prints the randon 20% of left data as Test set data
    predictions=[] #declared an array for predictions
    k=17 
    for x in range(len(testSet)): #here we are testing the testSet with the training set using the Euclidean Distance to get neighbours
        neighbors = getNeighbors(trainingSet, testSet[x], k)#calling getNeighbours function
        result = getResponse(neighbors)
        predictions.append(result)
        print('> Predicted=' + repr(result)+ ', actual=' +repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
main()

