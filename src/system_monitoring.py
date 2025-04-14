import tkinter as tk
from tkinter import ttk
import psutil

def main():
    # Setup window
    root = tk.Tk()
    root.title("System Process Monitor")
    root.geometry("700x500")
    root.configure(bg="black")

    # Setup style
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    fieldbackground="black",
                    rowheight=25)
    style.configure("Treeview.Heading",
                    background="black",
                    foreground="white")

    # Treeview setup
    columns = ("Name", "CPU %", "RAM %")
    tree = ttk.Treeview(root, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, anchor="center", width=150)

    tree.pack(fill="both", expand=True, pady=10)

    # Label for sensors
    sensor_label = tk.Label(root, text="", bg="black", fg="white", font=("Courier", 10))
    sensor_label.pack(pady=5)

    # Update function
    def update_tree():
        for row in tree.get_children():
            tree.delete(row)

        for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
            try:
                name = proc.info['name'] or "Unknown"
                cpu = f"{proc.info['cpu_percent']:.1f}"
                ram = f"{proc.info['memory_percent']:.1f}"
                tree.insert("", tk.END, values=(name, cpu, ram))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        info_lines = []

        battery = psutil.sensors_battery()
        if battery:
            battery_status = f"Battery: {battery.percent}% {'(Charging)' if battery.power_plugged else '(Discharging)'}"
            info_lines.append(battery_status)

        try:
            temps = psutil.sensors_temperatures()
            if temps:
                for name, entries in temps.items():
                    for entry in entries:
                        label = entry.label or 'Core'
                        info_lines.append(f"{name} - {label}: {entry.current}°C")
        except AttributeError:
            info_lines.append("Temperature not supported on this system.")

        sensor_label.config(text="\n".join(info_lines))
        root.after(3000, update_tree)

    update_tree()
    root.mainloop()

if __name__ == "__main__":
    main()
