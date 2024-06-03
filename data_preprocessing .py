import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from google.cloud import storage
from PIL import Image

# Set the environment variable to point to the service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/shaunkirthan/Downloads/hackathon-420319-f9105a6db91c.json"

# Create the storage client
storage_client = storage.Client()

# Set GCS parameters
bucket_name = 'brain-tumor-1'
prefix = 'data/Training'
save_prefix = 'data/Processed'
save_dir = 'augmented_images'

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def custom_preprocess(img):
    # Convert to grayscale
    img = tf.image.rgb_to_grayscale(img)
    
    # Resize images
    img = tf.image.resize(img, [128, 128])
    
    # Normalize image data to [0, 1]
    img = img / 255.0
    
    return img

def load_and_preprocess_image_from_gcs(path):
    img = tf.io.read_file(path)
    img = tf.image.decode_jpeg(img, channels=3)
    img = custom_preprocess(img)
    return img

def save_image_to_gcs(image, bucket_name, destination_path):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_path)
    image = (image * 255).numpy().astype(np.uint8)  # Convert back to uint8
    image = tf.image.encode_jpeg(tf.squeeze(image, axis=-1))  # Encode as JPEG
    blob.upload_from_string(image.numpy(), content_type='image/jpeg')
    print(f'Saved preprocessed image to {destination_path}')

def preprocess_and_load_data_from_gcs(bucket_name, prefix, batch_size=32):
    gcs_pattern = f"gs://{bucket_name}/{prefix}/*.jpg"
    file_list = tf.io.gfile.glob(gcs_pattern)
    
    dataset = tf.data.Dataset.from_tensor_slices(file_list)
    dataset = dataset.map(lambda x: load_and_preprocess_image_from_gcs(x), num_parallel_calls=tf.data.experimental.AUTOTUNE)
    dataset = dataset.batch(batch_size).prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
    
    return dataset

def save_preprocessed_batches(train_generator, total_images_to_save, save_dir):
    batch_size = train_generator.batch_size
    num_batches_to_save = total_images_to_save // batch_size

    # Loop through the generator and save images
    for i in range(num_batches_to_save):
        x_batch, y_batch = next(train_generator)
        for j in range(batch_size):
            img = x_batch[j]
            img_path = os.path.join(save_dir, f'aug_{i * batch_size + j}.jpeg')
            img = (img * 255).astype(np.uint8)  # Convert to uint8 for saving
            img = Image.fromarray(img.squeeze(), 'L')
            img.save(img_path)
            save_image_to_gcs(img, bucket_name, f'{save_prefix}/aug_{i * batch_size + j}.jpeg')

    # If the total_images_to_save is not a multiple of batch_size, save the remaining images
    remaining_images = total_images_to_save % batch_size
    if remaining_images > 0:
        x_batch, y_batch = next(train_generator)
        for j in range(remaining_images):
            img = x_batch[j]
            img_path = os.path.join(save_dir, f'aug_{num_batches_to_save * batch_size + j}.jpeg')
            img = (img * 255).astype(np.uint8)  # Convert to uint8 for saving
            img = Image.fromarray(img.squeeze(), 'L')
            img.save(img_path)
            save_image_to_gcs(img, bucket_name, f'{save_prefix}/aug_{num_batches_to_save * batch_size + j}.jpeg')

# Preprocess and load data directly from GCS
train_dataset = preprocess_and_load_data_from_gcs(bucket_name, prefix)

# Example: Get a batch of data and save the images
total_images_to_save = 100
train_generator = tf.data.Dataset.from_generator(
    lambda: train_dataset,
    output_signature=(
        tf.TensorSpec(shape=(None, 128, 128, 1), dtype=tf.float32),
        tf.TensorSpec(shape=(None,), dtype=tf.int32)
    )
)

# Save the preprocessed images to GCS
save_preprocessed_batches(train_generator, total_images_to_save, save_dir)

# Example: Get a single batch of data
for x_batch in train_generator.take(1):
    print(f'Batch shape: {x_batch.shape}')
