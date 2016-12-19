Control Your Raspberry Pi MQTT Service through MQTT.

The project subscribes to a topic which decides when to start/stop sending data to cloud.

You can start/stop publishing data to a particulat topic through your mobile phone or web based controller or even fron the aws iot platform itself.
Just send START/STOP as Mqtt messages to the topic in the code.

Usage:
	Use your credetials to authenticate 
	Host and Certificate Details.
	Place your certificate in cert Folder.
	The Project already contains the AWSIOTSDK. So no need to install seperately.
	Start running the code and Subscribe to topic "tc/things/pub/data" to check whether everything is working fine.
	Use topic "tc/things/sub/data" to send START/STOP messages to start/stop publishing the data.
	Edit the code to extend the service to your requirement.
	
	
Contact:
	technixweb@gmail.com