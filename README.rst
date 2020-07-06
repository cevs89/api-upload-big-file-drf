Basic Requirements:
==============
`>= Python 3x`

Virtual environment
==============

Step 1
-----------------
.. :: python
`virtualenv <path> --python=python3`

Step 2
-----------------
.. :: python
`source <path>/bin/activate`

Step 3
-----------------
.. :: python
`pip install -r requeriments.txt`


Config database:
==============
See folder: `simetrik/config`

You will find a file: `local.example`

Copy that file and change the extention to the new file, like this: `local.conf`

the file `local.conf` is your new file config local.
If neccesary must by change content by your config local or the production server

Note: In these file you can put any settings you need, just should not be repeated in the settings.py file


To generate the database, the following command is executed:
==============
.. :: python
`python manage.py migrate`


Generate external database - (SQLalchemy)
==============
.. :: python
`python db_setup.py`


Loaddata Users
==============
There is a default user:

`username: simetrik`
`password: backend-1234`

You can use it to request your access token.

you can load this user with the following command

.. :: python
`python manage.py loaddata fixtures/users.json`
