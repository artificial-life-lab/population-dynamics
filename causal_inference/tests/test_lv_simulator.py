#!/usr/bin/env python3
# flake8: noqa
from causal_inference import LotkaVolterra
from causal_inference import LV_PARAMS

def test_lotka_volterra():
    model = LotkaVolterra()

    assert model.A == LV_PARAMS['A']
    assert model.B == LV_PARAMS['B']
    assert model.C == LV_PARAMS['C']
    assert model.D == LV_PARAMS['D']
