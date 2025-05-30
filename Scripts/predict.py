import pandas as pd
import pickle

# Load the model
with open('correlation_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Load new data
new_data = pd.read_csv('newprofiles.csv')

# Make predictions
predictions = predict_with_loaded_model(new_data, loaded_model, method='full')
print(predictions)
