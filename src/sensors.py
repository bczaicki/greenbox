"""
Sensor classes for the GreenBox device.
Handles reading from various physical sensors.
"""

import logging
import random

logger = logging.getLogger(__name__)


class BaseSensor:
    """Base class for all sensors."""

    def __init__(self, pin=None):
        """Initialize sensor with optional pin."""
        self.pin = pin
        logger.debug(f"Initializing sensor on pin {pin}")

    def read(self):
        """Read sensor data. To be implemented by subclasses."""
        raise NotImplementedError("Sensor subclasses must implement read()")


class TemperatureSensor(BaseSensor):
    """Temperature sensor class."""

    def read(self):
        """Read temperature in Celsius."""
        try:
            # In a real implementation, this would read from hardware
            # Using mock data for development
            # Simulate temperature around 20°C
            temp = 20 + random.uniform(-2, 2)
            logger.debug(f"Temperature reading: {temp:.1f}°C")
            return temp
        except Exception as e:
            logger.error(f"Error reading temperature sensor: {e}")
            return None


class HumiditySensor(BaseSensor):
    """Humidity sensor class."""

    def read(self):
        """Read relative humidity percentage."""
        try:
            # In a real implementation, this would read from hardware
            # Using mock data for development
            # Simulate humidity around 60%
            humidity = 60 + random.uniform(-5, 5)
            logger.debug(f"Humidity reading: {humidity:.1f}%")
            return humidity
        except Exception as e:
            logger.error(f"Error reading humidity sensor: {e}")
            return None


class MoistureSensor(BaseSensor):
    """Soil moisture sensor class."""

    def read(self):
        """Read soil moisture level (0-100%)."""
        try:
            # In a real implementation, this would read from hardware
            # Using mock data for development
            # Simulate moisture around 50%
            moisture = 50 + random.uniform(-10, 10)
            logger.debug(f"Soil moisture reading: {moisture:.1f}%")
            return moisture
        except Exception as e:
            logger.error(f"Error reading moisture sensor: {e}")
            return None


class LightSensor(BaseSensor):
    """Light level sensor class."""

    def read(self):
        """Read light level in lux."""
        try:
            # In a real implementation, this would read from hardware
            # Using mock data for development
            # Simulate light level
            light_level = 500 + random.uniform(-100, 100)
            logger.debug(f"Light level reading: {light_level:.1f} lux")
            return light_level
        except Exception as e:
            logger.error(f"Error reading light sensor: {e}")
            return None
