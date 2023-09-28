//import "./NotifCard.css";
import { Link } from "react-router-dom"
import React from 'react';



const NotifCard = ( {properties} ) => {
    const handleClick = () => {
        // Handle any additional logic if needed
        console.log('Card clicked!');
      };


    return (
        <Link to={`/view-notifications/noficiation-properties/${properties.id}`} key={properties.id} onClick={handleClick} className="notifCard">
            <div className="cardTitle">
                <p className="cardDate"> 26/7 </p>
                <p className="cardWesbite"> {properties.website_url} </p>
            </div>
            <p> {properties.notif_description} </p>
        </Link>
    );
}

export default NotifCard;