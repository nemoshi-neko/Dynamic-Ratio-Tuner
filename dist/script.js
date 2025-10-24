var pre_freq = 440;
var now_freq = 440;
var freqtype = "sine";
//周波数：分子、分母
var frequencies = [1, 1, 2, 1, 3, 2, 4, 3, 5, 4, 5, 3, 6, 5, 7, 6, 7, 5, 7, 4, 8, 7, 8, 5, 9, 8, 9, 7, 9, 5,
    10, 9, 10, 7, 11, 10, 11, 9, 11, 8, 11, 7, 11, 6, 12, 11, 12, 7, 1, 2, 2, 3, 3, 4, 3, 5, 4, 5, 4, 7, 5, 6, 5, 7,
    5, 8, 5, 9, 6, 7, 7, 8, 7, 9, 7, 10, 7, 11, 7, 12, 7, 13, 8, 9, 8, 11, 8, 13, 9, 10, 9, 11, 9, 13];
//キーボードのイベントコード
var Key_input = ['Digit1', 'Digit2', 'Digit3', 'Digit4', 'Digit5', 'Digit6', 'Digit7', 'Digit8', 'Digit9', 'Digit0', 'Minus', 'Equal', 'IntlYen',
    'KeyQ', 'KeyW', 'KeyE', 'KeyR', 'KeyT', 'KeyY', 'KeyU', 'KeyI', 'KeyO', 'KeyP', 'BracketLeft', 'BracketRight',
    'KeyA', 'KeyS', 'KeyD', 'KeyF', 'KeyG', 'KeyH', 'KeyJ', 'KeyK', 'KeyL', 'Semicolon', 'Quote', 'Backslash',
    'KeyZ', 'KeyX', 'KeyC', 'KeyV', 'KeyB', 'KeyN', 'KeyM', 'Comma', 'Period', 'Slash'];
document.getElementById("Sine").addEventListener("click", function () { freqtype = "sine"; });
document.getElementById("Triangle").addEventListener("click", function () { freqtype = "triangle"; });
document.getElementById("Square").addEventListener("click", function () { freqtype = "square"; });
document.getElementById("Sawtooth").addEventListener("click", function () { freqtype = "sawtooth"; });
//今のhzと一個前のhzの表示を変更するためのelements
var pre_hz_con = document.getElementById('pre_hz_id');
var now_hz_con = document.getElementById('now_hz_id');
var pressedKeys = new Set(); // 押されたキーを管理するSet
var oscillators = {};
// キーボードを押したときの処理
document.addEventListener('keydown', function (event) {
    if (!event.repeat && Key_input.includes(event.code)) {
        pre_freq = now_freq;
        var index = Key_input.indexOf(event.code);
        now_freq *= frequencies[index * 2] / frequencies[index * 2 + 1];
        pre_hz_con.textContent = pre_freq + ' Hz';
        now_hz_con.textContent = now_freq + ' Hz';
        var key = event.key.toLowerCase();
        if (key == '\\')
            key = '\\\\';
        if (key in oscillators)
            oscillators[key].start(now_freq);
        else { // 新しいオシレーターを作成し、オブジェクトに追加
            var newOscillator = new Tone.Oscillator().toDestination();
            newOscillator.volume.value = -16;
            newOscillator.frequency.value = now_freq;
            newOscillator.type = freqtype;
            newOscillator.start();
            oscillators[key] = newOscillator;
        }
        var tds = document.querySelectorAll("td[id=\"".concat(key, "\"]"));
        if (tds.length > 0) {
            tds.forEach(function (td) {
                td.classList.add('bg-blue-300');
                pressedKeys.add(key);
            });
        }
    }
});
// キーボードを離したときの処理
document.addEventListener('keyup', function (event) {
    if (Key_input.includes(event.code)) {
        var key = event.key.toLowerCase();
        if (key == '\\')
            key = '\\\\';
        if (key in oscillators) {
            var fadeOutStartTime = Tone.now();
            oscillators[key].volume.rampTo(-Infinity, 6, fadeOutStartTime);
            oscillators[key].stop(6 + fadeOutStartTime);
            delete oscillators[key]; // 不要なオシレーターを削除
        }
        var tds = document.querySelectorAll("td[id=\"".concat(key, "\"]"));
        if (tds.length > 0) {
            tds.forEach(function (td) {
                td.classList.remove('bg-blue-300');
                pressedKeys.add(key);
            });
        }
    }
});
