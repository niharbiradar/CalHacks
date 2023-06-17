import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Load and preprocess the dataset
# Assuming you have a list of image paths and their corresponding labels
def preprocess_dataset(image_paths, labels):
    features = []
    for path in image_paths:
        image = cv2.imread(path)
        # Perform necessary preprocessing on the image
        # For example, resize, normalization, etc.
        preprocessed_image = preprocess_image(image)
        features.append(preprocessed_image)
    features = np.array(features)
    labels = np.array(labels)
    return features, labels

# Preprocess a single image (example)
def preprocess_image(image):
    # Example preprocessing steps
    resized_image = cv2.resize(image, (224, 224))
    normalized_image = resized_image / 255.0
    return normalized_image

# Load the dataset
image_paths = [...]  # List of image paths
labels = [...]  # List of corresponding labels (0 for authentic, 1 for deepfake)

# Preprocess the dataset
features, labels = preprocess_dataset(image_paths, labels)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Extract features using a pre-trained CNN model (example using OpenCV's DNN module)
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'pretrained.caffemodel')

def extract_features(image):
    blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(224, 224), mean=(104.0, 177.0, 123.0))
    net.setInput(blob)
    features = net.forward()
    return features.flatten()

# Extract features for training and testing sets
X_train_features = np.array([extract_features(image) for image in X_train])
X_test_features = np.array([extract_features(image) for image in X_test])

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_features)
X_test_scaled = scaler.transform(X_test_features)

# Train an SVM classifier
svm = SVC(kernel='linear', random_state=42)
svm.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = svm.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
