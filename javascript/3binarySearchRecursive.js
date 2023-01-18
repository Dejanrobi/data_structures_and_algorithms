function recursiveBinarySearch(list, target){
    console.log(list);

    // let first = 0;
    
    // check if the list is empty
    if(list.length ===0){
        return false
    }else{
        // finding the midpoint of the list
        // Math.floor is used to get the corrext midpoint of an array here
        let midpoint = Math.floor((list.length-1)/2);

        // compare if the value matches with the target
        if(list[midpoint]==target){
            return true
        // calling the function with  a sliced list if value is lesser than the target
        }else if(list[midpoint]<target){
            return recursiveBinarySearch(list.slice(midpoint+1), target);
        }else{
            return recursiveBinarySearch(list.slice(0,midpoint-1), target);
        }
    }
}

// Verifying the result
function verify(ans){
    console.log("Value in the list: ", ans);
    
}


// List
let list = [3, 3, 5, 6, 7, 9]

// result
let result = recursiveBinarySearch(list, 7);

// verifying
verify(result)