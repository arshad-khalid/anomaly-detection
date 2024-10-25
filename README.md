# Real-Time Anomaly Detection and Visualization

This project demonstrates a real-time data stream generator with anomaly detection using Z-score and visualization using `matplotlib`. The program simulates realistic data fluctuations and detects anomalies in real-time based on statistical analysis.

## Features
- **Data Stream Simulation**: Generates a data stream that includes seasonal variations (sine wave), trend, and noise to simulate real-world data.
- **Z-score Based Anomaly Detection**: Detects anomalies by calculating the Z-score of data points within a sliding window. Points with Z-scores greater than a predefined threshold are flagged as anomalies.
- **Real-Time Visualization**: Visualizes both the data stream and detected anomalies in real-time using `matplotlib`.

## How It Works
1. **Data Stream Generator**: A sine wave combined with a slight trend and random noise is generated. Occasionally, random anomalies (spikes) are introduced.
2. **Z-score Anomaly Detection**: A sliding window is used to maintain the most recent data points. The Z-score of each point is calculated and compared to a threshold to determine if the point is an anomaly.
3. **Real-Time Visualization**: The data points and detected anomalies are plotted in real-time using `matplotlib`. Detected anomalies are highlighted on the plot.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/arshad-khalid/anomaly-detection.git
    ```
2. And run the py file:
    ```bash
    python anomaly_detection.py
    ```

3. The program will generate a data stream, detect anomalies using the Z-score method, and visualize the results in real-time.

