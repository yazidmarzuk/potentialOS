
function runPythonScript() {
    // Get the path to the Python script.
    var pythonScriptPath = "/home/marzuk-pe/netwrork-test.py";
    // Run the Python script.
    subprocess.run(["python3", pythonScriptPath]);

    document.getElementById('network-test').innerHTML = `${network_id.toFixed(1)}`;

  }

