async function showBMIChart() {

    const response =
        await fetch("http://127.0.0.1:5000/history");

    const data = await response.json();

    const labels = [];

    const bmiValues = [];

    data.forEach(item => {

        labels.push(item.name);

        bmiValues.push(item.bmi);
    });

    const ctx =
        document.getElementById('bmiChart');

    new Chart(ctx, {

        type: 'line',

        data: {

            labels: labels,

            datasets: [{

                label: 'BMI Trend Analysis',

                data: bmiValues,

                borderWidth: 3,

                tension: 0.3
            }]
        }
    });
}