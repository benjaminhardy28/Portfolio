package com.platform.PlatformerAPI.repository;

import org.springframework.data.repository.ListCrudRepository;
import com.platform.PlatformerAPI.model.Player;

public interface PlayerRepository extends ListCrudRepository<Player, Integer> {
    
    Player findByUsername(String username);

}
