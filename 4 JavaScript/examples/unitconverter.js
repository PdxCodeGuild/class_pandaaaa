const distance = prompt("enter the distance: ");
const units = prompt("enter the units: ");
const convertTo = prompt("enter the units to conver to: ");

// data = distance.split(" ")

conversionFactor = {
  feet: 0.3048,
  miles: 1609.34,
  m: 1,
  km: 1000,
  yd: 0.9144,
  inch: 0.0254,
};

console.log(
  `${distance} is ${
    (distance * conversionFactor[units]) / conversionFactor[convertTo]
  } ${convertTo}`
);
