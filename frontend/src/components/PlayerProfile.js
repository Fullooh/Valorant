import React, { useState } from "react";

const PlayerProfile = () => {
  // Placeholder data simulating the API response
  const [playerData, setPlayerData] = useState({
    username: "Fullooh#ttv",
    rank: "Diamond 3",
    kda: "1.6",
    winLossRatio: "0.75",
    averageCombatScore: "250",
  });

  return (
    <div>
      <h1>Player Profile</h1>
      <p>Username: {playerData.username}</p>
      <p>Rank: {playerData.rank}</p>
      <p>KDA: {playerData.kda}</p>
      <p>Win/Loss Ratio: {playerData.winLossRatio}</p>
      <p>Average Combat Score: {playerData.averageCombatScore}</p>
    </div>
  );
};

export default PlayerProfile;
