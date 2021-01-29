# -*- coding: utf-8 -*- 
from odoo import models, fields 
class MeetingsTask(models.Model): 
    _name = 'meetings'
    _description = 'Meetings Manager'
    asunto = fields.Char('Asunto')
    trabajador = fields.Char('Trabajador')
    cliente = fields.Char('Cliente')
    informacion = fields.Char('Informacion')
    is_done = fields.Boolean('Completada?')