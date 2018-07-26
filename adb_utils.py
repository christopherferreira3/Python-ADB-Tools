import subprocess
import os

class AdbUtils():

    def get_connected_devices(self):
        """
        Returns a list of tuples containing the Device name and the android Version
        :return:
        """
        devices = []
        devices_output = subprocess.check_output(["adb", "devices"]).decode("utf-8").strip("List of devices attached").split("\n")
        for device in devices_output:
            if device is None or device == "":
                pass
            else:
                device_name = device.strip('\tdevice')
                android_version = subprocess.check_output(["adb", "-s", device_name, "shell", "getprop", "ro.build.version.release"])
                devices.append((device_name, android_version.decode('utf-8').strip("\r\n")))

        return devices


    def install_app(self, apk_path=None, device=None):
        """
        Installs an APK file into a device.
        The app installed with the -r option so the apk gets replaced it exists or installed if it doenst
        :param apk_path: Path for the APK
        :param device:   Device name
        :return: True if success , False if fail
        """
        if str(apk_path).startswith("/"):
            path = os.getcwd() + apk_path
        else:
            path = os.getcwd() + "/" + apk_path

        if apk_path is not None and device is not None:
            if os.path.isfile(path):
                command = ["adb", "-s" , device, "install", "-r", path]
                p = subprocess.Popen(command, stdout=None)
                p.wait()
                p.terminate()
                print("APK {0} was installed in {1}".format(apk_path, device))
                return True
            else:
                print("File {0} not found!".format(path))

        else:
            print("Device and/or apk not found or not specified")
            return False


    def is_device_connected(self, device):
        all_connected = self.get_connected_devices()
        for device_connected, version in all_connected:
            if device == device_connected:
                return True
        return False


    def unintall_app(self, package=None, device=None):
        """
        Uninstall an app from the device
        :return:
        """
        command = ["adb", "-s", device, "uninstall", package]

        if package is not None:
            if device is None:
                command.pop(1)
                command.pop(1)

            p = subprocess.Popen(command, stdout=None)
            p.wait()
            p.terminate()
        else:
            print("App package was not specified.")


    def is_app_installed(self, package=None, device=None):
        """
        Returns True if the package is installed or False if it is not
        :param package:
        :return:
        """
        command = ["adb", "-s", device, "shell", "pm", "list", "packages |", "grep", package]

        if device is None:
            command.pop(1)
            command.pop(1)

        out = subprocess.check_output(command, stderr=None)

        return True if out.decode('utf-8').strip("\r\n") == "package:{0}".format(package) else False



