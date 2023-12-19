package com.platform.PlatformerGame.gamestates;


import com.platform.PlatformerGame.main.Game;

public class State{
    protected Game game;

    public State(Game game){
        this.game = game;
    }

    public Game getGame(){
        return game;
    }
    
}
