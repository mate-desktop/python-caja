caja_extensiondir=$(CAJA_EXTENSION_DIR)

caja_extension_LTLIBRARIES = libcaja-python.la

libcaja_python_la_SOURCES =     	\
	caja-python.c		\
	caja-python.h		\
	caja-python-object.c	\
	caja-python-object.h

libcaja_python_la_CPPFLAGS = \
	-I$(top_srcdir)	\
	-I$(top_builddir) \
	-DG_LOG_DOMAIN=\"Caja-Python\" \
	-DDATADIR=\"$(datadir)\" \
	-DLIBDIR=\"$(libdir)\" \
	-DPYTHON_VERSION=\"$(PYTHON_VERSION)\" \
	-DPY_LIB_LOC="\"$(PYTHON_LIB_LOC)\"" \
	$(PYTHON_INCLUDES) \
	$(AM_CPPFLAGS)

libcaja_python_la_CFLAGS = \
	$(CAJA_PYTHON_CFLAGS) \
	$(AM_CFLAGS)

libcaja_python_la_LDFLAGS = -module -avoid-version
libcaja_python_la_LIBADD  = $(CAJA_PYTHON_LIBS) $(PYTHON_LIBS)
