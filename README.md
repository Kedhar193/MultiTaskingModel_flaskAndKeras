# Flask and Deep Learning Project

## Overview

This project combines Flask, a web framework for Python, with a deep learning model to create an interactive web application. The application accepts images, processes them using a pre-trained deep learning model, and provides predictions for digit recognition and color classification.

## Features

- User authentication system (signup, login, logout)
- Dashboard for authenticated users to upload images and receive predictions
- Integration of a pre-trained deep learning model for digit and color classification
- Responsive web design for seamless user experience

## Technologies Used

- Python
- Flask
- TensorFlow
- HTML/CSS
- MySQL 

## About Deep Learning model 

It is a multi-task model that performs digit recognition and color classification simultaneously.


#### Input Layer: 
Accepts images with a shape of (28, 28, 3), assuming a 28x28 pixel image with 3 color channels (RGB).
#### Digit Recognition Branch:
-Convolutional layer with 32 filters and a kernel size of 3.


-ReLU activation function.


-MaxPooling layer with a pool size of 4.


-Flatten layer.


-Dense layer with 10 units and softmax activation for digit classification.

#### Color Classification Branch:


-Convolutional layer with 32 filters and a kernel size of 3.


-ReLU activation function.


-Convolutional layer with 32 filters and a kernel size of 3.


-Element-wise addition with the output of the first convolutional layer.


-ReLU activation function.


-MaxPooling layer with a pool size of 4.


-Flatten layer.


-Dense layer with 1 unit and sigmoid activation for color classification.



![image](https://github.com/Kedhar193/flask-and-dl-project/assets/115712936/335ee877-30f1-4b15-91f1-b778aaac5ff6)



# outputs of the project 

##### signup page

![Screenshot (73)](https://github.com/Kedhar193/flask-and-dl-project/assets/115712936/07ba3ddb-e793-4adc-bba4-cf43d28b019c)


##### login page

![Screenshot (72)](https://github.com/Kedhar193/flask-and-dl-project/assets/115712936/6c4dc7e3-017b-42b0-88ed-d63d9adb865c)

##### proof that the dashboard is not accessible without logging in 

![Screenshot (74)](https://github.com/Kedhar193/flask-and-dl-project/assets/115712936/98a623d9-b1f3-4c30-98da-abaeda1fc61c)

##### after logging in the dashboard looks like this and we are uploading the image into the interface

![Screenshot (77)](https://github.com/Kedhar193/flask-and-dl-project/assets/115712936/b3517105-7512-4fea-8387-01a32600e8ed)

##### uploading the following picture into the model 

![download](https://github.com/Kedhar193/flask-and-dl-project/assets/115712936/755b8c3a-2754-4545-aab0-11e75806c0c8)

##### final predictions after uploading the image 

![Screenshot (76)](https://github.com/Kedhar193/flask-and-dl-project/assets/115712936/a61d71c1-4257-4362-a9c2-292ac177ed15)
