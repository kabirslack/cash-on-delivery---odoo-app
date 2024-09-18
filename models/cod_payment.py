from odoo import api, fields, models

class PaymentAcquirerCOD(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('cod', 'Cash on Delivery')], ondelete={'cod': 'set default'})

    def _get_cod_urls(self):
        return {
            'return_url': '/payment/cod/return',
        }

    def cod_form_generate_values(self, values):
        """Generate values for the Cash on Delivery method."""
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        values.update({
            'return_url': f'{base_url}/payment/cod/return',
        })
        return values
