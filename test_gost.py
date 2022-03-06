import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.ssl_ import create_urllib3_context

# https://stackoverflow.com/questions/40373115/how-to-select-specific-the-cipher-while-sending-request-via-python-request-modul
CIPHERS = (
    "ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:"
    "DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:GOST2012-GOST8912-GOST8912"
)


class GOSTAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs["ssl_context"] = context
        return super(GOSTAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs["ssl_context"] = context
        return super(GOSTAdapter, self).proxy_manager_for(*args, **kwargs)


s = requests.Session()
s.verify = False
s.mount("https://api.sb.mdlp.crpt.ru", GOSTAdapter())
headers = {
    "ContentType": "application/json;charset=UTF-8",
    "CacheControl": "co_cache",
    "AcceptEncoding": "ru",
    "Accept": "*/*",
    "UserAgent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0",
    "Authorization": "token 8d3c4949-5119-4349-bd04-7dfabdca365a",
}
request_body = {
    "filter": {"reg_entity_type": 1, "inn": "7727662722"},
    "start_from": 0,
    "count": 100,
}
r = s.post(
    "https://api.sb.mdlp.crpt.ru/api/v1/reestr_partners/filter",
    headers=headers,
    json=request_body,
)

print(r.text)