import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {TOKEN}'
        }
        params = {'path': file_path, 'overwrite': 'true'}
        url_ya = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        response = requests.get(url_ya, headers=headers, params=params)
        if response.status_code == 200:
            print('Ответ получен')
        else:
            print('Ошибка в URL')
        url_ya_upload = response.json()
        href = url_ya_upload['href']
        response = requests.put(href, data=open(file_path, 'rb'))
        if response.status_code == 201:
            print('Файл загружен')
        else:
            print('Проверьте status code загрузки')



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input(f'Введите путь к файлу на пк: ')
    token = input(f'Введите ваш TOKEN: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
