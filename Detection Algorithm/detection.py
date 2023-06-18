import os
import numpy as np
import cv2
from keras.applications.vgg16 import VGG16
from keras.models import Model
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

directory = 'Detection Algorithm/faces_224'
def load_images_from_directory(directory):
    images = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        image = cv2.imread(file_path)
        image = cv2.resize(image, (224, 224))
        images.append(image)
    return np.array(images)

# Step 1: Data Collection and Preprocessing
training_directory_real = 'Detection Algorithm/training/real'
training_directory_fake = 'Detection Algorithm/training/fake'
validation_directory_real = 'Detection Algorithm/validation/real'
validation_directory_fake = 'Detection Algorithm/validation/fake'

real_images_train = load_images_from_directory(training_directory_real)
fake_images_train = load_images_from_directory(training_directory_fake)
real_images_val = load_images_from_directory(validation_directory_real)
fake_images_val = load_images_from_directory(validation_directory_fake)

labels_train = np.concatenate((np.ones(len(real_images_train)), np.zeros(len(fake_images_train))))
labels_val = np.concatenate((np.ones(len(real_images_val)), np.zeros(len(fake_images_val))))

# Step 2: Feature Extraction
def extract_features(images):
    model = VGG16(weights='imagenet', include_top=False)
    feature_extractor = Model(inputs=model.input, outputs=model.get_layer('fc2').output)
    features = feature_extractor.predict(images)
    return features

real_features_train = extract_features(real_images_train)
fake_features_train = extract_features(fake_images_train)
real_features_val = extract_features(real_images_val)
fake_features_val = extract_features(fake_images_val)

all_features_train = np.concatenate((real_features_train, fake_features_train))
all_features_val = np.concatenate((real_features_val, fake_features_val))

# Step 3: Feature Fusion
# Perform feature fusion here, e.g., concatenation or averaging of features

# Step 4: Classifier Training
X_train, X_val, y_train, y_val = train_test_split(all_features_train, labels_train, test_size=0.2, random_state=42)

# Normalize the features
X_train /= 255.0
X_val /= 255.0

# Encode labels
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_val_encoded = label_encoder.transform(y_val)

# Train SVM classifier
svm = SVC(kernel='linear')
svm.fit(X_train, y_train_encoded)

# Step 5: Testing and Evaluation
X_test = all_features_val / 255.0
y_val_pred = svm.predict(X_val)
y_val_pred = label_encoder.inverse_transform(y_val_pred)

print("Validation Results:")
print(classification_report(y_val, y_val_pred))

y_test_pred = svm.predict(X_test)
y_test_pred = label_encoder.inverse_transform(y_test_pred)

print("Testing Results:")
print(classification_report(labels_val, y_test_pred))
