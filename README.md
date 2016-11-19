# django-sparkle-project

Django-sparkle-project is a fork from [Django-sparkle](https://github.com/Mobelux/django-sparkle) - a Django application to make it easy to publish updates for your mac application using [sparkle](http://sparkle.andymatuschak.org/).

In addition to publishing updates via the appcast feed, Django-sparkle-project can also collect system profile information if sparkle is configured to report it.


## Requirements

* OpenSSL

## Setup

1. `pip install https://github.com/ruuti/django-sparkle-project`
2. Add `sparkle` to your installed apps
4. In `settings.py` add `SPARKLE_PRIVATE_KEY_PATH` which is the path to your private DSA key for signing your releases.
5. In `urls.py` include the sparkle URLs by adding something like `(r'^sparkle/', include('sparkle.urls'))`.
6. Ensure your domain name is properly configured in the sites framework.
7. `python manage.py syncdb` to create the tables needed for sparkle.

## Usage

Create an application and optionally add some versions.

The application's appcast feed will be available at `/whatever_you/configured_in/your_urls_py/(?P<application_id>\d+)/appcast.xml`.

Set the `SUFeedURL` key in your Info.plist to point to the sparkle application's appcast URL. `http://example.com/sparkle/1/appcast.xml` for example.

If you want to enable system profiling, be sure to set the `SUEnableSystemProfiling` key in your Info.plist to `YES`.

### Settings

`SPARKLE_PRIVATE_KEY_PATH`

The path to your DSA private key for signing releases.  Defaults to `None`.  If not provided, releases will not be automatically signed when uploaded.