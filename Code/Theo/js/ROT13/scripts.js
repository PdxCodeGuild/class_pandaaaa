let encrypt_btn = document.querySelector('#encrypt_btn')
encrypt_btn.addEventListener('click',function() {
    let result = '';
    let char_val = 0;
    let cipher_offset = 13;
    let cipher_array = [];
    let cipher_input = document.querySelector('#cipher_input').value;
    cipher_array = cipher_input.split('');
    for (i=0;i<cipher_array.length;++i){
        if ((/[a-zA-Z]/).test(cipher_array[i]) != true)
            result += cipher_array[i];
        else {
            char_val = cipher_array[i].charCodeAt() + cipher_offset;
            if (char_val > 122)
                char_val = char_val - 26;
            result += String.fromCharCode(char_val);
        }
    }
    alert(result);
});