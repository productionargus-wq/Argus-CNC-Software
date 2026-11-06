"""
Argus CNC Software - Automatic Title Bar & Window Icon Branding Hook
Runs on GUI initialization to enforce Argus CNC logo, window titles, and Gesture navigation.
"""

import os
import FreeCAD

# Silently enforce Gesture 3D mouse navigation (drag to rotate)
try:
    FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View").SetString(
        "NavigationStyle", "Gui::GestureNavigationStyle"
    )
except Exception:
    pass

if FreeCAD.GuiUp:
    import FreeCADGui
    from PySide import QtCore, QtGui

    def enforce_argus_branding():
        try:
            home = FreeCAD.getHomePath()
            ico_file = os.path.join(home, "bin", "Argus_Icon.ico")
            png_file = os.path.join(home, "bin", "Argus_Icon_32.png")
            if not os.path.exists(png_file):
                png_file = os.path.join(home, "icons", "Argus_Icon_32.png")

            app_icon = None
            if os.path.exists(ico_file):
                app_icon = QtGui.QIcon(ico_file)
            if not app_icon or app_icon.isNull():
                if os.path.exists(png_file):
                    app_icon = QtGui.QIcon(QtGui.QPixmap(png_file))

            if app_icon and not app_icon.isNull():
                QtGui.QApplication.setWindowIcon(app_icon)
                mw = FreeCADGui.getMainWindow()
                if mw:
                    mw.setWindowIcon(app_icon)
        except Exception:
            pass

    # Enforce branding on startup and after GUI event loop starts
    QtCore.QTimer.singleShot(0, enforce_argus_branding)
    QtCore.QTimer.singleShot(100, enforce_argus_branding)
    QtCore.QTimer.singleShot(300, enforce_argus_branding)
    QtCore.QTimer.singleShot(800, enforce_argus_branding)
