var resultChart = document.getElementById("resultChart");
(Chart.defaults.global.defaultFontFamily = "Arial"),
    (Chart.defaults.global.defaultFontColor = "#1e1e1f");
var resultChartData = {
        labels: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        datasets: [
            {
                label: "Business",
                data: [10, 35, 5, 22, 32, 20, 30, 40, 20, 30, 50, 30],
                backgroundColor: "#15b2ec",
                borderColor: "#15b2ec",
                pointBackgroundColor: "#ffffff",
                pointHoverBackgroundColor: "#15b2ec",
                pointBorderColor: "#15b2ec",
                borderWidth: 2,
                pointRadius: 4,
                fill: !1,
            },
            {
                label: "Others",
                data: [5, 12, 25, 18, 15, 34, 54, 20, 30, 50, 30, 60],
                backgroundColor: "#f5a416",
                borderColor: "#f5a416",
                pointBackgroundColor: "#ffffff",
                pointHoverBackgroundColor: "#f5a416",
                pointBorderColor: "#f5a416",
                borderWidth: 2,
                pointRadius: 4,
                fill: !1,
            },
        ],
    },
    resultChartOptions = {
        responsive: !0,
        scales: {
            xAxes: [
                {
                    gridLines: { display: !1, drawBorder: !1 },
                    ticks: { maxTicksLimit: 7 },
                },
            ],
            yAxes: [
                {
                    ticks: { maxTicksLimit: 5, padding: 10 },
                    gridLines: {
                        color: "rgb(234, 236, 244)",
                        zeroLineColor: "rgb(234, 236, 244)",
                        drawBorder: !1,
                        borderDash: [2],
                        zeroLineBorderDash: [2],
                    },
                },
            ],
        },
        legend: { position: "bottom", labels: { usePointStyle: !0 } },
    },
    lineChart = new Chart(resultChart, {
        type: "line",
        data: resultChartData,
        options: resultChartOptions,
    });
