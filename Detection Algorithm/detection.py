import os
import pandas as pd
from efficientnet.tfkeras import EfficientNetB0
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img


# Set the paths for real.txt and fake.txt files
real_file_path = 'Detection Algorithm/real.txt'
fake_file_path = 'Detection Algorithm/fake.txt'

# Set the path for the images folder
img_folder_path = 'Detection Algorithm/faces_224'

# Define the image size and batch size
input_size = 224
batch_size_num = 56

# Load the list of real videonames from the real.txt file
with open(real_file_path, 'r') as file:
    real_videonames = [line.strip() for line in file]

# Load the list of fake videonames from the fake.txt file
with open(fake_file_path, 'r') as file:
    fake_videonames = [line.strip() for line in file]

# Create an empty DataFrame to store the results
test_results = pd.DataFrame(columns=["Filename", "Prediction"])

# Load the EfficientNet model
efficient_net = EfficientNetB0(
    weights='imagenet',
    input_shape=(input_size, input_size, 3),
    include_top=False,
    pooling='max'
)

model = Sequential()
model.add(efficient_net)
model.add(Dense(units=512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))
model.summary()

# Compile the model
model.compile(optimizer=Adam(lr=0.0001), loss='binary_crossentropy', metrics=['accuracy'])

checkpoint_filepath = './tmp_checkpoint'
print('Creating Directory: ' + checkpoint_filepath)
os.makedirs(checkpoint_filepath, exist_ok=True)

custom_callbacks = [
    EarlyStopping(
        monitor='val_loss',
        mode='min',
        patience=5,
        verbose=1
    ),
    ModelCheckpoint(
        filepath=os.path.join(checkpoint_filepath, 'best_model.h5'),
        monitor='val_loss',
        mode='min',
        verbose=1,
        save_best_only=True
    )
]

# Create an ImageDataGenerator for data augmentation and normalization
data_generator = ImageDataGenerator(
    rescale=1.0/255.0,  # Normalize pixel values to [0, 1]
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Create data generators for training and validation
train_generator = data_generator.flow_from_directory(
    directory='Detection Algorithm/train',
    target_size=(input_size, input_size),
    batch_size=batch_size_num,
    class_mode='binary'
)

val_generator = data_generator.flow_from_directory(
    directory='Detection Algorithm/validation',
    target_size=(input_size, input_size),
    batch_size=batch_size_num,
    class_mode='binary',
    shuffle=False
)

# Train the network
num_epochs = 20
history = model.fit(
    train_generator,
    epochs=num_epochs,
    validation_data=val_generator,
    callbacks=custom_callbacks
)

# Load the saved model that is considered the best
best_model = load_model(os.path.join(checkpoint_filepath, 'best_model.h5'))

# Iterate over the real videonames and predict the results
for videoname in real_videonames:
    image_path = os.path.join(img_folder_path, videoname)
    image = load_img(image_path, target_size=(input_size, input_size))
    # Make predictions using the best model
    # prediction = best_model.predict(image)
    # Update the test_results DataFrame with the prediction
