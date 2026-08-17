# Linux Commands

| Command | What it does |
|---------|--------------|
| `echo "Hello" > file.txt` | Creates a file and writes text |
| `cat file.txt` | Shows file content |
| `echo "Line 2" >> file.txt` | Adds text to the file |
| `head -2 file.txt` | Shows first 2 lines |
| `tail -3 file.txt` | Shows last 3 lines |
| `mkdir new_folder` | Creates a folder |
| `cd new_folder` | Moves into a folder |
| `pwd` | Shows current location |
| `cd ..` | Goes back one folder |
# Linux Advanced Commands

| Command | What it does |
|---------|--------------|
| `grep -r "text" .` | Searches for text in all files |
| `sort file.txt` | Sorts lines alphabetically |
| `sort file.txt \| uniq` | Removes duplicate lines |
| `ps aux` | Shows all running processes |
| `df -h` | Shows disk space in human-readable format |
| `free -m` | Shows memory usage in MB |

## Permission Commands
| Command | What it does |
|---------|--------------|
| `chmod 755 file` | User: read+write+execute, Group: read+execute, Others: read+execute |
| `chmod 644 file` | User: read+write, Group: read, Others: read |
| `chmod u+x file` | Adds execute permission for user |
| `chmod go-r file` | Removes read permission for group and others |
| `ls -l file` | Shows current permissions of a file |
## Linux Commands - tar and gzip

### `tar` (Combine files)
| Command | What it does |
|---------|--------------|
| `tar -czf archive.tar.gz file1 file2` | Creates a compressed archive |
| `tar -tzf archive.tar.gz` | Lists contents of the archive |
| `tar -xzf archive.tar.gz` | Extracts the archive |

### `gzip` (Compress files)
| Command | What it does |
|---------|--------------|
| `gzip file.txt` | Compresses a file to `.gz` |
| `gunzip file.txt.gz` | Decompresses the file back |

### Key options:
| Option | Meaning |
|--------|---------|
| `-c` | Create |
| `-z` | Compress with gzip |
| `-f` | File name |
| `-x` | Extract |
| `-t` | List contents |
