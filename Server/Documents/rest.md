# AmritaSGM Server Code Summary

This document provides a summary of the key components and functionalities of the AmritaSGM server code.

## Introduction
The AmritaSGM server code is a Python-based web application that serves as a middleware for managing and controlling various aspects of Amrita Intelligent Infrastructure. It includes features for user authentication, data retrieval, and interaction with IoT devices.

## Code Structure
The code is structured into several sections, each serving a specific purpose:

1. **Imports**: The code begins by importing necessary Python modules and libraries, including Flask for web application development, MySQL for database operations, and others.

2. **App Configuration**: It configures the Flask application with database credentials, secret key, and other settings.

3. **User Authentication**: The code implements user authentication using a dictionary of pre-defined usernames and hashed passwords. Users can log in to access protected routes.

4. **Routes and Functions**: The application defines various routes and functions to handle HTTP requests. Some of the notable routes and their functionalities include:
   - `/login`: Handles user login and session management.
   - `/logout`: Logs the user out and clears the session.
   - `/timenow`: Returns the current server time.
   - `/temperature`: Retrieves temperature data from the database.
   - `/stp/test`: Executes a test command for STP (Sewage Treatment Plant) data.
   - `/stp/pumplist`: Retrieves a list of STP pumps.
   - `/stp/<meterName>`: Retrieves STP data for a specific meter.
   - `/stp/state/<meterName>`: Retrieves the state of an STP meter.
   - `/deadnodes`: Identifies and retrieves information about dead nodes.
   - `/xlgen`: Generates an Excel report.
   - `/reboot`: Initiates a server reboot.
   - `/updateserver`: Updates the server code from a Git repository.
   - `/switchname/<node>`: Retrieves switch names for a specific node.
   - `/restart`: Restarts a service.
   - `/mqttlog`: Retrieves MQTT (Message Queuing Telemetry Transport) logs.
   - Various other routes for retrieving data from different IoT devices and sensors.

5. **Database Operations**: The code connects to a MySQL database and performs operations such as inserting API logs, retrieving data, and updating switch states.

6. **APIs for IoT Devices**: The code contains commented-out routes for interfacing with Dispenser devices. These routes handle address generation, data transmission, and monetary transactions.

7. **Custom Decorators**: It defines a custom decorator `login_required` to protect routes that require user authentication.

8. **Node and Device Information**: The code includes a dictionary (`nodeId`) that maps node IDs to their corresponding URLs for IoT devices.

## Functionality
- User Authentication: Users can log in with their credentials, and unauthorized access is restricted.
- Data Retrieval: The application provides various routes to retrieve real-time data from IoT devices such as STP pumps, weather data, energy meters, and more.
- Control Commands: Some routes allow users to trigger actions on IoT devices, such as sending commands to switches and initiating server updates.
- Error Handling: The code includes error handling to address issues such as database connection errors and API access errors.
- API Logs: It logs information about API requests, including client IP addresses and user agents.

## Conclusion
The AmritaSGM server code serves as a central hub for managing and monitoring various IoT devices and sensors. It offers user authentication, data retrieval, and control capabilities, making it a crucial component of the Amrita Intelligent Infrastructure.
