def test_model():
    model = bm.nn.LSTM(128)
    input_data = np.array([[0.1], [0.2], [0.3]])
    print(f"Test output: {model.predict(input_data)}")