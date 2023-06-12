import json
import matplotlib.pyplot as plt

# Read JSON data from a file
with open('./res-macos/httpserver/http.json') as file:
    data = json.load(file)

# Extract response time histogram values
histogram_data = []
for entry in data:
    response_time_histogram = entry['responseTimeHistogram']
    histogram_data.extend(float(key) for key in response_time_histogram.keys())

# Create histogram
plt.hist(histogram_data, bins=10, edgecolor='black')
plt.xlabel('Response Time')
plt.ylabel('Frequency')
plt.title('Response Time Histogram')
plt.show()
