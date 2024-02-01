# xmacchanger

## Description
xmacchanger is a command-line tool for changing the MAC address of a network interface on Unix-like systems. It allows users to spoof their MAC address for privacy or security reasons.

## Features
- Change MAC address of a specified network interface.
- Generate a random MAC address.
- Set a custom MAC address.
- Restore the original MAC address.

## Installation
1. Clone the repository:
2. git clone https://github.com/yourusername/xmacchanger.git
3. Navigate to the project directory:
   cd xmacchanger
4. pip install -r requirements.txt
5. It's ready!
## Usage
python3 xmc.py [options]  -i (--interface) interface
- `-i, --interface`: Name of the network interface (e.g., eth0, wlan0).

### Options
- `-r, --random`: Generate and set a random MAC address.
- `-m, --mac MAC_ADDR`: Set a custom MAC address.
- `-s, --show`: Show the current MAC address.
- `-p, --permanent`: Restore the permanent(orginal) MAC address.
- `-h, --help`: Display help information.


## EXAMPLE
1. Setting a custom MAC address
2. python3 xmc.py -m 00:11:22:33:44:55 -i eth0
3. Generate and set a random MAC address
4. python3 xmc.py -r  -i eth0
5. Restore the permanent(orginal) MAC address
6. python3 xmc.py -p  -i eth0

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
