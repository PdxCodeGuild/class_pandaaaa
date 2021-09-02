let units = {
    'ft':0.3048,
    'mi':1609.34,
    'm':1,
    'km':1000,
    'yard':0.9144,
    'inch': 0.0254
};

convert = function(distance,input_units,output_units,units){
    try{
        total = distance * units[input_units] * (1/units[output_units]);
        alert(total);
        return total;

    }
    catch {
        return 0;
    }
}

// isTrue = true
while(true){
    distance = Number(prompt("What is the distance?"));
    if (isNaN(distance)) {
        alert('That is not a number, try again!');
        continue;
    }
    input_units = prompt("What are the input units?");
    output_units = prompt("What are the output units?");
    
    converted_units = convert(distance,input_units,output_units,units)
    if (converted_units == 0){
        alert("Invalid units");
        break;
    }
    
    else{
        alert(`${distance}${input_units} is ${Math.round(converted_units,2)}${output_units}`);
        break;
    }
}