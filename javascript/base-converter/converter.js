document.querySelector('form').onsubmit = function(event) {
    event.preventDefault(); // prevents webpage auto-refresh by the form
    convertBase();
};

function convertBase(){
    let number = Number(document.querySelector('#number').value);
    let base = Number(document.querySelector('#base').value);
    let result = number.toString(base);
    //alert(`Base ${base} of Base-10 Number ${number} = ${result}`);

    const resultDisplay = document.createElement('h2');
    resultDisplay.textContent = `Base ${base} number for (Base-10) ${number} = \n${result}`;
    resultDisplay.style.color = 'red';
    resultDisplay.style.position = 'relative';
    resultDisplay.style.top = '50%';
    resultDisplay.style.left = '50%';
    resultDisplay.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(resultDisplay);
}