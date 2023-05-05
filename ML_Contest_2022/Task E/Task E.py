from math import tan, cos, sin, sqrt
from tensorflow.keras import Sequential
from tensorflow.keras.layers import  Dense 
import numpy as np
import time 

PATH = ""
input_filename = PATH + "input.txt"
output_filename = PATH + "output.txt"

def load_input_data(input_filename):
    with open(input_filename, 'r') as file:
        # Считываем строки из входного файла
        rows = list(map(str.strip, file.readlines()))
        count_x = int(rows[0])
        rows_xf = []
        for i in range(count_x):
            rows_xf.append([float(n) for n in rows[i+1].split(" ")])
    return rows_xf

def main():
    rows_xf = load_input_data(input_filename)

    x_train = []
    y_train = []
    for row in data:
        x_vector = []
        x = row[0]
        f = row[1]
        x_vector.append(tan(x))
        x_vector.append(sin(x)**2)
        x_vector.append(2*sin(x)*cos(x))
        x_vector.append(cos(x)**2)
        x_vector.append(sqrt(x))
        x_train.append(x_vector)
        y_train.append(f)
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_train.shape, y_train.shape

    # start_time = time.time()
    model = Sequential()
    model.add(Dense(1, input_shape=(x_train.shape[1],), activation=None, use_bias=False )) # Т.к. нам необходимо подобрать коэфициенты, то отключаем базис и функцию активации
    model.compile(optimizer='Nadam', loss='mae') 
    history = model.fit(x_train, y_train, epochs=600,  verbose=False, batch_size=1)
    # print(time.time() - start_time)
    
    w = model.layers[0].weights
    
    a  = round(float(w[0][0][0]),2) # для tan(x) 
    b  = round(float(sqrt(abs(w[0][1][0]))),2) # для sin(x)**2 
    # элемент w[0][1] пропускаем, т.к. попадает на 2*sin(x)*cos(x) 
    c  = round(float(sqrt(abs(w[0][3][0]))),2) # для cos(x)**2 
    d  = round(float(w[0][4][0]),2) # для sqrt(x) 
    res_values = f"{a} {b} {c} {d}"
    # print(res_values)

    with open(output_filename, "w") as file:
        file.write(res_values)

if __name__ == '__main__':
    main()