from funfactory.settings_base import *


# Django Settings
##############################################################################

# Defines the views served for root URLs.
ROOT_URLCONF = 'careers.urls'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

INSTALLED_APPS = list(INSTALLED_APPS) + [
    'careers.base',
    'careers.careers',
    'careers.university',

    'django.contrib.admin',

    'django_jobvite',
    'jingo_minify',
    'south',
]


# Third-party Libary Settings
##############################################################################

# Because Jinja2 is the default template loader, add any non-Jinja templated
# apps here:
JINGO_EXCLUDE_APPS = [
    'admin',
    'registration',
]

# Accepted locales
PROD_LANGUAGES = ('de', 'en-US', 'es', 'fr',)

# Bundles is a dictionary of two dictionaries, css and js, which list css files
# and js files that can be bundled together by the minify app.
MINIFY_BUNDLES = {
    'css': {
        'base': (
            'css/base.css',
        ),
        'careers': (
            'css/careers.css',
        ),
        'careers-ie8': (
            'css/careers-ie8.css',
        ),
        'university': (
            'js/libs/video-js/video-js.css',
            'js/libs/video-js/video-js-sandstone.css',
            'css/university.css',
        ),
        'university-ie8': (
            'css/university-ie8.css',
        ),
    },
    'js': {
        'jquery': (
            'js/libs/jquery-1.7.1.min.js',
        ),
        'common': (
            'js/libs/modernizr.custom.05289.js',
            'js/libs/waypoints.min.js',
            'js/base.js',
        ),
        'listings': (
            'js/filters.js',
        ),
        'university': (
            'js/libs/video-js/video.dev.js',
            'js/university.js',
        ),
        'university_links': (
            'js/university_links.js',
        ),
        'careers': (
            'js/careers.js',
        ),
        'ie8shims': (
            'js/libs/html5shiv-printshiv.js',
        ),
        'university-ie8': (
            'js/libs/video-js/video.dev.js',
            'js/university-ie8.js',
        ),
    }
}

# Testing configuration.
NOSE_ARGS = ['--logging-clear-handlers', '--logging-filter=-factory,-south']


# Careers-specific Settings
##############################################################################

# URI of Jobvite job feed.
JOBVITE_URI = 'https://www.jobvite.com/CompanyJobs/Xml.aspx?c=qpX9Vfwa&cf=e'
