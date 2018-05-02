# Self Driving Car Simulation
This repository consists of code for training and running Udacity's self driving car simulator.


![GIF](https://github.com/pradeeshvishnu/self_driving_car_simulation/blob/master/autonomous.gif)


## Dependencies

You can install all dependencies by running one of the following commands

You need a [anaconda](https://www.continuum.io/downloads) or [miniconda](https://conda.io/miniconda.html) to use the environment setting.

```python
# Use TensorFlow without GPU
conda env create -f environments.yml 

# Use TensorFlow with GPU
conda env create -f environment-gpu.yml
```

### To train the model

You'll need the folder 'data' which contains the training images.

```python
python model.py
```

## Usage


### Run the pretrained model for simulator

Start up [the Udacity self-driving simulator](https://github.com/udacity/self-driving-car-sim), choose a scene and press the Autonomous Mode button.  Then, run the model as follows:

```python
python drive.py model.h5 autonomous
```
The folder 'autonomous' will contain the images to make a video using the code

'''python
python video.py autonomous
'''

## Changing the absolute address of the images to local address
Use the code
'''python
python directory_change.py
'''
to change the abolute address of the images in the driving_log.csv to local address.
