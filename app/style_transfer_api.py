# app/style_transfer_api.py
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image
import io

# Cargamos el modelo preentrenado de Style Transfer desde TensorFlow Hub
model = hub.load("https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2")

def load_image(image_bytes):
    """Convierte una imagen en bytes a tensor de TensorFlow normalizado"""
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((256, 256))  # Tamaño fijo por performance
    img_array = np.array(image) / 255.0  # Normalizar a [0, 1]
    return tf.constant(img_array, dtype=tf.float32)[tf.newaxis, ...]

def transfer_style(content_bytes, style_bytes):
    """Aplica el estilo de style_image sobre content_image usando el modelo"""
    content_image = load_image(content_bytes)
    style_image = load_image(style_bytes)

    # Ejecuta el modelo
    stylized_image = model(content_image, style_image)[0]

    # Convierte de tensor a imagen de PIL
    output_image = tf.image.convert_image_dtype(stylized_image[0], dtype=tf.uint8)
    return Image.fromarray(output_image.numpy())
