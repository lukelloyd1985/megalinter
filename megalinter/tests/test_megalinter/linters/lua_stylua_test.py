# !/usr/bin/env python3
"""
Unit tests for LUA linter stylua
This class has been automatically @generated by .automation/build.py, please don't update it manually
"""

from unittest import TestCase

from megalinter.tests.test_megalinter.LinterTestRoot import LinterTestRoot


class lua_stylua_test(TestCase, LinterTestRoot):
    descriptor_id = "LUA"
    linter_name = "stylua"