# myday: a simple yet powerful app for journaling

> __Warning__: this app is not usable yet!

This is going to be a simple and powerful app for making daily journals.

## What is this app (goals)

This is a note-taking and diary writing app

### Why powerful?

Below are the basic requirements this app has to satisfy

- you can add text, image and files to your journals.
- everything is encrypted.
- you can have several journals, each with its own password.
- you have got a powerful command-line interface (CLI).

### Why simple?

There are things this app should avoid.  
looking at items below you can find.

- this is completely cli based so that anyone can make a gui for this.
- adding entries to journal is very easy.

## How to use

This app is not ready to use yet because it does not have a suitable user interface.  
but there is a sample CLI for it, you can use for testing.

### Download and Install

First, clone this repository

```bash
$ git clone 'https://github.com/ekm507/myday.git'
```

then go into folder

```bash
$ cd myday
```

We recommend you to use pipenv for easy installation:

```bash
pipenv --python 3.9 # put your own python version here instead of 3.9
pipenv install --skip-lock
```

optionally you can later lock your installation by creating a Pipfile.lock file via below code:

```bash
pipenv lock
```

or you can manually install all dependencies with pip and virtualenv

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configure this app

Then you have to configure it for yourself.  
To do so copy file `config.py.default` into `config.py`

```bash
$ cp config.py.default config.py
```

Then you need to edit `config.py` file.

Set directory and name of your database file, or the one you want to be created. for example:

```python
database_filename = '/home/myname/.myday.db'
```

Set name of your default journal. you can have several journals but one of them is your default.

```python
first_table_name = 'diary'
```

For encryption, a hash salt is needed. you do not need to change this line, but if you want to do so:

```python
hash_salt = 'your hash salt goes here'.encode()
```

### CLI usage example

The sample CLI file is named `sample_cli.py`

To show all entries in default journal:

```bash
$ python sample_cli.py show
```

When you run it, it will ask you for password. if it's first time running the app, this password will be used to encrypt
default journal.

to add a new text to the journal:

```bash
$ python sample_cli.py text 'your text goes here'
```

To add an image file to the journal. it can only use jpeg format (yet!):

```bash
$ python sample_cli.py image '/address/to/your/image.jpg'
```

To download an image and add it to the journal (cool right?)

```bash
$ python sample_cli link 'https://link_to_image.jpg'
```

## Todo

- Write a CLI

## Contributors

This app is made with great contributions from contributors.

- [Erfan Kheyrollahi](https://github.com/ekm507)
- [Mahdi Baghbani](https://github.com/MahdiBaghbani)
