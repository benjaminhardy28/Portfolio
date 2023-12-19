package com.platform.PlatformerAPI.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
//import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.platform.PlatformerAPI.model.Player;
import com.platform.PlatformerAPI.repository.PlayerRepository;
//import org.springframework.web.server.ResponseStatusException;

import java.util.List;

@RestController
@RequestMapping("/Player")
@CrossOrigin
public class PlayerController {

    private final PlayerRepository repository; 

    @Autowired
    public PlayerController(PlayerRepository repository){
        this.repository = repository;
    }


    @GetMapping("") //get request to return information for all of the players
    public List<Player> findAll() {
        return repository.findAll();
    }

    @GetMapping("/{username}") //get request to return the information for a single player 
    public Player findById(@PathVariable String username){
        return repository.findByUsername(username);
       // .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Player Not Found!"));
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("") //Post request to put in a new player into the database
    public void create(@RequestBody Player player){
        if (repository.findByUsername(player.username()) != null){
            Player past_player = repository.findByUsername(player.username());
            Player updated_player = new Player(past_player.id(), player.username(), player.losses(), player.wins());
            repository.save(updated_player);
        }
        else{
            repository.save(player);
        }
    }
}