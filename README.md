# Python-ADB-Tools

Installation
======
You can install this package via pip
`pip install python_adb_utils`

or

`pip3 install python_adb_utils`


Usage:
======

To use these tools you only need to import and create an instance of AdbUtils()

`from adb_utils import AdbUtils`

`adb_instance = AdbUtils()`

___

Available Methods
======

### **get_connected devices()**
This method will return you a list of tuples having the device name and Android version for that specific version.

### **install_app()**
Installs an app to the chosen device.


### **unistall_app()**
Uninstalls an app


### **is_device_connected()**
Returns True if a device is connected.


### **is_app_installed()**
Check if an app is installed on a specific device.