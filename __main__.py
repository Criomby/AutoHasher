# Copyright 2021 Criomby
# criomby@pm.me

import hashlib
import tkinter as tk
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import os
import sys

class App(tk.Tk):

    def __init__(self):
        super(App, self).__init__()

        # GUI
        self.title('AutoHasher')
        self.iconbitmap(self.resource_path('autohasher_logo.ico'))
        self.geometry('420x530')
        self.resizable(True, False)

        # image
        self.logo = self.resource_path('hash_logo_incode_grey.jpg')
        self.logo_open = Image.open(self.logo)
        self.img_logo = ImageTk.PhotoImage(self.logo_open)
        self.label_logo = tk.Label(image=self.img_logo)

        # labels
        self.label_select_menu = tk.Label(text='Select the hash algorithm:')
        self.label_file = tk.Label(text='File:')
        self.filename_opened = tk.StringVar()
        self.label_filename = tk.Label(textvariable=self.filename_opened)
        self.label_hash_output = tk.Label(text='The hash value is:')
        self.label_check = tk.Label(text='Enter a hash value to check:')
        self.label_check_text = tk.Label(text='Result:')
        self.checkresult = tk.StringVar()
        self.label_check_result = tk.Label(textvariable=self.checkresult)

        # entry
        self.entry_hash_output = tk.Entry(width=70)
        self.entry_hashtocheck = tk.Entry(width=70)

        # dropdown menu
        # guaranteed algorithms by hashlib:
        # {'md5', 'shake_256', 'blake2s', 'sha224', 'sha1', 'blake2b', 'sha3_384',
        # 'sha3_224', 'sha3_256', 'sha3_512', 'sha384', 'sha256', 'sha512', 'shake_128'}
        self.hash_algorithms = ('SHA1', 'SHA224', 'SHA3_224', 'SHA256', 'SHA3_256',
                                'SHA384', 'SHA3_384', 'SHA512', 'SHA3_512', 'MD5',
                                'blake2s', 'blake2b', 'shake_128', 'shake_256'
                                )
        self.options_var = tk.StringVar(self)  # to get selection: menu_options.get()
        self.options_var.set(self.hash_algorithms[3]) # set default selection
        self.option_menu = tk.OptionMenu(
            self,
            self.options_var,
            *self.hash_algorithms
        )

        # buttons
        self.button_openfile = tk.Button(text='Open file', command=self.open_file,
                                         height=2, width=10,
                                         #relief='groove'
                                         )
        self.button_check = tk.Button(text='Check', command=self.checkhash,
                                      height=2, width=10,
                                      #relief='groove'
                                      )

        # packs
        self.label_logo.pack()
        self.label_select_menu.pack(pady=5)
        self.option_menu.pack(pady=5)
        self.button_openfile.pack(pady=10)
        self.label_file.pack(pady=5)
        self.label_filename.pack(pady=5)
        self.label_hash_output.pack(pady=5)
        self.entry_hash_output.pack(pady=5, expand=True, fill='x')
        self.label_check.pack(pady=5)
        self.entry_hashtocheck.pack(pady=5, expand=True, fill='x')
        self.button_check.pack(pady=5)
        self.label_check_text.pack(pady=5)
        self.label_check_result.pack(pady=5)

    # functions
    def open_file(self):
        global filename
        filetypes = (
            ('All files', '*.*'),
        )
        username = os.getlogin()
        if os.path.isdir('C:/Users/' + username + '/Downloads'):
            filename = fd.askopenfilename(
                title='Open a file',
                initialdir='C:/Users/' + username + '/Downloads',
                filetypes=filetypes)
        else:
            filename = fd.askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=filetypes)

        # adjust for case that no file is opened
        if filename == '':
            None
        else:
            print('File openend:', filename)
            self.head, self.tail = os.path.split(filename)
            self.filename_opened.set(self.tail)
            # generate and output file hash value
            self.entry_hash_output.delete(0, tk.END)
            hash_value = self.gen_hash()
            self.entry_hash_output.insert(0, hash_value)

    def checkhash(self):
        generated_hash = self.entry_hash_output.get()
        inserted_hash = self.entry_hashtocheck.get()
        if generated_hash == '' and inserted_hash == '':
            print('No two hash values found')
            self.checkresult.set('Please enter two hash values.')
        elif generated_hash == '':
            print('Open a file first. The hash value will be generated automatically.')
            self.checkresult.set('Open a file first. The hash value will then be generated automatically.')
        elif inserted_hash == '':
            print('No hash value inserted for comparison.')
            self.checkresult.set('Please enter a hash value for comparison.')
        elif generated_hash == inserted_hash.lower():
            print('Match!')
            self.checkresult.set('Match!')
        else:
            print('No match!')
            self.checkresult.set('No match!')

    def gen_hash(self):
        global filename
        # hash block method from: https://nitratine.net/blog/post/how-to-hash-files-in-python/
        file = filename  # Location of the file
        BLOCK_SIZE = 65536  # The size of each read from the file
        # Create the hash object
        if self.options_var.get() == 'SHA1':
            file_hash = hashlib.sha256()
        elif self.options_var.get() == 'SHA224':
            file_hash = hashlib.sha224()
        elif self.options_var.get() == 'SHA3_224':
            file_hash = hashlib.sha3_224()
        elif self.options_var.get() == 'SHA256':
            file_hash = hashlib.sha256()
        elif self.options_var.get() == 'SHA3_256':
            file_hash = hashlib.sha3_256()
        elif self.options_var.get() == 'SHA384':
            file_hash = hashlib.sha384()
        elif self.options_var.get() == 'SHA3_384':
            file_hash = hashlib.sha3_384()
        elif self.options_var.get() == 'SHA512':
            file_hash = hashlib.sha512()
        elif self.options_var.get() == 'SHA3_512':
            file_hash = hashlib.sha3_512()
        elif self.options_var.get() == 'MD5':
            file_hash = hashlib.md5()
        elif self.options_var.get() == 'blake2s':
            file_hash = hashlib.blake2s()
        elif self.options_var.get() == 'blake2b':
            file_hash = hashlib.blake2b()
        elif self.options_var.get() == 'shake_128':
            file_hash = hashlib.shake_128()
        elif self.options_var.get() == 'shake_256':
            file_hash = hashlib.shake_256()
        else:
            print('error in gen_hash()')
        with open(file, 'rb') as f:  # Open the file to read it's bytes
            fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
            while len(fb) > 0:  # While there is still data being read from the file
                file_hash.update(fb)  # Update the hash
                fb = f.read(BLOCK_SIZE)  # Read the next block from the file
        output = file_hash.hexdigest() # Get the hexadecimal digest of the hash
        print('Algorithm:', self.options_var.get())
        print('Hash value:', output)
        return output


    # function to get files found in the pyinstaller --onefile exe,
    # which sets the path not as 'env' anymore, but as sys._MEIPASS
    # Copyright:
    # https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    app = App()
    app.mainloop()
