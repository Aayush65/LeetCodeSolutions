/**
 * @param {Object} obj
 * @return {Object}
 */
var compactObject = function(obj) {
    if (Array.isArray(obj)){
        const newArr = [];
        for (const i in obj){
            if (typeof obj[i] === "object")
                obj[i] = compactObject(obj[i])
            if (obj[i])
                newArr.push(obj[i]);
        }
        return newArr
    } else {
        for (const key in obj){
            if (typeof obj[key] === "object")
                obj[key] = compactObject(obj[key])
            if (!obj[key])
                delete obj[key];
        }
        return obj
    }
};