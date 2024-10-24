#ANOMALY DETECTION
#Arshad Khalid

# The code below is to simulate a real-time data stream, detect anomalies, and visualize the result in real-time


# Imported libraries: 
# numpy for numerical calculations, matplotlib for real-time plotting, 
# deque for a sliding window for storing recent data points, and random for generating noise and simulating anomalies.
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import random

# 1. Data Stream Generator
    # simulates a data stream combining seasonal variation (sine wave), a trend component, 
    # and random noise to create realistic data fluctuations

def data_stream_generator(num_points=1000):

    # basic validation and error handling to ensure num_points is a positive integer
    if not isinstance(num_points, int) or num_points <= 0:
        raise ValueError("num_points must be a positive integer")
    
    for i in range(num_points):
        season = np.sin(i * 0.05) * 10      # sine pattern
        trend = i * 0.01                    # slight trend
        noise = random.gauss(0, 1)          # random noise (Normal distribution)
        value = season + trend + noise      # final value

        # introducing an anomaly with a small probability
        if random.random() < 0.01:
            value += random.gauss(50, 10)    # Large spike for anomaly
        yield round(value, 2)                # Rounding the value to 2 decimal places

# 2. Z-score Anomaly Detection
    # this algorithm computes the z-score of a data point, which measures how many standard deviations
    # a value is from the mean of recent data points (using a sliding window)

    # The z-score formula is:  Z = (X - mean) / stddev
    # where:
    # -> X is the new value,
    # -> mean is the average of recent values in the sliding window,
    # -> std is the standard deviation of those values
    # if the absolute Z-score exceeds a pre-defined threshold (in this case 3), the value is flagged as an anomaly

    # Effectiveness:
    # the z-score method is effective for detecting outliers in data that has a roughly normal distribution
    #it allows for quick, real-time detection of significant deviations from the recent data pattern

class ZScoreAnomalyDetector:
    def __init__(self, window_size=50, threshold=3.0):

        # basic validation and error handling to ensure num_points is a positive 
        # integer and window size is reasonable
        if not isinstance(window_size, int) or window_size <= 0:
            raise ValueError("window_size must be a Positive Integer")
        if threshold <= 0:
            raise ValueError("threshold must be a Positive Number")

        # window_size: Number of recent data points to consider for z-score calculation
        # threshold: z-score threshold above which a point is considered an anomaly
        self.window_size = window_size
        self.threshold = threshold
        self.data_window = deque(maxlen=window_size)
        self.mean = 0
        self.std = 0

    # update the mean and standard deviation based on the current data window
    def update_statistics(self):
        if len(self.data_window) > 1: # ensure there is enough data to calculate statistics
            self.mean = np.mean(self.data_window)
            self.std = np.std(self.data_window)

    # detect if the new data point is an anomaly based on the z-score
    def detect(self, new_value):
        
        # a sliding window (using deque) stores the last window_size data points
        # update the sliding window
        self.data_window.append(new_value)
        self.update_statistics()

        # avoid division by zero for std = 0
        if self.std == 0:
            return False

        # calculate z-score
        zscore = (new_value - self.mean) / self.std

        # flag if z-score exceeds threshold
        return abs(zscore) > self.threshold

# 3. Real-time Visualization with Anomaly Logging
    # visualizes the data stream and detected anomalies in real-time using matplotlib

def real_time_visualization(detector, num_points=1000):
    data_stream = data_stream_generator(num_points)
    values = []                                         # to store all data points
    anomalies = []                                      # to store detected anomalies 
    count = 0

    plt.ion()                                           # allows plot to be updated/plotted in real-time
    fig, ax = plt.subplots()
    
    for i, point in enumerate(data_stream):

        #check if the point is an anomaly
        is_anomaly = detector.detect(point)

        values.append(point) #append new point
        anomalies.append(point if is_anomaly else None)

        # log detected anomalies (in console, for viewing purposes)
        if is_anomaly:
            count +=1
            print(f"--> Anomaly detected at X-axis {i} & Y-axis {point}\n")

        # plot the data stream and anomalies in real-time
        ax.clear()
        ax.plot(values, label="Data Stream") #plot all values
        ax.scatter(range(len(anomalies)), anomalies, color='red', label=f"Anomalies (Detected: {count})") #plots anomalies in a red dot
        ax.set_title(f"Real-time Data Stream with Anomaly Detection (Points Visualized: {i + 1})")
        ax.legend()

        plt.pause(0.01) # small pause to simulate real-time plotting

    plt.ioff()          # turn off interactive mode
    plt.show()

# 4. Running the Detection and Visualization program

# create a Z-score detector with a sliding window of 50 points and a threshold of 3.0
detector = ZScoreAnomalyDetector(window_size=50, threshold=3.0)
# run the real-time visualization for 500 data points
real_time_visualization(detector, num_points=500)

