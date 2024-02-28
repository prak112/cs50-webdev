# Overview
Practicing Javascript by implementing concepts (in my own way) learnt from CS50 W.

# Plan
- Improvise and implement concepts learned
- Implement course project
- Advance learning in [DevSchool-Javascript repo](https://github.com/prak112/DevSchool-Javascript) with freeCodeCamp projects

# Concepts Learned
## CS50 W
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
    - `querySelectorAll`, `forEach(function())`
    - `<button data-color="red">`, `button.dataset.color` 
- Assigning functions to `onclick` Events
- Writing anonymous functions in `addEventListener`

## MDN Web Docs
- [Expressions & Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)
    - `+` unary operator - converts a variable type to Number if it is not
    - `Number(variableName)` - alternative variable conversion to Number type
    - `delete` - deletes any value configured by User
    - `typeof`- returns data type of the variable
    - `instanceof`
        - returns instance type of the variable,
        - useful for catching exceptions at runtime

- Never used, but fun to know!
    - [Bitwise Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#bitwise_operators) 
        - comparison of numerals in binary representation
    - Prepared a [numeral converter](/javascript/base-converter) to convert decimal numbers to binary, octal or hexadecimal
    - Assignment operators for 
        - shifting bits left or right
        - bitwise AND, OR, XOR assignments
        - logical AND, OR assignments


## GitHub CoPilot
- `preventDefault()` method to prevent webpage auto-refresh when using `<form>` element
    ```javascript
        function(event){
            event.preventDefault();
            anotherFunction();
        }
    ```

