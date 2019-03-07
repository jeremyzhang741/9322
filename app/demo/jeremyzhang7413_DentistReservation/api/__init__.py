# -*- coding: utf-8 -*-
from __future__ import absolute_import

import flask_restful as restful

from ..validators import request_validate, response_filter

Data_loc = [{
  "id":12345,
  "data":"2018-01-01,15:30",
  "complete":True,
}]

class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]