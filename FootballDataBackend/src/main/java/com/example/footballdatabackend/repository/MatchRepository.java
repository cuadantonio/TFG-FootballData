package com.example.footballdatabackend.repository;

import com.example.footballdatabackend.model.Match;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;
import java.util.Optional;

public interface MatchRepository extends MongoRepository<Match, ObjectId> {
    Optional<List<Match>> findAllByTeamId(Integer TeamId);
    Optional<Match> findMatchByFixtureIdAndTeamId(Integer fixtureId, Integer TeamId);
}
