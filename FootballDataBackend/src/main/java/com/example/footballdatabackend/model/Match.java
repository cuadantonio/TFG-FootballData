package com.example.footballdatabackend.model;

import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "TeamsDataByMatch")
public class Match {

    @Id
    private ObjectId _id;
    private Integer fixtureId;
    private Integer round;
    private Integer teamId;
    private String teamName;
    private String side;
    private String rivalTeam;
    private Integer rivalTeamId;
    private String score;
    private Integer shotsOnGoal;
    private Integer shotsOffGoal;
    private Integer totalShots;
    private Integer blockedShots;
    private Integer shotsInsidebox;
    private Integer shotsOutsidebox;
    private Integer fouls;
    private Integer corners;
    private Integer offsides;
    private String ballPossession;
    private Integer yellowCards;
    private Integer redCards;
    private Integer goalkeeperSaves;
    private Integer totalPasses;
    private Integer passesAccurate;
    private String passesPercentage;
    private Integer winnerId;

    public Match() {
    }

    public Match(ObjectId _id, Integer fixtureId, Integer round, Integer teamId, String teamName, String side, String rivalTeam, Integer rivalTeamId, String score, Integer shotsOnGoal, Integer shotsOffGoal, Integer totalShots, Integer blockedShots, Integer shotsInsidebox, Integer shotsOutsidebox, Integer fouls, Integer corners, Integer offsides, String ballPossession, Integer yellowCards, Integer redCards, Integer goalkeeperSaves, Integer totalPasses, Integer passesAccurate, String passesPercentage, Integer winnerId) {
        this._id = _id;
        this.fixtureId = fixtureId;
        this.round = round;
        this.teamId = teamId;
        this.teamName = teamName;
        this.side = side;
        this.rivalTeam = rivalTeam;
        this.rivalTeamId = rivalTeamId;
        this.score = score;
        this.shotsOnGoal = shotsOnGoal;
        this.shotsOffGoal = shotsOffGoal;
        this.totalShots = totalShots;
        this.blockedShots = blockedShots;
        this.shotsInsidebox = shotsInsidebox;
        this.shotsOutsidebox = shotsOutsidebox;
        this.fouls = fouls;
        this.corners = corners;
        this.offsides = offsides;
        this.ballPossession = ballPossession;
        this.yellowCards = yellowCards;
        this.redCards = redCards;
        this.goalkeeperSaves = goalkeeperSaves;
        this.totalPasses = totalPasses;
        this.passesAccurate = passesAccurate;
        this.passesPercentage = passesPercentage;
        this.winnerId = winnerId;
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

    public Integer getTeamId() {
        return teamId;
    }

    public void setTeamId(Integer teamId) {
        this.teamId = teamId;
    }

    public String getTeamName() {
        return teamName;
    }

    public void setTeamName(String teamName) {
        this.teamName = teamName;
    }

    public String getSide() {
        return side;
    }

    public void setSide(String side) {
        this.side = side;
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

    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }

    public Integer getShotsOnGoal() {
        return shotsOnGoal;
    }

    public void setShotsOnGoal(Integer shotsOnGoal) {
        this.shotsOnGoal = shotsOnGoal;
    }

    public Integer getShotsOffGoal() {
        return shotsOffGoal;
    }

    public void setShotsOffGoal(Integer shotsOffGoal) {
        this.shotsOffGoal = shotsOffGoal;
    }

    public Integer getTotalShots() {
        return totalShots;
    }

    public void setTotalShots(Integer totalShots) {
        this.totalShots = totalShots;
    }

    public Integer getBlockedShots() {
        return blockedShots;
    }

    public void setBlockedShots(Integer blockedShots) {
        this.blockedShots = blockedShots;
    }

    public Integer getShotsInsidebox() {
        return shotsInsidebox;
    }

    public void setShotsInsidebox(Integer shotsInsidebox) {
        this.shotsInsidebox = shotsInsidebox;
    }

    public Integer getShotsOutsidebox() {
        return shotsOutsidebox;
    }

    public void setShotsOutsidebox(Integer shotsOutsidebox) {
        this.shotsOutsidebox = shotsOutsidebox;
    }

    public Integer getFouls() {
        return fouls;
    }

    public void setFouls(Integer fouls) {
        this.fouls = fouls;
    }

    public Integer getCorners() {
        return corners;
    }

    public void setCorners(Integer corners) {
        this.corners = corners;
    }

    public Integer getOffsides() {
        return offsides;
    }

    public void setOffsides(Integer offsides) {
        this.offsides = offsides;
    }

    public String getBallPossession() {
        return ballPossession;
    }

    public void setBallPossession(String ballPossession) {
        this.ballPossession = ballPossession;
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

    public Integer getGoalkeeperSaves() {
        return goalkeeperSaves;
    }

    public void setGoalkeeperSaves(Integer goalkeeperSaves) {
        this.goalkeeperSaves = goalkeeperSaves;
    }

    public Integer getTotalPasses() {
        return totalPasses;
    }

    public void setTotalPasses(Integer totalPasses) {
        this.totalPasses = totalPasses;
    }

    public Integer getPassesAccurate() {
        return passesAccurate;
    }

    public void setPassesAccurate(Integer passesAccurate) {
        this.passesAccurate = passesAccurate;
    }

    public String getPassesPercentage() {
        return passesPercentage;
    }

    public void setPassesPercentage(String passesPercentage) {
        this.passesPercentage = passesPercentage;
    }

    public Integer getWinnerId() {
        return winnerId;
    }

    public void setWinnerId(Integer winnerId) {
        this.winnerId = winnerId;
    }
}
