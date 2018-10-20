FROM jupyter/datascience-notebook

# Set the working directory to /app
WORKDIR /home/jovyan/work

# Copy the current directory contents into the container at /app
COPY requirements.txt /home/jovyan/work

RUN pip install -r requirements.txt
