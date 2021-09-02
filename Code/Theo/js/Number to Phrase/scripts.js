let numbers_dict = {
    0:['zero','0','0'],
    1:['one','0','I'],
    2:['two','twenty','II'],
    3:['three','thirty','III'],
    4:['four','fourty','IV'],
    5:['five','fifty','V'],
    6:['six','sixty','VI'],
    7:['seven','seventy','VII'],
    8:['eight','eighty','VIII'],
    9:['nine','ninety','IX'],
    10:['ten','X'],
    11:['eleven'],
    12:['twelve'],
    13:['thirteen'],
    14:['fourteen'],
    15:['fifteen'],
    16:['sixteen'],
    17:['seventeen'],
    18:['eighteen'],
    19:['nineteen'],
    50:['L'],
    100:['C'],
    500:['D'],
    1000:['M']
};

let parse_english = function(user_input){
    if (user_input <= 19){
        return numbers_dict[user_input][0];
    }
    else if (user_input <= 99){
        singles = numbers_dict[user_input % 10][0];
        tens = numbers_dict[Math.floor(user_input / 10) ][1];
        if (singles == 'zero'){
            return tens;
        }
        return tens + '-' + singles

    }
    else{

        hundreds_num = Math.floor(user_input / 100)
        hundreds = numbers_dict[hundreds_num][0]
        user_input = user_input - (hundreds_num*100)
        if (user_input == 0){
            return hundreds + ' hundred'
        }
        if (user_input > 10 && user_input <=19){
            return hundreds + 'hundred and ' + numbers_dict[user_input][0]
        }
        tens = numbers_dict[Math.floor(user_input / 10)][1]
        singles = numbers_dict[user_input % 10][0]
        if (singles == 'zero'){
            return hundreds + 'hundred' + tens 
        }
        return hundreds + ' hundred and ' + tens + '-' + singles
    }
}

while(true) {
    input = prompt('Enter a number 1-999');
    output = parse_english(input);
    alert(output);
    break;
}