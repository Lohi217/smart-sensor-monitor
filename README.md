Project Description

The Smart Sensor Monitoring & Alert System is a Python-based application designed to monitor and analyze temperature, humidity, voltage, and current sensor readings. It evaluates sensor values against predefined safety thresholds and classifies them as NORMAL, WARNING, or CRITICAL.

The system provides a sensor dashboard, smart alert summary, CSV-based data logging, statistical analysis, trend analysis, and input validation. These capabilities help users identify abnormal sensor conditions, track sensor data, and understand changes in system parameters effectively.

Key Features

• Multi-sensor monitoring for temperature, humidity, voltage, and current.
• Automatic NORMAL, WARNING, and CRITICAL status classification.
• Sensor dashboard for quick monitoring.
• Smart alert summary for abnormal conditions.
• CSV-based sensor data logging with timestamps.
• Statistical analysis including average, minimum, and maximum values.
• Trend analysis to identify increasing, decreasing, and stable readings.
• Input validation and error handling for reliable operation.
• Git and GitHub based version-controlled development.

Technologies Used

• Python
• Python CSV Module
• Python Datetime Module
• Git
• GitHub

How to Run

1. Install Python 3.x on your system.
2. Clone this repository:
   git clone https://github.com/Lohi217/smart-sensor-monitor.git
3. Open the project folder:
   cd smart-sensor-monitor
4. Run the program:
   python sensor_monitor.py
5. Select the required option from the menu and enter the sensor readings.
6. Use the available options to view statistics, dashboard, alerts, and trend analysis.

The sensor readings are automatically stored in "sensor_data.csv" for future analysis.

Sample Output

========================================
     SMART SENSOR MONITORING SYSTEM
========================================

1. Enter Sensor Readings
2. View Statistics
3. View Dashboard
4. Smart Alert Summary
5. Trend Analysis
6. Exit

--- ENTER SENSOR READINGS ---
Temperature (°C): 38
Humidity (%): 75
Voltage (V): 5.2
Current (A): 1.2

----------- CURRENT STATUS ------------
Temperature : 38.00 °C [WARNING]
Humidity    : 75.00 % [WARNING]
Voltage     : 5.20 V [WARNING]
Current     : 1.20 A [WARNING]

OVERALL STATUS: WARNING

The system can also display sensor statistics, dashboard information, smart alerts, and trend analysis. Sensor readings are stored in "sensor_data.csv" for further analysis.

Git Workflow Demonstration

Git was used throughout the development of this project to track changes, maintain versions, and build the application systematically.

The project was developed through multiple meaningful commits, with each commit representing a specific stage of development. New functionality was added incrementally, including sensor monitoring, threshold detection, statistics, dashboard, smart alerts, CSV data logging, trend analysis, and input validation.

This approach allows the development history to be reviewed, different versions to be maintained, and previous working versions to be recovered when required. GitHub was used to host the source code and maintain the complete version history.
