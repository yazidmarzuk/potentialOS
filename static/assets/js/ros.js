// Create a ROSLIB.Ros object
var ros = new ROSLIB.Ros();

// Define ROS bridge URL
var rosBridgeUrl = 'ws://localhost:9090';

// Connect to ROS
ros.connect(rosBridgeUrl);

// Define topic to subscribe to
var topicName = '/chatter';

// Create a ROSLIB.Topic object
var listener = new ROSLIB.Topic({
    ros: ros,
    name: topicName,
    messageType: 'std_msgs/Float32'
});

// Define a callback function to handle received messages
listener.subscribe(function(message) {
    // Update the HTML element with received data
    document.getElementById('data').innerHTML = message.data;
});
