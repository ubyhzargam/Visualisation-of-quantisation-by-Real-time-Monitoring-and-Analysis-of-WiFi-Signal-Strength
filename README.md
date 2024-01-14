This Python script aims to provide a real-time monitoring and analysis of WiFi signal strength over time. The project utilizes the subprocess, time, and matplotlib libraries to retrieve WiFi signal strength, sample the signal with added random noise, and quantize the sampled signal. The monitoring is presented through three subplots representing the original WiFi signal strength, the sampled version, and the quantized version.

Here's a breakdown of the key components:

WiFi Signal Retrieval:
The get_wifi_strength function uses the subprocess module to execute a command that retrieves WiFi information, specifically the Received Signal Strength Indication (RSSI) value.
Data Collection:
The script continuously collects WiFi signal strength (rssi) and corresponding timestamps (time_values) at regular intervals (every 2 seconds).
Signal Processing:
The collected RSSI values are stored in rssi_values.
Random noise is added to create a sampled version (sampled_rssi_values) of the signal.
Quantization is applied to round the sampled values to the nearest multiple of 10 (quantized_rssi_values).
Real-time Plotting:
The script utilizes Matplotlib to create three vertically stacked subplots:
Original WiFi signal strength over time (ax1).
Sampled WiFi signal strength over time (ax2).
Quantized WiFi signal strength over time (ax3).
Each subplot is continuously updated as new data is collected.
Visualization:
The plots include interactive elements (plt.ion()) for real-time updates.
X and Y-axis labels, titles, and gridlines provide clarity in understanding the displayed information.
Continuous Monitoring:
The script runs in an infinite loop, continuously updating and visualizing the WiFi signal strength.
Note: Make sure to run this script in an environment with the necessary permissions to access WiFi information. Additionally, consider adding an exit condition for the infinite loop to gracefully stop the monitoring.
This code is run on Mac platform with maltplotlib and python installed in your system
