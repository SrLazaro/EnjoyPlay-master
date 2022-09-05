let game

window.onload = function(){

    const config = {
        type: Phaser.Canvas,
        width: 800,
        height: 600,
        scene: [Init,
                Scene01]
    }

    game = new Phaser.Game(config)

}