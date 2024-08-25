# DarkSkull

![Screenshot from 2024-08-25 21-39-29](https://github.com/user-attachments/assets/031acad9-a76e-4670-8c43-fbb03729c284)

DarkSkull is a tool for performing various WiFi network security tasks, including enabling monitor mode, scanning for networks, capturing handshakes, and cracking WPA/WPA2 handshakes. This script utilizes popular tools like `airmon-ng`, `airodump-ng`, `aireplay-ng`, `hcxpcapngtool`, and `hashcat` to achieve its functionalities.

## Features

- **Monitor Mode**: Enables monitor mode on your wireless network interface.
- **Network Scanning**: Scans for WiFi networks in the vicinity.
- **Handshake Capture**: Captures WPA/WPA2 handshakes and performs a deauthentication attack to force client reconnections.
- **Handshake Cracking**: Cracks WPA/WPA2 handshakes using either GPU (with hashcat) or CPU (with aircrack-ng).

## Requirements

Ensure the following tools are installed on your system:

- **airmon-ng**: For enabling monitor mode.
- **airodump-ng**: For scanning networks and capturing handshakes.
- **aireplay-ng**: For performing deauthentication attacks.
- **hcxpcapngtool**: For converting handshake files for use with hashcat.
- **hashcat**: For GPU-based cracking.
- **aircrack-ng**: For CPU-based cracking.
- **xterm**: Required for running aireplay-ng in a separate terminal.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/ALHARAMM/F-Reporter.git
    ```

2. **Navigate to the directory**:

    ```bash
    cd F-Reporter
    ```

3. **Install the required tools**:

    For Debian-based systems (e.g., Ubuntu), you can install them with:

    ```bash
    sudo apt-get update
    sudo apt-get install aircrack-ng hashcat xterm
    ```

4. **Ensure Python 3 is installed** on your system.

## Usage

1. **Run the script**:

    ```bash
    python3 DarkSkull.py
    ```

2. **Select an option** from the menu:

    - **Monitor Mode**: Enable monitor mode on your wireless interface.
    - **Scan Area**: Scan for nearby WiFi networks.
    - **Get Handshake**: Capture a handshake from a specific network and perform a deauthentication attack.
    - **Crack Handshake**: Crack the captured handshake file using either GPU or CPU.
    - **Exit**: Exit the tool.

3. **Follow the prompts** to provide necessary inputs such as BSSID, channel number, network name, and file paths.

## Example

```bash
# Start the tool
python3 DarkSkull.py

# Example menu options:
[1] Monitor mode.
[2] Scan the networks in the area.
[3] Get a handshake file of the network.
[4] Crack a handshake file.
[5] Exit.
```

## Notes

- This tool is intended for educational purposes and ethical hacking only. Unauthorized use against networks without explicit permission is illegal and can result in severe penalties.
- Ensure you have appropriate permissions before using this tool on any network.
- Use responsibly and comply with all relevant laws and regulations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **ALHARAMM** - [GitHub Profile](https://github.com/ALHARAMM)

## Acknowledgements

- Special thanks to the developers of aircrack-ng, hashcat, and other tools used in this project.

