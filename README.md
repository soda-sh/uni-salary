# uni-salary

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
         +----------+     |     +-----------+
         | excel.py |  <--+-->  | prompt.py |  =>  inputFilesPath.txt
         +----------+     |     +-----------+
                          |
 +------------------+     |     +----------------------+
 | output_dialog.py |  <--+-->  | profInsertionForm.py |  =>  profList.xlsx
 +------------------+     |     +----------------------+
                          |
                          |     +----------------------+
                          +-->  | resources/logo_rc.py |  <=  resources/logo.png
                          |     +----------------------+
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
    + If you want to make it responsive (which I think it's better not to),
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

        self.actionNew.triggered.connect(self.newPressed)

    def newPressed(self):
        print("New was pressed")
        pass
# ...
```

## `convert.sh` Script

now this script takes arguments

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

You need to create a  directory (folder) called `rawUI` and place all `*.ui`
files in there. That's the place which `convert.sh` will be looking for files to
convert.

> If you are going to use `venv`, make sure you name it `venv`, (what?!)
> I mean create it like this:
> 
> ```bash
> python -m venv venv
> ```

All `.ui` files will have a `tmp-` prefix when they are converted to avoid
all the work being overwritten. you need to manually compare each `tmp-*.py`
files with the old `*.py` files and then apply the changes yourself.

> You can use a diff tool like `nvim -d` or `vimdiff`
> 
> P.S: I know nothing about vscode but I'm sure you can find one there ;)

## Dependencies

```bash
pip install PyQt5 openpyxl
```

+ All the UI designed were done with `Qt 5 Designer` program from the Qt Development Tools

## References

+ [YouTube video about openpyxl](https://youtu.be/7YS6YDQKFh0?si=N-D3giaDBtqcaV7y)
+ [openpyxl documentations](https://openpyxl.readthedocs.io/en/stable/)
