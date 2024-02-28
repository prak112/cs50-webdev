document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#color-dropdown').onchange = function() {
        document.body.style.backgroundColor = this.value;
    }
});
//console.log('dropdown.js loaded!');
