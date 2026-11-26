# Mission 03 — Understand the operating system

## 1. Task / objective
Observe OS information, storage, processes, paths and file permissions, then describe OS responsibilities.

## 2. Work completed
| Information | Privacy-safe observation |
|---|---|
| Operating system | macOS 27.0.1 (Darwin) |
| Current account | Redacted; the username is not included in the repository |
| Storage | The workspace volume reported 926 GiB total, 142 GiB used and 755 GiB available (16% used) |
| Process snapshot | The `ps` command was blocked by workspace permissions; no process list is published |

Apps visible in the workspace included a browser and a code editor. A process is a running instance of a program; a PID is the numeric identifier assigned to that instance.

### Paths and permissions
- Redacted absolute example: `[assignment-root]/mission-02-terminal/terminal-practice/notes.txt`
- Relative example from the repository root: `mission-02-terminal/terminal-practice/notes.txt`
- The practice file permission mode was `-rw-r--r--`. Its owner can read and write it, but the execute bit is not set.

An operating system manages hardware resources, memory, files, running processes, permissions and the interface applications use to perform work.

## 3. Commands / tools used
`sw_vers` identified macOS; `df -h` reported storage totals; `ps -Ao pid,comm` was attempted once and returned “operation not permitted”; `stat` and `ls -l` showed file permissions. The username and full home path were redacted.

## 4. My understanding
Add your own explanation of why the OS manages processes, files and permissions.

## 5. Difficulties faced
The process-list command was blocked by the workspace's permissions.

## 6. How I resolved them
The error was recorded without retrying. The account name and full path were kept out of the public repository.

## 7. Evidence / files
- `mission-02-terminal/terminal-practice/notes.txt` (permissions and contents)
- Safe OS and storage observations above

## 8. Commit details
This reference draft still needs your own explanation before it can count as a completed mission commit.
