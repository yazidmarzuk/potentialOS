var dataPoints = [];
var maxDataPoints = 10;  // Maximum number of data points to keep
var dataPointInterval = 500;  // Time interval for updating the chart in milliseconds
var maxDepth = 500;
var depthFluctuation = 20;  // Adjust the range of depth fluctuations
var depthIncreaseRate = 0.1;  // Adjust the rate of depth increase

document.addEventListener("DOMContentLoaded", () => {
  var chart = new ApexCharts(document.querySelector("#reportsChart"), {
    series: [{
      name: 'ROV Depth',
      data: dataPoints,
    }],
    chart: {
      height: 350,
      type: 'area',
      toolbar: {
        show: false
      },
      animations: {
        enabled: false // Disable animations for smoother scrolling
      },
    },
    markers: {
      size: 4
    },
    colors: ['#47A785'],
    fill: {
      type: "gradient",
      gradient: {
        shadeIntensity: 1,
        opacityFrom: 0.3,
        opacityTo: 0.4,
        stops: [0, 90, 100]
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth',
      width: 2
    },
    xaxis: {
      
      type: 'datetime',
      
      labels: {
        formatter: function (value, timestamp) {
          var date = new Date(value);
          var istOptions = {
            timeZone: 'Asia/Kolkata',
            year: 'numeric',
            month: 'numeric',
            day: 'numeric',
            hour: 'numeric',
            minute: 'numeric',
            second: 'numeric',
            hour12: false
          };
          return new Intl.DateTimeFormat('en-US', istOptions).format(date);
        }
      }
    },
    yaxis: {
      color: "#ffffff" ,
      reversed: true,  // Invert the y-axis
      max: maxDepth,   // Set max depth explicitly
      labels: {
        formatter: function (value) {
          return value.toFixed(2);
        }
      }
    },
    tooltip: {
      x: {
        format: 'HH:mm'
      },
    },
    scrollbar: {
      enabled: false,
    },
  });

  chart.render();

  // Function to generate gradually increasing and fluctuating ROV depth pattern
  function generateDepthPattern() {
    var currentTime = new Date().getTime();
    var previousDataPoint = dataPoints.length > 0 ? dataPoints[dataPoints.length - 1][1] : 0;
    var depthFluctuationValue = Math.random() * depthFluctuation - depthFluctuation / 2;
    var depthIncrease = depthIncreaseRate * (maxDepth - previousDataPoint);
    var depth = Math.max(0, Math.min(maxDepth, previousDataPoint + depthIncrease + depthFluctuationValue));
    return [currentTime, depth];
  }

  // Function to update the chart data
  function updateChart() {
    var newDataPoint = generateDepthPattern();
    dataPoints.push(newDataPoint);

    // Keep the number of data points within the maximum limit
    if (dataPoints.length > maxDataPoints) {
      dataPoints.shift();  // Remove the oldest data point
    }

    chart.updateSeries([{ data: dataPoints }]);
  }

  // Set up an interval to update the chart periodically
  setInterval(function () {
    updateChart();
  }, dataPointInterval);
});