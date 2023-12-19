package com.platform.PlatformerAPI.model;



import org.springframework.data.annotation.Id;


public record Player (
    @Id
    Integer id,
    String username,
    Integer losses,
    Integer wins
){
}

