#!/usr/bin/env python3
"""
PyCalc CLI using Python Fire
"""
import fire
from libboost import add

class Calculator(object):
    """Rust Calculator Class"""

    def native_add(self, num1, num2):
        """Native add two numbers"""
        return num1 + num2

    def accelerated_add(self, num1, num2):
        """Accelerated add two numbers"""
        return add(num1, num2)

if __name__ == "__main__":
    fire.Fire(Calculator)
    