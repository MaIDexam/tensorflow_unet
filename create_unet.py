## import tensorflow as tf
# elu
import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras import layers
from tensorflow import keras

# создать экземпляр стратегии распространения

reg = keras.regularizers.l2(0.1)
keras.backend.clear_session()
def create_model():
    mp = 2  # maxpooling
    inputs = keras.Input((256, 256, 3))
    s = Lambda(lambda x: x / 255)(inputs)
    st = 2
    fa = 'relu'  # функция активации
    cs = 3  # conv size

    list43 = [25, 50, 100, 200, 400, 13]
    # , kernel_regularizer=reg, bias_regularizer=reg

    c0 = Conv2D(list43[-1], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(s)
    c0 = layers.BatchNormalization()(c0)
    c0 = Conv2D(list43[-1], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(c0)
    c0 = layers.BatchNormalization()(c0)
    p0 = MaxPooling2D(pool_size=(mp, mp), strides=st)(c0)

    c1 = Conv2D(list43[0], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(p0)
    c1 = layers.BatchNormalization()(c1)
    c1 = Conv2D(list43[0], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(c1)
    c1 = layers.BatchNormalization()(c1)
    p1 = MaxPooling2D(pool_size=(mp, mp), strides=st)(c1)

    c2 = Conv2D(list43[1], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(p1)
    c2 = layers.BatchNormalization()(c2)
    c2 = Conv2D(list43[1], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(c2)
    c2 = layers.BatchNormalization()(c2)
    p2 = MaxPooling2D(pool_size=(mp, mp), strides=st)(c2)

    c3 = Conv2D(list43[2], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(p2)
    c3 = layers.BatchNormalization()(c3)
    c3 = Conv2D(list43[2], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(c3)
    c3 = layers.BatchNormalization()(c3)
    p3 = MaxPooling2D(pool_size=(mp, mp), strides=st)(c3)

    c4 = Conv2D(list43[3], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(p3)
    c4 = layers.BatchNormalization()(c4)
    c4 = Conv2D(list43[3], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(c4)
    c4 = layers.BatchNormalization()(c4)
    p4 = MaxPooling2D(pool_size=(mp, mp), strides=st)(c4)

    c5 = Conv2D(list43[4], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(p4)
    c5 = layers.BatchNormalization()(c5)
    c5 = Conv2D(list43[4], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(c5)
    c5 = layers.BatchNormalization()(c5)

    u6 = Conv2DTranspose(list43[3], (mp, mp), strides=(st, st), padding='same')(c5)
    u6 = layers.BatchNormalization()(u6)
    u6 = concatenate([u6, c4])
    c6 = Conv2D(list43[3], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(u6)
    c6 = layers.BatchNormalization()(c6)
    c6 = Conv2D(list43[3], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(c6)
    c6 = layers.BatchNormalization()(c6)

    u7 = Conv2DTranspose(list43[2], (mp, mp), strides=(st, st), padding='same')(c6)
    u7 = layers.BatchNormalization()(u7)
    u7 = concatenate([u7, c3])
    c7 = Conv2D(list43[2], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(u7)
    c7 = layers.BatchNormalization()(c7)
    c7 = Conv2D(list43[2], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(c7)
    c7 = layers.BatchNormalization()(c7)

    u8 = Conv2DTranspose(list43[1], (mp, mp), strides=(st, st), padding='same')(c7)
    u8 = layers.BatchNormalization()(u8)
    u8 = concatenate([u8, c2])
    c8 = Conv2D(list43[1], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(u8)
    c8 = layers.BatchNormalization()(c8)
    c8 = Conv2D(list43[1], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(c8)
    c8 = layers.BatchNormalization()(c8)

    u9 = Conv2DTranspose(list43[0], (mp, mp), strides=(st, st), padding='same')(c8)
    u9 = layers.BatchNormalization()(u9)
    u9 = concatenate([u9, c1])
    c9 = Conv2D(list43[0], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(u9)
    c9 = layers.BatchNormalization()(c9)
    c9 = Conv2D(list43[0], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(c9)
    c9 = layers.BatchNormalization()(c9)

    u10 = Conv2DTranspose(list43[-1], (mp, mp), strides=(st, st), padding='same')(c9)
    u10 = layers.BatchNormalization()(u10)
    u10 = concatenate([u10, c0])
    c10 = Conv2D(list43[-1], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(u10)
    c10 = layers.BatchNormalization()(c10)
    c10 = Conv2D(list43[0 - 1], (cs, cs), activation=fa, kernel_initializer='normal', padding='same')(c10)
    c10 = layers.BatchNormalization()(c10)

    outputs = Conv2D(2, (1, 1), activation='softmax')(c10)
    # outputs = layers.BatchNormalization()(outputs)
    model = keras.Model(inputs=[inputs], outputs=[outputs])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])
    return model