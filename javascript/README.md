# Overview
Practicing Javascript by implementing concepts (in my own way) learnt from CS50 W.

# Plan
- Improvise and implement concepts learned
- Implement course project
- Advance learning in [DevSchool-Javascript repo](https://github.com/prak112/DevSchool-Javascript) with projects from [MDN Web Docs - Javscript Guide](https://developer.mozilla.org/en-US/docs/Learn/JavaScript)

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
### [Expressions & Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)
- `+` unary operator - converts a variable type to Number if it is not
- `Number(variableName)` - alternative variable conversion to Number type
- `delete` - deletes any value configured by User
- `typeof`- returns data type of the variable
- `instanceof`
    - returns instance type of the variable,
    - useful for catching exceptions at runtime

<details>
    <summary>Never used, but fun to know!</summary>

- [Bitwise Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators#bitwise_operators) 
    - comparison of numerals in binary representation
- Prepared a [numeral converter](/javascript/base-converter) to convert decimal numbers to binary, octal or hexadecimal
- Assignment operators for 
    - shifting bits left or right
    - bitwise AND, OR, XOR assignments
    - logical AND, OR assignments
</details>


### [AJAX](https://developer.mozilla.org/en-US/docs/Glossary/AJAX) 
<table>
    <tr>
        <th>What is it?</th>
        <td>AJAX (Asynchronous Javascript and XML), an asynchronous server communication technique for web development</td>
    </tr>
    <tr>
        <th>What is it useful for?</th>
        <td>Enables dynamic client-side interaction without reloading the webpage</td>
    </tr>
    <tr>
        <th>Returns</th>
        <td>Either of the following:
            <ul>
                <li>a <em>Promise</em> for handling asynchronous data, Or</li>
                <li> a XMLHttpRequest object such as JSON, HTML, XML, plain text, etc.</li>
            </ul>
        </td>
    </tr>
</table>

- AJAX can be efficient in developing a Single-Page Application (SPA) in web development.
- With reference to a Django project, AJAX could be used in the following way :
    - Build a Django Backend API (Django Rest Framework)
    - Modify View functions to `return JsonResponse()`
    - Generate `fetch()` requests, handle responses in Templates
    - *This would enable the ability of an SPA in a Django project !*

- There are several abstractions of AJAX mainly for the convenience of implementation, some of them are namely :
    - **Promise**
    - **FetchAPI**
    - **jQuery**


### [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
<table>
    <tr>
        <th>What is it?</th>
        <td>
        <ul>
            <li>Technically - An object representing the state of an asynchronous operation</li>
            <li>Analogy - A conductor which decides which block of asynchronous code to execute based on the success/failure of the asynchronous operation, for ex. an API request</li>
        </ul>
        </td>
    </tr>
    <tr>
        <th>What is it useful for?</th>
        <td>
            <ul>
                <li>Reduces complexity with clarity in structure for handling asynchronous data flow</li>
                <li>Handles data flow through FetchAPI / <code>async/await</code> </li>
                <li>FetchAPI consists of following methods : <code>.then()</code> for handling successful callbacks, <code>.catch()</code> for handling failure callbacks. for ex. errors</li>
                <li>Avoids 'Callback Hell' </li>
            </ul>
        </td>
    </tr>
    <tr>
        <th>Returns</th>
        <td>Response of an asynchronous operation - Success/Failure</td>
    </tr>
</table>


- Chained-functions a.k.a The *Pyramid of Doom* since every function is dependent on the success of the previous, such as the following:
    ```javascript
        doSomething(function (result) {
            doSomethingElse(result, function (newResult) {
                doThirdThing(newResult, function (finalResult) {
                    console.log(`Got the final result: ${finalResult}`);
                 }, failureCallback);
            }, failureCallback);
        }, failureCallback);
    ```

- This *Pyramid of Doom* could be reiterated using *Promises*, as follows:
    ```javascript
        doSomething()
        .then((result) => doSomethingElse(result))
        .then((newResult) => doThirdThing(newResult))
        .then((finalResult) => {
            console.log(`Got the final result: ${finalResult}`);
        })
        .catch(failureCallback);
    ```

- *Promises* are useful to summarize the Chaining-functions but the syntax might be confusing to represent the `return` *Promise*
- This could happen in cases when the preceding function does not return a *Promise* as follows:
    ```javascript
        doSomething()
        .then((url) => {
            fetch(url); // missing keyword 'return'
        })
        .then((result) => {
        });

    ```
    - Due to the missing keyword, `return`, a *Promise* is not returned by the `fetch` request, leading to an undefined state of the following function

- The above situation could be averted using `async/await` which also conveniently resembles synchronous code :
    ```javascript
        responseData = []
        async function logIngredients() {
            const url = await doSomething();
            const res = await fetch(url);
            const data = await res.json();
            responseData.push(data);
            console.log(responseData);
        }
    ```


### [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes)
- *...Understanding In Progress...*


<br>
<hr>
<hr>

# Debugger Logs
## Personal Takeaways
- A good night's sleep is ALWAYS the solution for a debug hassle!

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

