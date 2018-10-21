# Datascience Quick Start Environment
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

## License
```sh
MIT License

Copyright (c) 2018 Mácio Arruda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```