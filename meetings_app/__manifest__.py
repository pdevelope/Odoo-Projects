{ 
    'name': 'Meetings Application', 
    'version': '1.0', 
    'description': 'Manage your personal meetings.', 
    'author': 'Pablo', 
    'depends': ['base'], 
    'application': True, 
    'data' : [
        'views/meetings_app_views.xml', 
        'security/ir.model.access.csv',
            ],
}