# Overview
Practicing Javascript by implementing concepts (in my own way) learnt from CS50 W.

# Plan
- Improvise and implement concepts learned
- Implement course project
- Advance learning in [DevSchool-Javascript repo](https://github.com/prak112/DevSchool-Javascript) with freeCodeCamp projects

# Concepts Learned
## CS50 W
- Functions
    - Arrow  (`=>`) notation for `function`
        ```javascript
            // default notation
            document.addEventListener('DOMContentLoaded', function (parameter) {
                //function logic
            };
            ...
            // arrow notation
            document.addEventListener('DOMContentLoaded', parameter => {
                //function logic
            };
            ...
            // arrow notation - if no parameters
            document.addEventListener('DOMContentLoaded', () => {
                //function logic
            }
            ...
        ```
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

<hr>
<hr>

# Debugger Logs
## CoPilot (GitHub/Codeium)
### Regular `function()` vs Arrow function `() =>`
-  In complicated terms:
    - Value of `this` keyword is set based on how the function is called. It could be :
        - Global object, 
        - Object that the function is a method of, 
        - New instance in case of a constructor call, or
        - Specified object if the function is called with `apply/call/bind`.
- In simpler terms :
    - regular `function()` : `this` keyword is referred to an object in the global context, i.e., an event, instance or variable defined INSIDE the function
    - arrow function `() =>` : `this` keyword is referred to an object in the sorrounding context, i.e., an event, instance or variable either defined OUTSIDE the function or a Global object (if any)
- For example, in my code :
    - The Bug :
    ```javascript
        document.addEventListener('DOMContentLoaded', () => {   // refers to a global event -which cannot be reached
        document.querySelector('#color-dropdown').onchange = () => {    // refers to global event/HTML element -which cannot be reached
            document.body.style.backgroundColor = this.value;
        }
    });
    ```
    - The Solution :
    ```javascript
        document.addEventListener('DOMContentLoaded', function() {   // refers to a global event -which is reachable
        document.querySelector('#color-dropdown').onchange = function() {    // refers to global event/HTML element -which is reachable
            document.body.style.backgroundColor = this.value;
        }
    });
    ```
- In layman terms, I would think :
    - regular `function()` = 'original' defintion,
    - arrow function `() =>` = 'delegated' definition.

<hr>

### HTML `form` Auto-Refresh
- `preventDefault()` method to prevent webpage auto-refresh when using `<form>` element
    ```javascript
        function(event){
            event.preventDefault();
            anotherFunction();
        }
    ```
- In the same context as above, to prevent form data submission to server for handling Client-side interaction,
    ```javascript
        function(){
            ...
            //function logic
            ...
            return false; // enables Client-side interaction
        }
    ```
<hr>

