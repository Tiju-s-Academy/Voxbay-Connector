{
    'name': "Voxbay Connector",
    'author': 'Rizwaan',
    'version': "17.0.0.0",
    'sequence': "0",
    'depends': ['base','crm','odoo-rest-api'],
    'data': [
        'security/ir.model.access.csv',
        'views/call_data.xml',
    ],
    'demo': [],
    'summary': "Voxbay Connector",
    'description': "Voxbay Telphony integration plugin for Odoo",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': False
}