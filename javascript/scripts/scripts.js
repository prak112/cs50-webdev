let colorCounter = 0;
// sayHello() -returns function value, sayHello -calls the function
// document.getElementById('say-hello').onclick = sayHello;    
// document.getElementById('change-color').onclick = changeColor;
document.querySelector('form').onsubmit = sayHello;

// change h1 font color
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.color').forEach(function(button){
        button.onclick = function() {
            document.querySelector('h1').style.color = button.dataset.color;
        }
    })

    document.querySelector('.color').addEventListener('click', changeCounter);  // bug-doesn't update for all buttons
});


// function changeColor(){
//     // change background color between specific colors
//     const colors = ['red', 'pink', 'green', 'yellow', 'brown'];
//     let hexcolor = colors[Math.floor(Math.random() * colors.length)];
//     document.body.style.backgroundColor = hexcolor;



//     colorNarrator = document.querySelector('span')
//     colorNarrator.innerHTML = hexcolor;
//     if (hexcolor == 'green'){
//         colorNarrator.innerHTML = 'GREEN! Yaay!';
//     }
//     else if (hexcolor == 'red'){
//         colorNarrator.innerHTML = 'RED! Oh no!';
//     }
//     else {
//         colorNarrator.innerHTML += ' ...Not GREEN! Booo!';
//     }
// }

// count number of times color was changed
function changeCounter(){
    colorCounter++;
    document.getElementById('change-counter').innerHTML = colorCounter;
    if (colorCounter % 5 === 0){
        alert(`Color was changed ${colorCounter} times!`);
    }
}

// prompt user input to display greeting
function sayHello(){
    const name = document.querySelector('#name').value;
    // let greeting = document.createElement('h2');
    // greeting.textContent = 'Hello, ' + name + '!';
    // document.body.appendChild(greeting);
    alert(`Hello, ${name}!`)
}



