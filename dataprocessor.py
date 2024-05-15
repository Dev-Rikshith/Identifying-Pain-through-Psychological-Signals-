# Import required default libraries
import statistics
import csv

# Import data preprocessing libraries
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Declare lists for storing the features belonging to each data_type
dia = []
syst = []
eda = []
res = []
all = []

# Function to read the data from CSV and send it to computation and processing 
def data_reader(data_file):
    # Reading of the data
    with open(data_file+".csv") as file:
        data = csv.reader(file)
        # Iterating over the data to create hand crafted features
        for row in data:
            numbers = convert_to_numbers(row[3:])
            # Computes mean, variance, min and max with the data provided in the file
            mean, variance, min, max = compute_metrics(numbers)
            final_row = []
            final_row.append(row[0])
            final_row.append(row[1])
            final_row.append(row[2])
            final_row.append(mean)
            final_row.append(variance)
            final_row.append(min)
            final_row.append(max)
            #Segregates data into respective datatype arrays
            build_data(final_row)

    # Returns the datatype arrays in the format of np arrays
    return np.array(dia), np.array(syst), np.array(eda), np.array(res), np.array(all)

# Function to convert strings to floats
def convert_to_numbers(str_list):
    return [float(x) for x in str_list]

# Function to calculate mean, variance, min and max
def compute_metrics(numbers):
    # Return None if empty
    if not numbers:
        return None, None, None, None
    
    mean = round(statistics.mean(numbers), 5)
    variance = round(statistics.variance(numbers), 5)
    minimum = min(numbers)
    maximum = max(numbers)
    
    return mean, variance, minimum, maximum

# Function to build data and segregate into respective datatype arrays
def build_data(row):
    if row[1] == "BP Dia_mmHg":
        dia.append(row[2:])
    elif row[1] == "EDA_microsiemens":
        eda.append(row[2:])
    elif row[1] == "LA Systolic BP_mmHg":
        syst.append(row[2:])
    elif row[1] == "Respiration Rate_BPM":
        res.append(row[2:])
    # Saving a copy of combined data to process it later
    all.append(row[2:])

# Function to process the saved combined data to scale the features from 4 features to 16 features
def fusion_data(data):
    # Seperate labels
    binary_data = data[:, 0]
     # Instantiate label encoder and change categorical data to numerical data.
     # This step is performed because combined data is processed seperately
    label_encoder = LabelEncoder()
    l_data = label_encoder.fit_transform(binary_data)
    # Supressing labels to fit (120,) shape
    l_data = l_data[::4]
    # Dropping labels from the main data
    data = data[:, 1]
    # Shaping the data and scaling it to 16 features
    num_rows = int(data.shape[0] / 16)
    f_data = data.reshape(num_rows, 16)
    standard_scaler = StandardScaler()
    f_data = standard_scaler.fit_transform(f_data)

    # Return the final data after processing
    return np.array(f_data),np.array(l_data)
    
# Function to convert label data which is categorical 
# values to Numerical values (Binary in this case such 
# as Pain to 1 and No Pain to 0)
def data_encoder(data):
    binary_data = data[:, 0]
    # Instantiate label encoder and change categorical data to numerical data
    label_encoder = LabelEncoder()
    encoded_binary_data = label_encoder.fit_transform(binary_data)
    # Stack with the original data
    encoded_data = np.column_stack((encoded_binary_data, data[:, 1:].astype(float)))
    return np.array(encoded_data)