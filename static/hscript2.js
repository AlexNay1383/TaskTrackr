document.getElementById('createTaskBtn').addEventListener('click', openModal);
document.getElementsByClassName('close')[0].addEventListener('click', closeModal);
document.getElementById('addTaskBtn').addEventListener('click', addTask);

function openModal() {
    document.getElementById('taskModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('taskModal').style.display = 'none';
}

function addTask() {
    const startTime = document.getElementById('startTime').value;
    const endTime = document.getElementById('endTime').value;
    const taskTitle = document.getElementById('taskTitle').value;
    const taskDescription = document.getElementById('taskDescription').value;

    const taskContainer = document.createElement('div');
    taskContainer.className = 'task';
    taskContainer.innerHTML = `<button onclick="openModal()">+</button> ${startTime} - ${endTime} <strong>${taskTitle}</strong> - ${taskDescription}`;
    document.getElementById('tasks').appendChild(taskContainer);

    closeModal();
}

// Mock functions for navbar actions
function login() {
    alert('Login function');
}

function signUp() {
    alert('Sign Up function');
}

function logout() {
    alert('Logout function');
}

function deleteAccount() {
    alert('Delete Account function');
}
