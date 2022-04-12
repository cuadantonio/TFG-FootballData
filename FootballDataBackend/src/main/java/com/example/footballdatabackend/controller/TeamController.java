package com.example.footballdatabackend.controller;

import com.example.footballdatabackend.model.Player;
import com.example.footballdatabackend.model.Team;
import com.example.footballdatabackend.repository.TeamRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@CrossOrigin(origins = "http://localhost:8081")
@RestController
@RequestMapping("/api")
public class TeamController {

    @Autowired
    TeamRepository teamRepository;

    @GetMapping("/teams")
    public ResponseEntity<List<Team>> getAllTeams() {
        List<Team> teams = teamRepository.findAll();
        return new ResponseEntity<>(teams, HttpStatus.OK);
    }

    @GetMapping("/teams/{Id}")
    public ResponseEntity<Team> getAllTeamsById(@PathVariable("Id") Integer id) {
        Optional<Team> team = teamRepository.findTeamById(id);
        return new ResponseEntity<>(team.get(), HttpStatus.OK);
    }
}
