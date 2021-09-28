// アラートを出す
document.getElementById("display_alert").addEventListener("click", () => {
    alert('hello world!!')
  });
  
  // 確認ダイアログを出す
  document.getElementById("display_confirm").addEventListener("click", () => {
    if (confirm('are you alright?')) {
      alert('great!')
    } else {
      alert('sorry')
    }
  });
  
  // 入力フォーム付きのダイアログ
  document.getElementById("display_fizz_buzz").addEventListener("click", () => {
    alert(fizzbuzz(prompt('数字を入力してください')))
  });