# 🚀 Potential OS Flask Dashboard

Welcome to the Potential OS Flask Dashboard project! This project provides a dynamic dashboard for displaying ROV (Remotely Operated Vehicle) data and controlling the ROV remotely. The dashboard subscribes to a ROS topic (`/potential_os_data`) using rospy, a Python library for ROS, and updates the webpage in real-time with the received data. Additionally, it allows users to control the ROV through interactive elements on the dashboard.

## 🌟 Features

- Real-time display of ROV data on a dynamic dashboard.
- Control functionalities to remotely operate the ROV.
- Minimal delay between ROS message publication and display update.
- Easy setup and integration with existing ROS systems.
- Lightweight and simple Flask web server.

## 📋 Requirements

- ROS: Make sure you have ROS installed on your system.
- Python: This project requires Python 2.7+ or Python 3.x.
- Flask: Install Flask using `pip install flask`.
- rospy: Install rospy using `pip install rospy`.
- Python Virtual Environment (optional but recommended)

## 🛠️ Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yazidmarzuk/potentialOS.git
    cd potentialOS
    ```

2. Create and activate a Python virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    .\venv\Scripts\activate    # On Windows
    ```

3. Install Flask and rospy dependencies:

    ```bash
    pip install flask rospy
    ```

4. Install ROSlib.js:

    ```bash
    npm install roslib
    ```

    Note: Make sure you have Node.js and npm installed on your system. You can download them from [here](https://nodejs.org/).

## 🚀 Usage

1. Start your ROS master node:

    ```bash
    roscore
    ```

2. Launch the ROS web server (rosbridge):

    ```bash
    roslaunch rosbridge_server rosbridge_websocket.launch
    ```

3. Start your ROS node publishing data to the `/potential_os_data` topic (replace `/potential_os_data` with your actual topic):

    ```bash
    rosrun your_package_name your_node_name.py
    ```

4. Start the Flask application:

    ```bash
    python app.py
    ```

5. Open your web browser and navigate to `http://localhost:5000` to access the dynamic dashboard for Potential OS data display and control.

## 📁 File Structure

- `app.py`: Python Flask application that subscribes to the ROS topic and serves the dynamic dashboard.
- `templates/index.html`: HTML template for the dynamic dashboard displaying ROV data and control functionalities.

## 🤝 Contributing

Contributions are welcome! If you find any bugs or want to suggest improvements, please open an issue or submit a pull request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
