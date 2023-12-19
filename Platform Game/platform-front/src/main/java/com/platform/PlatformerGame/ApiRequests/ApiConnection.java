package com.platform.PlatformerGame.ApiRequests;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.exc.MismatchedInputException;
import com.fasterxml.jackson.core.type.TypeReference;

import java.io.IOException;
import com.fasterxml.jackson.core.JsonProcessingException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpRequest.BodyPublisher;
import com.platform.PlatformerGame.ApiRequests.PlayerInfo;

public class ApiConnection {
    
    HttpClient httpClient = HttpClient.newHttpClient();
    ObjectMapper mapper = new ObjectMapper();
    int wins = 0;
    int losses = 0;


    public PlayerInfo getUserInfo(String username){
            try {
            HttpRequest getRequest = HttpRequest.newBuilder()
                .uri(new URI("http://localhost:8080/Player/"+ username))
                .build();
            HttpResponse<String> response = httpClient.send(getRequest, HttpResponse.BodyHandlers.ofString());
            System.out.println(response.body());
            PlayerInfo response_player = mapper.readValue(response.body(), new TypeReference<PlayerInfo>() {});
            System.out.println(response_player);


            return response_player;
            } catch (URISyntaxException e) {
                System.out.println("URISyntaxException");
            } catch (IOException e) {
                System.out.println("IOException");
            }catch (InterruptedException e) {
                System.out.println("InterruptedException");
            }
            System.out.println("pringint null");
            return null;
    }

    public void updateUserInfo(PlayerInfo updatedPlayer){
        try {
        String jsonString = mapper.writeValueAsString(updatedPlayer);
        System.out.println(jsonString);
        HttpRequest postRequest = HttpRequest.newBuilder()  
            .uri(new URI("http://localhost:8080/Player"))
            .POST(HttpRequest.BodyPublishers.ofString(jsonString))
            .header("Content-Type", "application/json")
            .build();
        HttpResponse<String> response = httpClient.send(postRequest, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
        }
        catch (URISyntaxException e) { 
            System.out.println("Could not send post request");
        }catch (JsonProcessingException e) { 
            System.out.println("Could not send post request");
        } catch (InterruptedException e) {
                e.printStackTrace();
        }catch (IOException e) {
                e.printStackTrace();
        }

    }

    public void postUserUpdate(String username){

    }

}
