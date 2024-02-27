# Overview
Practicing Javascript by implementing concepts (in my own way) learnt from CS50 W.

# Plan
- Improvise and implement concepts learned
- Progress with course project
- Advance learning in [DevSchool-Javascript repo](https://github.com/prak112/DevSchool-Javascript)

# Concepts Learned
- Functions
- Complications of misplacing keywords (for ex. `let` and `const`)
- DOM Manipulation
    - `querySelector`
        ```javascript
        document.querySelector('HTMLelement');
        document.querySelector('#elementId');
        document.querySelector('.elementClass');
        ```
    - `getElementById`
        ```javascript
        document.getElementById('HTMLelementId');
        ```        
    - `addEventListener`
        ```javascript
        document.addEventListener('NameOfTheEvent', function() {
            // code for anonymous function
        })
        ```
    - `createElement`, `appendChild`
        ```javascript
        ...
        let subHeading = document.createElement('h2');
        subHeading.textContent = 'Hello, Javascript!';
        document.body.appendChild(subHeading);
        ...        
        ```
- Assigning functions to `onclick` Events
- Writing anonymous functions in `addEventListener` 
