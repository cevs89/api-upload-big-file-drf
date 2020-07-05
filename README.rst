Basic Requirements:
==============
`>= Python 3x`

Virtual environment
==============

Step 1
-----------------
`virtualenv <path> --python=python3`

Step 2
-----------------
`source <path>/bin/activate`

Step 3
-----------------
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
`python manage.py migrate`
