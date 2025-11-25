const API_URL = "http://localhost:5000";

const taskList = document.getElementById("task-list");
const taskInput = document.getElementById("task-input");
const addBtn = document.getElementById("add-btn");

//Fetch tasks when page loads
async function loadTasks() {
    const res = await fetch(`${API_URL}/tasks`);
    const tasks = await res.json();

    taskList.innerHTML = "";

    tasks.forEach(task => {
        const li = document.createElement("li");
        li.classList.add("task-item");
        if (task.is_complete) li.classList.add("complete")
    

    li.innerHTML = `
        <span>${task.title}</span>
        <div>
            <button onclick="toggleTask(${task.id}, ${task.is_complete})✔</button>
            <button onclick="deleteTask(${task.id})">✖</button>
            </div>
         `;

         task.List.appendChild(li);
    });

}


//Add a new task
addBtn.addEventListener("click", async () => {
    const title = taskInput.ariaValueMax.trim();
    if (!title) return;

    await fetch(`${API_URL}/tasks`, {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify({title})
    });

    taskInput.value = "";
    loadTasks();

});


//Mark a task complete / incomplete
async function toggleTask(id, current) {
    await fetch(`${API_URL}/tasks/${id}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({is_complete: !current})
});

    loadTasks();

}


//Delete a task
async function deleteTask(id) {
    await fetch(`${API_URL}/tasks/${id}`, {
        method: "DELETE"
    });

    loadTasks();
}

loadTasks();