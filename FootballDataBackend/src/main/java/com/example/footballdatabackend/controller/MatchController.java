package com.example.footballdatabackend.controller;

import com.example.footballdatabackend.model.Match;
import com.example.footballdatabackend.repository.MatchRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@CrossOrigin(origins = "http://localhost:8081")
@RestController
@RequestMapping("/api")
public class MatchController {

    @Autowired
    MatchRepository matchRepository;

    @GetMapping("/matches")
    public ResponseEntity<List<Match>> getAllMatches() {
        List<Match> matches = matchRepository.findAll();
        return new ResponseEntity<>(matches, HttpStatus.OK);
    }

    @GetMapping("/matches/{TeamId}")
    public ResponseEntity<List<Match>> getAllMatchesByTeamId(@PathVariable("TeamId") Integer teamId) {
        Optional<List<Match>> matches = matchRepository.findAllByTeamId(teamId);
        return new ResponseEntity<>(matches.get(), HttpStatus.OK);
    }

    @GetMapping("/match/{FixtureId}/{TeamId}")
    public ResponseEntity<Match> getMatchByFixtureIdAndTeamId(@PathVariable("FixtureId") Integer fixtureId,@PathVariable("TeamId") Integer TeamId) {
        Optional<Match> match = matchRepository.findMatchByFixtureIdAndTeamId(fixtureId,TeamId);
        return new ResponseEntity<>(match.get(), HttpStatus.OK);
    }
}
