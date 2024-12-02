# Periodic Table of Elements
**Author**: Al Sweigart (al@inventwithpython.com)

Displays detailed atomic information about the elements in the periodic table. Users can explore the properties of elements by entering their symbol or atomic number.

## Project Overview
This project provides a simple interface to display information about chemical elements based on data from the periodic table. Users can view properties such as atomic number, symbol, atomic weight, density, melting and boiling points, and more.

The script uses data sourced from Wikipedia's chemical elements table and processes it from a CSV file.

## Features
- Interactive user interface to explore elements.
- Displays a visual representation of the periodic table.
- Provides the following information for each element:
   - Atomic Number
   - Symbol
   - Element Name
   - Origin of Name
   - Group and Period
   - Atomic Weight
   - Density
   - Melting and Boiling Points
   - Specific Heat Capacity
   - Electronegativity
   - Abundance in Earth's Crust
- Handles both element symbols and atomic numbers as input.

## Requirements
- Python 3.7 or later
- Required libraries:
  - csv (built-in)
  - sys (built-in)
  - re (built-in)

## Setup Instructions
1. Download the CSV File:
The project requires periodictable.csv, which contains the data for all chemical elements.

   - Download the file from this link or create it manually by copying the table from Wikipedia to a CSV file.
2. Save the File:
Place periodictable.csv in the same directory as the script (periodictable.py).

4. Run the Program:
Run the following command in your terminal or IDE:

```css
python main.py
```

## How to Use
1. Run the program to see a graphical representation of the periodic table.
2. Enter the atomic number or symbol of the element you want to examine.
3. The program will display detailed information about the selected element.
4. To exit, type QUIT.

## Example
### Input:
```markdown
> H
```
### Output:
```yaml
Atomic Number          : 1
Symbol                 : H
Element                : Hydrogen
Origin of name         : Greek: 'hydro' and 'genes' (water forming)
Group                  : 1
Period                 : 1
Atomic weight          : 1.008 u
Density                : 0.08988 g/cm^3
Melting point          : 13.99 K
Boiling point          : 20.271 K
Specific heat capacity : 14.304 J/(g*K)
Electronegativity      : 2.20
Abundance in earth's crust: 1400 mg/kg
```
## Notes
If the CSV file is missing or misplaced, the program will display a FileNotFoundError. Ensure periodictable.csv is in the correct directory.
The project handles minor formatting inconsistencies (e.g., bracketed references from Wikipedia) for cleaner output.

## Acknowledgments
Data from Wikipedia.
This project is part of the "Big Book of Small Python Projects" by Al Sweigart. For more details, visit nostarch.com.

## License
See the [LICENSE](LICENSE) file for details.
