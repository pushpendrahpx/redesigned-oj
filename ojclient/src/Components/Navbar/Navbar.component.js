import React from "react"
import { Link } from "react-router-dom";
import "./Navbar.component.css";

function NavbarComponent(){
    return <div className="navbar-base">
        <div className="navbar-base-object">
            <a className="navbar-brand" href="/">Redesigned OJ</a>

            <div className="navbar-controls">
                <Link className="account" to="/login">Login</Link>
            </div>
        </div>
    </div>
}
export default NavbarComponent