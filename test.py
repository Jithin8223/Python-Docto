# 1. Create a mapping dictionary during training
state_mapping = {
    'New York': 0,
    'California': 1,
    'Florida': 2
    # Add more states as needed
}

# 2. Reverse mapping for prediction interpretation
reverse_state_mapping = {v: k for k, v in state_mapping.items()}

# 3. During inference/testing, use this function
def predict_with_state_name(model, input_data, state_name):
    # Convert state name to its encoded value
    if state_name in state_mapping:
        encoded_state = state_mapping[state_name]
        
        # Replace the appropriate column in input_data with the encoded value
        input_data['State_encoded'] = encoded_state
        
        # Make prediction
        prediction = model.predict(input_data)
        return prediction
    else:
        return f"Error: State '{state_name}' not found in training data"