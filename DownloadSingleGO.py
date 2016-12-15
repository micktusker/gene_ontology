import requests
class DownloadSingleGO:
    def __init__(self, go_id):
        '''Initialize with a single GO identifier.'''
        url_template = 'http://www.ebi.ac.uk/QuickGO/GTerm?id=%s&format=json'
        self._go_id = go_id
        self.url = url_template % go_id
        self._http_status_code = -1
    def get_json(self):
        '''
        Use the initialized URL to query Quick GO for the given GO identifier.
        'Set the HTTP status code for the call
        :return: JSON string
        '''
        req = requests.get(self.url)
        self._http_status_code = req.status_code
        return req.json()
    def get_http_status_code(self):
        '''
        Return the status code for the last HTTP call.
        Used to check if the call returned a code of 200. If not, this method
        gives the return code.
        :return: int
        '''
        return self._http_status_code
if __name__ == '__main__':
    import json
    dnld_go = DownloadSingleGO('GO:0003824')
    obj = dnld_go.get_json()
    print(obj['term']['name'])
    print(obj['term']['definition'])
    print(dnld_go.get_http_status_code())