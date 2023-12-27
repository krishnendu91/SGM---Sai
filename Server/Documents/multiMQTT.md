##AmritaSGM MQTT Server Code Summary Report

This document provides a summary of the key components and functionalities of the AmritaSGM MQTT server code.

## Introduction
The AmritaSGM MQTT server code is a Python script designed to handle MQTT (Message Queuing Telemetry Transport) messages from various IoT devices and sensors. It acts as a message broker, receiving data and storing it in a MySQL database for further processing and analysis.

## Code Structure
The code follows a straightforward structure and flow:

1. **Imports**: The script begins by importing necessary Python modules and libraries, including `paho.mqtt.client` for MQTT communication, `json` for JSON data parsing, `grabrest` for data handling, `pymysql` for database operations, and others.

2. **Global Variables**: Global variables like `mqttclient`, `broker`, and `port` are defined to set up the MQTT client and specify the MQTT broker's address and port.

3. **MySQL Database Connection**: The script establishes a connection to a MySQL database named "AmritaSGM" with specified credentials.

4. **MQTT Client Configuration**: It configures the MQTT client with a unique client ID and enables a clean start (no session persistence).

5. **Callback Functions**: Several callback functions are defined to handle incoming MQTT messages for various topics. These functions include:
   - `test`: Handles test channel messages and logs them to the database.
   - Functions like `datafetch_dimis_gm1_direct`, `datafetch_dimis_lm1_direct`, and others process specific data types and store them in the database.
   - `on_log`: Logs MQTT client activity to the database.

6. **MQTT Message Callback Registration**: Callback functions are registered for specific MQTT topics to handle incoming messages accordingly.

7. **MQTT Client Connection**: The script connects the MQTT client to the MQTT broker, subscribes to specific MQTT topics using wildcard patterns, and enters a loop to listen for incoming messages.

## Functionality
- MQTT Message Handling: The script receives MQTT messages on various topics and parses them into JSON format.
- Database Storage: It stores the parsed data in a MySQL database named "AmritaSGM" in tables corresponding to the specific data type.
- Callbacks for Different Data Types: Custom callback functions are defined for different types of data sources, ensuring data is correctly processed and stored.
- MQTT Client Configuration: The MQTT client is configured to connect to the specified MQTT broker and subscribe to relevant topics.

## Conclusion
The AmritaSGM MQTT server code serves as a crucial component for collecting and storing data from diverse IoT devices and sensors. It efficiently handles MQTT messages and stores them in a MySQL database for further analysis and utilization within the AmritaSGM infrastructure.
