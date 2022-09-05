class Scene01 extends Phaser.Scene{
    constructor() {
        super('Scene01')
    }

    preload(){
       
        this.load.image('background', '/img/background.png')
        
    }

    create(){

        this.background = this.add.image(0,0,'background').setOrigin(0,0)
    
    }

    update(){
        

    }

}