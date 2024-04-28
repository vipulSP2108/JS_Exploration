/**
 * @param {string} word
 * @return {number}
 */
var numberOfSpecialChars = function(word) {
    var upper_list = []
    var lower_list = []
    var checkinlist = (list, char) => {
        for (var i = 0; i<list.length; i++){
            if (char == list[i]){
                return true
            }
        }
        return false
    }
    var checkupper = (char) => {
        if (char == char.toUpperCase()){
            return true
        }
        if (char != char.toUpperCase()){
            return false
        }
    }


    for(let i = 0; i < word.length; i += 1){
        if (!checkupper(word[i])){
            if(!checkinlist(lower_list, word[i])){
                lower_list.push(word[i])
            }
        }
        else{
            if(!checkinlist(upper_list, word[i])){
                upper_list.push(word[i])
            }
        }
    }

    var count = 0;
    for(let i = 0; i < upper_list.length; i += 1){
        for(let j = 0; j < lower_list.length; j += 1){
            if (lower_list[j].toUpperCase() == upper_list[i]){
                count += 1;
                break
            }
        }
    }
    return count
};
