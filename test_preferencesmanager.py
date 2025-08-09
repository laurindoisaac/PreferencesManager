# test_preferencesmanager.py
"""
Tests for PreferencesManager module.
"""

import unittest
from preferencesmanager import PreferencesManager

class TestPreferencesManager(unittest.TestCase):
    """Test cases for PreferencesManager class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PreferencesManager()
        self.assertIsInstance(instance, PreferencesManager)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PreferencesManager()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
