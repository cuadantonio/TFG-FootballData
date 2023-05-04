package com.example.footballdatabackend.model;

import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "PlayersDataByMatch")
public class PlayerInMatch {
    @Id
    private ObjectId _id;
    private Integer fixtureId;
    private Integer round;
    private String team;
    private Integer teamId;
    private String rivalTeam;
    private Integer rivalTeamId;
    private Integer playerId;
    private String playerName;
    private String playerPhoto;
    private Integer minutes;
    private Integer offsides;
    private Integer totalShots;
    private Integer shotsOn;
    private Integer totalGoals;
    private Integer concededGoals;
    private Integer assists;
    private Integer saves;
    private Integer totalPasses;
    private Integer keyPasses;
    private String passesAccuracy;
    private Integer totalTackles;
    private Integer blockTackles;
    private Integer interceptionTackles;
    private Integer totalDuels;
    private Integer duelsWon;
    private Integer dribblesAttempts;
    private Integer dribblesSuccess;
    private Integer dribblesPast;
    private Integer foulsDrawn;
    private Integer foulsCommitted;
    private Integer yellowCards;
    private Integer redCards;
    private Integer penaltiesWon;
    private Integer penaltiesCommited;
    private Integer penaltiesScored;
    private Integer penaltiesMissed;
    private Integer penaltiesSaved;
    private Integer winnerId;
    private String score;

    public PlayerInMatch() {
    }

    public PlayerInMatch(ObjectId _id, Integer fixtureId, Integer round, String team, Integer teamId, String rivalTeam, Integer rivalTeamId, Integer playerId, String playerName, String playerPhoto, Integer minutes, Integer offsides, Integer totalShots, Integer shotsOn, Integer totalGoals, Integer concededGoals, Integer assists, Integer saves, Integer totalPasses, Integer keyPasses, String passesAccuracy, Integer totalTackles, Integer blockTackles, Integer interceptionTackles, Integer totalDuels, Integer duelsWon, Integer dribblesAttempts, Integer dribblesSuccess, Integer dribblesPast, Integer foulsDrawn, Integer foulsCommitted, Integer yellowCards, Integer redCards, Integer penaltiesWon, Integer penaltiesCommited, Integer penaltiesScored, Integer penaltiesMissed, Integer penaltiesSaved, Integer winnerId, String score) {
        this._id = _id;
        this.fixtureId = fixtureId;
        this.round = round;
        this.team = team;
        this.teamId = teamId;
        this.rivalTeam = rivalTeam;
        this.rivalTeamId = rivalTeamId;
        this.playerId = playerId;
        this.playerName = playerName;
        this.playerPhoto = playerPhoto;
        this.minutes = minutes;
        this.offsides = offsides;
        this.totalShots = totalShots;
        this.shotsOn = shotsOn;
        this.totalGoals = totalGoals;
        this.concededGoals = concededGoals;
        this.assists = assists;
        this.saves = saves;
        this.totalPasses = totalPasses;
        this.keyPasses = keyPasses;
        this.passesAccuracy = passesAccuracy;
        this.totalTackles = totalTackles;
        this.blockTackles = blockTackles;
        this.interceptionTackles = interceptionTackles;
        this.totalDuels = totalDuels;
        this.duelsWon = duelsWon;
        this.dribblesAttempts = dribblesAttempts;
        this.dribblesSuccess = dribblesSuccess;
        this.dribblesPast = dribblesPast;
        this.foulsDrawn = foulsDrawn;
        this.foulsCommitted = foulsCommitted;
        this.yellowCards = yellowCards;
        this.redCards = redCards;
        this.penaltiesWon = penaltiesWon;
        this.penaltiesCommited = penaltiesCommited;
        this.penaltiesScored = penaltiesScored;
        this.penaltiesMissed = penaltiesMissed;
        this.penaltiesSaved = penaltiesSaved;
        this.winnerId = winnerId;
        this.score = score;
    }

    public ObjectId get_id() {
        return _id;
    }

    public void set_id(ObjectId _id) {
        this._id = _id;
    }

    public Integer getFixtureId() {
        return fixtureId;
    }

    public void setFixtureId(Integer fixtureId) {
        this.fixtureId = fixtureId;
    }

    public Integer getRound() {
        return round;
    }

    public void setRound(Integer round) {
        this.round = round;
    }

    public String getTeam() {
        return team;
    }

    public void setTeam(String team) {
        this.team = team;
    }

    public Integer getTeamId() {
        return teamId;
    }

    public void setTeamId(Integer teamId) {
        this.teamId = teamId;
    }

    public String getRivalTeam() {
        return rivalTeam;
    }

    public void setRivalTeam(String rivalTeam) {
        this.rivalTeam = rivalTeam;
    }

    public Integer getRivalTeamId() {
        return rivalTeamId;
    }

    public void setRivalTeamId(Integer rivalTeamId) {
        this.rivalTeamId = rivalTeamId;
    }

    public Integer getPlayerId() {
        return playerId;
    }

    public void setPlayerId(Integer playerId) {
        this.playerId = playerId;
    }

    public String getPlayerName() {
        return playerName;
    }

    public void setPlayerName(String playerName) {
        this.playerName = playerName;
    }

    public String getPlayerPhoto() {
        return playerPhoto;
    }

