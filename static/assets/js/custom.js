function updateValues() {
    // Get the current voltage and current values from the HTML content
    const currentContent = document.getElementById('voltageCurrent').innerHTML;
    const currentContent2 = document.getElementById('voltageCurrent2').innerHTML;
    const [currentVoltage, currentCurrent] = currentContent.split(' | ');
    const [currentVoltage2, currentCurrent2] = currentContent2.split(' | ');

    const speedContent = document.getElementById('speed').innerHTML;
    

    // Parse the current values to numbers
    const currentVoltageValue = parseFloat(currentVoltage);
    const currentCurrentValue = parseFloat(currentCurrent);
    const currentVoltageValue2 = parseFloat(currentVoltage2);
    const currentCurrentValue2= parseFloat(currentCurrent2);
    const currentSpeedContent = parseFloat(speedContent)
    
    // Calculate new values within the specified fluctuation range
    const newVoltage = currentVoltageValue + getRandomFluctuation(-5, 5);
    const newCurrent = currentCurrentValue + getRandomFluctuation(-0.5, 0.5);
    
    const newVoltage2 = currentVoltageValue2 + getRandomFluctuation(-2, 2);
    const newCurrent2 = currentCurrentValue2 + getRandomFluctuation(-5, 5);
    const NewSpeed = currentSpeedContent + getRandomFluctuation(0, 0.2);


    const newPower = newCurrent*newVoltage; 
    const newPower2 = newCurrent2*newVoltage2; 

    // Update the HTML content with the new values
    document.getElementById('voltageCurrent').innerHTML = `${newVoltage.toFixed(1)} V | ${newCurrent.toFixed(1)}A`;
    // document.getElementById('power').innerHTML = `${newPower.toFixed(1)} W`;
    document.getElementById('voltageCurrent2').innerHTML = `${newVoltage2.toFixed(1)} V | ${newCurrent2.toFixed(1)}A`;
    // document.getElementById('power2').innerHTML = `${newPower2.toFixed(1)} W`;
    document.getElementById('speed').innerHTML = `${NewSpeed.toFixed(1)} m/s`;



}

  function getRandomFluctuation(min, max) {
    // Generate a random fluctuation value within the specified range
    return (Math.random() * (max - min) + min);
  }

  // Update values every 3 seconds (3000 milliseconds)
  setInterval(updateValues, 3000);
  setInterval(updateValues, 3000);




  