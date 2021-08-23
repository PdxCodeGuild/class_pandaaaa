class Encryptor {
    constructor() {
        this.rot13_dict = { 'a': 'n',
        'b': 'o',
        'c': 'p',
        'd': 'q',
        'e': 'r',
        'f': 's',
        'g': 't',
        'h': 'u',
        'i': 'v',
        'j': 'w',
        'k': 'x',
        'l': 'y',
        'm': 'z',
        'n': 'a',
        'o': 'b',
        'p': 'c',
        'q': 'd',
        'r': 'e',
        's': 'f',
        't': 'g',
        'u': 'h',
        'v': 'i',
        'w': 'j',
        'x': 'k',
        'y': 'l',
        'z': 'm',
        ' ': ' '
        }
    }

    convert() {
        let user_input = document.getElementById('encrypt').value
        console.log(user_input)
        let output = '';
        for (let i = 0; i < user_input.length; i++) {
            output += this.rot13_dict[user_input[i]];
        }
        // for (letter in user_input) {
        //     output += letter;

        return output;    
        }
    }

let rot_13 = function() {
    let rot_13_convert = new Encryptor();
    let solution = document.getElementById('encrypted')
    let encryption = rot_13_convert.convert()
    console.log(encryption)
    solution.innerText = encryption
}


let submit = document.getElementById('submit')
submit.addEventListener('click',rot_13)
 
// console.log(rot_13_convert.convert())