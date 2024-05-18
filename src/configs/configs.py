import datetime
from hydra import compose, initialize

initialize(version_base=None, config_path=".", job_name="app")

MEDIA_TYPE = 'application/soap+xml; charset=utf-8'
HEADERS = {'Server': 'gSOAP/2.8E',
        'Connection': 'close',
        'X-Frame-Options': 'DENY',
        'X-XSS-Protection': '1; mode=block',
        'X-Content-Type-Options': 'nosniff',
        'Strict-Transport-Security': 'max-age=63072000; includeSubdomains;',
        'Date': datetime.datetime.utcnow().isoformat("T") + "Z"}
PATH_TAG = compose(config_name="path_tag")