// クリックさたときに動作させる

var target = document.getElementById('introuction')
target.addEventListener('click', () => {
    console.log('click');
});

// 画像の読み込みが完了したら発動させる
window.onload = () => {
    console.log('started!');
}