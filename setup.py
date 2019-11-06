# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

# with open("readme.md", "r", encoding='utf-8') as fh:
    # long_desc = fh.read()

setup(
    name="QssStylesheetEditor",  # ProjectName
    version="1.5",
    python_requires='>=3.0.*, <4',  # python的依赖关系
    install_requires=['PyQt5', 'Qscintilla'],

    # Module
    package_dir={'': 'src'},  # tell distutils packages are under src
    packages=find_packages(where='src', include=('*'), exclude=[
        '*.bak',
    ]),  #
    py_modules=['app', 'bootstrapper'],  # single file

    # data
    package_data={
        'config': ['*.toml'],  # *.toml files found in config package
        'data': ['*.qss', '*.qsst'],
        'i18n': ['*.qm', '*.toml'],
        'res': ['*'],
        '': ['*.zip']
    },
    exclude_package_data={
        '': [
            '*.ts',
            '*.qrc',
        ],
        'res': [
            'img',
        ],
        'data':['__init__.py'] # not work
    },

    # excutable
    # scripts=['src/app.py','src/bootstrapper.py'],# 指定脚本会被安装到Python3x/Scripts下
    entry_points={
        "console_scripts":[
        'qsseditor = bootstrapper', # create qsseditor.exe in Python3x/Scripts
        'qssteditor =  app:main', # app:main
        ],
        "gui_scripts":[
        'QssStylesheetEditor = bootstrapper',
        ]
    },

    # metadata to display on PyPI
    author='lileilei',
    author_email='hustlei@sina.cn',
    description="A Qt Stylesheet(QSS) editor",
    keywords="QSS",
    # long_description=long_desc,
    # long_description_content_type="text/markdown",
    url="https://github.com/hustlei/QssStylesheetEditor"  # project home page, if any
)

# <https://www.jianshu.com/p/e0e7420e3141>
# <https://www.cnblogs.com/yangwm/p/11243346.html>
# <https://www.cnblogs.com/ls-2018/p/10451393.html>

# python setup.py build  # 编译
# python setup.py sdist  # zip格式包
# python setup.py bdist_wininst # exe格式包
# python setup.py bdist_rpm # rpm格式包
# python setup.py bdist --help-formats # 获取所有支持的平台
# python setup.py --help-commands 显示相关可用命令
# python setup.py install #安装
