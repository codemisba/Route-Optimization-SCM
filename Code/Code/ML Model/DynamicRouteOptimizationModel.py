import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Simulated route data (we would replace this with real geospatial route data)
# Each record: [distance_matrix_flattened] -> optimal_route_index_order
# For example purposes, let's say we have 5 delivery points (5x5 matrix = 25 features)

# Load the real data instead of the below dummy data
def generate_dummy_data(n_samples=1000, n_points=5):
    X, y = [], []
    for _ in range(n_samples):
        dist_matrix = np.random.rand(n_points, n_points)
        np.fill_diagonal(dist_matrix, 0)
        dist_flat = dist_matrix.flatten()

        optimal_route = np.argsort(np.sum(dist_matrix, axis=1))  # dummy heuristic
        X.append(dist_flat)
        y.append(optimal_route)

    return np.array(X), np.array(y)

X, y = generate_dummy_data()

# Normalize input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

# Define TensorFlow model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X.shape[1],)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(y.shape[1], activation='linear')  # predict route positions
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train model
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Evaluate
loss, mae = model.evaluate(X_test, y_test)
print(f"Test MAE: {mae:.2f}")

# Predict example
sample = X_test[0].reshape(1, -1)
predicted_route = model.predict(sample)
predicted_order = np.argsort(predicted_route.flatten())
print("Predicted route order:", predicted_order)
# Save model
model.save('dynamic_route_optimization_model.h5')