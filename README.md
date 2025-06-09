# Badgel
A GUI for MHohenberg's fork of https://github.com/jnweiger/led-name-badge-ls32
This tool allows you to upload text and images to a 44x11 LED name badge

## Features
Write up to 8 messages
Choose one of 9 different animations for each message
Choose the speed of each message
Insert images into messages (Image should be 44x11 at the largest)
To add selectable images, place a PNG file in the gfx folder

## Installation/Dependencies

### Debian/Ubuntu

    sudo pip install pyhidapi
    sudo apt-get install libhidapi-hidraw0
    sudo ln -s /usr/lib/x86_64-linux-gnu/libhidapi-hidraw.so.0  /usr/local/lib/
  or
    sudo apt install python3-usb

### Mac

    pip install pyhidapi
    brew install hidapi

### Windows 10

    Download inf-wizard.exe to your desktop. Right click 'Run as Administrator'
       -> Click 0x0416 0x5020 LS32 Custm HID
       -> Next -> Next -> Documents LS32_Sustm_HID.inf -> Save (we don't need that file)
       -> Install Now... -> Driver Install Complete -> OK

    Download python from python.org
      [x] install Launcher for all Users
      [x] Add Python 3.7 to PATH
       -> Click the 'Install Now ...' text message.

    Run cmd.exe as Administrator, enter:
      pip install pyusb
