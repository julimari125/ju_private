// const 後から再定義できない
// let は再定義可能

const add = (x , y) => {
    let result = x + y;
    return result;
};
console.log(add(3,6))


//クラス

const Taiyaki = class {
    constructor(kiji,price) {
        this.kiji;
        this.price;
    }

    //インスタンスメソッド
    display() {
        return `${this.kiji}たい焼き (${this.price})`;
    }
};

// var 値を初期化する

var plane_taiyaki = new Taiyaki("プレーン","あんこ");
console.log(plane_taiyaki.kiji);
console.log(plane_taiyaki.price);
console.log(plane_taiyaki.display());
