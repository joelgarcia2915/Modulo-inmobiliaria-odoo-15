# -*- coding: utf-8 -*-
# from odoo import http


# class Inmobiliaria-lifter(http.Controller):
#     @http.route('/inmobiliaria-lifter/inmobiliaria-lifter', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inmobiliaria-lifter/inmobiliaria-lifter/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inmobiliaria-lifter.listing', {
#             'root': '/inmobiliaria-lifter/inmobiliaria-lifter',
#             'objects': http.request.env['inmobiliaria-lifter.inmobiliaria-lifter'].search([]),
#         })

#     @http.route('/inmobiliaria-lifter/inmobiliaria-lifter/objects/<model("inmobiliaria-lifter.inmobiliaria-lifter"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inmobiliaria-lifter.object', {
#             'object': obj
#         })
