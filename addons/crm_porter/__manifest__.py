{
    'name': "Avaliação Módulo CRM",
    'version': '1.0',
    'depends': ['crm'],
    'author': "Mateus Vitor",
    'category': 'Sales/CRM',
    'description': """
        O módulo permite que os nossos consultores de venda realizem 
        o cadastro das informações de qualificação dos clientes.
    """,
    # data files always loaded at installation
    'data': [
        'views/crm_porter.xml',
    ],
}