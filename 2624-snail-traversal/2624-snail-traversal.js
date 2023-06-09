/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    if (this.length !== rowsCount * colsCount)
        return [];
    let mat = Array(rowsCount).fill(0).map(() => Array(colsCount).fill(0));
    let goingDown = true;
    let r = 0;
    let c = 0;
    for (let ele of this){
        mat[r][c] = ele;
        if (goingDown){
            r ++;
            if (r === rowsCount){
                r --;
                c ++;
                goingDown = false;
            }    
        } else {
            r --;
            if (r === -1){
                r ++;
                c ++;
                goingDown = true;
            }
        }
    }
    return mat;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */