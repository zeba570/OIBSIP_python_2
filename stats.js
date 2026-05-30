async function loadStatistics() {

    const response =
        await fetch("http://127.0.0.1:5000/stats");

    const data = await response.json();

    document.getElementById("stats").innerHTML = `

        <h3>Average BMI: ${data.average}</h3>

        <h3>Highest BMI: ${data.highest}</h3>

        <h3>Lowest BMI: ${data.lowest}</h3>

        <h3>Total Records: ${data.total}</h3>
    `;
}