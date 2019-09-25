import Adafruit_WS2801

import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI


class PixelsManager:
    PIXEL_COUNT = 32

    SPI_PORT = 0
    SPI_DEVICE = 0

    pixels = None

    @staticmethod
    def setup():
        PixelsManager.pixels = Adafruit_WS2801.WS2801Pixels(PixelsManager.PIXEL_COUNT,
                                                            spi=SPI.SpiDev(PixelsManager.SPI_PORT, PixelsManager.SPI_DEVICE),
                                                            gpio=GPIO)
        print(PixelsManager.pixels)
