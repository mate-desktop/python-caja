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
	-DPYTHON_ABIFLAGS=\"$(PYTHON_ABIFLAGS)\" \
	-DPY_LIB_LOC="\"$(PYTHON_LIB_LOC)\"" \
	$(CAJA_PYTHON_CFLAGS) \
	$(AM_CPPFLAGS)

libcaja_python_la_CFLAGS = \
	$(PYTHON_CFLAGS)
	$(CAJA_PYTHON_CFLAGS) \
	$(AM_CFLAGS)

libcaja_python_la_LDFLAGS = -module -avoid-version -Wl,-z,defs
libcaja_python_la_LIBADD  = $(PYTHON_LIBS) $(CAJA_PYTHON_LIBS)
