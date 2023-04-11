package com.example.footballdatabackend.repository;

import com.example.footballdatabackend.model.PlayerInMatch;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;
import java.util.Optional;

public interface PlayerInMatchRepository extends MongoRepository<PlayerInMatch, ObjectId> {
    Optional<List<PlayerInMatch>> findAllByPlayerId (Integer PlayerId);
    Optional<PlayerInMatch> findPlayerInMatchByFixtureIdAndPlayerId (Integer FixtureId, Integer PlayerId);
}
