# -*- coding: utf-8 -*-

def get(id):
    print('fetch user [{0}]'.format(id))
    return {'id': id, 'name': 'taro'}

def post(data):
    print(data)
    return data
