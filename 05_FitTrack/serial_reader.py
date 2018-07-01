import sys, serial, math, atexit
import matplotlib.pyplot as plt

def serial_port():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = ""
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result = str(port)
        except (OSError, serial.SerialException):
            pass
    return result

port = serial_port()
baud = 115200

s = serial.Serial(port)
s.baudrate = baud
output_file = open("output_data.csv", 'w')
accels = []
times = []
time = 0

while True:
    data = s.readline()
    if data.decode().startswith('done'):
        plt.plot(times,accels)
        plt.xlabel('Time')
        plt.ylabel('Acceleration')
        plt.show()
        exit
    else:
        time = time + .2
        x_accel, y_accel, z_accel = data.decode().split(",")
        accel = math.sqrt(int(x_accel)**2 + int(y_accel)**2 + int(z_accel)**2)
        accels.append(accel)
        times.append(time)
        output_file = open("output_data.csv", 'a')
        output_file.write(str(accel) + ',')
        output_file.close()
        print(accel)
	
