# -*- coding: utf-8 -*- 
from odoo import models, fields 
class TodoTask(models.Model): 
    _name = 'meetings'
    _description = 'Meetings Manager'
    asunto = fields.Char('Asunto', required=True)
    trabajador = fields.Char('Trabajador', required=True)
    cliente = fields.Char('Cliente', required=True)
    informacion = fields.Char('Informacion', required=True)
    is_done = fields.Boolean('Completada?')