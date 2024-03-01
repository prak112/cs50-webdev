// Test submitting a task
document.querySelector('form').dispatchEvent(new Event('submit'));
// Assert that the task is added to the task list
console.assert(document.querySelector('#task-list').innerHTML.includes('<li>Task 1</li>'), 'Task not added to task list');
// Assert that the task is added to the tasks array
console.assert(tasks.includes('Task 1'), 'Task not added to tasks array');
// Assert that the input is cleared after submission
console.assert(document.querySelector('#task').value === '', 'Input not cleared after submission');
// Assert that the submit button is disabled after submission
console.assert(document.getElementById('submit').disabled === true, 'Submit button not disabled after submission');