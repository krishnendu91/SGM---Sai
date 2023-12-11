# Code Documentation for Utils.py

This Python code is for monitoring and controlling various devices using MQTT communication, as well as for handling data from different types of meters. 
The code is designed to work with the AmritaSGM project and includes functionality for the following:

1. **Switch Control (`switchrest`)**
    - Update the state of a switch and publish it using MQTT.
    - Retrieve IP addresses and node ID for communication.

2. **Meter ID Retrieval (`getmeterid`)**
    - Retrieve a meter ID based on node ID and meter type from a MySQL database.

3. **System Information Retrieval (`sysinfo`)**
    - Retrieve IP addresses and node ID using system commands.

4. **Data Decoding for DIMIS Meters (`dimisdecode`)**
    - Decode data received from DIMIS meters.
    - Extract various parameters such as voltage, current, power, energy, and more.
    - Create a JSON object with decoded values.

5. **Database Dump for DIMIS Meters (`todbdimis`)**
    - Insert decoded DIMIS meter data into a MySQL database.

6. **Database Dump for MAXIM Meters (`todbmaxim`)**
    - Insert MAXIM meter data into a MySQL database.

7. **Switch Status Update (`switchstatus`)**
    - Update the status of a contactor switch.
    - Decode I2C data to determine the switch status.
    - Insert the switch status into a MySQL database.

8. **Database Dump for Schneider Meters (`todbsch`)**
    - Insert Schneider meter data into a MySQL database.

## Dependencies
- The code relies on several Python libraries, including `socket`, `mqttservice`, `time`, `json`, `datetime`, `pymysql`, and `subprocess`.

## Usage
To use this code, follow these steps:
1. Ensure that you have all the required Python libraries installed.
2. Configure the MQTT broker IP address and port in the `mqttservice.mqtt_publish` function calls.
3. Configure the MySQL database connection details in the `pymysql.connect` function calls.
4. Use the provided functions as needed for your project to control switches, retrieve meter IDs, decode meter data, and insert data into the database.

Please make sure to customize the code to fit your specific project requirements and database setup.
