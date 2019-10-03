# Create a virtual serial port by writing
#   sudo socat PTY,link=/dev/ttyS18 PTY,link=/dev/ttyS19
#   chmod a+rw /dev/ttyS18
#   chmod a+rw /dev/ttyS19
# Now there is a virtual serial tunnel between /dev/ttyS18 and /dev/ttyS19
# Also make sure that user is in the 'dialout' group
# You can test the serial connection with 'cu'
#   cu -s 9600 -l /dev/ttyS18
# To exit press ~~.   (escape character in cu is ~)

import sys
import glob
import serial # https://pyserial.readthedocs.io/en/latest/shortintro.html

def list_serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException) as err:
            #print("OS error: ", err)
            #print("OS error: {0}".format(err))
            pass
    return result


if __name__ == '__main__':
    ports = list_serial_ports()
    if (len(ports) == 0):
        raise SystemExit('Error: No available Serial ports found')
    
    print("Available ports:", ports)
    
    # Open first available port
    ser = serial.Serial(ports[0])
    
    # Write some data to the port
    writeMsg = 'Test'
    bwriteMsg = writeMsg.encode()    
    print("Writing to port:", writeMsg.encode())
    ser.write(writeMsg.encode()) # could also have been:  ser.write(b'Test')
    
    # Read available data from port    
    data = ser.read_all()
    print("Read available data:", data)