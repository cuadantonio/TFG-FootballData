package com.example.footballdatabackend.controller;

import com.example.footballdatabackend.model.PlayerInMatch;
import com.example.footballdatabackend.repository.PlayerInMatchRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "http://localhost:8081")
@RestController
@RequestMapping("/api")
public class PlayerInMatchController {

    @Autowired
    PlayerInMatchRepository playerInMatchRepository;

    @GetMapping("/playerinmatch/matches/{PlayerId}")
    public ResponseEntity<List<PlayerInMatch>> getAllByPlayerId(@PathVariable("PlayerId") Integer PlayerId){
        List<PlayerInMatch> matches = playerInMatchRepository.findAllByPlayerId(PlayerId).get();
        return new ResponseEntity<>(matches, HttpStatus.OK);
    }

    @GetMapping("/playerinmatch/match/{FixtureId}/{PlayerId}")
    public ResponseEntity<PlayerInMatch> getPlayerInMatchByFixtureIdAndPlayerId(@PathVariable("FixtureId") Integer FixtureId, @PathVariable("PlayerId") Integer PlayerId){
        PlayerInMatch match = playerInMatchRepository.findPlayerInMatchByFixtureIdAndPlayerId(FixtureId, PlayerId).get();
        return new ResponseEntity<>(match,HttpStatus.OK);
    }
}
