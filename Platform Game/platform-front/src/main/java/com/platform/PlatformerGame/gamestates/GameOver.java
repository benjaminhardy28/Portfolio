package com.platform.PlatformerGame.gamestates;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.MouseEvent;
import com.platform.PlatformerGame.main.Game;
import com.platform.PlatformerGame.utilz.LoadSave;
import com.platform.PlatformerGame.ApiRequests.PlayerInfo;

public class GameOver extends State implements Statemethods{


    String username;

    public Game game;



    public GameOver(Game game) {
        super(game);
        this.game = game;
       
    }

    @Override
    public void update() {
        // TODO Auto-generated method stub
    }




    @Override
    public void draw(Graphics g) {
        g.setColor(new Color(170, 74, 68));
        g.setFont(new Font("Monospaced", Font.BOLD, 30));
        username = game.menuFrame.nameField.getText();
        PlayerInfo player_info = game.getPlayerInfo();
        g.drawString("Oh no. Try again, " + username, 50,150);
        //API CALL TO GET WINS AND LOSES FOR NAME, if no user exists, create new user with 1 loss and 0 wins
        g.drawString("wins:" + player_info.getWins() + ", Loses:" + player_info.getLosses(), 50,250);
        g.drawImage(LoadSave.getSpriteAtlas(LoadSave.ENDING_SCREEN), 100, 300, 500,350, null);
    }

   
    
    @Override
    public void mouseClicked(MouseEvent e) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'mouseClicked'");
    }

    @Override
    public void mousePressed(MouseEvent e) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'mousePressed'");
    }

    @Override
    public void mouseReleased(MouseEvent e) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'mouseReleased'");
    }

    @Override
    public void mouseMoved(MouseEvent e) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'mouseMoved'");
    }

    public void keyPressed(KeyEvent e) {
      
    }

    public void keyReleased(KeyEvent e) {
    }
    
}