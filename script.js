const API = "http://127.0.0.1:5000";


async function calculateBMI() {

    const name = document.getElementById("name").value;

    const weight = document.getElementById("weight").value;

    const height = document.getElementById("height").value;

    const response = await fetch(`${API}/calculate`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            name,
            weight,
            height
        })
    });

    const data = await response.json();
    if (data.error) {

    document.getElementById("result").innerHTML =
        data.error;

} else {

    document.getElementById("result").innerHTML =
        `
        ${data.name}<br>
        BMI: ${data.bmi}<br>
        Status: ${data.category}
        `;

    // Refresh everything automatically
    loadHistory();

    showBMIChart();

    loadStatistics();
}

}


async function loadHistory() {

    const response = await fetch(`${API}/history`);

    const data = await response.json();

    const table = document.getElementById("historyTable");

    table.innerHTML = "";

    data.forEach(item => {

        table.innerHTML += `

            <tr>

                <td>${item.name}</td>

                <td>${item.weight}</td>

                <td>${item.height}</td>

                <td>${item.bmi}</td>

                <td>${item.category}</td>

            </tr>
        `;
    });
}
window.onload = function () {

    loadHistory();

    showBMIChart();

    loadStatistics();
}