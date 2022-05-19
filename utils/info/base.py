kwargs_info = {
    'dir_check':{
        'type': 'func',
        'name': '_dir_check'
    },
    'crawling_set':{
        'type': 'func',
        'name': '_selenium_ops_config'
    },
}


base_info = {
    'dirs': [
        'Data',
        'Data/pkl',
        'Data/chromedriver',
        'Data/download',
        'log',
    ],
}

selenium_info = {
    'options': [
        'ignore-certificate-errors',
        'dns-prefetch-disable',
        'disable-extensions',
        'headless',
    ],
    'prefs': {'download.default_directory': 'Data/chrome_driver'},
}
