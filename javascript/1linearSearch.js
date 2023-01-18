// Starts at the start of a list
// compares the current value with the target value
// if it matches, it returns the index of the value
// if not, it moves to the next value sequentially and repeats step 2


function linearSearch(list, target){
    // Looping through the entire list
    for(let i=0; i<list.length;i++){
        // checking whether the current value equals the target value
        if(list[i]===target){
            // return midpoint if it matches the target
            return i;        
        }

    }
    // returns none if value not found
    return false;
}

// Verifying our result
function verify(index){
    if(index){
        console.log("The value was found at index", index)
    }
    else{
        console.log("The value was not found on the list!!!")
    }
}

// List
let list = [3, 5, 6, 7, 8, 9, 10]

// Getting the result
let resultAnswer = linearSearch(list, 4);

// Calling the verify function
verify(resultAnswer);

