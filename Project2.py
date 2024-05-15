# Import required default libraries
import sys

# Import functions from different helper files
from analysis_functions import PrintEvalMetrics
from classfiers import CrossFoldValidation, FusionCrossFoldValidation
from dataprocessor import data_encoder, data_reader, fusion_data

# Main Function
def main():
    # Store command line arguments
    data_type = sys.argv[1]
    data_file = sys.argv[2]
    # Read data, compute hand-crafted features, segregate the data
    # into the respective data_types and return numpy arrays
    dia_df, syst_df, eda_df, res_df, all_df = data_reader(data_file)
    # Assign processed dataframe to the classifier
    if data_type == "dia":
        final_df = data_encoder(dia_df)
    elif data_type == "sys":
        final_df = data_encoder(syst_df)
    elif data_type == "eda":
        final_df = data_encoder(eda_df)
    elif data_type == "res":
        final_df = data_encoder(res_df)
    elif data_type == "all":
        f_data, l_data = fusion_data(all_df)
    # print(final_df)
    # Run respective classifier for individual data and fusion data respectively
    if(data_type == "all"):
        predictions, test_indices, y = FusionCrossFoldValidation(f_data, l_data)
    else:
        predictions, test_indices, y = CrossFoldValidation(final_df)

    #Printing the Evaluation metrics
    PrintEvalMetrics(predictions, test_indices, y)


# Calling the main function
if __name__ == "__main__":
    main()