AC_INIT([python-caja], [1.20.1],
	[https://github.com/mate-desktop/python-caja/issues],
	[python-caja], [http://mate-desktop.org])

AC_SUBST(PACKAGE)
AC_SUBST(VERSION)

AM_INIT_AUTOMAKE(1.10 dist-xz no-dist-gzip check-news)
AC_CONFIG_HEADERS(config.h)
AC_CONFIG_MACRO_DIR([m4])

CAJA_REQUIRED=1.17.1

AC_PROG_CC
AC_DISABLE_STATIC
AC_PROG_LIBTOOL

dnl Check for pkgconfig first
AC_CHECK_PROG(HAVE_PKGCONFIG, pkg-config, yes, no)
AC_PATH_PROG(PKG_CONFIG, pkg-config, no)

dnl Give error and exit if we dont have pkgconfig
if test "x$HAVE_PKGCONFIG" = "xno"; then
  AC_MSG_ERROR([you need to have pkgconfig installed !])
fi

dnl i18n
GETTEXT_PACKAGE=python-caja
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE, "$GETTEXT_PACKAGE", [GetText Package])

AM_GLIB_GNU_GETTEXT
IT_PROG_INTLTOOL([0.35.0])

dnl Check for gtk-doc
GTK_DOC_CHECK(1.9)

dnl **************************************************
dnl * Check for Python
dnl **************************************************
AM_PATH_PYTHON([2.7])
PKG_CHECK_MODULES([PYTHON], [python-${PYTHON_VERSION}])
PYTHON_LIB_LOC="`pkg-config python-${PYTHON_VERSION} --variable=libdir`"
AC_SUBST(PYTHON_LIBS)
AC_SUBST(PYTHON_CFLAGS)
AC_SUBST(PYTHON_LIB_LOC)

PYGOBJECT_MAJOR_VERSION=3
PYGOBJECT_MINOR_VERSION=0
PYGOBJECT_MICRO_VERSION=0

PYGOBJECT_REQUIRED=$PYGOBJECT_MAJOR_VERSION.$PYGOBJECT_MINOR_VERSION.$PYGOBJECT_MICRO_VERSION
AC_DEFINE_UNQUOTED(PYGOBJECT_MAJOR_VERSION,[$PYGOBJECT_MAJOR_VERSION], [PyGObject major version.])
AC_DEFINE_UNQUOTED(PYGOBJECT_MINOR_VERSION,[$PYGOBJECT_MINOR_VERSION], [PyGObject minor version.])
AC_DEFINE_UNQUOTED(PYGOBJECT_MICRO_VERSION,[$PYGOBJECT_MICRO_VERSION], [PyGObject micro version.])

PKG_CHECK_MODULES(CAJA_PYTHON, [pygobject-3.0 >= $PYGOBJECT_REQUIRED
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
if test "${ac_with_cajadir}" = ""; then
	ac_with_cajadir=`$PKG_CONFIG --variable=extensiondir libcaja-extension`
fi

AC_MSG_NOTICE([installing caja plugin in ${ac_with_cajadir}])
AC_SUBST([CAJA_EXTENSION_DIR], [${ac_with_cajadir}])

dnl ---------------------------------
dnl Check for gtk-doc dependencies
dnl ---------------------------------
if test "${enable_gtk_doc}" != no; then
    dnl Check for xsltproc
    AC_PATH_PROG([XSLTPROC], [xsltproc])
    if test -z "$XSLTPROC"; then
        echo " disabling generation of docs"
        enable_gtk_doc=no
    fi
fi

AC_OUTPUT([
  Makefile
  libcaja-python.caja-extension.in
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
echo "        Caja Prefix: ${prefix}"
echo "      Documentation: ${enable_gtk_doc}"
echo
