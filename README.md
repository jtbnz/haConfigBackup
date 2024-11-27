# Home Assistant Pyscript Integration

This guide will help you install Pyscript in Home Assistant using HACS, add the integration, copy the script into the Pyscript directory, and restart Home Assistant.

## Prerequisites

- Home Assistant installed and running
- HACS (Home Assistant Community Store) installed

## Step-by-Step Guide

### 1. Install Pyscript via HACS

1. Open Home Assistant and navigate to HACS.
2. Go to the "Integrations" tab.
3. Click on "Explore & Add Repositories".
4. Search for "Pyscript" and click on it.
5. Click on "Download" to install Pyscript.

### 2. Add the Pyscript Integration

1. After installing Pyscript, go to the Home Assistant Configuration panel.
2. Click on "Integrations".
3. Click on the "+" button to add a new integration.
4. Search for "Pyscript" and select it.
5. Follow the on-screen instructions to complete the setup.

### 3. Copy the Script into the Pyscript Directory

1. Navigate to your Home Assistant configuration directory.
2. Create a new directory called `pyscript` if it doesn't already exist.
3. Inside the `pyscript` directory, create a new file called `yaml_backup.py`.
4. Copy the script into `yaml_backup.py`:

### 4. Restart Home Assistant
After copying the script, restart Home Assistant to apply the changes.
You can restart Home Assistant from the Configuration panel by clicking on "Server Controls" and then "Restart".

