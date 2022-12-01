-- noinspection SqlNoDataSourceInspectionForFile

CREATE DATABASE our_app;
CREATE USER 'admin'@'%' IDENTIFIED BY 'Daybreak-Craving-Unmolded-Shelter-Uselessly3';
GRANT ALL PRIVILEGES ON our_app.* TO 'admin'@'%';
FLUSH PRIVILEGES;

USE our_app;


CREATE TABLE schedule (
    schedule_id INT,
    season YEAR,
    PRIMARY KEY (schedule_id)
);

INSERT INTO schedule 
VALUES
    (22, 2022);


CREATE TABLE team (
    teamName VARCHAR(30),
    country VARCHAR(30),
    city VARCHAR(30),
    win_percentage DOUBLE,
    avg_yrds_per_push DOUBLE,
    net_yrds_per_pass DOUBLE,
    inter_prcnt DOUBLE,
    conference VARCHAR(30),
    division VARCHAR(30),
    schedule_id INT,
    projected_perf DOUBLE,
    PRIMARY KEY (teamName),
    FOREIGN KEY (schedule_id) REFERENCES schedule (schedule_id)
);

INSERT INTO team
VALUES
    

CREATE TABLE coach (
    coach_id INT,
    firstName VARCHAR(20),
    lastName VARCHAR(20),
    teamName VARCHAR(30),
    PRIMARY KEY (coach_id),
    FOREIGN KEY (teamName) REFERENCES team (teamName)
);

INSERT INTO coach
VALUES
    

CREATE TABLE athlete (
    athlete_id INT,
    firstName VARCHAR(20),
    lastName VARCHAR(20),
    height DOUBLE,
    weight DOUBLE,
    age DOUBLE,
    teamName VARCHAR(30),
    PRIMARY KEY (athlete_id),
    FOREIGN KEY (teamName) REFERENCES team (teamName)
);

INSERT INTO athlete
VALUES
    

CREATE TABLE athlete_career_stats (
    athlete_id INT,
    pass_attempts INT,
    completed_passes INT,
    -- pass_percentage INT, can be pass_attempts / completed_passes in a view
    passing_yards INT,
    -- avg_yds_per_pass_attempt INT, can be pass_attempts / passing_yards in a view
    touchdown_passes INT,
    interceptions_thrown INT,
    times_sacked INT,
    rushing_attempts INT,
    rushing_yards INT,
    -- avg_yds_per_rush INT, can be rushing_yards / rushing_attempts
    rushing_touchdowns INT,
    rushing_first_downs INT,
    longest_rush INT,
    total_fumbles INT,
    fumbles_lost INT,
    FOREIGN KEY (athlete_id) REFERENCES athlete (athlete_id),
    PRIMARY KEY (athlete_id)
);

INSERT INTO athlete_career_stats
VALUES


CREATE TABLE bet (
    bet_id INT,
    better_id INT, -- See note in better table definition below
    favored_moneyline DOUBLE,
    underdog_moneyline DOUBLE,
    favored_team_bet_amount DOUBLE,
    underdog_team_bet_amount DOUBLE,
    favored_team_spread_amount DOUBLE,
    underdog_team_spread_amount DOUBLE,
    PRIMARY KEY (bet_id)
);

INSERT INTO bet
VALUES 

CREATE TABLE odds (
    odds_ID INT,
    calculated_favored_team_ml DOUBLE,
    calculated_underdog_team_ml DOUBLE,
    calcuated_underdog_total DOUBLE,
    calculated_favored_total DOUBLE,
    calculated_favored_spread DOUBLE,
    caclulated_underdog_spread DOUBLE,
    PRIMARY KEY (odds_ID)
);

INSERT INTO odds
VALUES



-- Another idea would probably be doing away with odds_and_bets and adding a oddsID to a bet. This isn't necessary, but
-- it would make it cleaner.
CREATE TABLE odds_and_bets(
    oddsID INT,
    betID INT,
    FOREIGN KEY (oddsID) REFERENCES odds (odds_ID),
    FOREIGN KEY (betID) REFERENCES bet (bet_id)
);

INSERT INTO odds_and_bets
VALUES

CREATE TABLE game (
    game_id INT,
    homeTeam VARCHAR(30),
    awayTeam VARCHAR(30),
    gameStatus VARCHAR(30),
    homeResult VARCHAR(5),
    awayResult VARCHAR(5),
    finalScore VARCHAR(20),
    weather VARCHAR(30),
    scheduleID INT,
    oddsID INT,
    PRIMARY KEY (game_id),
    FOREIGN KEY (homeTeam) REFERENCES team (teamName),
    FOREIGN KEY (awayTeam) REFERENCES team (teamName),
    FOREIGN KEY (scheduleID) REFERENCES schedule (schedule_id),
    FOREIGN KEY (oddsID) REFERENCES odds (odds_ID)
);

INSERT INTO game
VALUES

CREATE TABLE better (
    user_id INT,
    currencyTotal DOUBLE,
    -- betID INT, We need to discuss decoupling betIDs from betters to allow multiple bets to one better
    PRIMARY KEY (user_id)
    -- FOREIGN KEY (betID) REFERENCES bet (bet_id)
);

INSERT INTO better
VALUES

CREATE TABLE team_in_game (
    teaminGameName VARCHAR(30),
    teamStats VARCHAR(200),
    PRIMARY KEY (teaminGameName),
    FOREIGN KEY (teaminGameName) REFERENCES team (teamName)
);

INSERT INTO team_in_game
VALUES