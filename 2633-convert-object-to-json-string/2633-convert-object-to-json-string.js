/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === null || typeof object !== "object")
        return typeof object === "string" ? '"' + object + '"' : String(object);
    const json = [];
    if (Array.isArray(object)){
        json.push('[');
        for (let i of object){
            json.push(jsonStringify(i));
            json.push(',');
        }
        if (json[json.length - 1] === ',')
            json.pop();
        json.push(']');
    } else {
        json.push('{');
        for (let i in object){
            let entry = '"' + i + '"' + ':' + jsonStringify(object[i]);
            json.push(entry);
            json.push(',');
        }
        if (json[json.length - 1] === ',')
            json.pop();
        json.push('}');
    }
    return json.join('')
};