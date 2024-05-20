# -*- coding: utf-8 -*-

# ==============================
# @author: Joycat
# @time: 2024/04/05
# ==============================

###########################################################################
##
## PLEASE DO *NOT* EDIT THIS FILE!
##
###########################################################################

###########################################################################
## RUN MAIN FUNCTION
###########################################################################

from wx import App
from myFrameMain import MyFrameMain

if __name__ == "__main__":
    app = App(False)
    frame = MyFrameMain(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()