# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource, Data_loc
from .. import schemas


class TimeslotsIdReserve(Resource):

    def get(self, id):
        for n in Data_loc:
            if 'id' not in n:
                continue
            if id == n['id']:
                return n, 200, None
            
            else:
                continue
        return "id not exist", 400, None

    def post(self, id):
        flag = 0
        for n in Data_loc:
            if 'id' not in n:
                continue
            if id == n['id']:
                return "id is existed", 400, None
            
            else:
                continue
        data = request.get_json(force=True)
        if data['id'] != id:
            return "wrong id input", 400, None
        
        for n in Data_loc:
            if data['data'] == n['data'] and 'id' not in n:
                flag = 1
                Data_loc.remove(n)
                break
            continue
        if flag == 0:
            return "wrong data input", 400, None
        if data['complete'] == False:
            return "wrong book input", 400, None
        Data_loc.append(data)
        return data, 200, None