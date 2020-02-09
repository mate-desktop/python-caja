AC_INIT([python-caja], [1.24.0],
	[https://github.com/mate-desktop/python-caja/issues],
	[python-caja], [http://mate-desktop.org])

AC_SUBST(PACKAGE)
AC_SUBST(VERSION)

AM_INIT_AUTOMAKE(1.10 dist-xz no-dist-gzip check-news)
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])
AC_CONFIG_HEADERS(config.h)
AC_CONFIG_MACRO_DIR([m4])

CAJA_REQUIRED=1.17.1

AC_PROG_CC
AC_DISABLE_STATIC
AC_PROG_LIBTOOL

PKG_PROG_PKG_CONFIG
dnl Give error and exit if we dont have pkgconfig
AS_IF([test "x$PKG_CONFIG" = "x"],[
  AC_MSG_ERROR([you need to have pkgconfig installed !])
])

dnl i18n
GETTEXT_PACKAGE=python-caja
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE, "$GETTEXT_PACKAGE", [GetText Package])

AM_GNU_GETTEXT_VERSION([0.19.8])
AM_GNU_GETTEXT([external])
dnl Check for gtk-doc
GTK_DOC_CHECK(1.9)

dnl **************************************************
dnl * Check for Python
dnl **************************************************
AM_PATH_PYTHON([3.6])
PYTHON_PKG="python-${PYTHON_VERSION}-embed"
PKG_CHECK_MODULES([PYTHON], [${PYTHON_PKG}],,
	[
		PYTHON_PKG=python-${PYTHON_VERSION}
		PKG_CHECK_MODULES([PYTHON], [${PYTHON_PKG}])
	]
)
PYTHON_LIB_LOC="`${PKG_CONFIG} ${PYTHON_PKG} --variable=libdir`"
PYTHON_ABIFLAGS=`$PYTHON -c 'import sys; exec("try: print (sys.abiflags)\nexcept: pass")'`
AC_SUBST(PYTHON_LIBS)
AC_SUBST(PYTHON_CFLAGS)
AC_SUBST(PYTHON_LIB_LOC)
AC_SUBST(PYTHON_ABIFLAGS)

PYGOBJECT_MAJOR_VERSION=3
PYGOBJECT_MINOR_VERSION=0
PYGOBJECT_MICRO_VERSION=0

PYGOBJECT_REQUIRED=$PYGOBJECT_MAJOR_VERSION.$PYGOBJECT_MINOR_VERSION.$PYGOBJECT_MICRO_VERSION
AC_DEFINE_UNQUOTED(PYGOBJECT_MAJOR_VERSION,[$PYGOBJECT_MAJOR_VERSION], [PyGObject major version.])
AC_DEFINE_UNQUOTED(PYGOBJECT_MINOR_VERSION,[$PYGOBJECT_MINOR_VERSION], [PyGObject minor version.])
AC_DEFINE_UNQUOTED(PYGOBJECT_MICRO_VERSION,[$PYGOBJECT_MICRO_VERSION], [PyGObject micro version.])

PKG_CHECK_MODULES(CAJA_PYTHON, [pygobject-3.0 >= $PYGOBJECT_REQUIRED
                                gmodule-no-export-2.0
                                libcaja-extension >= $CAJA_REQUIRED])

PYGOBJECT_DATADIR=`$PKG_CONFIG --variable=datadir pygobject-3.0`
AC_SUBST(PYGOBJECT_DATADIR)

PYGOBJECT_PYGDOCS="`$PKG_CONFIG --variable=pygdocs pygobject-3.0`"
AC_SUBST(PYGOBJECT_PYGDOCS)

PYGOBJECT_FIXXREF="$PYTHON `$PKG_CONFIG --variable=fixxref pygobject-3.0`"
AC_SUBST(PYGOBJECT_FIXXREF)

CAJA_LIBDIR=`$PKG_CONFIG --variable=libdir libcaja-extension`
AC_SUBST(CAJA_LIBDIR)
AC_DEFINE_UNQUOTED(CAJA_LIBDIR, "$CAJA_LIBDIR", [Caja libdir])

dnl ---------------------------------
dnl Get caja extensions directory
dnl ---------------------------------
AC_ARG_WITH(cajadir,
	AS_HELP_STRING([--with-cajadir=DIR],[Installation path for Caja extension @<:@auto@:>@]),
	[ac_with_cajadir=$withval],
	[ac_with_cajadir=""])
AS_IF([test "${ac_with_cajadir}" = ""],[
	ac_with_cajadir=`$PKG_CONFIG --variable=extensiondir libcaja-extension`
])

AC_MSG_NOTICE([installing caja plugin in ${ac_with_cajadir}])
AC_SUBST([CAJA_EXTENSION_DIR], [${ac_with_cajadir}])

dnl ---------------------------------
dnl Check for gtk-doc dependencies
dnl ---------------------------------
AS_IF([test "${enable_gtk_doc}" != no],[
    dnl Check for xsltproc
    AC_PATH_PROG([XSLTPROC], [xsltproc])
    AS_IF([test -z "$XSLTPROC"],[
        echo " disabling generation of docs"
        enable_gtk_doc=no
    ])
])

AC_OUTPUT([
  Makefile
  libcaja-python.caja-extension.desktop.in
  examples/Makefile
  src/Makefile
  caja-python.pc
  docs/Makefile
  docs/reference/entities.docbook
  po/Makefile.in
])

echo
echo " caja-python $PACKAGE_VERSION"
echo
echo "      Caja Prefix:             ${prefix}"
echo "      Python version:          ${PYTHON_VERSION}"
echo "      Python library location: ${PYTHON_LIB_LOC}"
echo "      Documentation:           ${enable_gtk_doc}"
echo
