from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import to_categorical

# Optenemos los datos de entrenamiento y prueba
(train_data, train_labels), (test_data, test_labels) = cifar10.load_data()

# Normalizamos los datos de entrada dividiendo por 255.0 (escala de grises)\
train_data = train_data / 255.0
test_data = test_data / 255.0

# Transformamos los datos
train_labels = to_categorical(train_labels, 10)
test_labels = to_categorical(test_labels, 10)

# Creamos el modelo de la red neuronal
model = Sequential()
model.add(Flatten(input_shape=(32,32, 3)))
model.add(Dense(1000, activation = 'relu'))
model.add(Dense(10, activation = 'softmax'))

# Compilamos el modelo
model.compile(
    optimizer = 'adam',
    loss = 'categorical_crossentropy',
    metrics = ['accuracy']
)

# Entrenamiento del modelo
model.fit(
    train_data,
    train_labels,
    epochs = 10,
    batch_size = 64,
    validation_data=(test_data, test_labels),
    verbose = False
)

model.save("cifar10_model.h5")