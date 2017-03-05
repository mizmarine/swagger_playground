# -*- coding: utf-8 -*-
import yaml
from jsonschema import Draft4Validator, ValidationError, draft4_format_checker
import pytest


class TestRequestBodyValidator(object):
    def setup(self):
        with open('swagger/api.yaml') as f:
            spec = yaml.load(f)
        schema = spec['paths']['/member']['post']['parameters'][0]['schema']
        self.validator = Draft4Validator(schema, format_checker=draft4_format_checker)

    def test_name(self):
        data = {'name': 'masa'}
        assert self.validator.validate(data) is None

    def test_without_name(self):
        data = {}
        with pytest.raises(ValidationError):
            self.validator.validate(data)
