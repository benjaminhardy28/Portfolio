//import "./CreateNotifCard.css";
import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSquareCheck } from "@fortawesome/free-solid-svg-icons";
import axios from '../../api/axios.js';
import useAuth from '../../hooks/useAuth';
import { faSquareFull, faMessage, faEnvelope } from "@fortawesome/free-regular-svg-icons";

const SET_NOTIF_URL = "set_notification";

const CreateNotifCard = ({ children }) => {
    const { auth } = useAuth();
    const [websiteURLText, setWebsiteURLText] = useState('')
    const [websitePromptText, setWebsitePromptText] = useState('')
    const [notifName, setNotifName] = useState('')
    const [textCheckBox, setTextCheckBox] = useState(false)
    const [emailCheckBox, setEmailCheckBox] = useState(false)

    const handleTextCheckBox = (event) => {
        setTextCheckBox(!textCheckBox);
    };
    
    const handleEmailCheckBox = (event) => {
        setEmailCheckBox(!emailCheckBox);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try{
            const response = await axios.post(
                SET_NOTIF_URL,
                JSON.stringify({
                  website_url: websiteURLText,
                  notif_description: websitePromptText,
                  communication_prefs: 2,
                  websites_update: 0
                }),
                {
                  headers: { 'Content-Type': 'application/json', 'x-access-token': auth.accessToken },
                  withCredentials: true // Set credentials option here
                }
              ); 
            console.log(JSON.stringify(response));
        }catch(err){
        }
    }

    return (
        <div className = "createNewNotifCard">
            {children}
            <h2>
                Complete the boxes below to customize your own notification
            </h2>
            <div className="inputGroup">
                <input className="standardTextEntry inputGroup__input" id="notifName" type="text" onChange={(notifName => setNotifName(notifName.target.value))} required >
                </input>
                <label htmlFor="notifName" className="inputGroup__label" >Notification Name</label>
            </div>
            <div className="inputGroup">
                <input className="standardTextEntry inputGroup__input" id="url" type="text" onChange={(websiteURLText => setWebsiteURLText(websiteURLText.target.value))} required >
                </input>
                <label htmlFor="url" className="inputGroup__label" >Website URL</label>
            </div>
            <div className="infoContainer">
                <p>
                    Enter in any information you would like to be notified about if changed on the website.
                    Be as descriptive as possible in a clear and concise manner
                </p>   
            </div>      
            <div className="inputGroup">
                <input className="promptInput inputGroup__input" id="websitePrompt" type="text" onChange={(websitePromptText => setWebsitePromptText(websitePromptText.target.value))} required placeholder="ex: Changes in price of any t-shirts." >
                </input>
                <label htmlFor="websitePrompt" className="inputGroup__label">Website Prompt</label>
            </div>
            <p>
                Please select your preffered method of receiving your notifications.
            </p>
            <div className="buttonsContainer">
                <div className="buttonContainer">
                    <FontAwesomeIcon className= "messageIconExpansion" icon={faMessage} size="2xl" style={{color: "#00ff04",}} />
                    <button className="checkBoxButton" onClick={handleTextCheckBox}>
                        <FontAwesomeIcon className={textCheckBox ? "checkBoxExpansion" : ""} icon={textCheckBox ? faSquareCheck : faSquareFull} size="2xl" style={{color: "#5c2cde",}} />
                    </button>
                </div>
                <div className="buttonContainer">
                    <FontAwesomeIcon className= "messageIconExpansion" icon={faEnvelope} size="2xl" style={{color: "#005eff",}} />
                    <button className="checkBoxButton" onClick={handleEmailCheckBox}>
                        <FontAwesomeIcon className={emailCheckBox ? "checkBoxExpansion" : ""} icon={emailCheckBox ? faSquareCheck : faSquareFull} size="2xl" style={{color: "#5c2cde",}} />
                    </button>
                </div>
            </div>
            <div className="submitButtonContainer">
                <button className="submitNotifButton" onClick={handleSubmit}>
                    <h>
                        Submit Notification
                    </h>
                </button>
            </div>
        </div>
    );
};


export default CreateNotifCard;