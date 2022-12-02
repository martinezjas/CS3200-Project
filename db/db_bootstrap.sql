-- noinspection SqlNoDataSourceInspectionForFile

CREATE DATABASE our_app;
CREATE USER 'admin'@'%' IDENTIFIED BY 'Daybreak-Craving-Unmolded-Shelter-Uselessly3';
GRANT ALL PRIVILEGES ON our_app.* TO 'admin'@'%';
FLUSH PRIVILEGES;

USE our_app;


CREATE TABLE schedule (
    schedule_id INT NOT NULL AUTO_INCREMENT,
    season YEAR NOT NULL,
    PRIMARY KEY (schedule_id)
);

INSERT INTO schedule (season)
VALUES (2022);


CREATE TABLE team (
    teamName VARCHAR(30) NOT NULL,
    country VARCHAR(30) NOT NULL,
    city VARCHAR(30) NOT NULL,
    win_percentage DOUBLE,
    avg_yrds_per_push DOUBLE,
    net_yrds_per_pass DOUBLE,
    inter_prcnt DOUBLE,
    conference VARCHAR(30) NOT NULL,
    division VARCHAR(30) NOT NULL,
    schedule_id INT NOT NULL,
    projected_perf DOUBLE,
    PRIMARY KEY (teamName),
    FOREIGN KEY (schedule_id) REFERENCES schedule (schedule_id)
);

INSERT INTO team
VALUES
    ('Northeastern Huskies', 'United States', 'Boston', 
    78.9878, 11.30, 32.2400, 64.8743, 
    'New England', 'Massachusetts', 22, 52.000) ,
    ('BU Terriers', 'United States', 'Boston',
    64.4538, 18.4324, 24.9543, 78.4342,
    'New England', 'Massachusetts', 22, 48.000);

CREATE TABLE coach (
    coach_id INT NOT NULL AUTO_INCREMENT,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    teamName VARCHAR(30) NOT NULL,
    PRIMARY KEY (coach_id),
    FOREIGN KEY (teamName) REFERENCES team (teamName)
);

INSERT INTO coach
VALUES
    (1, 'Joseph', 'Aoun', 'Northeastern Huskies'),
    (2, 'Robert', 'Brown', 'BU Terriers');

CREATE TABLE athlete (
    athlete_id INT NOT NULL AUTO_INCREMENT,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    height DOUBLE NOT NULL,
    weight DOUBLE NOT NULL,
    age DOUBLE NOT NULL,
    teamName VARCHAR(30) NOT NULL,
    PRIMARY KEY (athlete_id),
    FOREIGN KEY (teamName) REFERENCES team (teamName)
);

INSERT INTO athlete
VALUES
    (1, 'Paws', 'Husky', 5.950, 182, 32, 'Northeastern Huskies'),
    (2, 'Rhett', 'Terrier', 5.432, 145, 30, 'BU Terriers');

CREATE TABLE athlete_career_stats (
    athlete_id INT NOT NULL,
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
    (1, 15, 10, 326, 5, 3, 20, 32, 40, 9, 7, 60, 24, 20),
    (2, 20, 15, 434, 3, 2, 32, 40, 32, 1, 0, 150, 30, 24);

CREATE TABLE bet (
    bet_id INT NOT NULL AUTO_INCREMENT,
    better_id INT NOT NULL, -- See note in better table definition below
    favored_moneyline DOUBLE NOT NULL,
    underdog_moneyline DOUBLE NOT NULL,
    favored_team_bet_amount DOUBLE NOT NULL,
    underdog_team_bet_amount DOUBLE NOT NULL,
    favored_team_spread_amount DOUBLE NOT NULL,
    underdog_team_spread_amount DOUBLE NOT NULL,
    PRIMARY KEY (bet_id)
);

INSERT INTO bet
VALUES 

CREATE TABLE odds (
    odds_ID INT NOT NULL AUTO_INCREMENT,
    calculated_favored_team_ml DOUBLE NOT NULL,
    calculated_underdog_team_ml DOUBLE NOT NULL,
    calcuated_underdog_total DOUBLE NOT NULL,
    calculated_favored_total DOUBLE NOT NULL,
    calculated_favored_spread DOUBLE NOT NULL,
    caclulated_underdog_spread DOUBLE NOT NULL,
    PRIMARY KEY (odds_ID)
);

INSERT INTO odds
VALUES



-- Another idea would probably be doing away with odds_and_bets and adding a oddsID to a bet. This isn't necessary, but
-- it would make it cleaner.
CREATE TABLE odds_and_bets(
    oddsID INT NOT NULL,
    betID INT NOT NULL,
    FOREIGN KEY (oddsID) REFERENCES odds (odds_ID),
    FOREIGN KEY (betID) REFERENCES bet (bet_id)
);

INSERT INTO odds_and_bets
VALUES

CREATE TABLE game (
    game_id INT NOT NULL AUTO_INCREMENT,
    homeTeam VARCHAR(30) NOT NULL,
    awayTeam VARCHAR(30) NOT NULL,
    gameStatus VARCHAR(30) NOT NULL,
    homeResult VARCHAR(5),
    awayResult VARCHAR(5),
    finalScore VARCHAR(20),
    weather VARCHAR(30) NOT NULL,
    scheduleID INT NOT NULL,
    oddsID INT NOT NULL,
    PRIMARY KEY (game_id),
    FOREIGN KEY (homeTeam) REFERENCES team (teamName),
    FOREIGN KEY (awayTeam) REFERENCES team (teamName),
    FOREIGN KEY (scheduleID) REFERENCES schedule (schedule_id),
    FOREIGN KEY (oddsID) REFERENCES odds (odds_ID)
);

INSERT INTO game
VALUES
    (1, 'Northeastern Huskies', 'BU Terriers', 'Completed', 'Win', 'Loss', '24-17', 'Sunny, Low 40s', 1, 1);


CREATE TABLE better (
    user_id INT NOT NULL AUTO_INCREMENT,
    currencyTotal DOUBLE NOT NULL,
    -- betID INT, We need to discuss decoupling betIDs from betters to allow multiple bets to one better
    PRIMARY KEY (user_id)
    -- FOREIGN KEY (betID) REFERENCES bet (bet_id)
);

INSERT INTO better
VALUES

CREATE TABLE team_in_game (
    teaminGameName VARCHAR(30) NOT NULL,
    teamStats VARCHAR(200) NOT NULL,
    PRIMARY KEY (teaminGameName),
    FOREIGN KEY (teaminGameName) REFERENCES team (teamName)
);

INSERT INTO team_in_game
VALUES
    ('Northeastern Huskies', 'ExampleStatsHere'),
    ('BU Terriers', 'ExampleStatsHere');