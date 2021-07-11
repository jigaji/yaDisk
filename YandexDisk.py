import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        headers = {'Authozation':'OAuth{}'.format(self.token)}
        file = {'file': open(file_path, 'rb')}
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {'path': file_path, 'overwrite': "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = response.json().get('href')
        upload = requests.post(href, file=file)
        return print(upload.status_code)

if __name__ == '__main__':
    uploader = YaUploader('')
    result = uploader.upload('c:\my_folder\file.txt')
