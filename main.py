import winapps
import json
from datetime import datetime

with open('bad_version_program.json', encoding='utf-8') as json_file:
    bad_version_program = json.load(json_file)
    pass


def get_app_version(app_name):
    for app in winapps.search_installed(name=app_name):
        app_version = app.version
        if app_version is not None:
            return app_version


def save_to_file(to_save):
    with open('file.txt', 'a+') as txt_file:
        txt_file.write(f'\n\n{datetime.now().strftime("%d.%m.%Y | %H:%M:%S")}')
        txt_file.write(f'\n{"-" * 25}')
        for i in to_save['data']:
            txt_file.write(f'\n{i["name"]} | {i["version"]}'
                           f'\nОпасность: {i["danger"]}'
                           f'\nРекомендации: {i["recomedation"]}')
    input()


def main():
    exploit_data = dict()
    exploit_data['data'] = list()
    for i in bad_version_program['data']:
        a = get_app_version(i['name'])
        if a is not None:
            user_app_version = int(a.replace('.', ''))
            fstek_app_version = int(i['version'].replace('.', ''))
            if user_app_version <= fstek_app_version:
                print(f'{i["name"]} версии {a} не соответствует версии {i["version"]} и выше\n'
                      f'Опасность: {i["danger"]}\n'
                      f'Рекомендация: {i["recomedation"]}')
                exploit_data['data'].append({
                    'name': i['name'],
                    'version': a,
                    'danger': i['danger'],
                    'recomedation': i['recomedation']
                })
    if len(exploit_data['data']) == 0:
        print('Уязвимостей нет')
        input()
    else:
        save_to_file(exploit_data)


if __name__ == '__main__':
    main()
