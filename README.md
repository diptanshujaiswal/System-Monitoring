# System Process Monitor

## Overview
The System Process Monitor is a Python-based desktop application that utilizes Tkinter for GUI and Psutil for real-time system monitoring. It provides an intuitive interface for users to view currently running processes along with their CPU and RAM usage. Additionally, it displays hardware sensor information such as battery status and CPU temperature (if supported).

## Purpose
This project was developed as a part of the induction process for ARC (Automation & Robotics Club). Its main goal is to demonstrate proficiency in Python GUI development and system-level monitoring by building a useful and elegant tool for system diagnostics.

## Objectives
- Monitor system processes in real time.
- Display key resource usage metrics: CPU and RAM usage.
- Display hardware sensor data such as battery percentage and temperature.
- Build an intuitive and minimal black-themed user interface.
- Package the Python application into a standalone executable for easy sharing.

## Features
- Real-time updates of system processes.
- Displays process name, CPU usage, and RAM usage.
- Shows battery status (percentage and charging state).
- Displays temperature readings (if supported).
- Modern command-line-like UI with black background and white text.
- Available as a standalone executable (.exe) for Windows users.

## Tools and Technologies Used
- **Python**: Core programming language.
- **Tkinter**: GUI development.
- **Psutil**: For accessing system and process information.
- **PyInstaller**: For converting Python script to executable.

## Principle of Working
The application uses `psutil.process_iter()` to fetch active processes and their CPU and memory usage. It updates the TreeView widget every few seconds to reflect real-time data. Battery and temperature details are retrieved using `psutil.sensors_battery()` and `psutil.sensors_temperatures()` respectively. The GUI is designed using `Tkinter` and `ttk` widgets styled to simulate a terminal look.

## How to Use
### Running from Python
1. Ensure Python is installed on your system.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python system_monitor.py
   ```

### Running Executable
1. Navigate to the `dist` folder.
2. Double-click the `SystemMonitor.exe` file.
3. The application will open without needing Python installed.

## Future Enhancements
- Add sorting and filtering capabilities for processes.
- Include more system metrics like disk usage and network activity.
- Provide logs or reports for monitored sessions.
- Add a search bar to quickly locate specific processes.
- Build cross-platform support and compatibility.

## Contribution
This project was developed as an individual contribution for ARC club induction, demonstrating system-level programming, GUI development, and software packaging.

