from time import sleep
import spidev
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  # or GPIO.setmode(GPIO.BOARD)

class EPaperDisplay:
    def __init__(self, width, height, cs_pin, dc_pin, reset_pin):
        self.width = width
        self.height = height
        self.cs_pin = cs_pin
        self.dc_pin = dc_pin
        self.reset_pin = reset_pin
        self.spi = spidev.SpiDev()
        self.init_display()

    def init_display(self):
        GPIO.setup(self.cs_pin, GPIO.OUT)
        GPIO.setup(self.dc_pin, GPIO.OUT)
        GPIO.setup(self.reset_pin, GPIO.OUT)

        self.spi.open(0, 0)
        self.spi.max_speed_hz = 2000000

        self.reset_display()
        self.send_command(0x12)  # Software reset
        sleep(0.1)
        self.send_command(0x01)  # Driver output control
        self.send_data((self.height - 1) & 0xFF)
        self.send_data(((self.height - 1) >> 8) & 0xFF)
        self.send_data(0x00)  # GD = 0; SM = 0; TB = 0

    def reset_display(self):
        GPIO.output(self.reset_pin, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(self.reset_pin, GPIO.LOW)
        sleep(0.1)
        GPIO.output(self.reset_pin, GPIO.HIGH)
        sleep(0.1)

    def send_command(self, command):
        GPIO.output(self.dc_pin, GPIO.LOW)
        GPIO.output(self.cs_pin, GPIO.LOW)
        self.spi.xfer2([command])
        GPIO.output(self.cs_pin, GPIO.HIGH)

    def send_data(self, data):
        GPIO.output(self.dc_pin, GPIO.HIGH)
        GPIO.output(self.cs_pin, GPIO.LOW)
        self.spi.xfer2([data])
        GPIO.output(self.cs_pin, GPIO.HIGH)

    def update_display(self, image_data):
        self.send_command(0x10)  # Write RAM
        for byte in image_data:
            self.send_data(byte)
        self.send_command(0x12)  # Refresh display
        sleep(2)

    def clear_display(self):
        self.send_command(0x10)  # Write RAM
        for _ in range(self.width * self.height // 8):
            self.send_data(0xFF)  # Clear the display
        self.send_command(0x12)  # Refresh display
        sleep(2)

    def close(self):
        self.spi.close()
        GPIO.cleanup()