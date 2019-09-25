import Adafruit_WS2801

import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI


class GameManager:
    PIXEL_COUNT = 32

    SPI_PORT = 0
    SPI_DEVICE = 0

    objects = []
    pixels = None

    @staticmethod
    def setup():
        GameManager.pixels = Adafruit_WS2801.WS2801Pixels(GameManager.PIXEL_COUNT,
                                                          spi=SPI.SpiDev(GameManager.SPI_PORT, GameManager.SPI_DEVICE),
                                                          gpio=GPIO)
        print(GameManager.pixels)

    @staticmethod
    def run():
        GameManager.setup()

        while True:
            for obj in GameManager.objects:
                obj.update()
            GameManager.pixels.clear()
            for obj in GameManager.objects:
                obj.draw(GameManager.pixels)
            GameManager.pixels.show()
