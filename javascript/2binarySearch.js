// BINARY SEARCH ALGORITHM
// Checks a value by getting the midpoint of a list
// Compares the midpoint with the target value 
// If it matches, it returns the midpoint
// If not, it discards all the values that are less than it and repeats step 1


// Binary search function
function binarySearch(list, target){
    // Setting the first and the last indexes of the list
    let first = 0;
    let last = (list.length) - 1

    // while the first value is less or equal to the last value
    // The list continues executing
    while(first<=last){
        // Get the midpoint of the list
        let midpoint = Math.floor((first+last)/2)

        // checki if the midpoint value equals the target
        if(list[midpoint]=== target){
            return midpoint;
        // discarding all lesser values if greater
        }else if(list[midpoint]<target){
            first = midpoint+1;
        }else{
            last = midpoint-1;
        }

    }
    return false;
}

// Verifying the function
function verify(index){
    if(index){
        console.log("The value was found at index: ", index);
    }else{
        console.log("The value was not found!!!")
    }
}

// List
let list = [6, 5, 6, 8, 7, 6, 9]

// result
let result = binarySearch(list, 6);

// verifying
verify(result)