#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull
# See LICENSE.rst for details.

"""
Tests for the :py:mod:`OPi.sysfs` module.
"""
import pytest

from OPi.sysfs import export, unexport, direction, input, output, edge
from OPi.constants import IN, OUT, LOW, HIGH, NONE, RISING, FALLING, BOTH


def test_export(fs):
    fs.CreateFile("/sys/class/gpio/export")
    export(19)
    with open("/sys/class/gpio/export") as fp:
        assert fp.read() == "19"


def test_unexport(fs):
    fs.CreateFile("/sys/class/gpio/unexport")
    unexport(26)
    with open("/sys/class/gpio/unexport") as fp:
        assert fp.read() == "26"


@pytest.mark.parametrize("test_input,expected", [
    (IN, "in"),
    (OUT, "out"),
])
def test_direction(fs, test_input, expected):
    fs.CreateFile("/sys/class/gpio/gpio198/direction")
    direction(198, test_input)
    with open("/sys/class/gpio/gpio198/direction") as fp:
        assert fp.read() == expected


@pytest.mark.parametrize("test_input,expected", [
    ("0", LOW),
    ("1", HIGH),
])
def test_input(fs, test_input, expected):
    fs.CreateFile("/sys/class/gpio/gpio0/value")
    with open("/sys/class/gpio/gpio0/value", "w") as fp:
        fp.write("{0}\n".format(test_input))
    assert input(0) == expected


@pytest.mark.parametrize("test_input,expected", [
    (LOW, "0"),
    (HIGH, "1"),
])
def test_output(fs, test_input, expected):
    fs.CreateFile("/sys/class/gpio/gpio15/value")
    output(15, test_input)
    with open("/sys/class/gpio/gpio15/value") as fp:
        assert fp.read() == expected


@pytest.mark.parametrize("test_input,expected", [
    (NONE, "none"),
    (RISING, "rising"),
    (FALLING, "falling"),
    (BOTH, "both"),
])
def test_edge(fs, test_input, expected):
    fs.CreateFile("/sys/class/gpio/gpio5/edge")
    edge(5, test_input)
    with open("/sys/class/gpio/gpio5/edge") as fp:
        assert fp.read() == expected
