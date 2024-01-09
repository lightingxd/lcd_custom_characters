var pixels = new Array(8).fill(0).map(() => new Array(5).fill(0));

function togglePixel(row, col) {
    var pixel = document.getElementById(`pixel-${row}-${col}`);
    pixel.style.backgroundColor = pixel.style.backgroundColor === "black" ? "white" : "black";
    updateCodeDisplay();
}

function updateCodeDisplay() {
    var codeDisplay = document.getElementById("code-display");
    var code = "[";

    for (var i = 0; i < pixels.length; i++) {
        var rowCode = "";
        for (var j = 0; j < pixels[i].length; j++) {
            pixels[i][j] = document.getElementById(`pixel-${i}-${j}`).style.backgroundColor === "black" ? 1 : 0;
            rowCode += pixels[i][j];
        }
        code += `"${rowCode}"`;
        if (i < pixels.length - 1) {
            code += ", ";
        }
    }

    code += "]";
    codeDisplay.textContent = code;
}

window.onload = function () {
    updateCodeDisplay();
};