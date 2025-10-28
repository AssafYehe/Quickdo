# Task Manager

A simple, lightweight task management tool - much cleaner than bulky project management apps!

![Task Manager Demo](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- 🚀 **Two interfaces**: Fast CLI + Beautiful Web UI
- ⚡ **Lightning fast**: No loading times, instant access
- 📁 **Simple data**: One JSON file, easy to backup/sync
- ⌨️ **Keyboard-friendly**: CLI for power users
- 🎨 **Clean UI**: Modern, minimal web interface
- 🔒 **Private**: Your data stays on your machine

## 🎯 Quick Start

### CLI Version (Quick & Fast)

```bash
# Add a task
python3 task_manager.py add "Review pull requests" in-progress

# List all tasks
python3 task_manager.py list

# List tasks by status
python3 task_manager.py list in-progress

# Update task status
python3 task_manager.py update 5 done

# Search tasks
python3 task_manager.py search "website"

# Delete a task
python3 task_manager.py delete 3

# Show help
python3 task_manager.py help
```

### Web Interface (Visual & Clean)

```bash
# Install Flask (one-time setup)
pip3 install -r requirements.txt

# Start the web server
python3 task_web.py

# Open http://localhost:5000 in your browser
```

## 📊 Status Categories

- **backlog** - Future tasks
- **up-next** - Prioritized next tasks
- **in-progress** - Currently working on
- **top-priority** - Urgent/important tasks
- **done** - Completed tasks

## 💾 Data Storage

All tasks are stored in a simple `tasks.json` file in the same directory.

- ✅ Easy to backup
- ✅ Easy to sync (Dropbox, Git, etc.)
- ✅ Easy to migrate
- ✅ Plain text format

## ⚡ Shell Aliases (Optional)

Add these to your `~/.zshrc` or `~/.bashrc` for even faster access:

```bash
alias t='python3 ~/task-manager/task_manager.py'
alias ta='python3 ~/task-manager/task_manager.py add'
alias tl='python3 ~/task-manager/task_manager.py list'
alias tw='python3 ~/task-manager/task_web.py'
```

Then you can use:

```bash
ta "New task" backlog
tl in-progress
tw  # Start web interface
```

## 📸 Screenshots

### CLI Interface
```
=== BACKLOG (2) ===
  #4: Global wrapper
  #5: CRM DD - GDPR issues

=== UP-NEXT (1) ===
  #3: ResiConnect next steps

=== IN-PROGRESS (1) ===
  #2: Tech council next session

=== TOP-PRIORITY (1) ===
  #1: Portugal website Project
```

### Web Interface
Clean, modern interface with drag-free column view and quick actions.

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/task-manager.git
cd task-manager

# For CLI only, no installation needed!
python3 task_manager.py help

# For Web interface, install Flask
pip3 install -r requirements.txt
```

## 📝 Requirements

- Python 3.7+
- Flask 3.0+ (only for web interface)

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Why This Tool?

Built for people who find traditional project management tools too clunky and slow. This tool focuses on simplicity, speed, and keeping your data under your control.

- ⚡ **Faster** - No loading times, instant access
- 🎯 **Focused** - Just tasks, no distractions
- 📁 **Portable** - One JSON file, easy to backup/sync
- ⌨️ **Keyboard-friendly** - CLI for power users
- 🎨 **Clean UI** - Web version when you want visual
- 🔒 **Private** - Your data stays on your machine

