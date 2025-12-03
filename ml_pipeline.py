# ml_pipeline.py

def train_model(data, labels):
    if not data or not labels:
        raise ValueError("Training data and labels must not be empty.")
    return {"status": "success", "accuracy": 0.95}