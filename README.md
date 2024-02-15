# uni-salary

Work In Progress

## convert script

now this script takes arguments

+ `-ui` for convert *.ui files to *.py
+ `-eol` for convert EOL char from unix (`<LF>`) to dos (`<LF><CR>`)
+ `no argument` does nothing, you need to specify at least one of the above

## TODO

### urgent

+ get path from `prompt` ui and store it into a variable
+ use `excel` wrapper for r/w from/to files

### not urgent

+ ui is not responsive

## Dependencies

```bash
pip install PyQt5 openpyxl
```
