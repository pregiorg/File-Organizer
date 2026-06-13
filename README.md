# 🗂️ File Organizer

A Python script that automatically sorts files in a directory into categorized subfolders based on file extension.

## Features

- Sorts files into folders: `images`, `videos`, `music`, `zip`, `documents`, `setup`, `programs`
- Unsupported file types go into `others/`
- Case-insensitive extension matching (handles `.JPG`, `.MP4`, etc.)
- Auto-creates destination folders if they don't exist
- Skips subdirectories — only moves files
- Graceful error handling with descriptive messages

## Folder Structure After Running

```
📁 Your Directory/
├── 📁 images/       → .jpg .jpeg .png .gif
├── 📁 videos/       → .mp4 .mkv
├── 📁 music/        → .mp3 .wav
├── 📁 zip/          → .zip .rar
├── 📁 documents/    → .pdf .docx .txt
├── 📁 setup/        → .exe .msi
├── 📁 programs/     → .py .js .html .css .java .cpp
└── 📁 others/       → everything else
```

## Usage

1. Clone the repo:
```bash
git clone https://github.com/pregiorg/File_Organizer.git
cd file_organizer
```

2. Edit the target directory in `file_organizer.py`:
```python
os.chdir(os.path.expanduser("~/your/target/folder"))
```

3. Run:
```bash
python file_organizer.py
```

## Requirements

- Python 3.x
- No external libraries — uses `os` and `shutil` from the standard library

## Customization

Add or edit categories in the `extensions` dictionary:

```python
extensions = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    # Add a new category:
    "ebooks": [".epub", ".mobi"],
}
```

## What I Learned

- Working with `os` and `shutil` for filesystem operations
- Debugging escape sequence issues in Windows paths
- Using `os.path.expanduser()` for portable paths
- Structuring `try/except/else` blocks correctly
- Writing defensive code (skipping dirs, case-insensitive matching)

## License

MIT
