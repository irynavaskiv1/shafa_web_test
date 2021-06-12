import os


def get_logs_and_put_to_log_file():
    pass


def run():
    testPath = r'D:\work_with_shafa_website\tests'
    os.system(f'pytest -svx {testPath}')


run()
