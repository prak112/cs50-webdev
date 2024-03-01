// if page active after period of inactivity
const tasks = retrieveTasks();

document.addEventListener('DOMContentLoaded', function() {
    //retrieveTasks();

    // if page active
    addTask();

    // if page active
    toggleSubmitButton();

    // clear all tasks
    clearTasks();
});



function retrieveTasks(){
    // retrieve from localStorage
    let allTasks = localStorage.getItem('tasksObject');
    
    // parse allTasks from string to array
    allTasks = isNaN(allTasks) ? [] : JSON.parse(allTasks);

    // validate localStorage
    if (!allTasks || allTasks.length < 1){
        //document.getElementById('task-list').innerHTML = 'Your tasks are done!\n';
        document.getElementById('clear-tasks').style.display = "none";
        let tasks = [];

        return tasks;
    }
    else if (allTasks.length > 1) {
        //document.querySelector('#task-list').innerHTML = 'Tasks for the day!\n';
        document.getElementById('clear-tasks').style.display = "block";

        for (let i=0; i < allTasks.length; i++){
            const li = document.createElement('li');
            li.innerHTML = allTasks[i];
            document.querySelector('#task-list').append(li);
        }

        return allTasks;
    }
}



function addTask(){
    // add list item to task-list
    document.querySelector('form').onsubmit = function(event) {
        event.preventDefault();

        // update tasks array
        
        // add new task
        let task = document.querySelector('#task').value;
        tasks.push(task);        
        
        // add task as list item
        const li = document.createElement('li');
        li.innerHTML = task;
        document.querySelector('#task-list').append(li);

        // pushing to localStorage
        localStorage.setItem('tasksObject', JSON.stringify(tasks));

        // reset input and submit
        document.querySelector('#task').value = ''; // clear input after submit
        document.getElementById('submit').disabled = true; // disable submit

        return false; // prevent form submission to server, for client-side interaction
    }
}



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


function clearTasks() {
    let clearButton = document.getElementById('clear-tasks');
    clearButton.style.display = "block";
    clearButton.onclick = function() {
        if (tasks.length == 0){
            alert('Nothing to clear. You are good to take-off!');
        }
        else{
            localStorage.clear();
            tasks.length = 0;
            document.querySelectorAll('li').forEach((li) => {
                li.style.display = 'none';
            });
        }
    }
}