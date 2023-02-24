## It's Sample

directory

```
python_library_sample
    |--MANIFEST.in
    |--README.md
    |--requirements.txt
    |--setup.py
    |--src
    |  |--package_hero
    |  |  |--__init__.py
    |  |  |--superman.py
    |  |  |--common
    |  |  |  |--text.json
    |  |
    |  |--package_enemy
    |  |  |--__init__.py
    |  |  |--badman.py
    |  |  |--common
    |  |  |  |--text.png
```

- Library Name: python_library_sample
- Packages: 「src/package_hero」と「src/package_enemy」
- Modules: 「src/package_hero/superman」と「src/package_enemy/badman」
- Other Files: 「src/package_hero/common/text.json」と「src/package_enemy/common/text.json」


## Install

`1 local install` or `2 git install`


1 local install

```
your_project
|--main.py
|
|--python_library_sample
|  |--.....
```

```
pip install -e /your_project/python_library_sample
```


2 git install


```
pip install git+https://github.com/ryofujimotox/python_library_sample
```


## How it Work



``` python

```





