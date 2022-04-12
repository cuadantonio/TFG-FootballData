package com.example.footballdatabackend.repository;

import com.example.footballdatabackend.model.Team;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.Optional;

public interface TeamRepository extends MongoRepository<Team, ObjectId> {
    Optional<Team> findTeamById(Integer Id);
}
