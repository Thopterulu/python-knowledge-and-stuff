# Python knowledge and stuff

things, stuff, foo & bar I learnt. I didn't learn English tho...

## Python LBYL (look before you leap) vs EAFP (easier to ask forgiveness than permission)

Even if it doesn't seem's natural in python in generally better to use EAFP than LBYL.
Links that explains this :

- https://stackoverflow.com/a/204523
- https://stackoverflow.com/a/1835844

Basically they explain that it's faster to try and ask forgiveness than checking with if.. in ..

## config parsing / loading json. Why, when, where, tell me more tell me more, does he look like a ... ?

> fun fact : Configparser is in python 2.7 and python 3.5-3.X and might even be in python 4 when it will be released.

[configparser's documentation](https://docs.python.org/3/library/configparser.html)

### why parsing a config file instead of just having my values in my code

>I mean this one is kinda obvious : maintainability, reusability, the possibility to share just the file with your associates. The file is really simple to read, really simple to write, really simple to parse. Security is also a big plus, you can choose to keep this file on your computer while your git can be open to visitors.

### when should I use configfiles & configparser

> I recommand to use it in every project with logins, passwords or keys. Or even when you have to use "Globals" vars or pre execution vars. I recommand to store them in a config file.

### now you can do the same with JSON

> I wont do the full comparison between using a configparser and using a JSON but the mains points are:

|criteria|configparser|JSON|
|---|---|---|
Typing| only string |support every big types like dictionnaries, list, integers, strings...
Readability|Very readable, can contains sections|It's up to you actually, but doesn't contains section.

If you need to keep, list or dictionnaries I strongly suggest you to use JSON configparser isn't made for theses types(if you try hard you can use it actually but it will be nasty.)

## Globals in python

There's no GLOBALS in python, everything in python stays inside a file as long as you don't import them everywhere. You can use scopes inside a file (it's pretty bad, 0/10 wouldn't recommand.) but please think for the random guys that just want to read your code.

## pipenv vs virtualenv

virtualenv is the famous package from pip that helps you setup virtual environnement with a specific python and specific packages inside. Strongly helps when you have a lot of projects and a lot of python versions/dependancies.

[pipenv on github](https://github.com/pypa/pipenv)

pipenv is the same but just better, it's an overlay of virtualenv. It's made to use virtual environnements faster, better.

First thing you should know, pipenv create virtualenvs in the hidden directory named ```.local``` actually the full link is ```/Username/.local/share/virtualenvs``` in virtualenvs you will see all of your virtual envs linked to everywhere on your disk. This is the end of the people creating virtualenv in thier branch and pushing the virtualenv inside a repo or just having to use a .gitignore for the venv.

But that's not it! Pipenv can update, clean, check vulnerabilities, activate the env without having to write a ```venv/bin/activate```! It also auto detects ```requirements.txt``` files and install dependancies! It create files like requirements for other pipenv users !

[pipenv documentation](https://pipenv-fork.readthedocs.io/en/latest/)

10/10 verrrry nice.
