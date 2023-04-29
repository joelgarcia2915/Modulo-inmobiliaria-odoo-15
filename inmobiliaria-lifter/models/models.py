# -*- coding: utf-8 -*-

from odoo import models, fields

#class ResInmobiliaria(models.Model):
#     _name = 'res.inmobiliaria'
#   _description = 'inmobiliaria'

#    name = fields.Char("Nombre")
#   state =fields.Char("Estado")
#    value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
