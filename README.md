# uni-salary

> [!IMPORTANT]
> This repository will not be updated.
> Feel free to fork for furthur development.

Approximately done.

All the development were done on Linux Mint / Ubuntu.
It's recommended that you do the same.

## Structure

### Diagram

```
                             +---------+
                             |  ui.py  |
                             +----+----+
                                  |
                                  |     +-----------+
                                  +-->  | prompt.py |  =>  inputFilesPath.txt
                                  |     +-----------+
                 +----------+     |
                 | excel.py |  <--+
                 +----------+     |
                                  |
                                  |     +----------------------+
                                  +-->  | profInsertionForm.py |  =>  profList.xlsx
                                  |     +----------------------+
                                  |
         +------------------+     |
         | output_dialog.py |  <--+
         +------------------+     |
                                  |     +----------------------+
                                  +-->  | resources/logo_rc.py |  <=  resources/logo.png
                                  |     +----------------------+
                                  |
 +--------------------------+     |
 | input-excel-files/*.xlsx |  <--+
 +--------------------------+     |
                                  |
                                  v

                           +-------------+
                   output  | {name}.xlsx |
                           +-------------+
```

### Description

+ The main file which needs to be executed is `ui.py`.
+ `prompt.py` is the dialog window which takes all input files from user and
  stores their path inside a file called `inputFilesPath.txt`.
  The program will use them later.
    + Note that the file will be overwritten everytime this function is called.
+ `excel.py` is a wrapper for `openpyxl` module to handle the r/w to/from all
  excel files.
+ `output_dialog.py` is just a dialog box to give the user errors and warnings
+ `profInsertionForm.py` takes an excel file (list of professor) and appends to
  it.
+ `resources/logo_rc.py` is the logo which is used in the UI.

## TODO

+ UI is not responsive
    + Due to current structure of the project, I recommend to skip this.
      after making the GUI responsive, it's a big hasle to merge the changes.
      You will read about it in the `convert.sh` section.
    + If you want to make it responsive,
      it's highly recommended to use `loadUi` method from `PyQt5.uic` module
      to read directly from `*.ui`

Example:

```python
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("menubar/main.ui")

        # connecting signals/functions goes here
        self.actionAppendProf.triggered.connect(self.appendProfForm)
        ...

    # functions goes here
    def appendProfForm(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = profInsertionForm.Ui_profInsertionForm()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
    ...

...
```

## input files

> [!WARNING]
> Application only supports `.xlsx` files.
> 
> The `.xlsx` files inside `input-excel-files/` directory are samples.
> Any changes to their `row title` or `column title` WILL break the program.
> If you want to change, you need to also change the code (they are hard-coded).


## `convert.sh` Script

Script takes arguments

+ `-ui` for convert *.ui files to *.py
+ `-eol` for convert EOL char from unix (`<LF>`) to dos (`<LF><CR>`)
+ `no argument` does nothing, you need to specify at least one of the above

### What to do next?

This section is a little bit tricky. `convert.sh` can do:

1. convert all `.ui` files to `.py`
1. replace Linux EOL (End Of Line) characters to Windows's EOL characters.

#### `*.ui` files: After converting

> If you are using `loadUi` module from `PyQt5.uic`,
> then you can skip this section.

You need to create a  directory (folder) called `rawUi` and place all `*.ui`
files in there. That's the place which `convert.sh` will be looking for files to
convert.

> If you are going to use `venv`, make sure you name it `venv`, (what?!)
> I mean create it like this:
> 
> ```bash
> python -m venv venv
> ```

All `.ui` files will have a `tmp-` prefix when they are converted to avoid
the works being overwritten. You need to manually compare each `tmp-*.py`
file with the old `*.py` files and then apply the changes yourself.

> You can use a diff tool like `nvim -d` or `vimdiff`
> 
> VSCode has a GUI tool for this (`Select for compare`),
> you are just one Google search away from it ;)

## Dependencies

```bash
pip install PyQt5 openpyxl
```

+ All the UI designings were done with `Qt 5 Designer` program from the Qt Development Tools

## References

+ [YouTube PyQt5 Playlist](https://www.youtube.com/playlist?list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj)
+ [YouTube video about openpyxl](https://youtu.be/7YS6YDQKFh0?si=N-D3giaDBtqcaV7y)
+ [openpyxl documentations](https://openpyxl.readthedocs.io/en/stable/)
+ [Packaging tutorial: .py to .exe](https://youtu.be/p3tSLatmGvU?si=ykLtv16RQwxt6UyE)
