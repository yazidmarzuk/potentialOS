fetchData();

setInterval(fetchData, 2000);
document.getElementById('runSpeedtestBtn').onclick = fetchSpeedtest()

function fetchData() {
  fetch("http://127.0.0.1:5000/sensor-data")
    .then((response) => {
      // Check if the response is successful (status code 200)
      if (response.ok) {
        // Parse the JSON data from the response
        console.log("response recieved");
        return response.json();
      } else {
        // If the response is not successful, throw an error
        throw new Error("Failed to fetch data");
      }
    })
    .then((data) => {
      for (const key in data) {
        if (data.hasOwnProperty(key)) {
          const element = document.getElementById(key);
          if (element) {
            if (typeof data[key] === "object") {
              // If the value is an object, iterate over its keys
              for (const subKey in data[key]) {
                if (data[key].hasOwnProperty(subKey)) {
                  const subElement = document.getElementById(subKey);
                  if (subElement) {
                    subElement.innerHTML = data[key][subKey];
                    // console.log(data)
                  }
                }
              }
            } else {
              // If the value is not an object, update the element directly
              element.innerHTML = data[key];
            }
          }
        }
      }

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
          var depth =                     var dataPoints = [];
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
                        console.log(Math.max(0, Math.min(maxDepth, previousDataPoint + depthIncrease + depthFluctuationValue)))
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

    })
    .catch((error) => {
      // Handle any errors that occurred during the fetch
      console.error("Error fetching data:", error);
    });
}
