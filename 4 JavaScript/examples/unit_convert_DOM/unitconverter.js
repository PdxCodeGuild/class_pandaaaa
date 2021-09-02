conversionFactor = {
  feet: 0.3048,
  miles: 1609.34,
  m: 1,
  km: 1000,
  yd: 0.9144,
  inch: 0.0254,
};


let convert = function(){
 let distance = document.getElementById('distance').value 
 let units = document.getElementById('units').value
 let convertTo = document.getElementById('convertTo').value

 let solution = document.getElementById('converted')
 converted.innerHTML = `${distance} is ${
    (distance * conversionFactor[units]) / conversionFactor[convertTo]
  } ${convertTo}`
}
let btn = document.getElementById("convert")
console.log(btn)
btn.addEventListener('click', convert)