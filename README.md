# Visual Matrix

<img src="https://img.shields.io/badge/vismatrix-0.5-green"/><img src="https://img.shields.io/badge/python-3.7+-blue"/>

## About:

Visual Matrix - module for python, allowing you to display matrices or tables in a beautiful form.

### Functional:

- Create and view tables and matrix;

## Screenshots:
<img src="https://sun9-17.userapi.com/impg/35t9SG9C-tf7DuLms4WoOkewe2vVIoa3NybRKQ/dt42NuuGIug.jpg?size=293x120&quality=96&sign=c1d27e697734cffac0573176622a62ca&type=album" alt="si5"/>

>Table visual

<img src="https://sun9-46.userapi.com/impg/ecfuTnvTRIGqnguk_FdxRGdJYRWPUOMAqe3DdA/pDpnUwACbCw.jpg?size=199x153&quality=96&sign=4291f3bdaf0154f4b470fbfedbfc1a3c&type=album" alt="si5"/>

>Table visual (with border) 

<img src="https://sun9-49.userapi.com/impg/0N59CEwlpFneyIFmnLkTUlXXlhyjXTaCyIIodA/9ZGEdYVwY1s.jpg?size=286x118&quality=96&sign=63552c7f9da7b9f2757aeeaaef78f292&type=album" alt="si5"/>

>Matrix visual

## How to use:

```python
from vismatrix import VisualMatrix

header = ["Name", "Age", "Sex"]

m = [["Alexandra", "18", "Female"],
     ["Igor", "21", "Male"],
     ["Vladimir", "18", "No"]]

matrix = VisualMatrix() # initialization

matrix.setMatrix(m, header, True) # method in which you can immediately initialize a matrix with header 
                                   # and without borders
matrix.myMatrix()

matrix.setMatrix(m) # method in which you can immediately initialize a matrix without header
matrix.myMatrix()
```

>First way

```python
from vismatrix import VisualMatrix

matrix = VisualMatrix() # initialization

# second way (in this way you cant change no_border parameter)
matrix.addHeader(["Name", "Age", "Sex"])
matrix.addRow(["Alexandra", "18", "Female"])
matrix.addRow(["Igor", "21", "Male"])
matrix.addRow(["Vladimir", "18", "No"])
matrix.myMatrix()

matrix.addRow(["Alexandra", "18", "Female"])
matrix.addRow(["Igor", "21", "Male"])
matrix.addRow(["Vladimir", "18", "No"])
matrix.myMatrix()
```

>Second way

-The output from both methods will be the same. You can immediately assign lists to methods (as in the first method with header)

#### addHeader(header)

Adds a table header.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `header`  | `list` | Is the header for the table |

#### addRow(row)

Adds a row table/matrix.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `row`      | `list` | Matrix or table row |

#### setMatrix(user_matrix, header, no_border)

Creates a matrix or table (Depending on whether a header is specified or not).

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user_matrix`      | `list` | Matrix or table`s data |
| `header`      | `list` | Table`s header |
| `no_border`      | `bool` | Use borders (True - No, False - Yes) |

#### myMatrix()

Output table or matrix. **Must be written at the end of creating a matrix or table**

## Install:

```bash
pip install vismatrix
```
