// Make a GET request to the API URL

setInterval(fetchData, 2000);

function fetchData() {

    fetch('http://localhost:5000/api-call')
    .then(response => {
        // Check if the response is successful (status code 200)
        if (response.ok) {
        // Parse the JSON data from the response
        console.log("response recieved")
        return response.json();
        } else {
        // If the response is not successful, throw an error
        throw new Error('Failed to fetch data');
        }
    })
    .then(data => {

        for (const key in data) {
            if (data.hasOwnProperty(key)) {
                const element = document.getElementById(key);
                if (element) {
                    if (typeof data[key] === 'object') {
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

        console.log(data);
        document.getElementById("disk-main-data").innerHTML = data['Disk Usage']['Percentage']
        document.getElementById("disk-partition-data").innerHTML = "nvme0n1p1"
        document.getElementById("disk-used-data").innerHTML = data['Disk Usage']['Used']
        document.getElementById("disk-avail-data").innerHTML = data['Disk Usage']['Available']
        document.getElementById("disk-total-data").innerHTML = data['Disk Usage']['Total']



        
        // // Process the JSON data
        // // data['System Information']);
        // // data['Network Information']);
        // // data['Voltage Information']);
        // // data['Disk Usage']);
        // // setInterval(fetchData, 2000);
        // // console.log(data['System Status']['Temperature'])
    })
    .catch(error => {
        // Handle any errors that occurred during the fetch
        console.error('Error fetching data:', error);
    });
}