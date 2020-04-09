"""
Unit tests for the calculator library
"""

import vcr
import requests

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        # hehe
        assert 100 == calculator.multiply(10, 10)

    @vcr.use_cassette('fixtures/vcr_cassettes/synopsis.yaml')
    def test_iana(self):
        r = requests.get('http://www.iana.org/domains/reserved')
        assert 'Example domains' in r.text
