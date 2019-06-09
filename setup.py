#!/usr/bin/env python3
# coding=utf8

from setuptools import setup, find_packages

required_modules = [
	'audiogen',
	'pytest',
	'pytest-runner',
	'mock'
	]
extras_require = {
	'soundcard_output': ['PyAudio'],
}

with open("README.md", "rb") as f:
	readme = f.read().decode('utf8')

setup(
	name="mid_piano",
	version="0.0.1",
	description=u"Transform a computer keyboard into a piano",
	author="Matheus M Moscardini",
	author_email="",
	url="https://github.com/mmoscardini/mid_piano",

	packages=find_packages(exclude='tests'),
	install_requires=required_modules,
	extras_require=extras_require,

	setup_requires=["pytest-runner"],
	tests_require=["pytest"],

	long_description=readme,
	classifiers=[
		"Environment :: Console",
		"License :: OSI Approved :: BSD License",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.7",
		"Intended Audience :: Developers",
		"Intended Audience :: End Users/Desktop",
		"Topic :: Multimedia :: Sound/Audio",
		"Topic :: Communications :: Ham Radio",
	]
)