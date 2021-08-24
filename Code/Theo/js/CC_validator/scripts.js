let validate = function(cc_str){
    let cc_array = [];
    let length = cc_str.length;
    let sum = 0;
    //Step 2 - Slice off the check digit
    check_digit = cc_str[length-1];
    cc_str = cc_str.slice(0,cc_str.length-1);
    length -= 1
    // Step 3 - Reverse the digits
    cc_str = cc_str.split('')
    cc_str = cc_str.reverse()
    // Step 1 - Convert to number
    for(i=0;i<length;++i){
        cc_array.push(cc_str[i]);
        if (isNaN(cc_array[i]) == true){
            return 'Invalid';
        }
    }
    // #Step 4 - Double every other element
    for (i=0;i<length; i+=2)
        cc_array[i] = cc_array[i]*2
    // #Step 5 - Subtract 9 for every number over 9
    for (i=0;i<length;++i){
        if(cc_array[i] > 9)
            cc_array[i] -= 9;
    }
    // #Step 6 - Sum all values
    for (i=0;i<length;++i)
        sum += cc_array[i];
    // #Step 7 - Take the second digit of that sum
    let compare_dig = sum % 10;
    if (compare_dig == check_digit)
        return 'Valid';
    return 'Invalid';
}

let cc_submit_btn = document.querySelector('#ccsubmit');

cc_submit_btn.onclick = function() {
    let cc_input_field = document.querySelector('#ccinput');
    let user_input = cc_input_field.value;
    let return_val = validate(user_input);
    alert(return_val);
}
