base_info = {
    'url': 'https://www.ema.europa.eu/en/search/search?search_api_views_fulltext=%22Clinical+investigation+of+medicinal+products%22',
    'test_url': 'https://www.ema.europa.eu/en/search/search?search_api_views_fulltext=%22Clinical%20investigation%20of%20medicinal%20products%22&page=w1',
    'selenium': {
        'ops': {
            'headless',
            'ignore-certificate-errors',
            'dns-prefetch-disable',
            'disable-extensions',
        },
        'prefs': {'download.default_directory' : 'Data/chrome_driver'},
    },
    'dirs': [
        'Data',
        'Data/pkl',
        'Data/chrome_driver',
        'Data/chrome_driver',
    ],
}
