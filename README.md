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

put

```
your_project
|--main.py
|
|--python_library_sample
|  |--.....
```

debug install

```
pip install -e /your_project/python_library_sample
```


2 git install


```
pip install git+https://github.com/ryofujimotox/python_library_sample
```


## How it Work

1 put `main.py`

``` python
from package_hero import greeting
from package_enemy import greeting as enemy_greeting


def main():
    greeting()
    enemy_greeting()
    exit()


if __name__ == "__main__":
    main()
```

2 run

```
python main.py
```

3 confirm outout

```
hero: HELLO I'm HERO
hero: You are welcome
badman: We lost.
```



## Customize










