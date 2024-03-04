// collect task-list items
const allTasks = JSON.parse(localStorage.getItem('tasks')) || [];

document.addEventListener('DOMContentLoaded', function() {    
    // if page active
    addTask();

    // if page active
    toggleSubmitButton();

    // clear all tasks
    clearTasks();
});



// add form input to task list
function addTask(){
    // add list item to task-list
    document.querySelector('form').onsubmit = function(event) {
        event.preventDefault();
        
        // add task to allTasks
        let task = document.querySelector('#task').value;
        allTasks.push(task);        
        
        // add task as list item
        const li = document.createElement('li');
        li.innerHTML = task;
        document.querySelector('#task-list').append(li);

        // push allTasks to localStorage
        localStorage.setItem('tasks', JSON.stringify(allTasks));

        // reset form - input and submit
        document.querySelector('#task').value = ''; // clear input after submit
        document.getElementById('submit').disabled = true; // disable submit

        return false; // prevent form submission to server, for client-side interaction
    }
}


// validate submit button
function toggleSubmitButton() {
    // disable submit button, by default
    let submitButton = document.getElementById('submit');
    submitButton.disabled = true;

    // when task typed, enable submit button
    let taskInput = document.getElementById('task');
    taskInput.addEventListener('keyup', () => {
        if (taskInput.value.length > 2){
            submitButton.disabled = false;
        }
        else{
            submitButton.disabled = true;
        }
    });
}



// reload content on webpage refresh
window.onload = function() {
    // validate and list localStorage items
    if (allTasks.length > 0) {
        for (let i = 0; i < allTasks.length; i++){
            const li = document.createElement('li');
            li.innerHTML = allTasks[i];
            document.querySelector('#task-list').append(li);
        }        
    }
}



// clear localStorage and list display
function clearTasks() {
    let clearButton = document.getElementById('clear-tasks');
    clearButton.style.display = "block";
    clearButton.onclick = function() {
        if (allTasks.length == 0){
            alert('Nothing to clear. You are good to take-off!');
        }
        else {
            localStorage.clear();
            allTasks.length = 0;
            document.querySelectorAll('li').forEach((li) => {
                li.style.display = 'none';
            });
        }
    }
}