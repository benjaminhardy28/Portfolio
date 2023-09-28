import "./Navbar.css";
import { Link, useMatch, useResolvedPath } from "react-router-dom"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser, faBell } from "@fortawesome/free-solid-svg-icons";

export default function Navbar() {
    return <nav className="nav">
        <Link to="/" className="site-title" >Notify</Link>
        <ul>
            <CustomLink to="/view-notifications">
                <FontAwesomeIcon icon={faBell} size="2xl" style={{color: "#fdf7f7",}} />
                View Notifications
            </CustomLink>
            <CustomLink to="/account-information">
                <FontAwesomeIcon icon={faUser} size="2xl" style={{color: "#fdf7f7",}} />
                Account Information
            </CustomLink>
        </ul>
    </nav>
}

function CustomLink({ to, children, ...props }) {
    const resolvedPath = useResolvedPath(to)
    const isActive = useMatch({ path: resolvedPath.pathname, end: true})
    return (
        <li className={isActive ? "active" : ""}>
            <Link to={to} {...props}>
                { children }
            </Link>
        </li>
    )
}