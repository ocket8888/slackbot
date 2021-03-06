#!/usr/bin/env python3

"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# To use a consistent encoding
import codecs
import os
import re
import sys

# RPMs generated for fedora/rhel/centos need to have a different name
# (debian/ubuntu automatically prepends python3-, but those do not)
import platform

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
	long_description = f.read()


setup(
	# This is the name of your project. The first time you publish this
	# package, this name will be registered for you. It will determine how
	# users can install this project, e.g.:
	#
	# $ pip install sampleproject
	#
	# And where it will live on PyPI: https://pypi.org/project/sampleproject/
	#
	# There are some restrictions on what makes a valid project name
	# specification here:
	# https://packaging.python.org/specifications/core-metadata/#name
	name="slackbot",  # Required

	# Versions should comply with PEP 440:
	# https://www.python.org/dev/peps/pep-0440/
	#
	# For a discussion on single-sourcing the version across setup.py and the
	# project code, see
	# https://packaging.python.org/en/latest/single_source_version.html
	version='1.0.0',  # Required

	# This is a one-line description or tagline of what your project does. This
	# corresponds to the "Summary" metadata field:
	# https://packaging.python.org/specifications/core-metadata/#summary
	description="A customizable 'bot for Slack (and possibly related platforms)",

	# This is an optional longer description of your project that represents
	# the body of text which users will see when they visit PyPI.
	#
	# Often, this is the same as your README, so you can just read it in from
	# that file directly (as we have already done above)
	#
	# This field corresponds to the "Description" metadata field:
	# https://packaging.python.org/specifications/core-metadata/#description-optional
	long_description=long_description,  # Optional

	# This should be a valid link to your project's main homepage.
	#
	# This field corresponds to the "Home-Page" metadata field:
	# https://packaging.python.org/specifications/core-metadata/#home-page-optional
	url='https://github.com/Sensibility/slackbot',  # Optional

	# This should be your name or the name of the organization which owns the
	# project.
	author='ocket8888',  # Optional

	# This should be a valid email address corresponding to the author listed
	# above.
	author_email='ocket8888@gmail.com',  # Optional

	# Classifiers help users find your project by categorizing it.
	#
	# For a list of valid classifiers, see
	# https://pypi.python.org/pypi?%3Aaction=list_classifiers
	classifiers=[  # Optional
		# How mature is this project? Common values are
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stable
		'Development Status :: 4 - Beta',

		# Indicate who your project is intended for
		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',

		# Topic of the project
		'Topic :: Communitcations :: Chat',
		'Topic :: Games/Entertainment',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: WSGI',
		'Topic :: Text Processing :: Markup :: HTML',
		'Topic :: Text Processing :: Markup :: LaTeX',

		# Pick your license as you wish
		'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',

		# Environment in which this program is designed to run
		'Environment :: Console',

		# Supported Operating Systems
		'Operating System :: POSIX',
		'Operating System :: POSIX :: Linux',
		'Operating System :: POSIX :: BSD',

		# Specify the Python versions you support here. In particular, ensure
		# that you indicate whether you support Python 2, Python 3 or both.
		'Programming Language :: Python :: Implementation :: CPython',
		'Programming Language :: Python :: Implementation :: PyPy',
		'Programming Language :: Python :: 3 :: Only'
	],

	# This field adds keywords for your project which will appear on the
	# project page. What does your project relate to?
	#
	# Note that this is a string of words separated by whitespace, not a list.
	keywords='preprocessor analysis static compile process preprocess pre-process',  # Optional

	# You can just specify package directories manually here if your project is
	# simple. Or you can use find_packages().
	#
	# Alternatively, if you just want to distribute a single Python file, use
	# the `py_modules` argument instead as follows, which will expect a file
	# called `my_module.py` to exist:
	#
	#
	packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

	# This field lists other packages that your project depends on to run.
	# Any package you put here will be installed by pip when your project is
	# installed, so they must be valid existing projects.
	#
	# For an analysis of "install_requires" vs pip's requirements files see:
	# https://packaging.python.org/en/latest/requirements.html
	install_requires=['setuptools', 'typing', 'slacker'],  # Optional

	# List additional groups of dependencies here (e.g. development
	# dependencies). Users will be able to install these using the "extras"
	# syntax, for example:
	#
	#   $ pip install sampleproject[dev]
	#
	# Similar to `install_requires` above, these must be valid existing
	# projects.
	# extras_require={  # Optional
	#     'dev': ['check-manifest'],
	#     'test': ['coverage'],
	# },

	# If there are data files included in your packages that need to be
	# installed, specify them here.
	#
	# If using Python 2.6 or earlier, then these have to be included in
	# MANIFEST.in as well.
	# package_data={  # Optional
	#     'connmonitor': ['package_data.dat'],
	# },

	# Although 'package_data' is the preferred approach, in some case you may
	# need to place data files outside of your packages. See:
	# http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
	#
	# In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
	data_files=[('/var/www/slackbot/', ['slackbot/modules'])],  # Optional

	# To provide executable scripts, use entry points in preference to the
	# "scripts" keyword. Entry points provide cross-platform support and allow
	# `pip` to create the appropriate form of executable for the target
	# platform.
	#
	# For example, the following would provide a command called `sample` which
	# executes the function `main` from this package when invoked:
	entry_points={  # Optional
		'console_scripts': [
			'slackbot=slackbot.__init__:main',
		],
	},

	# Runs our post-installation script to install the service
	# cmdclass={'install': installService},

	# Requires python version >= 3.4, but doesn't support python 4
	python_requires='~=3.0'
)
