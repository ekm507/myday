# myday: a simple yet powerful app for journaling

__note__: this app is not usable yet!

this is going to be a simple and powerful app for making daily journals.


## what is this app (goals)

this is a note taking and diary writing app

### why powerful?

below are the basic requirements this app has to satisfy

- you can add text, image and files to your journals.
- everything is encrypted.
- you can have several journals, each with it's own password.
- you have got a powerful command-line interface (CLI).


### why simple?

there are things this app should avoid.  
looking at items below you can find.

- this is completely cli based so that anyone can make a gui for this.
- adding entries to journal is very easy.

## how to use

this app is not ready to use yet because it does not have a suitable user interface.  
but there is a sample CLI for it you can use for testing.

### download this app and install requirements

first of all, clone this repository

```bash
$ git clone 'https://github.com/ekm507/myday.git'
```

then go into folder

```bash
$ cd myday
```

we recommend usage of virtualenv to run this.
```bash
$ virtualenv .venv
$ source .venv/bin/activate
```

then you need to install required libraries
```bash
$ pip install -r requirements.txt
```


### configure this app

then you have to configure it for yourself.  
to do so copy file `config.py.default` into `config.py`

```bash
$ cp config.py.default config.py
```

then you need to edit `config.py` file.

set directory and name of your database file or the one you want to be created. for example:
```python
database_filename = '/home/myname/.myday.db'
```

set name of your default journal. you can have several journals but one of them is your default.

```python
first_table_name = 'diary'
```

for encryption, a hash salt is needed. you do not need to change this line, but if you want to do so:
```python
hash_salt = 'your hash salt goes here'.encode()
```

### sample cli usage

the sample CLI file is named `sample_cli.py`

to show all entries in default journal:

```bash
$ python sample_cli.py show
```

when you run it, it will ask you for password. if it's first time running the app, this password will be used to encrypt default journal.


to add a new text to the journal:
```bash
$ python sample_cli.py text 'your text goes here'
```

to add an image file to the journal. it can only use jpeg format

```bash
$ python sample_cli.py image '/address/to/your/image.jpg'
```

to download an image and add it to the journal
```bash
$ python sample_cli link 'https://link_to_image.jpg'
```

## todo

- write a CLI
