# System Monitoring

## Project Overview
This project is a lightweight **System Monitoring GUI** built using **Python**, leveraging the `psutil` and `tkinter` libraries. It presents system resource usage such as CPU, RAM, and temperature in a clean, table-like format using the `ttk.Treeview` widget. The UI is styled to resemble a command-line interface, with a sleek black background and white text.

## Purpose
The main goal of this project is to create an intuitive visual tool for monitoring real-time system performance in a way that is both informative and accessible. It was developed as part of the **Induction Task for ARC - Automation & Robotics Club**, to showcase programming skills, UI/UX design, and system-level interfacing using Python.

## Features
- Displays running system processes in a tabular view
- Shows CPU and memory usage for each process
- Optionally shows system temperature (if supported by hardware)
- Periodic refresh of process data for real-time updates
- UI designed to resemble a black command prompt
- Scrollable and resizable table
- Custom column alignment and styling

## Objectives
- Understand and utilize system-level libraries like `psutil`
- Build a responsive GUI using `tkinter` and `ttk`
- Present real-time data in an intuitive and visually appealing format
- Explore data formatting and tree view customization in Python
- Demonstrate readiness for the ARC club by applying automation and interfacing concepts

## Tools & Technologies Used
- **Python 3.x**
- **psutil** - for system and process data
- **tkinter / ttk** - for the graphical user interface

## Principle Behind the Project
This project relies on the principle of **polling system data** at regular intervals using `psutil`, and updating the `Treeview` to reflect changes in real time. By abstracting hardware-level stats into an easy-to-read table, it emphasizes the core goals of automation and monitoring — key principles in robotics and system control.

## How to Use
1. **Install Requirements:**
    ```bash
    pip install psutil
    ```

2. **Run the Script:**
    ```bash
    python system_monitor.py
    ```

3. **Interact with the Interface:**
   - View running processes
   - Monitor their CPU and memory usage
   - Scroll through the list and observe real-time updates

> Note: Temperature data may only appear on systems with supported sensors.

## Future Enhancements
- Add sorting functionality to the table columns
- Add search/filter box to look up specific processes
- Include disk and network usage stats
- Add graph widgets for CPU/RAM over time
- Export process data to a CSV or log file
- Integrate dark mode toggle or user themes
- Add performance alerts or threshold warnings

---
