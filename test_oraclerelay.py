# test_oraclerelay.py
"""
Tests for OracleRelay module.
"""

import unittest
from oraclerelay import OracleRelay

class TestOracleRelay(unittest.TestCase):
    """Test cases for OracleRelay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OracleRelay()
        self.assertIsInstance(instance, OracleRelay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OracleRelay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
