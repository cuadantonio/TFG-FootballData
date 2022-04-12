package com.example.footballdatabackend.repository;

import com.example.footballdatabackend.model.Player;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;
import java.util.Optional;

public interface PlayerRepository extends MongoRepository<Player, ObjectId> {
    Optional<List<Player>> findAllByTeamIdAux(Integer teamIdAux);
    Optional<Player> findPlayerByPlayerId(Integer playerId);
}
