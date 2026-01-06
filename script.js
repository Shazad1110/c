const colorPicker = document.getElementById('colorPicker');
const colorDisplay = document.getElementById('colorDisplay');
const colorCode = document.getElementById('colorCode');

colorPicker.addEventListener('input', function() {
    const selectedColor = this.value;
    
    colorDisplay.style.backgroundColor = selectedColor;
    
    colorCode.textContent = `color: ${selectedColor};`;
});

colorPicker.addEventListener('change', function() {
    const selectedColor = this.value;
    console.log('Selected color:', selectedColor);
});