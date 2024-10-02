// src/pages/HomePage.js
import React from "react";
import { Link } from "react-router-dom";

const HomePage = () => {
  return (
    <div>
      <h1>Welcome to Valorant Predictor</h1>
      <p>
        This application predicts the outcome of your next Valorant match based
        on previous performance.
      </p>
      <Link to="/predict">Go to Prediction Page</Link>
    </div>
  );
};

export default HomePage; // Ensure this is a default export
