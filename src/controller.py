"""
Main controller for the GreenBox device.
Handles sensor reading, scheduling, and device control.
"""

from .sensors import TemperatureSensor, HumiditySensor
from .scheduler import Scheduler
import time
import logging

logger = logging.getLogger(__name__)

class GreenBoxController:
    """Main controller class for the GreenBox device."""
    
    def __init__(self, config=None):
        """Initialize controller with optional config."""
        self.config = config or {}
        self.temp_sensor = TemperatureSensor()
        self.humidity_sensor = HumiditySensor()
        self.scheduler = Scheduler()
        self.running = False
        
        logger.info("GreenBox controller initialized")
    
    def start(self):
        """Start the controller monitoring loop."""
        self.running = True
        logger.info("Starting GreenBox controller")
        
        try:
            while self.running:
                self._process_cycle()
                time.sleep(self.config.get("cycle_interval", 60))  # Default 60 seconds
        except KeyboardInterrupt:
            logger.info("Controller stopped by user")
        except Exception as e:
            logger.error(f"Controller error: {e}")
        finally:
            self.stop()
    
    def stop(self):
        """Stop the controller."""
        self.running = False
        logger.info("GreenBox controller stopped")
    
    def _process_cycle(self):
        """Process one monitoring and control cycle."""
        # Read sensor data
        temp = self.temp_sensor.read()
        humidity = self.humidity_sensor.read()
        
        logger.debug(f"Sensor readings - Temp: {temp}°C, Humidity: {humidity}%")
        
        # Process scheduled tasks
        self.scheduler.process_due_tasks()
        
        # Implement control logic based on sensor data
        if temp > self.config.get("max_temp", 30):
            logger.info(f"Temperature too high: {temp}°C")
            # Add cooling logic here
        
        if humidity < self.config.get("min_humidity", 40):
            logger.info(f"Humidity too low: {humidity}%")
            # Add watering logic here