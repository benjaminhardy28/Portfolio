//import "./NotifsBox.css";
import NotifCard from "./NotifCard";
import AddNotifCard from "./AddNotifCard";
import { useState, useEffect } from 'react'
import CreateNotifCard from './CreateNotifCard'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCircleXmark } from "@fortawesome/free-solid-svg-icons";


const NotifsBox = ( {props} ) => {
    const [showAddNotif, setShowAddNotif] = useState(false)

    return (
    <div >
        <div className= "notifCardContainer">
            <button className= "addNotif notifCard" onClick={() => setShowAddNotif(true)}>
                <AddNotifCard/>
            </button>
            {Array.isArray(props) && props.length > 0 ? (
                props.map((user_info) => (
                    <NotifCard properties={user_info} key={user_info.id} />
                ))
            ) : (
                <div>No data to display.</div>
            )}
        </div>
        {showAddNotif && (
            <div className="overlay">
                <CreateNotifCard>
                    <button className = "exitButton" onClick={() => setShowAddNotif(false)}>
                        <div className = "exitButtonIcon">
                            <FontAwesomeIcon icon={faCircleXmark} size="2xl" style={{color: "#f20707",}} />
                        </div>
                    </button>
                </CreateNotifCard> 
            </div>
        )}  
    </div>
    );
};
//<FontAwesomeIcon icon={faCircleXmark} size="2xs" style={{color: "#f20707",}} />
export default NotifsBox;
//{`notifCardContainer${showAddNotif ? 'blur' : ''}`}