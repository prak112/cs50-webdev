let colorCounter = 0;
document.getElementById('say-hello').onclick = sayHello;    // sayHello() returns function value, sayHello calls the function
document.getElementById('change-color').onclick = changeColor;


function changeColor(){
    // Random colors
    // const letters = '0123456789ABCDEF';
    // let hexcolor = '#';
    // for (let i = 0; i < 6; i++){
    //     hexcolor += letters[Math.floor(Math.random() * letters.length)];
    // }
    
    // specific colors
    const colors = ['#FF0000', '#0BA807', '#FF00FF', '#FFFFFF', '#0287EF'];
    let hexcolor = colors[Math.floor(Math.random() * colors.length)];
    document.body.style.backgroundColor = hexcolor;

    let changeColorButton = document.getElementById('change-color');    
    changeColorButton.addEventListener('click', changeCounter);

    colorNarrator = document.querySelector('span')
    colorNarrator.innerHTML = hexcolor;
    if (hexcolor == '#0BA807'){
        colorNarrator.innerHTML = 'GREEN! Yaay!';
    }
    else if (hexcolor == '#FF0000'){
        colorNarrator.innerHTML = 'RED! Oh no!';
    }
    else {
        colorNarrator.innerHTML += ' ...Not GREEN! Booo!';
    }
}

function sayHello(){
    let greeting = document.createElement('p');
    let userName = prompt('What is your name?');
    greeting.textContent = 'Hello, ' + userName + '!';
    document.body.appendChild(greeting);
    document.getElementById('say-hello').remove();
}


function changeCounter(){
    colorCounter++;
    document.getElementById('change-counter').innerHTML = colorCounter;
    if (colorCounter % 5 === 0){
        alert(`Color was changed ${colorCounter} times!`);
    }
}

