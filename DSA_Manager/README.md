# DSA Manager 🚀

A professional terminal-based DSA Problem Manager for VS Code. Scan hundreds of files across folders and find them instantly by their **actual problem title** (extracted from code comments), not just filenames.

## ✨ Features
- **🔍 Live Fuzzy Search:** Typo-tolerant search across titles, languages, and paths.
- **📂 Recursive Scanning:** Automatically indexes `.py`, `.cpp`, `.c`, `.java`, `.js`, `.ts` files.
- **📝 Title Extraction:** Intelligent extraction of titles from the first line comments.
- **⌨️ Keyboard Driven:** Optimized for speed with arrow navigation and shortcuts.
- **⚡ Fast Performance:** Uses caching (`.problem_index.json`) for near-instant loads.
- **🛠️ VS Code Integration:** Press `Enter` to open any problem directly in VS Code.
- **📊 Stats & Filters:** Quick overview of your problem distribution by language and folder.

## 🛠️ Installation

1. **Clone/Move** this folder into your DSA workspace.
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the application:
```bash
python main.py
```

### Shortcuts
| Key | Action |
|-----|--------|
| `Enter` | Open selected problem in VS Code |
| `F` / `/` | Focus search bar |
| `Esc` | Clear search |
| `R` | Rebuild file index |
| `Ctrl+S` | Sort alphabetically |
| `Ctrl+M` | Sort by recently modified |
| `Ctrl+F` | Sort by folder |
| `Q` | Quit |

## 🔌 VS Code Setup
To ensure the "Open in VS Code" feature works, the `code` command must be in your system's PATH.

### macOS
1. Open VS Code.
2. Open the **Command Palette** (`Cmd+Shift+P`).
3. Type `Shell Command: Install 'code' command in PATH`.

### Windows/Linux
Usually installed by default. If not, add the VS Code `bin` folder to your environment variables.

## 📁 Project Structure
- `main.py`: The core logic and terminal UI.
- `requirements.txt`: Necessary libraries (`textual`, `thefuzz`, `rich`).
- `.problem_index.json`: Local cache of your problems (generated on first run).
