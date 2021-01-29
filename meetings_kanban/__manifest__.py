# -*- encoding: utf-8 -*-
{
    'name': 'Meetings Kanban',
    'version': '1.0',
    'author': 'CEO',
    'description': """ Tablero Kanban para reuniones.""",
    'depends': ['meetings_user'],
    'data': ['views/meetings_kanban_views.xml',
    		 'views/meetings_board_views.xml',
    		 'views/meetings_hours_report.xml',
    		 'reports.xml'],
}