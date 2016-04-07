SUBDIRS = src examples po

if ENABLE_GTK_DOC
SUBDIRS += docs
endif

ACLOCAL_AMFLAGS = -I m4 -I . ${ACLOCAL_FLAGS}

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = caja-python.pc

extensiondir = $(datadir)/caja/extensions
extension_in_files = libcaja-python.caja-extension.in
extension_DATA = $(extension_in_files:.caja-extension.in=.caja-extension)
%.caja-extension: %.caja-extension.in $(INTLTOOL_MERGE) $(wildcard $(top_srcdir)/po/*.po) ; $(AM_V_GEN) LC_ALL=C $(INTLTOOL_MERGE) -d -u -c $(top_builddir)/po/.intltool-merge-cache $(top_srcdir)/po $< $@

EXTRA_DIST = autogen.sh caja-python.pc.in libcaja-python.caja-extension.in
CLEANFILES = libcaja-python.caja-extension

DISTCHECK_CONFIGURE_FLAGS=--enable-gtk-doc --with-cajadir='$${libdir}/caja/extensions-2.0-distcheck'

# Build ChangeLog from GIT  history
ChangeLog:
	$(AM_V_GEN) if test -d $(top_srcdir)/.git; then \
		GIT_DIR="$(top_srcdir)/.git" git log --stat > $@; \
	fi

dist: ChangeLog

.PHONY: ChangeLog
