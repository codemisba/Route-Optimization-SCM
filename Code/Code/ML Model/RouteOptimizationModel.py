import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

"""
What This Route Optimization Model Does ?

1) Generates synthetic data: Random customer coordinates (as if they are delivery points).

2) Creates optimal routes: A greedy nearest-neighbor approach to create target labels.

3) Trains a neural network: To learn the best route given customer locations using TensorFlow.

4) Output: A model that, given a set of coordinates, predicts a likely optimal route (as a permutation matrix).
"""

"""
For Production-Ready Route Optimization

1) Use a more sophisticated routing algorithm (e.g., Clarke-Wright Savings, Genetic Algorithm).
2) Use real-world data: GPS coordinates, road networks, etc.
3) Consider delivery constraints: vehicle capacity, time windows, depot location.
4) Consider Reinforcement Learning (e.g., with TensorFlow Agents or Ray RLlib) for dynamic route optimization.
5) Replace greedy routing with real optimization (e.g., OR-Tools or exact solvers).
6) Need Incorporate delivery constraints: vehicle capacity, time windows, depot location.

"""
# ---- Import necessary libraries ----
import numpy as np

#pip install tensorflow

# ---- Generate synthetic customer coordinates (lat, lon normalized) ----
def generate_data(num_samples=10000, num_points=10):
    data = np.random.rand(num_samples, num_points, 2)
    return data

# ---- Compute distance matrix and shortest route (greedy for simplicity) ----
def compute_targets(data):
    targets = []
    for sample in data:
        visited = [0]
        current = sample[0]
        route = [0]
        while len(visited) < len(sample):
            dists = np.linalg.norm(sample - current, axis=1)
            dists[visited] = np.inf
            next_idx = np.argmin(dists)
            visited.append(next_idx)
            route.append(next_idx)
            current = sample[next_idx]
        targets.append(route)
    return np.array(targets)

# ---- One-hot encode route for training ----
def one_hot_encode(routes, num_points):
    encoded = []
    for route in routes:
        one_hot = np.zeros((num_points, num_points))
        for i, idx in enumerate(route):
            one_hot[i, idx] = 1
        encoded.append(one_hot)
    return np.array(encoded)

# ---- Build the model ----
def build_model(num_points):
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(num_points, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(num_points * num_points, activation='softmax'),
        tf.keras.layers.Reshape((num_points, num_points))
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# ---- Main Training Logic ----
def train_model():
    num_samples = 5000
    num_points = 10

    X = generate_data(num_samples, num_points)
    Y_routes = compute_targets(X)
    Y = one_hot_encode(Y_routes, num_points)

    X, Y = shuffle(X, Y)

    model = build_model(num_points)
    model.summary()

    model.fit(X, Y, epochs=10, batch_size=32, validation_split=0.1)

    return model

# ---- Run training ----
model = train_model()
# Plotting training history
history = model.history.history
plt.plot(history['loss'])
plt.plot(history['val_loss']) 
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()

# Save the model
model.save('route_optimization_model.h5')
     
# ---- Save the model ----