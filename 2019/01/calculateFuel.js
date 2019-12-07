const fs = require('fs');
const path = require('path');

const INPUT_PATH = 'input.txt';

const simpleCalculateFuel = mass => Math.floor(mass / 3) - 2;

const calculateFuel = mass => {
  const requiredFuel = Math.floor(mass / 3) - 2;
  return requiredFuel > 0 ? requiredFuel + calculateFuel(requiredFuel) : 0;
};

const fuelCalculator = fuelCalculationMethod =>
  fs
    .readFileSync(INPUT_PATH, 'utf8')
    .trim()
    .split('\n')
    .reduce(
      (total, mass) => total + fuelCalculationMethod(parseInt(mass, 10)),
      0
    );

console.log(
  `Total fuel required by part 1: ${fuelCalculator(simpleCalculateFuel)}`
);
console.log(`Total fuel required by part 2: ${fuelCalculator(calculateFuel)}`);
