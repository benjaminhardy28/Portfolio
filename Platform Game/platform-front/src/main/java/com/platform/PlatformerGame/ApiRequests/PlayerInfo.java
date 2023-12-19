package com.platform.PlatformerGame.ApiRequests;

public class PlayerInfo {
    

    public Integer id = null;
    public String username;
    public int losses;
    public int wins;


    public PlayerInfo(){
        username = "";
        wins = 0;
        losses = 0;
    }

    public void updateName(String name){
        username = name;
    }


    public void updateWins(int increment){
        wins += increment;
    }

    public void updateLosses(int increment){
        losses += increment;
    }

    public int getWins(){
        return wins;
    }

    public int getLosses(){
        return losses;
    }

    public String toString(){
        return "This is the player" + username;
    }


}
