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
        Optional<List<Match>> matchesHome = matchRepository.findAllByHomeTeamId(teamId);
        Optional<List<Match>> matchesAway = matchRepository.findAllByAwayTeamId(teamId);
        matchesHome.get().addAll(matchesAway.get());
        return new ResponseEntity<>(matchesHome.get(), HttpStatus.OK);
    }

    @GetMapping("/match/{FixtureId}")
    public ResponseEntity<Match> getMatchByFixtureId(@PathVariable("FixtureId") Integer fixtureId) {
        Optional<Match> match = matchRepository.findMatchByFixtureId(fixtureId);
        return new ResponseEntity<>(match.get(), HttpStatus.OK);
    }
}
