package com.example.footballdatabackend.model;

import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "PlayersRealData")
public class Player {
    @Id
    private ObjectId _id;
    private String team;
    private Integer teamId;
    private String number;
    private String name;
    private String nickname;
    private String date;
    private Integer age;
    private Integer assists;
    private Integer blocks;
    private Integer concededGoals;
    private Integer dribblesAttempts;
    private Integer dribblesSuccess;
    private Integer duelsWon;
    private String firstname;
    private Integer foulsCommitted;
    private Integer foulsDrawn;
    private String fullname;
    private Integer goals;
    private String height;
    private Integer interceptions;
    private String isInjured;
    private Integer keyPasses;
    private String lastname;
    private String nationality;
    private Integer passes;
    private Integer passesAccuracy;
    private Integer penaltiesCommited;
    private Integer penaltiesMissed;
    private Integer penaltiesSaved;
    private Integer penaltiesScored;
    private Integer penaltiesWon;
    private String photo;
    private Integer playerId;
    private String position;
    private String rating;
    private Integer redCards;
    private Integer saves;
    private Integer shotsOn;
    private Integer tackles;
    private Integer teamIdAux;
    private Integer totalDuels;
    private Integer totalShots;
    private String weight;
    private Integer yellowCards;
    private Integer yellowredCards;
    private String comunioPoints;
    private String comunioPrice;
    private String misterFantasyPoints;
    private String misterFantasyPrice;
    private String futmondoPoints;
    private String futmondoPrice;
    private String biwengerPoints;
    private String biwengerPrice;
    private String laligaPoints;
    private String laligaPrice;

    public Player() {
    }

