import os
import pandas as pd
from efficientnet.tfkeras import EfficientNetB0
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.models import load_model
from keras.preprocessing.image import load_img

# Set the paths for real.txt and fake.txt files
real_file_path = 'Detection Algorithm/real.txt'
fake_file_path = 'Detection Algorithm/fake.txt'

img_to = "Detection Algorithm/savedImages.txt"

# Define the image size and batch size
input_size = 224
batch_size_num = 56

# Load the list of real videonames from the real.txt file
with open(real_file_path, 'r') as file:
    real_videonames = [line.strip() for line in file]
    if real_videonames == None:
        pass

# Load the list of fake videonames from the fake.txt file
with open(fake_file_path, 'r') as file:
    fake_videonames = [line.strip() for line in file]
    if fake_videonames == None:
        pass

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

# Train the network
num_epochs = 20
history = model.fit(
    x=None,  # No input data is used for training
    y=None,  # No target labels are used for training
    epochs=num_epochs,
    callbacks=custom_callbacks
)

# Load the saved model that is considered the best
best_model = load_model(os.path.join(checkpoint_filepath, 'best_model.h5'))

# Iterate over the real videonames and predict the results
for videoname in real_videonames:
    image_path = os.path.join("Detection Algorithm/faces_224", videoname)
    image = load_img(image_path, target_size=(input_size, input_size))
    image_array = img_to
