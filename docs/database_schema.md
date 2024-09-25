# Database Schema

## player_stats Table
| Column Name   | Data Type | Description                  |
|---------------|-----------|------------------------------|
| id            | Integer   | Primary key, auto-increment. |
| player_name   | String    | Name of the player.          |
| match_id      | Integer   | ID of the match.             |
| kills         | Integer   | Number of kills.             |
| deaths        | Integer   | Number of deaths.            |
| assists       | Integer   | Number of assists.           |
| economy_status| Float     | Economy status in the match. |
