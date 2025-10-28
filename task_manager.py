#!/usr/bin/env python3
"""
Simple Task Manager - A lightweight CLI tool for managing tasks
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional
import sys

class TaskManager:
    def __init__(self, data_file: str = "tasks.json"):
        self.data_file = data_file
        self.tasks = self.load_tasks()
        self.statuses = ["backlog", "up-next", "in-progress", "top-priority", "done"]
    
    def load_tasks(self) -> List[Dict]:
        """Load tasks from JSON file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, title: str, status: str = "backlog"):
        """Add a new task"""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "status": status,
            "created": datetime.now().isoformat(),
            "updated": datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Added task #{task['id']}: {title}")
    
    def list_tasks(self, status: Optional[str] = None):
        """List all tasks or tasks by status"""
        if status:
            filtered = [t for t in self.tasks if t['status'] == status]
            print(f"\n=== {status.upper()} ({len(filtered)}) ===")
            for task in filtered:
                print(f"  #{task['id']}: {task['title']}")
        else:
            for stat in self.statuses:
                filtered = [t for t in self.tasks if t['status'] == stat]
                if filtered:
                    print(f"\n=== {stat.upper()} ({len(filtered)}) ===")
                    for task in filtered:
                        print(f"  #{task['id']}: {task['title']}")
    
    def update_status(self, task_id: int, new_status: str):
        """Update task status"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = new_status
                task['updated'] = datetime.now().isoformat()
                self.save_tasks()
                print(f"✓ Updated task #{task_id} to {new_status}")
                return
        print(f"✗ Task #{task_id} not found")
    
    def delete_task(self, task_id: int):
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks.pop(i)
                self.save_tasks()
                print(f"✓ Deleted task #{task_id}")
                return
        print(f"✗ Task #{task_id} not found")
    
    def search_tasks(self, query: str):
        """Search tasks by title"""
        results = [t for t in self.tasks if query.lower() in t['title'].lower()]
        print(f"\n=== SEARCH RESULTS ({len(results)}) ===")
        for task in results:
            print(f"  #{task['id']}: {task['title']} [{task['status']}]")


def print_help():
    """Print help message"""
    help_text = """
Task Manager - Simple CLI Task Management

USAGE:
    python task_manager.py <command> [arguments]

COMMANDS:
    add <title> [status]     Add a new task (default status: backlog)
    list [status]            List all tasks or tasks by status
    update <id> <status>     Update task status
    delete <id>              Delete a task
    search <query>           Search tasks by title
    help                     Show this help message

STATUSES:
    backlog, up-next, in-progress, top-priority, done

EXAMPLES:
    python task_manager.py add "Fix login bug" in-progress
    python task_manager.py list
    python task_manager.py list in-progress
    python task_manager.py update 5 done
    python task_manager.py search "website"
    python task_manager.py delete 3
"""
    print(help_text)


def main():
    if len(sys.argv) < 2:
        print_help()
        return
    
    tm = TaskManager()
    command = sys.argv[1].lower()
    
    if command == "add":
        if len(sys.argv) < 3:
            print("✗ Error: Task title required")
            return
        title = sys.argv[2]
        status = sys.argv[3] if len(sys.argv) > 3 else "backlog"
        tm.add_task(title, status)
    
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        tm.list_tasks(status)
    
    elif command == "update":
        if len(sys.argv) < 4:
            print("✗ Error: Task ID and new status required")
            return
        task_id = int(sys.argv[2])
        new_status = sys.argv[3]
        tm.update_status(task_id, new_status)
    
    elif command == "delete":
        if len(sys.argv) < 3:
            print("✗ Error: Task ID required")
            return
        task_id = int(sys.argv[2])
        tm.delete_task(task_id)
    
    elif command == "search":
        if len(sys.argv) < 3:
            print("✗ Error: Search query required")
            return
        query = sys.argv[2]
        tm.search_tasks(query)
    
    elif command == "help":
        print_help()
    
    else:
        print(f"✗ Unknown command: {command}")
        print_help()


if __name__ == "__main__":
    main()

