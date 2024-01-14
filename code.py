import time
import subprocess
import matplotlib.pyplot as plt
import random

def get_wifi_strength():
    output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"])
    for line in output.decode("utf-8").splitlines():
        if "agrCtlRSSI" in line:
            return int(line.split(":")[1])

rssi_values = []
time_values = []
sampled_rssi_values = []  # Store sampled values
quantized_rssi_values = []  # Store quantized values

plt.ion()  # Turn on interactive plotting mode

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)  # Create three subplots vertically

# Original signal plot
line1, = ax1.plot([], [], 'o-', label='WiFi Strength (Original)')
ax1.set_xlabel("Time (seconds)")
ax1.set_ylabel("WiFi Strength (RSSI)")
ax1.set_title("Original WiFi Strength over Time")
ax1.grid(True)
ax1.set_xlim(0, 10)
ax1.set_ylim(-60, -10)

# Sampled version plot
line2, = ax2.plot([], [], 'o-', label='WiFi Strength (Sampled)')
ax2.set_xlabel("Time (seconds)")
ax2.set_ylabel("WiFi Strength (RSSI)")
ax2.set_title("Sampled WiFi Strength over Time")
ax2.grid(True)
ax2.set_xlim(0, 10)
ax2.set_ylim(-60, -10)

# Quantized version plot
line3, = ax3.plot([], [], 'o-', label='WiFi Strength (Quantized)')
ax3.set_xlabel("Time (seconds)")
ax3.set_ylabel("WiFi Strength (RSSI)")
ax3.set_title("Quantized WiFi Strength over Time")
ax3.grid(True)
ax3.set_xlim(0, 10)
ax3.set_ylim(-60, -10)

while True:
    rssi = get_wifi_strength()
    if rssi is not None:
        rssi_values.append(rssi)
        time_values.append(time.time())

        # Sample the RSSI value with added random noise
        sampled_rssi = rssi   # Adding random noise between -5 and 5
        sampled_rssi_values.append(sampled_rssi)

        # Quantize the sampled RSSI value
        quantized_rssi = round(sampled_rssi / 10) * 10
        quantized_rssi_values.append(quantized_rssi)

        # Update plots for all three versions
        line1.set_data(time_values, rssi_values)  # Update original signal plot
        line2.set_data(time_values, sampled_rssi_values)  # Update sampled signal plot
        line3.set_data(time_values, quantized_rssi_values)

        ax1.set_xlim(min(time_values), max(time_values) + 10)
        ax2.set_xlim(min(time_values), max(time_values) + 10)
        ax3.set_xlim(min(time_values), max(time_values) + 10)  # Adjust x-limits for all plots

        fig.canvas.draw()
        fig.canvas.flush_events()
    else:
        print("Unable to retrieve WiFi strength.")
    time.sleep(2)  # Wait for 2 seconds before the next measurement
