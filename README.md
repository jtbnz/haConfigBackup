
# Still trying to make this work so that it can access the config directory as of now this addon does not work!


# YAML Backup Addon for Home Assistant

This addon monitors specified YAML files for changes and creates backups with a timestamp whenever a change is detected. It is designed to help you keep track of changes in your Home Assistant configuration files.

## Features

- Monitors specified YAML files for changes
- Creates backups with a timestamp
- Easy to configure and use

## Installation

### Prerequisites

- Home Assistant installed and running
- Docker installed on your system

### Step-by-Step Guide


1. **Build the Docker Image**:
   - Open a terminal or command prompt and navigate to the directory where your addon files are located.
   - Run the following command to build the Docker image:
     ```bash
     docker build -t yaml_backup .
     ```

2. **Verify the Docker Image**:
   - After the build process completes, verify that the image was created successfully by running:
     ```bash
     docker images
     ```
   - You should see your `yaml_backup` image listed among the available Docker images.

3. **Run the Docker Container**:
   - To test your addon, run a container from the image using the following command:
     ```bash
     docker run -d --name yaml_backup_container yaml_backup
     ```

4. **Check the Logs**:
   - Check the logs of your running container to ensure everything is working correctly:
     ```bash
     docker logs yaml_backup_container
     ```

5. **Deploy the Addon in Home Assistant**:
    - Copy the addon directory to the `addons` folder in your Home Assistant configuration directory.
    - In Home Assistant, go to the Supervisor panel, click on "Add-on Store," and then click on the "three dots" menu in the top right corner. Select "Repositories" and add the path to your local addon repository.
    - Your addon should now appear in the list of available addons. Install and configure it using the options defined in `config.yaml`.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE . See the license file for details.

```

