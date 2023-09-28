//import "./NotifSettings.css";
import { useState, useEffect } from 'react';

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSquareCheck } from "@fortawesome/free-solid-svg-icons";
import { faSquareFull, faMessage, faEnvelope } from "@fortawesome/free-regular-svg-icons";
import DeleteNotifCard from './DeleteNotifCard'


const NotifSettings = ( { props } ) => {

    const [textCheckBox, setTextCheckBox] = useState(false)
    const [emailCheckBox, setEmailCheckBox] = useState(false)
    const [notifPrompt, setNotifPrompt] = useState(false)
    const [editing, setEditing] = useState(false)
    const [deletePopUp, setDeletePopUp] = useState(false)

    const handledeletePopUp = () => {
        setDeletePopUp(true)
    }

    const handleEditing = () => {
        setEditing(!editing)
    }

    const handleTextCheckBox = (event) => {
        setTextCheckBox(!textCheckBox);
    };
    
    const handleEmailCheckBox = (event) => {
        setEmailCheckBox(!emailCheckBox);
    };

    return (

        <div className="notifSettings">
            {/*{ deletePopUp &&(
                <div className="overlay">
                    <DeleteNotifCard/>
                </div>
            )};
            <div className="deleteButtonContainer">
                <button className="deleteButton" >
                     Delete
                </button>
            </div> */}
            <h>
                Notification Communication Method
            </h>
            <div className="buttonsContainer">
                <div className="buttonContainer">
                    <FontAwesomeIcon className= "messageIconExpansion" icon={faMessage} size="2xl" style={{color: "#00ff04",}} />
                    <button className="checkBoxButton" onClick={handleTextCheckBox} disabled={!editing}>
                        <FontAwesomeIcon className={textCheckBox ? "checkBoxExpansion" : ""} icon={textCheckBox ? faSquareCheck : faSquareFull} size="2xl" style={{color: "#5c2cde",}} />
                    </button>
                </div>
                <div className="buttonContainer">
                    <FontAwesomeIcon className= "messageIconExpansion" icon={faEnvelope} size="2xl" style={{color: "#005eff",}} />
                    <button className="checkBoxButton" onClick={handleEmailCheckBox} disabled={!editing}>
                        <FontAwesomeIcon className={emailCheckBox ? "checkBoxExpansion" : ""} icon={emailCheckBox ? faSquareCheck : faSquareFull} size="2xl" style={{color: "#5c2cde",}} />
                    </button>
                </div>
            </div>
            <div className="inputGroup">
                    <input type="text" id="notifPrompt" className="notifDescription inputGroup__input" required defaultValue={props[0].prompt} disabled={!editing}/>
                    <label htmlFor="notifPrompt" className="inputGroup__label">
                        Notification Description
                    </label>
                </div>
            <div className="editButtonContainer">
                <button className="button" onClick={handleEditing}>
                     {editing ? "Save new Settings": "Edit Notification Settings"}
                </button>
            </div>
        </div>
    );
};

export default NotifSettings;