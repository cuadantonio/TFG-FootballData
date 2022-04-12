package com.example.footballdatabackend.model;

import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "TeamsData")
public class Team {

    @Id
    private ObjectId _id;
    private Integer id;
    private String name;
    private String logo;
    private Integer totalYellowCards;
    private Integer totalRedCards;
    private Integer homeCleanSheets;
    private Integer awayCleanSheets;
    private Integer homeFailedToScore;
    private Integer awayFailedToScore;
    private Integer totalWins;
    private Integer totalLoses;
    private Integer totalDraws;
    private double homeGoalsForAverage;
    private double awayGoalsForAverage;
    private double totalGoalsForAverage;
    private double homeGoalsAgainstAverage;
    private double awayGoalsAgainstAverage;
    private double totalGoalsAgainstAverage;
    private Integer homeGoalsFor;
    private Integer awayGoalsFor;
    private Integer totalGoalsFor;
    private Integer homeGoalsAgainst;
    private Integer awayGoalsAgainst;
    private Integer totalGoalsAgainst;
    private String scoredPenaltiesPercentage;
    private Integer scoredPenalties;
    private String missedPenaltiesPercentage;
    private Integer missedPenalties;

    public Team() {
    }

    public Team(ObjectId _id, Integer id, String name, String logo, Integer totalYellowCards, Integer totalRedCards, Integer homeCleanSheets, Integer awayCleanSheets, Integer homeFailedToScore, Integer awayFailedToScore, Integer totalWins, Integer totalLoses, Integer totalDraws, double homeGoalsForAverage, double awayGoalsForAverage, double totalGoalsForAverage, double homeGoalsAgainstAverage, double awayGoalsAgainstAverage, double totalGoalsAgainstAverage, Integer homeGoalsFor, Integer awayGoalsFor, Integer totalGoalsFor, Integer homeGoalsAgainst, Integer awayGoalsAgainst, Integer totalGoalsAgainst, String scoredPenaltiesPercentage, Integer scoredPenalties, String missedPenaltiesPercentage, Integer missedPenalties) {
        this._id = _id;
        this.id = id;
        this.name = name;
        this.logo = logo;
        this.totalYellowCards = totalYellowCards;
        this.totalRedCards = totalRedCards;
        this.homeCleanSheets = homeCleanSheets;
        this.awayCleanSheets = awayCleanSheets;
        this.homeFailedToScore = homeFailedToScore;
        this.awayFailedToScore = awayFailedToScore;
        this.totalWins = totalWins;
        this.totalLoses = totalLoses;
        this.totalDraws = totalDraws;
        this.homeGoalsForAverage = homeGoalsForAverage;
        this.awayGoalsForAverage = awayGoalsForAverage;
        this.totalGoalsForAverage = totalGoalsForAverage;
        this.homeGoalsAgainstAverage = homeGoalsAgainstAverage;
        this.awayGoalsAgainstAverage = awayGoalsAgainstAverage;
        this.totalGoalsAgainstAverage = totalGoalsAgainstAverage;
        this.homeGoalsFor = homeGoalsFor;
        this.awayGoalsFor = awayGoalsFor;
        this.totalGoalsFor = totalGoalsFor;
        this.homeGoalsAgainst = homeGoalsAgainst;
        this.awayGoalsAgainst = awayGoalsAgainst;
        this.totalGoalsAgainst = totalGoalsAgainst;
        this.scoredPenaltiesPercentage = scoredPenaltiesPercentage;
        this.scoredPenalties = scoredPenalties;
        this.missedPenaltiesPercentage = missedPenaltiesPercentage;
        this.missedPenalties = missedPenalties;
    }

    public ObjectId get_id() {
        return _id;
    }

