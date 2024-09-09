## Personal Takeaways
- A good night's sleep is ALWAYS the solution for a debug hassle!

## Regular `function()` vs Arrow function `() =>`
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

## HTML `form` Auto-Refresh
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