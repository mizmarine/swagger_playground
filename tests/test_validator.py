# -*- coding: utf-8 -*-
import yaml
from jsonschema import Draft4Validator, ValidationError, draft4_format_checker
from connexion.decorators.validation import RequestBodyValidator
import pytest


class RequestBodyValidatorTestBase(object):
    def setup(self):
        with open('swagger/api.yaml') as f:
            spec = yaml.load(f)
        schema = spec['paths'][self.path]['post']['parameters'][0]['schema']
        self.validator = Draft4Validator(schema, format_checker=draft4_format_checker)

    def assert_success(self, data):
        assert self.validator.validate(data) is None

    def assert_fail(self, data):
        with pytest.raises(ValidationError):
            self.validator.validate(data)


# 以下でも良さそうだと思ったが，flaskのcontext以外で動かすとRuntimeErrorになるので却下
class RequestBodyValidatorTestBase2(object):
    def setup(self):
        with open('swagger/api.yaml') as f:
            spec = yaml.load(f)
        schema = spec['paths'][self.path]['post']['parameters'][0]['schema']
        consumes = spec.get('consumes', ['application/json'])
        self.validator = RequestBodyValidator(schema, consumes)

    def assert_success(self, data):
        assert self.validator.validate_schema(data) is None

    def assert_fail(self, data):
        problem = self.validator.validate_schema(data)
        assert problem.status == 400


class TestMember(RequestBodyValidatorTestBase):
    path = '/member'

    def test_name(self):
        self.assert_success({'name': 'masa'})
        self.assert_success({'name': '123 '})
        self.assert_success({'name': ' '})

    def test_empty_name(self):
        self.assert_fail({'name': ''})

    def test_without_name(self):
        self.assert_fail({})
