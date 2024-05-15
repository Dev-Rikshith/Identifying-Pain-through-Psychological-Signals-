#Importing KFold to compute Cross Fold Validation
from sklearn.model_selection import KFold

#Import our classifier
from sklearn.linear_model import LogisticRegression


def CrossFoldValidation(data):
        
    # Instantiate Logistic Regression Model
    clf = LogisticRegression()
    
    #Preprocessed features and labels
    X = data[:, 1:]
    y = data[:, 0]

    # X = X.reshape(-1, 1)
    #Lists to store predictions and test-indices
    pred=[]
    test_indices=[]

    #Create a k-fold cross-validation splitter
    kf = KFold(n_splits = 10)

    for i, (train_index, test_index) in enumerate(kf.split(X)):
        #Train the classifier on the training data
        clf.fit(X[train_index], y[train_index])
        #Predict labels for the test data
        pred.append(clf.predict(X[test_index]))
        #Store the test indices for later evaluation
        test_indices.append(test_index)

    #Return predictions, test indices, and true labels
    return pred, test_indices, y

def FusionCrossFoldValidation(f_data, l_data):
        
    # Instantiate Logistic Regression Model
    clf = LogisticRegression()
    
    #Preprocessed features and labels
    X = f_data.astype(float)
    y = l_data

    # X = X.reshape(-1, 1)
    #Lists to store predictions and test-indices
    pred=[]
    test_indices=[]

    #Create a k-fold cross-validation splitter
    kf = KFold(n_splits = 10)

    for i, (train_index, test_index) in enumerate(kf.split(X)):
        #Train the classifier on the training data
        clf.fit(X[train_index], y[train_index])
        #Predict labels for the test data
        pred.append(clf.predict(X[test_index]))
        #Store the test indices for later evaluation
        test_indices.append(test_index)

    #Return predictions, test indices, and true labels
    return pred, test_indices, y