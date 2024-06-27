from Base_CDR import BaseCDR
import h5py
import sys
import subprocess
import json
import base64
import os
import tempfile
import yaml


class H5CDR(BaseCDR):
    def __init__(self, path):
        super().__init__(path, "h5")
        self.__data = None
        self.__anomaly = False
        self.__tempFileName = None

    def scan(self):

        if not os.path.exists(self._path):
            raise FileNotFoundError("File not found")
        lambda_counter = 0
        try:
            # Open the HDF5 file
            with h5py.File(self._path, 'r+') as f:
                # Iterate over the keys (which are the group names)
                for key in f.keys():
                    print("Group:", key)
                    # Get the group
                    group = f[key]
                    # Iterate over the items (which can be datasets or subgroups) to find a lambda layer
                    for item_key in group.keys():

                        if item_key.startswith("lambda"):
                            lambda_counter += 1
                            print(f"Found suspicious layer: {item_key}, Lambda number {lambda_counter}")

                attacks_codes = []
                if lambda_counter > 0:
                    self.__anomaly = True
                    print("\nCheck if the lambda is white")
                    model_config = json.loads(f.attrs['model_config'])
                    layers = model_config['config']['layers']
                    for layer in layers:
                        if layer['class_name'] == 'Lambda':
                            attacks_codes.append(layer['config']['function']['config']['code'])
                self.__data = attacks_codes
                print(self.__data)
                self.analyze()
                return self.__anomaly
        except Exception as e:
            print("An error occurred:", e)

    def analyze(self):
        if self.__data is None:
            raise ValueError("No data to analyze, load the data first")

        # Analyze the data
        print("Analyzing the the data...")

        total_data = []
        for code in self.__data:
            # Decode the string
            total_data.append(str(base64.b64decode(code)))
        try:
            # Load the YAML configuration
            with open("config.yaml") as file:  # Replace "config.yaml" with your actual filename
                config_file = yaml.safe_load(file)
        except Exception as e:
            print("An error occurred:", e)
        # Clear the result
        self._result["bad_locations"].clear()
        self._result["bad_calls"].clear()
        self._result["bad_signals"].clear()
        self._result["bad_files"].clear()
        self._result["bad_shell_cmds"].clear()
        self._result["bad_chars"].clear()
        self._result["bad_cmds"].clear()
        self._result["bad_modules"].clear()
        self._result["bad_imports"].clear()

        total_bad = 0

        for data in total_data:
            # Check for bad locations
            for location in config_file["Windows"]:
                if location in data:
                    self._result["bad_locations"].append(location)
                    total_bad += 1
                    print(f"Bad location found: {location}")

            for location in config_file["Linux"]:
                if location in data:
                    self._result["bad_locations"].append(location)
                    total_bad += 1
                    print(f"Bad location found: {location}")

            # Check for bad calls
            for call in config_file["Bad Calls"]:
                if call in data:
                    self._result["bad_calls"].append(call)
                    total_bad += 1
                    print(f"Bad call found: {call}")

            # Check for bad signals
            for signal in config_file["Bad Signals"]:
                if signal in data:
                    self._result["bad_signals"].append(signal)
                    total_bad += 1
                    print(f"Bad signal found: {signal}")

            # Check for bad files
            for file in config_file["Bad Files"]:
                if file in data:
                    self._result["bad_files"].append(file)
                    total_bad += 1
                    print(f"Bad file found: {file}")

            # Check for bad shell commands
            for cmd in config_file["Bad Shell Cmds"]:
                if cmd in data:
                    self._result["bad_shell_cmds"].append(cmd)
                    total_bad += 1
                    print(f"Bad shell command found: {cmd}")

            # Check for bad characters
            for char in config_file["Bad Chars"]:
                if char in data:
                    self._result["bad_chars"].append(char)
                    total_bad += 1
                    print(f"Bad character found: {char}")

            # Check for bad commands
            for cmd in config_file["Bad Cmds"]:
                if cmd in data:
                    self._result["bad_cmds"].append(cmd)
                    total_bad += 1
                    print(f"Bad command found: {cmd}")

            # Check for bad modules
            for module in config_file["Bad Modules"]:
                if module in data:
                    self._result["bad_modules"].append(module)
                    total_bad += 1
                    print(f"Bad module found: {module}")

            # Check for bad imports
            for imp in config_file["Bad Imports"]:
                if imp in data:
                    self._result["bad_imports"].append(imp)
                    total_bad += 1
                    print(f"Bad import found: {imp}")

        print(f"Total bad elements found: {total_bad}")

        if total_bad == 0:
            self.__anomaly = False
            print("No bad elements found in the pickle file, it seems safe.")

        else:
            print("The keras file seems to be malicious, consider further analysis.")
        return self._result

    def disarm(self):
        try:
            destination_file = "clean.h5"
            # #destination_file = destination_file.replace('Models/', '')
            # destination_file = os.path.join(model_directory, destination_file.replace('.h5', '_safe.h5'))
            self.__tempFileName = destination_file

            # Open the source HDF5 file for reading
            with h5py.File(self._path, 'r') as source_f:
                # Open the destination HDF5 file for writing
                with h5py.File(destination_file, 'w') as dest_f:
                    # Copy attributes from source file to destination file
                    for attr_name, attr_value in source_f.attrs.items():
                        if attr_name != 'model_config':
                            dest_f.attrs[attr_name] = attr_value
                            print(f"Copied item '{attr_name}' to the new file.")
                    # Copy the weights from the source model to the target model
                    source_f.copy('model_weights', dest_f)

                    # Remove the lambda layer from the model configuration
                    if 'model_config' in source_f.attrs:
                        model_config = source_f.attrs['model_config']
                        # Remove any reference to the lambda layer from the config string
                        modified_config = self.remove_lambda_from_config(model_config)
                        # Save the modified model config back to the destination file attributes
                        dest_f.attrs['model_config'] = modified_config

                    print("The file disarm successfuly ! (⌐■_■)")
                    return True
        except Exception as e:
            print("An error occurred:", e)

    def remove_lambda_from_config(self, model_config):
        print("\n")
        # Parse the JSON-formatted string into a dictionary
        model_config_dict = json.loads(model_config)
        # Change the class name from "Functional" to "Sequential"
        model_config_dict["class_name"] = "Sequential"
        model_config_dict['config']['name'] = "sequential"
        # model_config_dict['config']['dtype'] = 'float32'
        # model_config_dict['config']['build_input_shape'] =  '[null, 784]'

        # print(model_config)
        # Access the 'config' key, then the 'layers' key from the dictionary
        layers = model_config_dict['config']['layers']
        # print(layers)
        modified_layers = []
        for layer in layers:
            if layer.get('class_name') != 'Lambda':
                modified_layers.append(layer)
            if layer.get('class_name') == 'InputLayer' or layer.get('class_name') == 'Dense':
                # Remove the 'name' key from the dictionary
                del layer['name']
                del layer['inbound_nodes']

                # Update the 'layers' key in the dictionary with the modified layers
        model_config_dict['config']['layers'] = modified_layers
        if 'input_layers' in model_config_dict['config']:
            del model_config_dict['config']['input_layers']
            del model_config_dict['config']['output_layers']

        # Convert the modified dictionary back to a JSON-formatted string
        modified_model_config = json.dumps(model_config_dict)

        # Print the pretty JSON

        return modified_model_config

    def save_as_new_file(self, path):
        path_file = path.split(".")[-1]
        print(path)
        print(path_file)
        # path_file = os.path.join("SafeModels", path)
        try:
            # Rename the file
            os.rename(self.__tempFileName, path)
            print(f"File renamed successfully: {self.__tempFileName} -> {path}")
        except OSError as e:
            # Handle potential errors (e.g., file not found, permission issues)
            print(f"Error renaming file: {e}")

