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

    def assert_success(self, data):
        assert self.validator.validate(data) is None

    def assert_fail(self, data):
        with pytest.raises(ValidationError):
            self.validator.validate(data)

    def test_name(self):
        self.assert_success({'name': 'masa'})
        self.assert_success({'name': '123 '})
        self.assert_success({'name': ' '})

    def test_empty_name(self):
        self.assert_fail({'name': ''})

    def test_without_name(self):
        self.assert_fail({})
