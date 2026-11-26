# Mission 05 — Numbers, Python and text encoding

## 1. Task / objective
Convert values between decimal, binary and hexadecimal; verify with Python; run a number converter; explain text encoding.

## 2. Work completed
### Conversion reference
| Conversion | Result |
|---|---:|
| Decimal 13 to binary | `1101` |
| Decimal 25 to binary | `11001` |
| Binary `1010` to decimal | `10` |
| Binary `1101` to decimal | `13` |
| Hexadecimal `A` to decimal | `10` |
| Hexadecimal `1F` to decimal | `31` |
| Binary `1111` to hexadecimal | `F` |

Python checks include `bin(13) == '0b1101'`, `int('1010', 2) == 10`, `hex(13) == '0xd'`, and `int('1F', 16) == 31`.

### Converter runs
| Input | Binary | Hexadecimal |
|---:|---:|---:|
| 13 | `1101` | `D` |
| 25 | `11001` | `19` |
| 42 | `101010` | `2A` |

The program uses `input()` to receive text, `int()` to parse a whole number, `bin()` to convert to binary and `hex()` to convert to hexadecimal. `bin` and `hex` include a base prefix, which the display code removes.

The ASCII decimal code for uppercase `A` is 65 and lowercase `a` is 97. ASCII covers a basic character set; UTF-8 can represent many more characters, including `é` and emoji. Encodings give computers a consistent mapping between characters and stored bytes.

## 3. Commands / tools used
`python3 number_converter.py` was run with 13, 25 and 42. `input`, `int`, `bin`, and `hex` are the Python functions used in the converter. `bin` and `hex` results were checked against the conversion table.

## 4. My understanding
Rewrite the base-conversion and encoding explanations in your own words. Show at least one manual calculation.

## 5. Difficulties faced
Add any difficulty you actually faced, or “No major difficulties” if true.

## 6. How I resolved them
Add your resolution or “Not applicable.”

## 7. Evidence / files
- `number_converter.py`
- Three converter outputs listed above

## 8. Commit details
This reference draft still needs your own manual working and explanation before it can count as a completed mission commit.