    public Player(ObjectId _id, String team, Integer teamId, String number, String name, String nickname, String date, Integer age, Integer assists, Integer blocks, Integer concededGoals, Integer dribblesAttempts, Integer dribblesSuccess, Integer duelsWon, String firstname, Integer foulsCommitted, Integer foulsDrawn, String fullname, Integer goals, String height, Integer interceptions, String isInjured, Integer keyPasses, String lastname, String nationality, Integer passes, Integer passesAccuracy, Integer penaltiesCommited, Integer penaltiesMissed, Integer penaltiesSaved, Integer penaltiesScored, Integer penaltiesWon, String photo, Integer playerId, String position, String rating, Integer redCards, Integer saves, Integer shotsOn, Integer tackles, Integer teamIdAux, Integer totalDuels, Integer totalShots, String weight, Integer yellowCards, Integer yellowredCards, String comunioPoints, String comunioPrice, String misterFantasyPoints, String misterFantasyPrice, String futmondoPoints, String futmondoPrice, String biwengerPoints, String biwengerPrice, String laligaPoints, String laligaPrice) {
        this._id = _id;
        this.team = team;
        this.teamId = teamId;
        this.number = number;
        this.name = name;
        this.nickname = nickname;
        this.date = date;
        this.age = age;
        this.assists = assists;
        this.blocks = blocks;
        this.concededGoals = concededGoals;
        this.dribblesAttempts = dribblesAttempts;
        this.dribblesSuccess = dribblesSuccess;
        this.duelsWon = duelsWon;
        this.firstname = firstname;
        this.foulsCommitted = foulsCommitted;
        this.foulsDrawn = foulsDrawn;
        this.fullname = fullname;
        this.goals = goals;
        this.height = height;
        this.interceptions = interceptions;
        this.isInjured = isInjured;
        this.keyPasses = keyPasses;
        this.lastname = lastname;
        this.nationality = nationality;
        this.passes = passes;
        this.passesAccuracy = passesAccuracy;
        this.penaltiesCommited = penaltiesCommited;
        this.penaltiesMissed = penaltiesMissed;
        this.penaltiesSaved = penaltiesSaved;
        this.penaltiesScored = penaltiesScored;
        this.penaltiesWon = penaltiesWon;
        this.photo = photo;
        this.playerId = playerId;
        this.position = position;
        this.rating = rating;
        this.redCards = redCards;
        this.saves = saves;
        this.shotsOn = shotsOn;
        this.tackles = tackles;
        this.teamIdAux = teamIdAux;
        this.totalDuels = totalDuels;
        this.totalShots = totalShots;
        this.weight = weight;
        this.yellowCards = yellowCards;
        this.yellowredCards = yellowredCards;
        this.comunioPoints = comunioPoints;
        this.comunioPrice = comunioPrice;
        this.misterFantasyPoints = misterFantasyPoints;
        this.misterFantasyPrice = misterFantasyPrice;
        this.futmondoPoints = futmondoPoints;
        this.futmondoPrice = futmondoPrice;
        this.biwengerPoints = biwengerPoints;
        this.biwengerPrice = biwengerPrice;
        this.laligaPoints = laligaPoints;
        this.laligaPrice = laligaPrice;
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

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public Integer getAssists() {
        return assists;
    }

    public void setAssists(Integer assists) {
        this.assists = assists;
    }

    public Integer getBlocks() {
        return blocks;
    }

    public void setBlocks(Integer blocks) {
        this.blocks = blocks;
    }

    public Integer getConcededGoals() {
        return concededGoals;
    }

    public void setConcededGoals(Integer concededGoals) {
        this.concededGoals = concededGoals;
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

    public Integer getDuelsWon() {
        return duelsWon;
    }

    public void setDuelsWon(Integer duelsWon) {
        this.duelsWon = duelsWon;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public Integer getFoulsCommitted() {
        return foulsCommitted;
    }

    public void setFoulsCommitted(Integer foulsCommitted) {
        this.foulsCommitted = foulsCommitted;
    }

    public Integer getFoulsDrawn() {
        return foulsDrawn;
    }

    public void setFoulsDrawn(Integer foulsDrawn) {
        this.foulsDrawn = foulsDrawn;
    }

    public String getFullname() {
        return fullname;
    }

    public void setFullname(String fullname) {
        this.fullname = fullname;
    }

    public Integer getGoals() {
        return goals;
    }

    public void setGoals(Integer goals) {
        this.goals = goals;
    }

    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public Integer getInterceptions() {
        return interceptions;
    }

    public void setInterceptions(Integer interceptions) {
        this.interceptions = interceptions;
    }

    public String getIsInjured() {
        return isInjured;
    }

    public void setIsInjured(String isInjured) {
        this.isInjured = isInjured;
    }

    public Integer getKeyPasses() {
        return keyPasses;
    }

    public void setKeyPasses(Integer keyPasses) {
        this.keyPasses = keyPasses;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public String getNationality() {
        return nationality;
    }

    public void setNationality(String nationality) {
        this.nationality = nationality;
    }

    public Integer getPasses() {
        return passes;
    }

    public void setPasses(Integer passes) {
        this.passes = passes;
    }

    public Integer getPassesAccuracy() {
        return passesAccuracy;
    }

    public void setPassesAccuracy(Integer passesAccuracy) {
        this.passesAccuracy = passesAccuracy;
    }

    public Integer getPenaltiesCommited() {
        return penaltiesCommited;
    }

    public void setPenaltiesCommited(Integer penaltiesCommited) {
        this.penaltiesCommited = penaltiesCommited;
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

    public Integer getPenaltiesScored() {
        return penaltiesScored;
    }

    public void setPenaltiesScored(Integer penaltiesScored) {
        this.penaltiesScored = penaltiesScored;
    }

    public Integer getPenaltiesWon() {
        return penaltiesWon;
    }

    public void setPenaltiesWon(Integer penaltiesWon) {
        this.penaltiesWon = penaltiesWon;
    }

    public String getPhoto() {
        return photo;
    }

    public void setPhoto(String photo) {
        this.photo = photo;
    }

    public Integer getPlayerId() {
        return playerId;
    }

    public void setPlayerId(Integer playerId) {
        this.playerId = playerId;
    }

    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public String getRating() {
        return rating;
    }

    public void setRating(String rating) {
        this.rating = rating;
    }

    public Integer getRedCards() {
        return redCards;
    }

    public void setRedCards(Integer redCards) {
        this.redCards = redCards;
    }

    public Integer getSaves() {
        return saves;
    }

    public void setSaves(Integer saves) {
        this.saves = saves;
    }

    public Integer getShotsOn() {
        return shotsOn;
    }

    public void setShotsOn(Integer shotsOn) {
        this.shotsOn = shotsOn;
    }

    public Integer getTackles() {
        return tackles;
    }

    public void setTackles(Integer tackles) {
        this.tackles = tackles;
    }

    public Integer getTeamIdAux() {
        return teamIdAux;
    }

    public void setTeamIdAux(Integer teamIdAux) {
        this.teamIdAux = teamIdAux;
    }

    public Integer getTotalDuels() {
        return totalDuels;
    }

    public void setTotalDuels(Integer totalDuels) {
        this.totalDuels = totalDuels;
    }

    public Integer getTotalShots() {
        return totalShots;
    }

    public void setTotalShots(Integer totalShots) {
        this.totalShots = totalShots;
    }

    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }

    public Integer getYellowCards() {
        return yellowCards;
    }

    public void setYellowCards(Integer yellowCards) {
        this.yellowCards = yellowCards;
    }

    public Integer getYellowredCards() {
        return yellowredCards;
    }

    public void setYellowredCards(Integer yellowredCards) {
        this.yellowredCards = yellowredCards;
    }

    public String getComunioPoints() {
        return comunioPoints;
    }

    public void setComunioPoints(String comunioPoints) {
        this.comunioPoints = comunioPoints;
    }

    public String getComunioPrice() {
        return comunioPrice;
    }

    public void setComunioPrice(String comunioPrice) {
        this.comunioPrice = comunioPrice;
    }

    public String getMisterFantasyPoints() {
        return misterFantasyPoints;
    }

    public void setMisterFantasyPoints(String misterFantasyPoints) {
        this.misterFantasyPoints = misterFantasyPoints;
    }

    public String getMisterFantasyPrice() {
        return misterFantasyPrice;
    }

    public void setMisterFantasyPrice(String misterFantasyPrice) {
        this.misterFantasyPrice = misterFantasyPrice;
    }

    public String getFutmondoPoints() {
        return futmondoPoints;
    }

    public void setFutmondoPoints(String futmondoPoints) {
        this.futmondoPoints = futmondoPoints;
    }

    public String getFutmondoPrice() {
        return futmondoPrice;
    }

    public void setFutmondoPrice(String futmondoPrice) {
        this.futmondoPrice = futmondoPrice;
    }

    public String getBiwengerPoints() {
        return biwengerPoints;
    }

    public void setBiwengerPoints(String biwengerPoints) {
        this.biwengerPoints = biwengerPoints;
    }

    public String getBiwengerPrice() {
        return biwengerPrice;
    }

    public void setBiwengerPrice(String biwengerPrice) {
        this.biwengerPrice = biwengerPrice;
    }

    public String getLaligaPoints() {
        return laligaPoints;
    }

    public void setLaligaPoints(String laligaPoints) {
        this.laligaPoints = laligaPoints;
    }

    public String getLaligaPrice() {
        return laligaPrice;
    }

    public void setLaligaPrice(String laligaPrice) {
        this.laligaPrice = laligaPrice;
    }

    public ObjectId get_id() {
        return _id;
    }

    public void set_id(ObjectId _id) {
        this._id = _id;
    }
}
