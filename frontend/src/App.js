import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./pages/HomePage";
import PredictionPage from "./pages/PredictionPage";
import Navbar from "./components/Navbar"; // Import Navbar
import "./index.css"; // Import Tailwind CSS styles

function App() {
  return (
    <Router>
      <Navbar /> {/* Add the Navbar here */}
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/predict" element={<PredictionPage />} />
      </Routes>
    </Router>
  );
}

export default App;
