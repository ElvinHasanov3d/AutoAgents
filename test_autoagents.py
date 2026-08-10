# test_autoagents.py
"""
Tests for AutoAgents module.
"""

import unittest
from autoagents import AutoAgents

class TestAutoAgents(unittest.TestCase):
    """Test cases for AutoAgents class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AutoAgents()
        self.assertIsInstance(instance, AutoAgents)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AutoAgents()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
