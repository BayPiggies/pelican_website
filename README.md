# pelican_website
Source files for pelican based website

How to build
virtualenv venv
. venv/bin/activate
pip install pelican markdown typogrify

git clone git@github.com:getpelican/pelican-themes.git
git clone git@github.com:BayPiggies/pelican_website.git  (or preferably your fork thereof)

cd pelican_website
make devserver

open a browser to: http://127.0.0.1:8000/

Then make your edits and save them, pelican will auto generate the website.

If you make errors, it may yield errors and you may need to run:
make devserver again
