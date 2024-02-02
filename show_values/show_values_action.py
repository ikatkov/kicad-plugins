#!/usr/bin/env python

import pcbnew
import os
import wx


class ShowValuesAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Show Values"
        self.category = "Modify PCB"
        self.description = "Hide the reference Designators on the silkscreen, show values, if designator is hidden - reverse"
        self.icon_file_name = os.path.join(
            os.path.dirname(__file__), "./resources/show-value.png")
        self.show_toolbar_button = True

    def Run(self):
        # Filter just selected footprints
        selected_footprints: list[pcbnew.FOOTPRINT] = [
            footprint for footprint in pcbnew.GetCurrentSelection()
            if type(footprint).__name__ == 'FOOTPRINT'
        ]

        if len(selected_footprints) == 0:
            # Show info dialog
            dlg = wx.MessageDialog(None, "Please select one or multiple footprints!",
                                   "No footprints selected", wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        for footprint in selected_footprints:
            reference = footprint.Reference()
            if reference.IsVisible():
                footprint.Value().SetLayer(reference.GetLayer())
                reference.SetVisible(False)
            else:
                footprint.Value().SetLayer(pcbnew.B_Fab if footprint.IsFlipped() else pcbnew.F_Fab)
                reference.SetVisible(True)

        pcbnew.Refresh()
        pcbnew.UpdateUserInterface()
