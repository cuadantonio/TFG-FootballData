package com.example.footballdatabackend.controller;

import com.example.footballdatabackend.model.Player;
import com.example.footballdatabackend.repository.PlayerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@CrossOrigin(origins = "http://localhost:8081")
@RestController
@RequestMapping("/api")
public class PlayerController {

    @Autowired
    PlayerRepository playerRepository;

    @GetMapping("/players/{teamIdAux}")
    public ResponseEntity<List<Player>> getAllPlayerByTeamIdAux(@PathVariable("teamIdAux") Integer teamIdAux) {
        Optional<List<Player>> players = playerRepository.findAllByTeamIdAux(teamIdAux);
        return new ResponseEntity<>(players.get(), HttpStatus.OK);
    }

    @GetMapping("/player/{playerId}")
    public ResponseEntity<Player> getPlayerById(@PathVariable("playerId") Integer playerId) {
        Optional<Player> player = playerRepository.findPlayerByPlayerId(playerId);
        return new ResponseEntity<>(player.get(), HttpStatus.OK);
    }
}
