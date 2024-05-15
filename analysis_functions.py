#Importing the necessary metric functions needed 
from sklearn.metrics import precision_score, recall_score, accuracy_score
from sklearn.metrics import confusion_matrix

#Function to print the confusion matrix
def PrintEvalMetrics(pred, indices, y):
    #Manually merge predictions and testing labels from each of the folds to make confusion matrix
    finalPredictions = []
    groundTruth = []

    for p in pred:
        #Extend the final predictions list with predictions from each fold
        finalPredictions.extend(p)
    for i in indices:
        #Extend the ground truth list with labels from each fold
        groundTruth.extend(y[i])

    #Compute and print the confusion matrix
    print(confusion_matrix(finalPredictions, groundTruth))

    #Compute and print precision-score, recall-score, and accuracy-score
    print("Precision: ", precision_score(groundTruth, finalPredictions, average='macro'))
    print("Recall: ", recall_score(groundTruth, finalPredictions, average='macro'))
    print("Accuracy: " , accuracy_score(groundTruth, finalPredictions))