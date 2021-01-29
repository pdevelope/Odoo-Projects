#-*- coding: utf-8 -*-
from odoo import models, fields, api
class MeetingsTask(models.Model):
    _name = 'meetings'
    _inherit = ['meetings','mail.thread']
    user_id = fields.Many2one('res.users', 'Organizador')
    date_deadline = fields.Date('Fecha Reunion')
    participantes_estimados = fields.Integer('Cupo de participantes')
    horas_estimadas = fields.Integer('Estimacion en horas')
    informacion = fields.Char('Descripcion')