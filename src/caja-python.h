/*
 *  caja-python.c - Caja Python extension
 *
 *  Copyright (C) 2004 Johan Dahlin
 *
 *  This library is free software; you can redistribute it and/or
 *  modify it under the terms of the GNU General Public
 *  License as published by the Free Software Foundation; either
 *  version 2 of the License, or (at your option) any later version.
 *
 *  This library is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 *  Library General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public
 *  License along with this library; if not, write to the Free
 *  Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 */

#ifndef CAJA_PYTHON_H
#define CAJA_PYTHON_H

#include <glib-object.h>
#include <glib/gprintf.h>
#include <Python.h>

#if defined(NO_IMPORT)
#define CAJA_PYTHON_VAR_DECL extern
#else
#define CAJA_PYTHON_VAR_DECL
#endif

typedef enum {
    CAJA_PYTHON_DEBUG_MISC = 1 << 0,
} CajaPythonDebug;

extern CajaPythonDebug caja_python_debug;

#define debug(x) { if (caja_python_debug & CAJA_PYTHON_DEBUG_MISC) \
                       g_printf( "caja-python:" x "\n"); }
#define debug_enter()  { if (caja_python_debug & CAJA_PYTHON_DEBUG_MISC) \
                             g_printf("%s: entered\n", __FUNCTION__); }
#define debug_enter_args(x, y) { if (caja_python_debug & CAJA_PYTHON_DEBUG_MISC) \
                                     g_printf("%s: entered " x "\n", __FUNCTION__, y); }


CAJA_PYTHON_VAR_DECL PyTypeObject *_PyGtkWidget_Type;
#define PyGtkWidget_Type (*_PyGtkWidget_Type)

CAJA_PYTHON_VAR_DECL PyTypeObject *_PyCajaColumn_Type;
#define PyCajaColumn_Type (*_PyCajaColumn_Type)

CAJA_PYTHON_VAR_DECL PyTypeObject *_PyCajaColumnProvider_Type;
#define PyCajaColumnProvider_Type (*_PyCajaColumnProvider_Type)

CAJA_PYTHON_VAR_DECL PyTypeObject *_PyCajaInfoProvider_Type;
#define PyCajaInfoProvider_Type (*_PyCajaInfoProvider_Type)

CAJA_PYTHON_VAR_DECL PyTypeObject *_PyCajaLocationWidgetProvider_Type;
#define PyCajaLocationWidgetProvider_Type (*_PyCajaLocationWidgetProvider_Type)

CAJA_PYTHON_VAR_DECL PyTypeObject *_PyCajaMenu_Type;
#define PyCajaMenu_Type (*_PyCajaMenu_Type)

CAJA_PYTHON_VAR_DECL PyTypeObject *_PyCajaMenuItem_Type;
#define PyCajaMenuItem_Type (*_PyCajaMenuItem_Type)

CAJA_PYTHON_VAR_DECL PyTypeObject *_PyCajaMenuProvider_Type;
#define PyCajaMenuProvider_Type (*_PyCajaMenuProvider_Type)

CAJA_PYTHON_VAR_DECL PyTypeObject *_PyCajaPropertyPage_Type;
#define PyCajaPropertyPage_Type (*_PyCajaPropertyPage_Type)

CAJA_PYTHON_VAR_DECL PyTypeObject *_PyCajaPropertyPageProvider_Type;
#define PyCajaPropertyPageProvider_Type (*_PyCajaPropertyPageProvider_Type)

CAJA_PYTHON_VAR_DECL PyTypeObject *_PyCajaOperationHandle_Type;
#define PyCajaOperationHandle_Type (*_PyCajaOperationHandle_Type)

#endif /* CAJA_PYTHON_H */
