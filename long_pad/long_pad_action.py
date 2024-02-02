#!/usr/bin/env python

import pcbnew
import os
import wx


def v(x_mm, y_mm):
    return pcbnew.VECTOR2I(pcbnew.wxPointMM(x_mm, y_mm))


class LongPadAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Long Pad"
        self.category = "Modify PCB"
        self.description = "Make round pad oblong"
        self.icon_file_name = os.path.join(
            os.path.dirname(__file__), "./resources/long-pad.png")
        self.show_toolbar_button = True

    def Run(self):
        # Filter just selected footprints
        selected_footprints: list[pcbnew.FOOTPRINT] = [
            footprint for footprint in pcbnew.GetCurrentSelection()
            if type(footprint).__name__ == 'PAD'
        ]

        if len(selected_footprints) == 0:
            # Show info dialog
            dlg = wx.MessageDialog(None, "Please select one or multiple footprints!",
                                   "No footprints selected", wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        print("Selected footprints: ", len(selected_footprints))
        for pad in selected_footprints:
            if pad.GetShape() == pcbnew.PAD_SHAPE_CIRCLE:
                pad.SetShape(pcbnew.PAD_SHAPE_OVAL)
                pad.SetSizeX(2*pad.GetSize()[0])
                pad.SetSizeY(pad.GetSize()[1])
            elif pad.GetShape() == pcbnew.PAD_SHAPE_OVAL and pad.GetSize()[0] > pad.GetSize()[1]:
                print("caseA")
                largeDimension = pad.GetSize()[0]
                pad.SetSizeX(pad.GetSize()[1])
                pad.SetSizeY(largeDimension)
            elif pad.GetShape() == pcbnew.PAD_SHAPE_OVAL and pad.GetSize()[0] < pad.GetSize()[1]:
                print("caseB")
                pad.SetSizeY(pad.GetSize()[0])
                pad.SetShape(pcbnew.PAD_SHAPE_CIRCLE)

        
