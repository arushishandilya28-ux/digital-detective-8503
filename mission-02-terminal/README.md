# Mission 02 — Become comfortable with the Terminal

## 1. Task / objective
Practise safe file operations inside the assignment repository and explain command options and pipes.

## 2. Work completed
Terminal practice was performed in `mission-02-terminal/terminal-practice/`.

| Operation | Command | Observed result |
|---|---|---|
| Current folder | `pwd` | `[assignment-root]/mission-02-terminal/terminal-practice` |
| List names | `ls` | `notes.txt`, `renamed-backup.txt` |
| Detailed listing | `ls -lah` | Shows permissions, sizes, dates and hidden entries; account name redacted |
| Parent folder | `cd ..` then `pwd` | Location changed to `[assignment-root]/mission-02-terminal` |
| Create folder | `mkdir -p terminal-practice` | Created the practice folder if it did not already exist |
| Create/write file | `printf '...' > notes.txt` | Created a file with the first line |
| Append | `printf '...' >> notes.txt` | Added a second line while retaining the first |
| Copy | `cp notes.txt backup.txt` | Made a second copy |
| Rename | `mv backup.txt renamed-backup.txt` | Renamed the copy |
| Display | `cat notes.txt` | Printed both lines |

The file contains: “First line: created with output redirection.” and “Second line: appended without replacing the first.” The copied file has the same 96-byte size. Owner names are omitted from public output.

### Flags, pipes and package managers
`-l` requests a long listing, `-a` includes hidden entries and `-h` makes sizes easier to read. A pipe (`|`) passes one command's output as the next command's input; for example, `ls -lah | head -n 3` limits the displayed listing. Homebrew 7.0.15 was present; `brew list --formula` displayed installed formula names. A package manager keeps software installation and updates organized.

## 3. Commands / tools used
`pwd`, `ls`, `cd`, `mkdir`, `printf`, `cp`, `mv`, `cat`, `head`, `brew --version`, and `brew list --formula` were used in the practice folder. `>` replaces file contents; `>>` appends. `cp` leaves the original in place; `mv` relocates or renames the source.

## 4. My understanding
Rewrite the reference above in your own words and include what you noticed when you ran the commands.

## 5. Difficulties faced
A detailed `ps` process snapshot was blocked by the workspace permissions during Mission 3; no repeated attempt was made.

## 6. How I resolved them
The restriction was recorded and private account information was removed from the file listing before sharing it.

## 7. Evidence / files
- `terminal-practice/notes.txt`
- `terminal-practice/renamed-backup.txt`

## 8. Commit details
This draft needs your own explanation before it can count as a completed mission commit.
