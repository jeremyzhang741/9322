# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource, Data_loc
from .. import schemas


class Timeslots(Resource):

    def get(self):

        return Data_loc, 200, None

    def post(self):
        
        data = request.get_json(force=True)
        Data_loc.append(data)
        return data, 200, None