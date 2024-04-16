import tensorflow as tf
import cv2
import os
import numpy as np

# Função para carregar e pré-processar as imagens
def load_images_from_folder(folder):
    images = []
    labels = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        img = cv2.imread(img_path)
        if img is not None:
            IMG_WIDTH = 224
            IMG_HEIGHT = 224
            # Redimensionar a imagem para o tamanho desejado
            img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
            # Normalizar os valores dos pixels para a faixa [0, 1]
            img = img / 255.0
            images.append(img)
            # Rotular a imagem com base no nome do arquivo ou pasta
            if "com_celular" in folder:
                labels.append(1)  # 1 para imagens com celular
            else:
                labels.append(0)  # 0 para imagens sem celular
    return np.array(images), np.array(labels)

# Definir o caminho para as pastas contendo imagens de treinamento e teste
train_folder_with_cellphone = r"C:\Users\Vanderlei\Desktop\FOTOSGOOGLE"
train_folder_without_cellphone = r"C:\Users\Vanderlei\Desktop\image"
test_folder_with_cellphone = r"C:\Users\Vanderlei\Desktop\imagem"
test_folder_without_cellphone = r"C:\Users\Vanderlei\Desktop\image"

# Carregar e pré-processar imagens de treinamento
train_images_with_cellphone, train_labels_with_cellphone = load_images_from_folder(train_folder_with_cellphone)
train_images_without_cellphone, train_labels_without_cellphone = load_images_from_folder(train_folder_without_cellphone)

# Carregar e pré-processar imagens de teste
test_images_with_cellphone, test_labels_with_cellphone = load_images_from_folder(test_folder_with_cellphone)
test_images_without_cellphone, test_labels_without_cellphone = load_images_from_folder(test_folder_without_cellphone)

# Combinar os conjuntos de dados de treinamento e teste
train_images = np.concatenate((train_images_with_cellphone, train_images_without_cellphone), axis=0)
train_labels = np.concatenate((train_labels_with_cellphone, train_labels_without_cellphone), axis=0)
test_images = np.concatenate((test_images_with_cellphone, test_images_without_cellphone), axis=0)
test_labels = np.concatenate((test_labels_with_cellphone, test_labels_without_cellphone), axis=0)

IMG_WIDTH = 224
IMG_HEIGHT = 224

# Definir o modelo de classificação (mesmo código do exemplo anterior)
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

# Salvar o modelo treinado para uso posterior
model.save("celular_model.keras")
