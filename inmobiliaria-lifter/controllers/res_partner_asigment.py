# _*_ coding: utf-8 -*-

from odoo import fields, models

class ResInmobiliariaAddCamp(models.Model):
    _name = 'res.inmobiliaria'

    property_type = fields.Many2one('property.type', 'Tipo De Propiedad', required=True, track_visibility='onchange')
    property_name = fields.Char('Nombre De La Propiedad', required=True, track_visibility='onchange')
    description = fields.Text('Descripcion', required=True, track_visibility='onchange')
    address = fields.Text('Direccion', required=True, track_visibility='onchange')
    price = fields.Float('precio', required=True, track_visibility='onchange')
    room_number = fields.Integer('Numero De Habitacion', required=True, track_visibility='onchange')
    bathroom_number = fields.Integer('Numero De Baños', required=True, track_visibility='onchange')
    total_area = fields.Integer('Area Total', required=True, track_visibility='onchange')
    area_measure = fields.Char('Medida', required=True, track_visibility='onchange')
    available_data = fields.Date('Fecha De Disponibilidad', required=True, track_visibility='onchange')
    sales_agent = fields.Many2one('res.partner', 'Agente De Ventas', required=True, track_visibility='onchange')
    photos = fields.Char('Fotografias', required=True, track_visibility='onchange')
    mane = fields.Char('Fotografias', required=True, track_visibility='onchange')
    status = fields.Char('Fotografias', required=True, track_visibility='onchange')