    public void set_id(ObjectId _id) {
        this._id = _id;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLogo() {
        return logo;
    }

    public void setLogo(String logo) {
        this.logo = logo;
    }

    public Integer getTotalYellowCards() {
        return totalYellowCards;
    }

    public void setTotalYellowCards(Integer totalYellowCards) {
        this.totalYellowCards = totalYellowCards;
    }

    public Integer getTotalRedCards() {
        return totalRedCards;
    }

    public void setTotalRedCards(Integer totalRedCards) {
        this.totalRedCards = totalRedCards;
    }

    public Integer getHomeCleanSheets() {
        return homeCleanSheets;
    }

    public void setHomeCleanSheets(Integer homeCleanSheets) {
        this.homeCleanSheets = homeCleanSheets;
    }

    public Integer getAwayCleanSheets() {
        return awayCleanSheets;
    }

    public void setAwayCleanSheets(Integer awayCleanSheets) {
        this.awayCleanSheets = awayCleanSheets;
    }

    public Integer getHomeFailedToScore() {
        return homeFailedToScore;
    }

    public void setHomeFailedToScore(Integer homeFailedToScore) {
        this.homeFailedToScore = homeFailedToScore;
    }

    public Integer getAwayFailedToScore() {
        return awayFailedToScore;
    }

    public void setAwayFailedToScore(Integer awayFailedToScore) {
        this.awayFailedToScore = awayFailedToScore;
    }

    public Integer getTotalWins() {
        return totalWins;
    }

    public void setTotalWins(Integer totalWins) {
        this.totalWins = totalWins;
    }

    public Integer getTotalLoses() {
        return totalLoses;
    }

    public void setTotalLoses(Integer totalLoses) {
        this.totalLoses = totalLoses;
    }

    public Integer getTotalDraws() {
        return totalDraws;
    }

    public void setTotalDraws(Integer totalDraws) {
        this.totalDraws = totalDraws;
    }

    public double getHomeGoalsForAverage() {
        return homeGoalsForAverage;
    }

    public void setHomeGoalsForAverage(double homeGoalsForAverage) {
        this.homeGoalsForAverage = homeGoalsForAverage;
    }

    public double getAwayGoalsForAverage() {
        return awayGoalsForAverage;
    }

    public void setAwayGoalsForAverage(double awayGoalsForAverage) {
        this.awayGoalsForAverage = awayGoalsForAverage;
    }

    public double getTotalGoalsForAverage() {
        return totalGoalsForAverage;
    }

    public void setTotalGoalsForAverage(double totalGoalsForAverage) {
        this.totalGoalsForAverage = totalGoalsForAverage;
    }

    public double getHomeGoalsAgainstAverage() {
        return homeGoalsAgainstAverage;
    }

    public void setHomeGoalsAgainstAverage(double homeGoalsAgainstAverage) {
        this.homeGoalsAgainstAverage = homeGoalsAgainstAverage;
    }

    public double getAwayGoalsAgainstAverage() {
        return awayGoalsAgainstAverage;
    }

    public void setAwayGoalsAgainstAverage(double awayGoalsAgainstAverage) {
        this.awayGoalsAgainstAverage = awayGoalsAgainstAverage;
    }

    public double getTotalGoalsAgainstAverage() {
        return totalGoalsAgainstAverage;
    }

    public void setTotalGoalsAgainstAverage(double totalGoalsAgainstAverage) {
        this.totalGoalsAgainstAverage = totalGoalsAgainstAverage;
    }

    public Integer getHomeGoalsFor() {
        return homeGoalsFor;
    }

    public void setHomeGoalsFor(Integer homeGoalsFor) {
        this.homeGoalsFor = homeGoalsFor;
    }

    public Integer getAwayGoalsFor() {
        return awayGoalsFor;
    }

    public void setAwayGoalsFor(Integer awayGoalsFor) {
        this.awayGoalsFor = awayGoalsFor;
    }

    public Integer getTotalGoalsFor() {
        return totalGoalsFor;
    }

    public void setTotalGoalsFor(Integer totalGoalsFor) {
        this.totalGoalsFor = totalGoalsFor;
    }

    public Integer getHomeGoalsAgainst() {
        return homeGoalsAgainst;
    }

    public void setHomeGoalsAgainst(Integer homeGoalsAgainst) {
        this.homeGoalsAgainst = homeGoalsAgainst;
    }

    public Integer getAwayGoalsAgainst() {
        return awayGoalsAgainst;
    }

    public void setAwayGoalsAgainst(Integer awayGoalsAgainst) {
        this.awayGoalsAgainst = awayGoalsAgainst;
    }

    public Integer getTotalGoalsAgainst() {
        return totalGoalsAgainst;
    }

    public void setTotalGoalsAgainst(Integer totalGoalsAgainst) {
        this.totalGoalsAgainst = totalGoalsAgainst;
    }

    public String getScoredPenaltiesPercentage() {
        return scoredPenaltiesPercentage;
    }

    public void setScoredPenaltiesPercentage(String scoredPenaltiesPercentage) {
        this.scoredPenaltiesPercentage = scoredPenaltiesPercentage;
    }

    public Integer getScoredPenalties() {
        return scoredPenalties;
    }

    public void setScoredPenalties(Integer scoredPenalties) {
        this.scoredPenalties = scoredPenalties;
    }

    public String getMissedPenaltiesPercentage() {
        return missedPenaltiesPercentage;
    }

    public void setMissedPenaltiesPercentage(String missedPenaltiesPercentage) {
        this.missedPenaltiesPercentage = missedPenaltiesPercentage;
    }

    public Integer getMissedPenalties() {
        return missedPenalties;
    }

    public void setMissedPenalties(Integer missedPenalties) {
        this.missedPenalties = missedPenalties;
    }
}
