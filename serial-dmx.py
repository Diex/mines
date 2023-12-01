
import serial

# Open the serial port for communication with the USB device
ser = serial.Serial('/dev/ttyUSB0', 115200)

# Function to send DMX message
def send_dmx_message(channel, value):
    # Create the DMX message
    message = [0] * 512
    message[channel - 1] = value

    # Send the DMX message
    ser.write(message)

# Example usage
send_dmx_message(1, 255)  # Set channel 1 to full intensity
send_dmx_message(2, 128)  # Set channel 2 to half intensity

# Close the serial port
ser.close()

