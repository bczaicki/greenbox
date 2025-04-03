"""
Scheduler for the GreenBox device.
Handles timed events and scheduled tasks.
"""

import time
import datetime
import logging
from threading import Lock

logger = logging.getLogger(__name__)

class Task:
    """Task class representing a scheduled operation."""
    
    def __init__(self, name, callback, interval=None, at_time=None, enabled=True):
        """
        Initialize a new task.
        
        Args:
            name (str): Name of the task
            callback (callable): Function to call when task is due
            interval (int, optional): Interval in seconds between executions
            at_time (str, optional): Time of day to execute (format: "HH:MM")
            enabled (bool): Whether the task is enabled
        """
        self.name = name
        self.callback = callback
        self.interval = interval
        self.at_time = at_time
        self.enabled = enabled
        self.last_run = None
        
        logger.debug(f"Task '{name}' created with interval={interval}, at_time={at_time}")
    
    def is_due(self):
        """Check if the task is due to run."""
        if not self.enabled:
            return False
            
        now = datetime.datetime.now()
        
        # Handle interval-based tasks
        if self.interval is not None:
            if self.last_run is None:
                return True
            
            elapsed = (now - self.last_run).total_seconds()
            return elapsed >= self.interval
        
        # Handle time-based tasks
        if self.at_time is not None:
            if self.last_run is not None:
                # Check if we've already run today
                if self.last_run.date() == now.date():
                    return False
            
            # Parse the time string
            try:
                hour, minute = map(int, self.at_time.split(':'))
                scheduled_time = now.replace(hour=hour, minute=minute, second=0)
                
                # Check if it's time to run
                return now >= scheduled_time
            except (ValueError, AttributeError):
                logger.error(f"Invalid time format for task '{self.name}': {self.at_time}")
                return False
        
        return False
    
    def run(self):
        """Execute the task."""
        if not self.enabled:
            return
            
        try:
            self.callback()
            self.last_run = datetime.datetime.now()
            logger.info(f"Task '{self.name}' executed at {self.last_run}")
        except Exception as e:
            logger.error(f"Error executing task '{self.name}': {e}")


class Scheduler:
    """Scheduler class for managing timed tasks."""
    
    def __init__(self):
        """Initialize the scheduler."""
        self.tasks = []
        self.lock = Lock()
        logger.info("Scheduler initialized")
    
    def add_task(self, task):
        """Add a task to the scheduler."""
        with self.lock:
            self.tasks.append(task)
        logger.debug(f"Task '{task.name}' added to scheduler")
    
    def remove_task(self, task_name):
        """Remove a task from the scheduler by name."""
        with self.lock:
            self.tasks = [t for t in self.tasks if t.name != task_name]
        logger.debug(f"Task '{task_name}' removed from scheduler")
    
    def process_due_tasks(self):
        """Process all tasks that are due to run."""
        with self.lock:
            for task in self.tasks:
                if task.is_due():
                    logger.debug(f"Executing task '{task.name}'")
                    task.run()
    
    def schedule_daily(self, name, callback, at_time):
        """Schedule a task to run daily at a specific time."""
        task = Task(name, callback, at_time=at_time)
        self.add_task(task)
        return task
    
    def schedule_interval(self, name, callback, interval):
        """Schedule a task to run at a fixed interval."""
        task = Task(name, callback, interval=interval)
        self.add_task(task)
        return task