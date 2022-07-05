import React from "react";
import {
  
  Routes,
  Route
} from "react-router-dom";

import HomePage from "./Pages/Home/Home.page";
import AboutPage from "./Pages/About/About.page";


import './App.css';
import NavbarComponent from "./Components/Navbar/Navbar.component";
import FooterComponent from "./Components/Footer/Footer.component";
import ProblemsetPage from "./Pages/Problemset/Problemset.page";
import LoginPage from "./Pages/Login/Login.page";
import RegisterPage from "./Pages/Register/Register.page";
import ProblemPage from "./Pages/Problem/Problem.page";
import ProblemSubmitPage from "./Pages/Problem/submit/ProblemSubmit.page";

export default function App() {
  return (

        <div>
            <NavbarComponent />
        <Routes>
          <Route exact path="" element={<HomePage />}  />
          <Route path="/problemset" element={<ProblemsetPage /> } />
          <Route path="/login" element={<LoginPage /> } />
          <Route path="/register" element={<RegisterPage /> } />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/problem/:id*" element={<ProblemPage /> } />
        </Routes>

            <FooterComponent />
        </div>
  );
}