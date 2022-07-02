# -*- coding: utf-8 -*-
from odoo import http

class Universite(http.Controller):
    @http.route('/universite/universite/', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/universite/universite/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('universite.listing', {
#             'root': '/universite/universite',
#             'objects': http.request.env['universite.universite'].search([]),
#         })

#     @http.route('/universite/universite/objects/<model("universite.universite"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('universite.object', {
#             'object': obj
#         })