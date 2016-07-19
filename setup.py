#!/usr/bin/python

from distutils.core import setup

setup(
	# Basic package information.
	name = 'zendesk',
	version = '0.0.0',
	packages = ['zendesk'],
	include_package_data = True,
	install_requires = ['httplib2', 'simplejson'],
	license='LICENSE.txt',
	url = 'https://github.com/alexcchan/zendesk/tree/master',
	keywords = 'zendesk api helpdesk',
	description = 'Python API Wrapper for Zendesk',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet'
	],
)


