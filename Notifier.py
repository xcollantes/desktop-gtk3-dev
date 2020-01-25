"""TODO(xcollantes): DO NOT SUBMIT without one-line documentation for Notifier.

TODO(xcollantes): DO NOT SUBMIT without a detailed description of Notifier.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Window(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title="WINDOW #1")

    self.button = Gtk.Button(label="CLICK")
    self.button.connect("clicked", self.on_button_clicked)
    self.add(self.button)

  def on_button_clicked(self, widget):
    print("HELLO WORLD")


def main():
#    window = Gtk.Window(title="This is a notify")
#    window.show()
#    window.connect("destroy", Gtk.main_quit)
#    Gtk.main()
#
#
     win = Window()
     win.connect("destroy", Gtk.main_quit)
     win.show_all()
     Gtk.main()


if __name__ == '__main__':
  main()
