"""
Tests for the GreenBox controller.
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the parent directory to the path so we can import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controller import GreenBoxController
from src.sensors import TemperatureSensor, HumiditySensor


class TestGreenBoxController(unittest.TestCase):
    """Test cases for GreenBoxController."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.controller = GreenBoxController()
    
    def tearDown(self):
        """Tear down test fixtures."""
        if self.controller.running:
            self.controller.stop()
    
    def test_initialization(self):
        """Test controller initialization."""
        self.assertIsInstance(self.controller.temp_sensor, TemperatureSensor)
        self.assertIsInstance(self.controller.humidity_sensor, HumiditySensor)
        self.assertFalse(self.controller.running)
    
    @patch('src.controller.time.sleep', return_value=None)
    def test_start_stop(self, mock_sleep):
        """Test controller start and stop."""
        # Mock _process_cycle to avoid infinite loop
        self.controller._process_cycle = MagicMock()
        
        # Start in a separate thread to avoid blocking
        import threading
        thread = threading.Thread(target=self.controller.start)
        thread.daemon = True
        thread.start()
        
        # Allow time for the thread to start
        import time
        time.sleep(0.1)
        
        # Check if running
        self.assertTrue(self.controller.running)
        
        # Stop the controller
        self.controller.stop()
        
        # Check if stopped
        self.assertFalse(self.controller.running)
        
        # Check if _process_cycle was called at least once
        self.controller._process_cycle.assert_called()
    
    @patch('src.sensors.TemperatureSensor.read', return_value=25.0)
    @patch('src.sensors.HumiditySensor.read', return_value=60.0)
    def test_process_cycle_normal(self, mock_humidity, mock_temp):
        """Test process cycle with normal temperature and humidity."""
        self.controller.scheduler.process_due_tasks = MagicMock()
        
        # Process one cycle
        self.controller._process_cycle()
        
        # Check that sensors were read
        mock_temp.assert_called_once()
        mock_humidity.assert_called_once()
        
        # Check that scheduler was called
        self.controller.scheduler.process_due_tasks.assert_called_once()
    
    @patch('src.sensors.TemperatureSensor.read', return_value=35.0)  # High temperature
    @patch('src.sensors.HumiditySensor.read', return_value=30.0)  # Low humidity
    def test_process_cycle_alert_conditions(self, mock_humidity, mock_temp):
        """Test process cycle with alert conditions."""
        self.controller.scheduler.process_due_tasks = MagicMock()
        
        # Set alert thresholds
        self.controller.config = {
            'max_temp': 30,
            'min_humidity': 40
        }
        
        # Process one cycle
        with self.assertLogs(level='INFO') as cm:
            self.controller._process_cycle()
            
            # Check for alert log messages
            self.assertTrue(any('Temperature too high: 35.0°C' in msg for msg in cm.output))
            self.assertTrue(any('Humidity too low: 30.0%' in msg for msg in cm.output))


if __name__ == '__main__':
    unittest.main()