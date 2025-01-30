"""Test cases for subclassing SkyCoord."""

import pytest

from astropy.coordinates import SkyCoord

def test_custom_skycoord_property_error():
    """Test that property access errors are properly propagated."""
    class CustomCoord(SkyCoord):
        @property
        def prop(self):
            return self.random_attr  # This should raise AttributeError

    c = CustomCoord('00h42m30s', '+41d12m00s', frame='icrs')
    
    # Test that accessing a non-existent property gives the right error
    with pytest.raises(AttributeError, match="'CustomCoord' object has no attribute 'random_attr'"):
        c.prop

    # Test that accessing a truly non-existent attribute gives the right error
    with pytest.raises(AttributeError, match="'CustomCoord' object has no attribute 'not_a_real_attr'"):
        c.not_a_real_attr
