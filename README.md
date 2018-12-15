# pelican_website
Source files for the BayPiggies (Bay Area Python Interest Group)
pelican-based website.

##How to build
```bash
virtualenv venv
. venv/bin/activate
pip install pelican markdown typogrify

~~git clone git@github.com:getpelican/pelican-themes.git~~
Had to make my own version to get it to work with pelican 4.0.1
git clone git@github.com:bdbaddog/pelican-themes.git
git clone git@github.com:BayPiggies/pelican_website.git
git clone --recursive https://github.com/getpelican/pelican-plugins

#(or preferably your fork thereof)

cd pelican_website
make devserver
```

open a browser to: http://127.0.0.1:8000/

Then make your edits and save them, pelican will auto generate the website.

If you make errors, it may yield errors and you may need to run:
make devserver again

## Metadata properties for meeting pages
By convention, we have the follow metadata properties for each meeting page:

* **date** - We set this to the date and time of the actual meeting (e.g. 2017-02-23 19:00).
* **modified** - We set this to the date/time of the last change to the page.
* **tags** - Be sure to include *meeting*. You might also want to include tags like *beginner*, *data-science*, or *advanced* as well as tags for the general topic of the talk.
* **category** - This should be *meetings*
* **slug** - Use meeting-YYYY-MM-DD
* **author** - We generally use the speakers name(s), rather than ours
* **summary** - Short one-line phrase (generally repeating the title)

For the current month *only*, we need the following additional tags in
order to force the meeting to show up both on the front page as well as
in the meetings tab:

* **save_as** - Set this to *index.html*
* **url** - Leave this blank

Here is an example:

~~~~
:date: 2017-02-23 19:00
:modified: 2017-01-28 13:00
:tags: meeting, data-science
:category: meetings
:slug: meeting-2017-02-23
:authors: Melanie Goetz
:summary: Python for Data Science
:save_as: index.html
:url:
~~~~
## Meetup.com integration
To create the meetup.com RSVP button, go to https://www.meetup.com/meetup_api/buttons/
and enter the meetup.com URL for the meeting. Note that you will get an authorization
error if you click the button from the test server. You need to deploy on
baypiggies.net to test the end-to-end operation.

