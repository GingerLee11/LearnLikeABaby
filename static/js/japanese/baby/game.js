function gameHandler() {
    const audioPath = document.getElementById('game-container').dataset.audioPath;

    return {
        level: 1,
        checkItem(item) {
            if (item === 'ringo') {
                this.playAudio('ringo');
            }
        },
        playAudio(itemId) {
            let audio = new Audio(audioPath + itemId + '.mp3');
            audio.play();
        }
    };
}
