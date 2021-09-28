// スタイルを変更
 document.getElementsByClassName("red")[0].style.color = "red";

// テキストを変更する
document.getElementById('introduction').textContent = "これはintroductionです";

// 要素を追加する
const child = document.createElement("p");

child.textContent = "追加" 
document.getElementById("introduction").appendChild(child);

// valueを取得する 
console.log(document.getElementById("js-fizzbuzz_input").value);

// 要素を非表示 / 表示する 
document.getElementsByClassName("red")[1].style.display = "none";