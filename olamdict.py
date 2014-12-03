#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import string
import unicodedata
import codecs
import csv
import pickle
import gtk

class OlamDict:
    def __init__(self):

        #open the dictionary file
        file = open("pickledatabase.dat", "r")
        self.mldict = pickle.load(file)
        file.close()
       
       
        self.window = gtk.Window()
        menubar = gtk.MenuBar()
        menu_file = gtk.Menu()
        menu_help = gtk.Menu()

        item_file = gtk.MenuItem("File")
        item_help = gtk.MenuItem("Help")
        item_quit = gtk.MenuItem("Quit")
        item_about = gtk.MenuItem("About")
        
        menu_file.append(item_quit)
        menu_help.append(item_about)
        item_file.set_submenu(menu_file)
        item_help.set_submenu(menu_help)
        menubar.append(item_file)
        menubar.append(item_help)


        button = gtk.Button("Look Up")
        self.buffer = gtk.TextBuffer()
        self.entry = gtk.Entry()
        liststore = gtk.ListStore(str)
        textview = gtk.TextView(self.buffer)
        
        completion = gtk.EntryCompletion()
        self.entry.set_completion(completion)
        completion.set_model(liststore)
        completion.set_text_column(0)

        
        for item in self.mldict:
            liststore.append([item])

        vbox = gtk.VBox(False, 3)
        hbox = gtk.HBox(False, 3)
        hbox2 = gtk.HBox(False, 3)
        textview.set_editable(False)
        hbox.pack_start(self.entry, True, True ,6)
        hbox.pack_start(button, False, False, 6)
        hbox2.pack_start(textview,True, True, 6)
        vbox.pack_start(menubar, False, False, 0) 
        vbox.pack_start(hbox, False, False)
        vbox.pack_start(hbox2, True, True, 6)
      
        #Event Handlers 
        button.connect("clicked", self.FindMeaning1)
        completion.connect("match-selected", self.FindMeaning)
        self.window.connect("destroy", lambda w: gtk.main_quit())
        self.entry.connect("activate", self.FindMeaning1)
        item_quit.connect("activate", lambda w: gtk.main_quit())
        item_about.connect("activate", self.ShowDialog)

        
        self.window.set_title("Dictionary")
        self.window.set_size_request(400, 520)
        self.window.add(vbox)
        self.window.show_all()



    def FindMeaning(self, completion, model, iter):
         word = model[iter][completion.get_text_column()]
         meaning = self.mldict[word].replace(';', '\n')
         self.buffer.set_text(meaning)

    def FindMeaning1(self, widget):
        word = self.entry.get_text()
        meaning = self.mldict[word].replace(';', '\n')
        self.buffer.set_text(meaning)

    def ShowDialog(self, widget):
        aboutdialog = gtk.AboutDialog()
        aboutdialog.set_name("Olam")
        aboutdialog.set_version("1.0")
        aboutdialog.set_comments("English Malayalam Dictionary")
        aboutdialog.set_website("http://olam.in")
        aboutdialog.set_website_label("olam.in")
        aboutdialog.set_authors(["Kiran PS"])
        aboutdialog.set_transient_for(self.window)
        aboutdialog.run()
        aboutdialog.destroy()

OlamDict()
gtk.main()
