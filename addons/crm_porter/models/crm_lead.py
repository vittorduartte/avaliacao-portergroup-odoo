from odoo import models, fields


class CrmPorter(models.Model):
    _inherit = 'crm.lead'

    qtd_unidade = fields.Integer(string='Quantidade de unidades')
    qtd_blocos = fields.Integer(string='Quantidade de blocos')
    qtd_moradores = fields.Integer(string='Quantidade de moradores')
    tipo_portaria = fields.Selection(string='Tipo de portaria', selection=[('propria', 'Própria'), ('terceirizada', 'Terceirizada')])
    turno_portaria = fields.Selection(string='Turno de portaria', selection=[('12', '12 Horas'), ('24', '24 Horas')])
