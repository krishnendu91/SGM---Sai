# Code Documentation for Datafetch Dimis

This Python script collects real-time data from an Evoleo Dimis Energy Meter and publishes it using MQTT. 
The script gathers data from different ports based on the configured node and meter types, processes it, and sends it to an MQTT broker for further analysis or visualization.

## Dependencies
- The code relies on several Python libraries, including `socket`, `mqttservice`, `algorithm`, `time`, `json`, `datetime`, `pymysql`, `subprocess`, and `utils`.

## Usage
To use this code, follow these steps:
1. Ensure that you have all the required Python libraries installed.
2. Configure the MQTT broker IP address and port in the `mqttservice.mqtt_publish` function calls.
3. Customize the code to match your specific project requirements, including the node configuration, port numbers, and meter types.
4. Run the script to collect data from the Evoleo Dimis Energy Meter, process it, and publish it via MQTT.

Make sure to adapt the code to your project's hardware setup and data collection needs.

## Code Explanation
1. It uses the utils.sysinfo() function to retrieve the IP addresses (ip_eth0 and ip_wlan0) and the node ID (id_node) and prints this information.
2. The script defines port numbers for different types of meters: GM (Grid Meter) and LM (Load Meter). These port numbers are used later in the code to establish connections.
3. The dimishelper function is defined to create a TCP/IP socket for data collection from the Dimis Energy Meter. It takes two arguments: ip (IP address) and port (port number). Inside the function, it checks the port argument to determine the meter type (GM1, LM, GM2) and attempts to retrieve the meter ID using the utils.getmeterid function.
4. The code creates a TCP/IP socket, binds it to the specified ip and port, and starts listening for incoming connections. It enters a loop to wait for a connection and, once established, receives data in chunks until a complete message is received (indicated by '\r\n'). It sends response messages back to the client after receiving data. The loop continues until count reaches a certain threshold, and then it closes the connection.
5. After receiving data from the meter, the dimishelper function calls utils.dimisdecode to decode the data based on the meter type and ID and returns the decoded value.
6. The code checks the id_node to determine which meters to fetch data from based on the node's configuration. If the node ID falls within certain ranges, it fetches data from GM1 and LM1 meters. Data is fetched using the dimishelper function and published via MQTT using mqttservice.mqtt_publish.
7. The code block fetches data from GM1, LM1, and GM2 meters based on the node configuration. It publishes the data via MQTT.
8. In the case of the source node (node 1), data is fetched from GM1 and published via MQTT.
9. The code fetches the status of a switch using the utils.switchstatus function and publishes it via MQTT.
10. Finally, it prints "MQTT Success" to indicate that the data fetching and publishing process has completed.

This code is designed to collect data from various meters based on the node's configuration, decode the data, and publish it to an MQTT broker for further processing or visualization. The specific actions taken may vary depending on the node's ID and configuration.
