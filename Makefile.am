SUBDIRS = po src examples

if ENABLE_GTK_DOC
SUBDIRS += docs
endif

ACLOCAL_AMFLAGS = -I m4 -I . ${ACLOCAL_FLAGS}

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = caja-python.pc

extensiondir = $(datadir)/caja/extensions
extension_in_files = libcaja-python.caja-extension.desktop.in
extension_DATA = $(extension_in_files:.caja-extension.desktop.in=.caja-extension)
$(extension_DATA): $(extension_in_files)
	$(AM_V_GEN) $(MSGFMT) --desktop --keyword=Name --keyword=Description --template $< -d $(top_srcdir)/po -o $@

EXTRA_DIST = autogen.sh caja-python.pc.in libcaja-python.caja-extension.desktop.in
CLEANFILES = libcaja-python.caja-extension

DISTCHECK_CONFIGURE_FLAGS= \
	--enable-gtk-doc \
	--with-cajadir='$${libdir}/caja/extensions-2.0-distcheck' \
	CFLAGS='-Wno-deprecated-declarations'

# Build ChangeLog from GIT  history
ChangeLog:
	$(AM_V_GEN) if test -d $(top_srcdir)/.git; then \
		GIT_DIR="$(top_srcdir)/.git" git log --stat > $@; \
	fi

dist: ChangeLog

.PHONY: ChangeLog
