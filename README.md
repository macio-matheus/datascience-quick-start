# Quick start of a development environment for data science
Development environment in Docker, which contains the most important tools 
for: 

```sh
    - Scientific Computing
    - Statistics 
    - Neural Networks 
    - Evolutionary Computing 
    - Machine Learning 
    - Deep Learning
    - Data analysis
    - Time Series Analysis
    - Data Visualization
    - Natural Language Processing
    - Computer Vision
```

## Main Tools
Below, a part of the tools contained in the environment
```sh
    - Numpy
    - Pandas 
    - Anaconda 
    - Jupyter 
    - Scikit-learn
    - Tensorflow
    - Python
    - R
    - Julia
    - NLTK
    - Opencv
    - Keras
    - Matplotlib
    - Deap
    - SciPy
    - Fbprophet
    - Scikit-Image
    - Scikit-fuzzy
    - Tensorflow
    - Keras
```


## Usage
First of all, build the container using docker-compose and then you can 
access the Jupyter that is ready to be used.

##### Run with docker compose
```sh
cd datascience-quick-start
docker-compose up -d --build
```

##### Accessing Jupyter
```sh
http://<your-ip>:8888/tree
```

##### Ports
```sh
    - 8888 => Jupyter
    - 6007 => Tensorboard
    - 5007 => Your App
```