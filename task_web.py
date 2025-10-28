#!/usr/bin/env python3
"""
Task Manager - Simple Web Interface
Run this for a clean, minimal web interface to manage your tasks
"""

from flask import Flask, render_template_string, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Task Manager</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            padding: 20px;
            line-height: 1.6;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        h1 {
            color: #333;
            margin-bottom: 30px;
            font-size: 32px;
        }
        .add-task {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .input-group {
            display: flex;
            gap: 10px;
        }
        input[type="text"] {
            flex: 1;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 6px;
            font-size: 14px;
        }
        input[type="text"]:focus {
            outline: none;
            border-color: #4CAF50;
        }
        select {
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 6px;
            font-size: 14px;
            background: white;
        }
        button {
            padding: 12px 24px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
        }
        button:hover { background: #45a049; }
        .columns {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
        }
        .column {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .column-header {
            font-weight: 600;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid #e0e0e0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .count {
            background: #e0e0e0;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 12px;
        }
        .task-card {
            background: #f9f9f9;
            padding: 12px;
            margin-bottom: 10px;
            border-radius: 6px;
            border-left: 3px solid #4CAF50;
            cursor: pointer;
            transition: all 0.2s;
        }
        .task-card:hover {
            transform: translateX(2px);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .task-title {
            font-size: 14px;
            color: #333;
            margin-bottom: 8px;
        }
        .task-actions {
            display: flex;
            gap: 5px;
        }
        .task-actions button {
            padding: 4px 8px;
            font-size: 11px;
            background: #666;
        }
        .task-actions button:hover { background: #555; }
        .delete-btn { background: #f44336 !important; }
        .delete-btn:hover { background: #da190b !important; }
        .backlog .column-header { color: #795548; }
        .backlog .task-card { border-left-color: #795548; }
        .up-next .column-header { color: #FF9800; }
        .up-next .task-card { border-left-color: #FF9800; }
        .in-progress .column-header { color: #2196F3; }
        .in-progress .task-card { border-left-color: #2196F3; }
        .top-priority .column-header { color: #9C27B0; }
        .top-priority .task-card { border-left-color: #9C27B0; }
        .done .column-header { color: #4CAF50; }
        .done .task-card { border-left-color: #4CAF50; opacity: 0.7; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📋 My Tasks</h1>
        
        <div class="add-task">
            <div class="input-group">
                <input type="text" id="taskTitle" placeholder="Enter new task..." />
                <select id="taskStatus">
                    <option value="backlog">Backlog</option>
                    <option value="up-next">Up Next</option>
                    <option value="in-progress">In Progress</option>
                    <option value="top-priority">Top Priority</option>
                    <option value="done">Done</option>
                </select>
                <button onclick="addTask()">Add Task</button>
            </div>
        </div>
        
        <div class="columns">
            <div class="column backlog">
                <div class="column-header">
                    <span>Backlog</span>
                    <span class="count" id="count-backlog">0</span>
                </div>
                <div id="tasks-backlog"></div>
            </div>
            
            <div class="column up-next">
                <div class="column-header">
                    <span>Up Next</span>
                    <span class="count" id="count-up-next">0</span>
                </div>
                <div id="tasks-up-next"></div>
            </div>
            
            <div class="column in-progress">
                <div class="column-header">
                    <span>In Progress</span>
                    <span class="count" id="count-in-progress">0</span>
                </div>
                <div id="tasks-in-progress"></div>
            </div>
            
            <div class="column top-priority">
                <div class="column-header">
                    <span>Top Priority</span>
                    <span class="count" id="count-top-priority">0</span>
                </div>
                <div id="tasks-top-priority"></div>
            </div>
            
            <div class="column done">
                <div class="column-header">
                    <span>Done</span>
                    <span class="count" id="count-done">0</span>
                </div>
                <div id="tasks-done"></div>
            </div>
        </div>
    </div>
    
    <script>
        const statuses = ['backlog', 'up-next', 'in-progress', 'top-priority', 'done'];
        
        function loadTasks() {
            fetch('/api/tasks')
                .then(r => r.json())
                .then(tasks => {
                    statuses.forEach(status => {
                        const container = document.getElementById(`tasks-${status}`);
                        const filtered = tasks.filter(t => t.status === status);
                        document.getElementById(`count-${status}`).textContent = filtered.length;
                        
                        container.innerHTML = filtered.map(task => `
                            <div class="task-card">
                                <div class="task-title">${task.title}</div>
                                <div class="task-actions">
                                    ${status !== 'done' ? `<button onclick="moveTask(${task.id}, 'done')">✓ Done</button>` : ''}
                                    ${status !== 'in-progress' ? `<button onclick="moveTask(${task.id}, 'in-progress')">▶ Progress</button>` : ''}
                                    <button class="delete-btn" onclick="deleteTask(${task.id})">✗ Delete</button>
                                </div>
                            </div>
                        `).join('');
                    });
                });
        }
        
        function addTask() {
            const title = document.getElementById('taskTitle').value.trim();
            const status = document.getElementById('taskStatus').value;
            
            if (!title) return;
            
            fetch('/api/tasks', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({title, status})
            }).then(() => {
                document.getElementById('taskTitle').value = '';
                loadTasks();
            });
        }
        
        function moveTask(id, newStatus) {
            fetch(`/api/tasks/${id}`, {
                method: 'PUT',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({status: newStatus})
            }).then(() => loadTasks());
        }
        
        function deleteTask(id) {
            if (confirm('Delete this task?')) {
                fetch(`/api/tasks/${id}`, {method: 'DELETE'})
                    .then(() => loadTasks());
            }
        }
        
        document.getElementById('taskTitle').addEventListener('keypress', e => {
            if (e.key === 'Enter') addTask();
        });
        
        loadTasks();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(load_tasks())

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    tasks = load_tasks()
    task = {
        "id": max([t['id'] for t in tasks], default=0) + 1,
        "title": data['title'],
        "status": data['status'],
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    return jsonify(task)

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = data['status']
            task['updated'] = datetime.now().isoformat()
            save_tasks(tasks)
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t['id'] != task_id]
    save_tasks(tasks)
    return jsonify({"success": True})

if __name__ == '__main__':
    print("🚀 Task Manager starting at http://localhost:5000")
    print("Press Ctrl+C to stop")
    app.run(debug=True, port=5000)

