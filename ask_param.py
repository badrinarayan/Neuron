#!/usr/bin/python
import sys
import gtk
import pygtk
import dbm
from train_window import train_window

class askparam_window:
    """Window For Asking Parameters about BPN Network"""
    def __init__(self,net):
        gladefile="./gui/config_parameter.xml"
        builder=gtk.Builder()
        builder.add_from_file(gladefile)
        self.type=net
        self.awindow=builder.get_object("config_standard")
        self.clabel=builder.get_object("config_label")
        self.numl_text=builder.get_object("numl_text")
        self.inputn_text=builder.get_object("inputn_text")
        self.outputn_text=builder.get_object("outputn_text")
        self.hiddenn_text=builder.get_object("hiddenn_text")
        self.numh_text=builder.get_object("numh_text")
        if (net == "SPR"):
            self.clabel.set_label("Enter Sparse BPN Parameters")
        elif (net == "STD"):
            self.clabel.set_label("Enter Standard BPN Parameters")
        elif (net == "SRT"):
            self.clabel.set_label("Enter Shortcut BPN Parameters")
        builder.connect_signals(self)

    def on_config_standard_destroy(self,widget,data=None):
        """Handler for the destroy event for the window."""
        self.awindow.destroy()

    def on_ok(self,widget,data=None):
        """Handler for the OK button for the window which is raised
        whenever it is clicked"""
        if not self.validate_parameters():
            em=gtk.MessageDialog(None,gtk.DIALOG_MODAL,gtk.MESSAGE_ERROR,gtk.BUTTONS_OK,"BPN Network Parameters Not Completed")
            em.run()
            em.destroy()
        else:
            db=dbm.open('config.dat','c')
            db['Network Type']=self.type
            db['Number of Layers']=self.numl_text.get_text()
            db['Input Neurons']=self.inputn_text.get_text()
            db['Output Neurons']=self.outputn_text.get_text()
            db['Hidden Neurons']=self.hiddenn_text.get_text()
            db['Number of Hidden Layers']=self.numh_text.get_text()
            db.close()
            self.awindow.hide()
            try:
                db=dbm.open('config.dat','c')
                temp=db['Maximum Neurons']
                db.close()
            except KeyError:
                twindow=train_window()

    def validate_parameters(self):
        """For Validating the Entry present in the Ask Parameter Window"""
        if self.numl_text.get_text_length()==0:
            return False
        elif self.inputn_text.get_text_length()==0:
            return False
        elif self.outputn_text.get_text_length()==0:
            return False
        elif self.hiddenn_text.get_text_length()==0:
            return False
        elif self.numh_text.get_text_length()==0:
            return False
        else:
            return True

if __name__=="__main__":
    create_window=askparam_window("SPR")
    gtk.main()

