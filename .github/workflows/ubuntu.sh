#!/usr/bin/bash

# Use grouped output messages
infobegin() {
	echo "::group::${1}"
}
infoend() {
	echo "::endgroup::"
}

# Required packages on Ubuntu
requires=(
	ccache # Use ccache to speed up build
)

requires+=(
	autoconf-archive
	autopoint
	git
	gtk-doc-tools
	libcaja-extension-dev
	libgirepository1.0-dev
	make
	mate-common
	python3-dev
	python-gi-dev
	quilt
)

infobegin "Update system"
apt-get update -y
infoend

infobegin "Install dependency packages"
env DEBIAN_FRONTEND=noninteractive \
	apt-get install --assume-yes \
	${requires[@]}
infoend