    public void setPlayerPhoto(String playerPhoto) {
        this.playerPhoto = playerPhoto;
    }

    public Integer getMinutes() {
        return minutes;
    }

    public void setMinutes(Integer minutes) {
        this.minutes = minutes;
    }

    public Integer getOffsides() {
        return offsides;
    }

    public void setOffsides(Integer offsides) {
        this.offsides = offsides;
    }

    public Integer getTotalShots() {
        return totalShots;
    }

    public void setTotalShots(Integer totalShots) {
        this.totalShots = totalShots;
    }

    public Integer getShotsOn() {
        return shotsOn;
    }

    public void setShotsOn(Integer shotsOn) {
        this.shotsOn = shotsOn;
    }

    public Integer getTotalGoals() {
        return totalGoals;
    }

    public void setTotalGoals(Integer totalGoals) {
        this.totalGoals = totalGoals;
    }

    public Integer getConcededGoals() {
        return concededGoals;
    }

    public void setConcededGoals(Integer concededGoals) {
        this.concededGoals = concededGoals;
    }

    public Integer getAssists() {
        return assists;
    }

    public void setAssists(Integer assists) {
        this.assists = assists;
    }

    public Integer getSaves() {
        return saves;
    }

    public void setSaves(Integer saves) {
        this.saves = saves;
    }

    public Integer getTotalPasses() {
        return totalPasses;
    }

    public void setTotalPasses(Integer totalPasses) {
        this.totalPasses = totalPasses;
    }

    public Integer getKeyPasses() {
        return keyPasses;
    }

    public void setKeyPasses(Integer keyPasses) {
        this.keyPasses = keyPasses;
    }

    public String getPassesAccuracy() {
        return passesAccuracy;
    }

    public void setPassesAccuracy(String passesAccuracy) {
        this.passesAccuracy = passesAccuracy;
    }

    public Integer getTotalTackles() {
        return totalTackles;
    }

    public void setTotalTackles(Integer totalTackles) {
        this.totalTackles = totalTackles;
    }

    public Integer getBlockTackles() {
        return blockTackles;
    }

    public void setBlockTackles(Integer blockTackles) {
        this.blockTackles = blockTackles;
    }

    public Integer getInterceptionTackles() {
        return interceptionTackles;
    }

    public void setInterceptionTackles(Integer interceptionTackles) {
        this.interceptionTackles = interceptionTackles;
    }

    public Integer getTotalDuels() {
        return totalDuels;
    }

    public void setTotalDuels(Integer totalDuels) {
        this.totalDuels = totalDuels;
    }

    public Integer getDuelsWon() {
        return duelsWon;
    }

    public void setDuelsWon(Integer duelsWon) {
        this.duelsWon = duelsWon;
    }

    public Integer getDribblesAttempts() {
        return dribblesAttempts;
    }

    public void setDribblesAttempts(Integer dribblesAttempts) {
        this.dribblesAttempts = dribblesAttempts;
    }

    public Integer getDribblesSuccess() {
        return dribblesSuccess;
    }

    public void setDribblesSuccess(Integer dribblesSuccess) {
        this.dribblesSuccess = dribblesSuccess;
    }

    public Integer getDribblesPast() {
        return dribblesPast;
    }

    public void setDribblesPast(Integer dribblesPast) {
        this.dribblesPast = dribblesPast;
    }

    public Integer getFoulsDrawn() {
        return foulsDrawn;
    }

    public void setFoulsDrawn(Integer foulsDrawn) {
        this.foulsDrawn = foulsDrawn;
    }

    public Integer getFoulsCommitted() {
        return foulsCommitted;
    }

    public void setFoulsCommitted(Integer foulsCommitted) {
        this.foulsCommitted = foulsCommitted;
    }

    public Integer getYellowCards() {
        return yellowCards;
    }

    public void setYellowCards(Integer yellowCards) {
        this.yellowCards = yellowCards;
    }

    public Integer getRedCards() {
        return redCards;
    }

    public void setRedCards(Integer redCards) {
        this.redCards = redCards;
    }

    public Integer getPenaltiesWon() {
        return penaltiesWon;
    }

    public void setPenaltiesWon(Integer penaltiesWon) {
        this.penaltiesWon = penaltiesWon;
    }

    public Integer getPenaltiesCommited() {
        return penaltiesCommited;
    }

    public void setPenaltiesCommited(Integer penaltiesCommited) {
        this.penaltiesCommited = penaltiesCommited;
    }

    public Integer getPenaltiesScored() {
        return penaltiesScored;
    }

    public void setPenaltiesScored(Integer penaltiesScored) {
        this.penaltiesScored = penaltiesScored;
    }

    public Integer getPenaltiesMissed() {
        return penaltiesMissed;
    }

    public void setPenaltiesMissed(Integer penaltiesMissed) {
        this.penaltiesMissed = penaltiesMissed;
    }

    public Integer getPenaltiesSaved() {
        return penaltiesSaved;
    }

    public void setPenaltiesSaved(Integer penaltiesSaved) {
        this.penaltiesSaved = penaltiesSaved;
    }

    public Integer getWinnerId() {
        return winnerId;
    }

    public void setWinnerId(Integer winnerId) {
        this.winnerId = winnerId;
    }

    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }
}
