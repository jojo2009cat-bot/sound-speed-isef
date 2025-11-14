<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aguamenti Calculator for Heavy Metals</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #E6F0FA; /* أزرق فاتح هادي */
        color: #333;
        text-align: center;
        padding: 20px;
    }
    h1 {
        color: #F5E79E; /* أصفر فاتح */
        margin-bottom: 5px;
    }
    h3 {
        color: #666;
        margin-bottom: 20px;
    }
    label {
        font-weight: bold;
        display: block;
        margin: 10px 0 5px;
    }
    select, input {
        padding: 8px;
        font-size: 16px;
        margin-bottom: 15px;
    }
    button {
        padding: 10px 20px;
        font-size: 16px;
        background-color: #F5E79E;
        border: none;
        cursor: pointer;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .result-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 20px;
        flex-wrap: wrap;
    }
    .result-box {
        padding: 15px;
        border-radius: 8px;
        min-width: 150px;
        font-weight: bold;
        font-size: 16px;
    }
    .moles, .mass {
        background-color: #B3D9FF; /* أزرق فاتح للمولات والكمية */
    }
    .safe {
        background-color: #C4F0C5; /* أخضر */
    }
    .unsafe {
        background-color: #FF8C8C; /* أحمر */
    }
</style>
</head>
<body>

<h1>Aguamenti Calculator for Heavy Metals</h1>
<h3>A calculator that gives you the amount of heavy metals in fresh water using the velocity of sound</h3>

<label for="metal">Choose the metal:</label>
<select id="metal">
    <option value="Pb">Lead (Pb)</option>
    <option value="Cd">Cadmium (Cd)</option>
    <option value="Hg">Mercury (Hg)</option>
</select>

<label for="velocity">Enter the velocity of sound (m/s):</label>
<input type="number" id="velocity" step="0.01">

<br>
<button onclick="calculate()">Calculate</button>

<div class="result-container">
    <div id="moles" class="result-box moles">Moles: </div>
    <div id="mass" class="result-box mass">Mass (mg): </div>
    <div id="safety" class="result-box">Safety: </div>
</div>

<script>
function calculate() {
    const metal = document.getElementById('metal').value;
    const v = parseFloat(document.getElementById('velocity').value);
    if (isNaN(v) || v <= 0) {
        alert("Please enter a valid positive velocity");
        return;
    }

    // Molar masses in g/mol
    const molarMasses = {
        Pb: 207.2,
        Cd: 112.41,
        Hg: 200.59
    };

    // Safety limits in mg
    const limits = {
        Pb: 0.01,
        Cd: 0.003,
        Hg: 0.001
    };

    // حساب عدد المولات
    const numerator = 2.2e9 * 1e-3;
    const molarMass = molarMasses[metal] * 1e-3; // تحويل للكيلوجرام
    let n = (numerator / (v*v)) - 1;
    n = n / molarMass;

    const molesBox = document.getElementById('moles');
    const massBox = document.getElementById('mass');
    const safetyBox = document.getElementById('safety');

    if (n < 0) {
        molesBox.textContent = "Moles: Error, negative result!";
        massBox.textContent = "Mass (mg): Error";
        safetyBox.textContent = "";
        return;
    }

    const massMg = n * molarMasses[metal] * 1000; // تحويل للملليجرام

    molesBox.textContent = "Moles: " + n.toFixed(6);
    massBox.textContent = "Mass (mg): " + massMg.toFixed(6);

    if (massMg > limits[metal]*1000) { // التحويل من مللي لتر لمليجرام على حسب كثافة تقريبية
        safetyBox.textContent = "Unsafe for human use";
        safetyBox.className = "result-box unsafe";
    } else {
        safetyBox.textContent = "Safe for human use";
        safetyBox.className = "result-box safe";
    }
}
</script>

</body>
</html>
