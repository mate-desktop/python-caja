INCLUDES =						\
	-DG_LOG_DOMAIN=\"Caja-Python\"	        \
	-DDATADIR=\"$(datadir)\"			\
	-DLIBDIR=\"$(libdir)\"				\
	-I$(top_srcdir)					\
	-I$(top_builddir)				\
	$(DISABLE_DEPRECATED_CFLAGS)			\
	$(CAJA_PYTHON_CFLAGS)			\
	-DPYTHON_VERSION=\"$(PYTHON_VERSION)\"		\
	-DPY_LIB_LOC="\"$(PYTHON_LIB_LOC)\""		\
	$(PYTHON_INCLUDES)

caja_extensiondir=$(CAJA_EXTENSION_DIR)

caja_extension_LTLIBRARIES = libcaja-python.la

libcaja_python_la_SOURCES =     	\
	caja-python.c		\
	caja-python.h		\
	caja-python-object.c	\
	caja-python-object.h

libcaja_python_la_LDFLAGS = -module -avoid-version
libcaja_python_la_LIBADD  = $(CAJA_PYTHON_LIBS) $(PYTHON_LIBS)
